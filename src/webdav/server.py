"""WebDAV server for receiving job output from the slurm cluster."""

import logging
import socketserver
import threading
from wsgiref.simple_server import WSGIRequestHandler, WSGIServer

from wsgidav.dc.base_dc import BaseDomainController
from wsgidav.fs_dav_provider import FilesystemProvider
from wsgidav.wsgidav_app import WsgiDAVApp

from src.constants import SCRATCH_DIR, WEBDAV_HOST, WEBDAV_PORT

logger = logging.getLogger(__name__)

_credentials: dict[str, str] = {}


def register(job_id: str, password: str) -> None:
    _credentials[job_id] = password


def deregister(job_id: str) -> None:
    _credentials.pop(job_id, None)


class _DomainController(BaseDomainController):
    def get_domain_realm(self, path_info, environ):
        return "ada-slurm-manager"

    def require_authentication(self, realm, environ):
        return True

    def basic_auth_user(self, realm, job_id, password, environ):
        expected_pass = _credentials.get(job_id)
        if password != expected_pass:
            return False
        # Only allow write to the jobs own dir
        path_info = environ.get("PATH_INFO", "") + "/"
        if not (path_info).startswith(f"/{job_id}/"):
            return False
        
        return job_id

    def supports_http_digest_auth(self):
        return False

# Creates a new thread per request
class _Server(socketserver.ThreadingMixIn, WSGIServer):
    # Threads are killed when the main process exits
    daemon_threads = True


def start() -> None:
    # Initialise base scratch dir
    SCRATCH_DIR.mkdir(parents=True, exist_ok=True)

    app = WsgiDAVApp({
        "provider_mapping": {"/": FilesystemProvider(str(SCRATCH_DIR))},
        "domain_controller": _DomainController,
        "http_authenticator": {"accept_basic": True, "accept_digest": False, "default_to_digest": False},
        "verbose": 0,
        "logging": {"enable_loggers": []},
    })

    server = _Server((WEBDAV_HOST, WEBDAV_PORT), WSGIRequestHandler)
    server.set_app(app)
    logger.info("WebDAV server started on %s:%s", WEBDAV_HOST, WEBDAV_PORT)
    threading.Thread(target=server.serve_forever, daemon=True).start()
