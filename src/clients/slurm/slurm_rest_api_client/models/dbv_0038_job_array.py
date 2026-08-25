from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dbv_0038_job_array_limits import Dbv0038JobArrayLimits


T = TypeVar("T", bound="Dbv0038JobArray")


@_attrs_define
class Dbv0038JobArray:
    """Array properties (optional)

    Attributes:
        job_id (int | Unset): Job id of array
        limits (Dbv0038JobArrayLimits | Unset): Limits on array settings
        task (str | Unset): Array task
        task_id (int | Unset): Array task id
    """

    job_id: int | Unset = UNSET
    limits: Dbv0038JobArrayLimits | Unset = UNSET
    task: str | Unset = UNSET
    task_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        job_id = self.job_id

        limits: dict[str, Any] | Unset = UNSET
        if not isinstance(self.limits, Unset):
            limits = self.limits.to_dict()

        task = self.task

        task_id = self.task_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if job_id is not UNSET:
            field_dict["job_id"] = job_id
        if limits is not UNSET:
            field_dict["limits"] = limits
        if task is not UNSET:
            field_dict["task"] = task
        if task_id is not UNSET:
            field_dict["task_id"] = task_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dbv_0038_job_array_limits import Dbv0038JobArrayLimits

        d = dict(src_dict)
        job_id = d.pop("job_id", UNSET)

        _limits = d.pop("limits", UNSET)
        limits: Dbv0038JobArrayLimits | Unset
        if isinstance(_limits, Unset):
            limits = UNSET
        else:
            limits = Dbv0038JobArrayLimits.from_dict(_limits)

        task = d.pop("task", UNSET)

        task_id = d.pop("task_id", UNSET)

        dbv_0038_job_array = cls(
            job_id=job_id,
            limits=limits,
            task=task,
            task_id=task_id,
        )

        dbv_0038_job_array.additional_properties = d
        return dbv_0038_job_array

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
