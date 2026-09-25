from enum import Enum


class V0039JobDescMsgKillWarningFlagsItem(str, Enum):
    ARRAY_TASK = "ARRAY_TASK"
    BATCH_JOB = "BATCH_JOB"
    FEDERATION_REQUEUE = "FEDERATION_REQUEUE"
    FULL_JOB = "FULL_JOB"
    FULL_STEPS_ONLY = "FULL_STEPS_ONLY"
    HURRY = "HURRY"
    NO_SIBLING_JOBS = "NO_SIBLING_JOBS"
    OUT_OF_MEMORY = "OUT_OF_MEMORY"
    RESERVATION_JOB = "RESERVATION_JOB"
    WARNING_SENT = "WARNING_SENT"

    def __str__(self) -> str:
        return str(self.value)
