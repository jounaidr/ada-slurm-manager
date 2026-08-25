from enum import Enum


class V0039RollupStatsItemType(str, Enum):
    INTERNAL = "internal"
    UNKNOWN = "unknown"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
