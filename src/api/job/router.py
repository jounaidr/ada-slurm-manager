import asyncio
import logging

from fastapi import APIRouter, Header

from src.api.job.schemas import JobSubmitRequest, JobSubmitResponse
from src.clients import slurm
from src.services import ceph_sync, job_builder
from src.webdav import scratch
from src.constants import WEBDAV_URL

router = APIRouter(prefix="/jobs", tags=["jobs"])
logger = logging.getLogger(__name__)


def _log_staging_error(task: asyncio.Task) -> None:
    if not task.cancelled() and task.exception():
        logger.error("Input staging failed for slurm_job_id=%s", task.get_name(), exc_info=task.exception())


@router.post("", response_model=JobSubmitResponse)
async def submit_job(
    request: JobSubmitRequest,
    x_slurm_user_token: str = Header(),
) -> JobSubmitResponse:
    
    script = job_builder.build_script(
        script_body=request.script_body,
        sync_interval_seconds=request.sync_interval_seconds,
        webdav_url=WEBDAV_URL,
    )

    slurm_job_id = await slurm.submit_job(
        script=script,
        token=x_slurm_user_token,
        job_name=request.job_name,
        partition=request.slurm.partition,
        time_limit_minutes=request.slurm.time_limit_minutes,
        memory_per_node_mb=request.slurm.memory_per_node_mb,
        num_nodes=request.slurm.num_nodes,
        tasks=request.slurm.tasks,
        cpus_per_task=request.slurm.cpus_per_task,
        environment=request.environment,
        gpus_per_node=request.slurm.gpus_per_node,
    )

    scratch.create(slurm_job_id, request.ceph_home)

    task = asyncio.create_task(
        ceph_sync.stage_inputs(slurm_job_id, request.input_files),
        name=str(slurm_job_id),
    )
    task.add_done_callback(_log_staging_error)

    return JobSubmitResponse(slurm_job_id=slurm_job_id)
