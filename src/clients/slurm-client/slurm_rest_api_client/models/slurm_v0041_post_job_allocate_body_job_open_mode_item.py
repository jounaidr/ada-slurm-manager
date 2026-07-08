from enum import Enum


class SlurmV0041PostJobAllocateBodyJobOpenModeItem(str, Enum):
    APPEND = "APPEND"
    TRUNCATE = "TRUNCATE"

    def __str__(self) -> str:
        return str(self.value)
