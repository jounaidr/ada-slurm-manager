from enum import Enum


class V0037JobPropertiesOpenMode(str, Enum):
    APPEND = "append"
    TRUNCATE = "truncate"

    def __str__(self) -> str:
        return str(self.value)
