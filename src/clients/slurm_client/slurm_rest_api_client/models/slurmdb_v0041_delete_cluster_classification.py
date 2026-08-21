from enum import Enum


class SlurmdbV0041DeleteClusterClassification(str, Enum):
    CAPABILITY = "CAPABILITY"
    CAPACITY = "CAPACITY"
    CAPAPACITY_BOTH_CAPABILITY_AND_CAPACITY = "CAPAPACITY (both CAPABILITY and CAPACITY)"
    UNCLASSIFIED = "UNCLASSIFIED"

    def __str__(self) -> str:
        return str(self.value)
