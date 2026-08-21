from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.v0041_openapi_job_info_resp_jobs_item_job_resources_nodes_allocation_item_sockets_item_cores_item import (
        V0041OpenapiJobInfoRespJobsItemJobResourcesNodesAllocationItemSocketsItemCoresItem,
    )


T = TypeVar("T", bound="V0041OpenapiJobInfoRespJobsItemJobResourcesNodesAllocationItemSocketsItem")


@_attrs_define
class V0041OpenapiJobInfoRespJobsItemJobResourcesNodesAllocationItemSocketsItem:
    """
    Attributes:
        index (int): Core index
        cores (list[V0041OpenapiJobInfoRespJobsItemJobResourcesNodesAllocationItemSocketsItemCoresItem]): Core in socket
    """

    index: int
    cores: list[V0041OpenapiJobInfoRespJobsItemJobResourcesNodesAllocationItemSocketsItemCoresItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        index = self.index

        cores = []
        for cores_item_data in self.cores:
            cores_item = cores_item_data.to_dict()
            cores.append(cores_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "index": index,
                "cores": cores,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v0041_openapi_job_info_resp_jobs_item_job_resources_nodes_allocation_item_sockets_item_cores_item import (
            V0041OpenapiJobInfoRespJobsItemJobResourcesNodesAllocationItemSocketsItemCoresItem,
        )

        d = dict(src_dict)
        index = d.pop("index")

        cores = []
        _cores = d.pop("cores")
        for cores_item_data in _cores:
            cores_item = V0041OpenapiJobInfoRespJobsItemJobResourcesNodesAllocationItemSocketsItemCoresItem.from_dict(
                cores_item_data
            )

            cores.append(cores_item)

        v0041_openapi_job_info_resp_jobs_item_job_resources_nodes_allocation_item_sockets_item = cls(
            index=index,
            cores=cores,
        )

        v0041_openapi_job_info_resp_jobs_item_job_resources_nodes_allocation_item_sockets_item.additional_properties = d
        return v0041_openapi_job_info_resp_jobs_item_job_resources_nodes_allocation_item_sockets_item

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
