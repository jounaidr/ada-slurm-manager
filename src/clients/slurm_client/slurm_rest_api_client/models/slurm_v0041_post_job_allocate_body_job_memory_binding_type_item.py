from enum import Enum


class SlurmV0041PostJobAllocateBodyJobMemoryBindingTypeItem(str, Enum):
    LOCAL = "LOCAL"
    MAP = "MAP"
    MASK = "MASK"
    NONE = "NONE"
    PREFER = "PREFER"
    RANK = "RANK"
    SORT = "SORT"
    VERBOSE = "VERBOSE"

    def __str__(self) -> str:
        return str(self.value)
