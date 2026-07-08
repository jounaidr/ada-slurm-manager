from enum import Enum


class V0042ClusterRecFlagsItem(str, Enum):
    EXTERNAL = "EXTERNAL"
    FEDERATION = "FEDERATION"
    MULTIPLE_SLURMD = "MULTIPLE_SLURMD"
    REGISTERING = "REGISTERING"

    def __str__(self) -> str:
        return str(self.value)
