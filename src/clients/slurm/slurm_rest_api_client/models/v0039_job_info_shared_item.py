from enum import Enum


class V0039JobInfoSharedItem(str, Enum):
    MCS = "mcs"
    NONE = "none"
    OVERSUBSCRIBE = "oversubscribe"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
