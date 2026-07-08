from enum import Enum


class V0041OpenapiUsersRespUsersItemFlagsItem(str, Enum):
    DELETED = "DELETED"
    NONE = "NONE"

    def __str__(self) -> str:
        return str(self.value)
