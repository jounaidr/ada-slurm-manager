"""Builds the Slurm job script for slurmrestd."""


def build_script(
    script_body: str,
    sync_interval_seconds: int,
) -> str:
    lines = [
        "#!/bin/bash",
        "export RCLONE_WEBDAV_USER=$SLURM_JOB_ID",
        # Create job output dir and redirect script output into it
        "JOB_PATH=$HOME/ada-$SLURM_JOB_ID",
        "mkdir -p $JOB_PATH",
        "exec > $JOB_PATH/stdout.log 2> $JOB_PATH/stderr.log",
        # Poll ada-slurm-manager for scratch and input initialization
        "until rclone lsf :webdav:$SLURM_JOB_ID/.ready; do sleep 5; done",
        # Pull input files staged by ada-slurm-manager
        "rclone copy :webdav:$SLURM_JOB_ID/ $JOB_PATH/ --exclude '.webdav_token' --exclude '.ready'",
        # Continuously push output back to ada-slurm-manager while job runs
        f"(while sleep {sync_interval_seconds}; do",
        "rclone copy $JOB_PATH/ :webdav:$SLURM_JOB_ID/",
        "done) &",
        "SYNC_PID=$!",
        # Core job commands from database
        script_body.strip(),
        # Stop background sync loop and clean up cluster job dir
        "kill $SYNC_PID",
        "wait $SYNC_PID 2>/dev/null",
        "rclone copy $JOB_PATH/ :webdav:$SLURM_JOB_ID/ && rm -rf $JOB_PATH",
    ]
    
    return "\n".join(lines)
