from enum import Enum


class SlurmdbV0039GetJobsSkipSteps(str, Enum):
    FALSE = "false"
    TRUE = "true"

    def __str__(self) -> str:
        return str(self.value)
