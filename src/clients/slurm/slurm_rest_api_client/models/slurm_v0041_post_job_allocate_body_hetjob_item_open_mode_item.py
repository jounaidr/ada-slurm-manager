from enum import Enum


class SlurmV0041PostJobAllocateBodyHetjobItemOpenModeItem(str, Enum):
    APPEND = "APPEND"
    TRUNCATE = "TRUNCATE"

    def __str__(self) -> str:
        return str(self.value)
