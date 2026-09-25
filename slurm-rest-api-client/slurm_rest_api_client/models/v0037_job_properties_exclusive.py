from enum import Enum


class V0037JobPropertiesExclusive(str, Enum):
    FALSE = "false"
    MCS = "mcs"
    TRUE = "true"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
