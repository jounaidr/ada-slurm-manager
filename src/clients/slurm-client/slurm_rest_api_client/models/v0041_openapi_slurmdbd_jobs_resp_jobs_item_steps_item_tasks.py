from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemTasks")


@_attrs_define
class V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemTasks:
    """
    Attributes:
        count (int | Unset): Total number of tasks
    """

    count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if count is not UNSET:
            field_dict["count"] = count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        count = d.pop("count", UNSET)

        v0041_openapi_slurmdbd_jobs_resp_jobs_item_steps_item_tasks = cls(
            count=count,
        )

        v0041_openapi_slurmdbd_jobs_resp_jobs_item_steps_item_tasks.additional_properties = d
        return v0041_openapi_slurmdbd_jobs_resp_jobs_item_steps_item_tasks

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
