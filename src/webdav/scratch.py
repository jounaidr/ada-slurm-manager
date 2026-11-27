"""Per job scratch directory and WebDAV credential management."""

import logging
import secrets
import shutil
import subprocess

from src.constants import SCRATCH_DIR, CEPH_HOME_FILE
from src.webdav import webdav_server

logger = logging.getLogger(__name__)


_SECRETS_FILE = ".webdav_token"


def create(job_id: int, ceph_home: str, webdav_token: str) -> None:
    # Create job sub dir
    job_path = SCRATCH_DIR / str(job_id)
    job_path.mkdir(parents=True, exist_ok=True)

    # Save token in job sub dir and register to WebDAV
    (job_path / _SECRETS_FILE).write_text(webdav_token)
    webdav_server.register(str(job_id), webdav_token)
    # Write user ceph home to job sub dir
    (job_path / CEPH_HOME_FILE).write_text(ceph_home)

    logger.info("Scratch dir created for slurm_job_id=%s", job_id)


def generate_token() -> tuple[str, str]:
    token = secrets.token_urlsafe(32)

    # rclone requires an obscured token, if we pass the plain token 
    # to the job script rclone will try and decrypt that before
    # making the request back, resulting in an invalid token
    token_obscured = subprocess.run(
        ["rclone", "obscure", token], capture_output=True, text=True, check=True
    ).stdout.strip()

    return token, token_obscured


def delete(job_id: int) -> None:
    job_path = SCRATCH_DIR / str(job_id)
    webdav_server.deregister(str(job_id))

    if job_path.exists():
        # Recursively delete job sub dir 
        shutil.rmtree(job_path)
        logger.info("Scratch dir deleted for slurm_job_id=%s", job_id)
    else:
        logger.warning("Scratch dir not found on delete for slurm_job_id=%s", job_id)


def restore() -> None:
    count = 0

    for job_dir in SCRATCH_DIR.iterdir():
        token_file = job_dir / _SECRETS_FILE
        if job_dir.is_dir() and token_file.exists():
            # Re-register each job to WebDAV server
            webdav_server.register(job_dir.name, token_file.read_text())
            count += 1
            logger.info("Restored WebDAV credentials for slurm_job_id=%s", job_dir.name)
    
    logger.info("Restored WebDAV credentials for %s active jobs", count)
