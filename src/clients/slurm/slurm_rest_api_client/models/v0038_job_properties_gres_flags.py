from enum import Enum


class V0038JobPropertiesGresFlags(str, Enum):
    DISABLE_BINDING = "disable-binding"
    ENFORCE_BINDING = "enforce-binding"

    def __str__(self) -> str:
        return str(self.value)
