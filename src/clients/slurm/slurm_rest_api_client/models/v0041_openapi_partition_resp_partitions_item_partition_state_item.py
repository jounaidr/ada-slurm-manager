from enum import Enum


class V0041OpenapiPartitionRespPartitionsItemPartitionStateItem(str, Enum):
    DOWN = "DOWN"
    DRAIN = "DRAIN"
    INACTIVE = "INACTIVE"
    UNKNOWN = "UNKNOWN"
    UP = "UP"

    def __str__(self) -> str:
        return str(self.value)
