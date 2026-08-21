from enum import Enum


class V0044ClusterRecFlagsItem(str, Enum):
    DELETED = "DELETED"
    EXTERNAL = "EXTERNAL"
    FEDERATION = "FEDERATION"
    MULTIPLE_SLURMD = "MULTIPLE_SLURMD"
    REGISTERING = "REGISTERING"

    def __str__(self) -> str:
        return str(self.value)
