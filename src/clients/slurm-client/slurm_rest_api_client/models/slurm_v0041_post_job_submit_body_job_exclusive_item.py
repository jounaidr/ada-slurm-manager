from enum import Enum


class SlurmV0041PostJobSubmitBodyJobExclusiveItem(str, Enum):
    FALSE = "false"
    MCS = "mcs"
    TOPO = "topo"
    TRUE = "true"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
