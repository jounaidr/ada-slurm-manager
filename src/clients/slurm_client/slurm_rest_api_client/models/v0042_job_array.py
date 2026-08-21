from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v0042_job_array_limits import V0042JobArrayLimits
    from ..models.v0042_uint_32_no_val_struct import V0042Uint32NoValStruct


T = TypeVar("T", bound="V0042JobArray")


@_attrs_define
class V0042JobArray:
    """
    Attributes:
        job_id (int | Unset): Job ID of job array, or 0 if N/A
        limits (V0042JobArrayLimits | Unset):
        task_id (V0042Uint32NoValStruct | Unset):
        task (str | Unset): String expression of task IDs in this record
    """

    job_id: int | Unset = UNSET
    limits: V0042JobArrayLimits | Unset = UNSET
    task_id: V0042Uint32NoValStruct | Unset = UNSET
    task: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        job_id = self.job_id

        limits: dict[str, Any] | Unset = UNSET
        if not isinstance(self.limits, Unset):
            limits = self.limits.to_dict()

        task_id: dict[str, Any] | Unset = UNSET
        if not isinstance(self.task_id, Unset):
            task_id = self.task_id.to_dict()

        task = self.task

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if job_id is not UNSET:
            field_dict["job_id"] = job_id
        if limits is not UNSET:
            field_dict["limits"] = limits
        if task_id is not UNSET:
            field_dict["task_id"] = task_id
        if task is not UNSET:
            field_dict["task"] = task

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v0042_job_array_limits import V0042JobArrayLimits
        from ..models.v0042_uint_32_no_val_struct import V0042Uint32NoValStruct

        d = dict(src_dict)
        job_id = d.pop("job_id", UNSET)

        _limits = d.pop("limits", UNSET)
        limits: V0042JobArrayLimits | Unset
        if isinstance(_limits, Unset):
            limits = UNSET
        else:
            limits = V0042JobArrayLimits.from_dict(_limits)

        _task_id = d.pop("task_id", UNSET)
        task_id: V0042Uint32NoValStruct | Unset
        if isinstance(_task_id, Unset):
            task_id = UNSET
        else:
            task_id = V0042Uint32NoValStruct.from_dict(_task_id)

        task = d.pop("task", UNSET)

        v0042_job_array = cls(
            job_id=job_id,
            limits=limits,
            task_id=task_id,
            task=task,
        )

        v0042_job_array.additional_properties = d
        return v0042_job_array

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
