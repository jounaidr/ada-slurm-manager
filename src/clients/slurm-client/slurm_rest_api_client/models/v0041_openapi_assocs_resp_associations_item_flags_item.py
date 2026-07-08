from enum import Enum


class V0041OpenapiAssocsRespAssociationsItemFlagsItem(str, Enum):
    DELETED = "DELETED"
    EXACT = "Exact"
    NOUPDATE = "NoUpdate"
    NOUSERSARECOORDS = "NoUsersAreCoords"
    USERSARECOORDS = "UsersAreCoords"

    def __str__(self) -> str:
        return str(self.value)
