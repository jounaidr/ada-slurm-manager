import logging

from slurm_rest_api_client.client import AuthenticatedClient
from slurm_rest_api_client.api.slurm import slurmctld_get_jobs
from slurm_rest_api_client.api.slurm import slurmctld_submit_job
from slurm_rest_api_client.models.v0037_job_properties import V0037JobProperties as JobProperties
from slurm_rest_api_client.models.v0037_job_response_properties import V0037JobResponseProperties as JobResponseProperties
from slurm_rest_api_client.models.v0037_job_submission import V0037JobSubmission as JobSubmission

from src.constants import SLURM_API_URL, SLURM_API_VERIFY_SSL

logger = logging.getLogger(__name__)


def _client(token: str) -> AuthenticatedClient:
    # Slurm token is per user and short lived, so a new client is created per request
    return AuthenticatedClient(
        base_url=str(SLURM_API_URL),
        token=token,
        verify_ssl=SLURM_API_VERIFY_SSL,
    )


async def submit_job(script: str, job_properties: JobProperties, token: str) -> int:
    body = JobSubmission(script=script, job=job_properties)

    # Open and close the connection cleanly.
    async with _client(token) as client:
        response = await slurmctld_submit_job.asyncio(client=client, body=body)

    if response is None:
        raise RuntimeError("No response from slurmrestd on job submission")
    if response.errors:
        messages = [str(e.error) for e in response.errors]
        raise RuntimeError(f"Slurm job submission failed: [{', '.join(messages)}]")
    if not isinstance(response.job_id, int):
        raise RuntimeError("Job submitted but no job_id in response")

    logger.info("Job submitted, slurm_job_id=%s", response.job_id)

    return response.job_id


async def get_jobs(token: str) -> list[JobResponseProperties]:
    # Open and close the connection cleanly.
    async with _client(token) as client:
        response = await slurmctld_get_jobs.asyncio(client=client)

    if response is None:
        raise RuntimeError("No response from slurmrestd on get_jobs")
    if response.errors:
        messages = [str(e.error) for e in response.errors]
        raise RuntimeError(f"Failed to get jobs from slurmrestd: [{', '.join(messages)}]")

    return response.jobs
