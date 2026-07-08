from enum import Enum


class V0044JobDescMsgMemoryBindingTypeItem(str, Enum):
    LOCAL = "LOCAL"
    MAP = "MAP"
    MASK = "MASK"
    NONE = "NONE"
    PREFER = "PREFER"
    RANK = "RANK"
    VERBOSE = "VERBOSE"

    def __str__(self) -> str:
        return str(self.value)
