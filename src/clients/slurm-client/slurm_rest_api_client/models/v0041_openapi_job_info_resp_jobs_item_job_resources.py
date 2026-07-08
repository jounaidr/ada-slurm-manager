from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.v0041_openapi_job_info_resp_jobs_item_job_resources_select_type_item import (
    V0041OpenapiJobInfoRespJobsItemJobResourcesSelectTypeItem,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v0041_openapi_job_info_resp_jobs_item_job_resources_nodes import (
        V0041OpenapiJobInfoRespJobsItemJobResourcesNodes,
    )
    from ..models.v0041_openapi_job_info_resp_jobs_item_job_resources_threads_per_core import (
        V0041OpenapiJobInfoRespJobsItemJobResourcesThreadsPerCore,
    )


T = TypeVar("T", bound="V0041OpenapiJobInfoRespJobsItemJobResources")


@_attrs_define
class V0041OpenapiJobInfoRespJobsItemJobResources:
    """Resources used by the job

    Attributes:
        select_type (list[V0041OpenapiJobInfoRespJobsItemJobResourcesSelectTypeItem]): Scheduler consumable resource
            selection type
        cpus (int): Number of allocated CPUs
        threads_per_core (V0041OpenapiJobInfoRespJobsItemJobResourcesThreadsPerCore): Number of processor threads per
            CPU core
        nodes (V0041OpenapiJobInfoRespJobsItemJobResourcesNodes | Unset):
    """

    select_type: list[V0041OpenapiJobInfoRespJobsItemJobResourcesSelectTypeItem]
    cpus: int
    threads_per_core: V0041OpenapiJobInfoRespJobsItemJobResourcesThreadsPerCore
    nodes: V0041OpenapiJobInfoRespJobsItemJobResourcesNodes | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        select_type = []
        for select_type_item_data in self.select_type:
            select_type_item = select_type_item_data.value
            select_type.append(select_type_item)

        cpus = self.cpus

        threads_per_core = self.threads_per_core.to_dict()

        nodes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.nodes, Unset):
            nodes = self.nodes.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "select_type": select_type,
                "cpus": cpus,
                "threads_per_core": threads_per_core,
            }
        )
        if nodes is not UNSET:
            field_dict["nodes"] = nodes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v0041_openapi_job_info_resp_jobs_item_job_resources_nodes import (
            V0041OpenapiJobInfoRespJobsItemJobResourcesNodes,
        )
        from ..models.v0041_openapi_job_info_resp_jobs_item_job_resources_threads_per_core import (
            V0041OpenapiJobInfoRespJobsItemJobResourcesThreadsPerCore,
        )

        d = dict(src_dict)
        select_type = []
        _select_type = d.pop("select_type")
        for select_type_item_data in _select_type:
            select_type_item = V0041OpenapiJobInfoRespJobsItemJobResourcesSelectTypeItem(select_type_item_data)

            select_type.append(select_type_item)

        cpus = d.pop("cpus")

        threads_per_core = V0041OpenapiJobInfoRespJobsItemJobResourcesThreadsPerCore.from_dict(
            d.pop("threads_per_core")
        )

        _nodes = d.pop("nodes", UNSET)
        nodes: V0041OpenapiJobInfoRespJobsItemJobResourcesNodes | Unset
        if isinstance(_nodes, Unset):
            nodes = UNSET
        else:
            nodes = V0041OpenapiJobInfoRespJobsItemJobResourcesNodes.from_dict(_nodes)

        v0041_openapi_job_info_resp_jobs_item_job_resources = cls(
            select_type=select_type,
            cpus=cpus,
            threads_per_core=threads_per_core,
            nodes=nodes,
        )

        v0041_openapi_job_info_resp_jobs_item_job_resources.additional_properties = d
        return v0041_openapi_job_info_resp_jobs_item_job_resources

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
