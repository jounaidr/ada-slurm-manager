from enum import Enum


class V0041OpenapiJobInfoRespJobsItemJobResourcesNodesAllocationItemSocketsItemCoresItemStatusItem(str, Enum):
    ALLOCATED = "ALLOCATED"
    INVALID = "INVALID"
    IN_USE = "IN_USE"
    UNALLOCATED = "UNALLOCATED"

    def __str__(self) -> str:
        return str(self.value)
