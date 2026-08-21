from enum import Enum


class V0041OpenapiSlurmdbdConfigRespUsersItemFlagsItem(str, Enum):
    DELETED = "DELETED"
    NONE = "NONE"

    def __str__(self) -> str:
        return str(self.value)
