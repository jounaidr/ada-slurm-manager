from pydantic import BaseModel, Field


class SlurmOptions(BaseModel):
    """Slurm resource allocation options for job"""

    partition: str = Field(
        description="Slurm partition to submit the job to", examples=["scarf"]
    )
    time_limit_minutes: int = Field(
        description="Job time limit in minutes", examples=[60]
    )
    memory_per_node_mb: int = Field(
        description="Memory per node in MB", examples=[4096]
    )
    num_nodes: int = Field(
        default=1, description="Number of nodes to allocate", examples=[1]
    )
    tasks: int = Field(default=1, description="Number of tasks", examples=[1])
    cpus_per_task: int = Field(default=1, description="CPUs per task", examples=[1])
    gpus_per_node: str | None = Field(
        default=None, description="GPUs per node", examples=["1", "A100:2"]
    )


class JobSubmitRequest(BaseModel):
    """Request body for submitting a job to Slurm"""

    job_name: str = Field(
        description="Job name used by Slurm", examples=["ada-refl1d-large"]
    )
    script_body: str = Field(
        description="Core job commands to execute, sourced from the database",
        examples=["srun refl1d.sif"],
    )
    sync_interval_seconds: int = Field(
        description="Seconds between rclone output syncs during job execution",
        examples=[30],
    )
    environment: dict[str, str] = Field(
        default_factory=dict,
        description="Job environment variables, sourced from the database",
        examples=[{"INPUT_FILE": "dataset.h5"}],
    )
    scarf_scratch_path: str = Field(
        description="Base scratch directory on SCARF for job output",
        examples=["/home/vol01/scarf1234"],
    )
    slurm: SlurmOptions


class JobSubmitResponse(BaseModel):
    """Response after submitting a job to Slurm"""

    slurm_job_id: int = Field(
        description="Slurm job ID assigned at submission", examples=[12345]
    )
