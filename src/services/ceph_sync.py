"""Input staging for job scratch directories."""

import asyncio
import logging
import shutil
from pathlib import Path

from src.constants import SCRATCH_DIR

logger = logging.getLogger(__name__)

_READY_FILE = ".ready"


async def stage_inputs(job_id: int, input_files: list[str]) -> None:
    scratch_path = SCRATCH_DIR / str(job_id)
    for file in input_files:
        file_path = Path(file)
        # Run copy in a separate thread as to not block event loop
        await asyncio.to_thread(shutil.copy2, file_path, scratch_path / file_path.name)
    (scratch_path / _READY_FILE).write_text("")
    logger.info("Input file staging complete for slurm_job_id=%s", job_id)


async def sync_output(job_id: int) -> None:
    scratch_path = SCRATCH_DIR / str(job_id)
    ceph_home = Path((scratch_path / ".ceph_home").read_text())

    ceph_job_dir = ceph_home / str(job_id)
    ceph_job_dir.mkdir(exist_ok=True)

    exclude_files = {".webdav_pass", ".ready", ".ceph_home"}
    for file in scratch_path.iterdir():
        if file.name not in exclude_files and file.is_file():
            # Run copy in a separate thread as to not block event loop
            await asyncio.to_thread(shutil.copy2, file, ceph_job_dir / file.name)
    logger.info("Output sync complete for slurm_job_id=%s", job_id)
