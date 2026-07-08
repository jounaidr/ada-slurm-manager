from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="V0041OpenapiJobInfoRespJobsItemJobResourcesNodesAllocationItemCpus")


@_attrs_define
class V0041OpenapiJobInfoRespJobsItemJobResourcesNodesAllocationItemCpus:
    """
    Attributes:
        count (int | Unset): Total number of CPUs assigned to job
        used (int | Unset): Total number of CPUs used by job
    """

    count: int | Unset = UNSET
    used: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        used = self.used

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if count is not UNSET:
            field_dict["count"] = count
        if used is not UNSET:
            field_dict["used"] = used

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        count = d.pop("count", UNSET)

        used = d.pop("used", UNSET)

        v0041_openapi_job_info_resp_jobs_item_job_resources_nodes_allocation_item_cpus = cls(
            count=count,
            used=used,
        )

        v0041_openapi_job_info_resp_jobs_item_job_resources_nodes_allocation_item_cpus.additional_properties = d
        return v0041_openapi_job_info_resp_jobs_item_job_resources_nodes_allocation_item_cpus

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
