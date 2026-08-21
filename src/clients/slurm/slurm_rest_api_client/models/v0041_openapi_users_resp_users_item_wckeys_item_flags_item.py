from enum import Enum


class V0041OpenapiUsersRespUsersItemWckeysItemFlagsItem(str, Enum):
    DELETED = "DELETED"

    def __str__(self) -> str:
        return str(self.value)
