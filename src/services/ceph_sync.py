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
