import logging
import secrets
import shutil

from src.constants import SCRATCH_DIR
from src.webdav import server

logger = logging.getLogger(__name__)