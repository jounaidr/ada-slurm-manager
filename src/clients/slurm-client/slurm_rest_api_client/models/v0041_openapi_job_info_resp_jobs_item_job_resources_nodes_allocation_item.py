from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v0041_openapi_job_info_resp_jobs_item_job_resources_nodes_allocation_item_cpus import (
        V0041OpenapiJobInfoRespJobsItemJobResourcesNodesAllocationItemCpus,
    )
    from ..models.v0041_openapi_job_info_resp_jobs_item_job_resources_nodes_allocation_item_memory import (
        V0041OpenapiJobInfoRespJobsItemJobResourcesNodesAllocationItemMemory,
    )
    from ..models.v0041_openapi_job_info_resp_jobs_item_job_resources_nodes_allocation_item_sockets_item import (
        V0041OpenapiJobInfoRespJobsItemJobResourcesNodesAllocationItemSocketsItem,
    )


T = TypeVar("T", bound="V0041OpenapiJobInfoRespJobsItemJobResourcesNodesAllocationItem")


@_attrs_define
class V0041OpenapiJobInfoRespJobsItemJobResourcesNodesAllocationItem:
    """Job resources for a node

    Attributes:
        index (int): Node index
        name (str): Node name
        sockets (list[V0041OpenapiJobInfoRespJobsItemJobResourcesNodesAllocationItemSocketsItem]): Socket allocations in
            node
        cpus (V0041OpenapiJobInfoRespJobsItemJobResourcesNodesAllocationItemCpus | Unset):
        memory (V0041OpenapiJobInfoRespJobsItemJobResourcesNodesAllocationItemMemory | Unset):
    """

    index: int
    name: str
    sockets: list[V0041OpenapiJobInfoRespJobsItemJobResourcesNodesAllocationItemSocketsItem]
    cpus: V0041OpenapiJobInfoRespJobsItemJobResourcesNodesAllocationItemCpus | Unset = UNSET
    memory: V0041OpenapiJobInfoRespJobsItemJobResourcesNodesAllocationItemMemory | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        index = self.index

        name = self.name

        sockets = []
        for sockets_item_data in self.sockets:
            sockets_item = sockets_item_data.to_dict()
            sockets.append(sockets_item)

        cpus: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cpus, Unset):
            cpus = self.cpus.to_dict()

        memory: dict[str, Any] | Unset = UNSET
        if not isinstance(self.memory, Unset):
            memory = self.memory.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "index": index,
                "name": name,
                "sockets": sockets,
            }
        )
        if cpus is not UNSET:
            field_dict["cpus"] = cpus
        if memory is not UNSET:
            field_dict["memory"] = memory

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v0041_openapi_job_info_resp_jobs_item_job_resources_nodes_allocation_item_cpus import (
            V0041OpenapiJobInfoRespJobsItemJobResourcesNodesAllocationItemCpus,
        )
        from ..models.v0041_openapi_job_info_resp_jobs_item_job_resources_nodes_allocation_item_memory import (
            V0041OpenapiJobInfoRespJobsItemJobResourcesNodesAllocationItemMemory,
        )
        from ..models.v0041_openapi_job_info_resp_jobs_item_job_resources_nodes_allocation_item_sockets_item import (
            V0041OpenapiJobInfoRespJobsItemJobResourcesNodesAllocationItemSocketsItem,
        )

        d = dict(src_dict)
        index = d.pop("index")

        name = d.pop("name")

        sockets = []
        _sockets = d.pop("sockets")
        for sockets_item_data in _sockets:
            sockets_item = V0041OpenapiJobInfoRespJobsItemJobResourcesNodesAllocationItemSocketsItem.from_dict(
                sockets_item_data
            )

            sockets.append(sockets_item)

        _cpus = d.pop("cpus", UNSET)
        cpus: V0041OpenapiJobInfoRespJobsItemJobResourcesNodesAllocationItemCpus | Unset
        if isinstance(_cpus, Unset):
            cpus = UNSET
        else:
            cpus = V0041OpenapiJobInfoRespJobsItemJobResourcesNodesAllocationItemCpus.from_dict(_cpus)

        _memory = d.pop("memory", UNSET)
        memory: V0041OpenapiJobInfoRespJobsItemJobResourcesNodesAllocationItemMemory | Unset
        if isinstance(_memory, Unset):
            memory = UNSET
        else:
            memory = V0041OpenapiJobInfoRespJobsItemJobResourcesNodesAllocationItemMemory.from_dict(_memory)

        v0041_openapi_job_info_resp_jobs_item_job_resources_nodes_allocation_item = cls(
            index=index,
            name=name,
            sockets=sockets,
            cpus=cpus,
            memory=memory,
        )

        v0041_openapi_job_info_resp_jobs_item_job_resources_nodes_allocation_item.additional_properties = d
        return v0041_openapi_job_info_resp_jobs_item_job_resources_nodes_allocation_item

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
