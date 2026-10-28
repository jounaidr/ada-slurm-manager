"""Builds the Slurm job script for slurmrestd."""


def build_script(
    script_body: str,
    sync_interval_seconds: int,
    webdav_url: str,
) -> str:
    lines = [
        "#!/bin/bash",
        # Create job output dir and redirect script output into it
        "JOB_PATH=$HOME/ada-$SLURM_JOB_ID",
        "mkdir -p $JOB_PATH",
        "exec > $JOB_PATH/stdout.log 2> $JOB_PATH/stderr.log",
        # Continuously push output to ada-slurm-manager while job runs
        f"(while sleep {sync_interval_seconds}; do",
        f"rclone sync $JOB_PATH {webdav_url}/$SLURM_JOB_ID/",
        "done) &",
        "SYNC_PID=$!",
        # Core job commands from database
        script_body.strip(),
        # Stop background sync loop
        "kill $SYNC_PID",
        "wait $SYNC_PID 2>/dev/null",
        # Final sync and clean up SCARF scratch if sync succeeds
        f"rclone sync $JOB_PATH {webdav_url}/$SLURM_JOB_ID/ && rm -rf $JOB_PATH",
    ]
    return "\n".join(lines)
