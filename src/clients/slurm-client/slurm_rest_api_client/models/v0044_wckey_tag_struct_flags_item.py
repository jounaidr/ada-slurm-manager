from enum import Enum


class V0044WckeyTagStructFlagsItem(str, Enum):
    ASSIGNED_DEFAULT = "ASSIGNED_DEFAULT"

    def __str__(self) -> str:
        return str(self.value)
