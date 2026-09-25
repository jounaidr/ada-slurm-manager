from enum import Enum


class V0038JobPropertiesOpenMode(str, Enum):
    APPEND = "append"
    TRUNCATE = "truncate"

    def __str__(self) -> str:
        return str(self.value)
