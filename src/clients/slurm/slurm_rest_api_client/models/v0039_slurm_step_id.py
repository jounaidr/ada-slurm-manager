from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="V0039SlurmStepId")


@_attrs_define
class V0039SlurmStepId:
    """step details

    Attributes:
        job_id (int | Unset): JobID
        step_het_component (int | Unset): HetStep
        step_id (str | Unset):
    """

    job_id: int | Unset = UNSET
    step_het_component: int | Unset = UNSET
    step_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        job_id = self.job_id

        step_het_component = self.step_het_component

        step_id = self.step_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if job_id is not UNSET:
            field_dict["job_id"] = job_id
        if step_het_component is not UNSET:
            field_dict["step_het_component"] = step_het_component
        if step_id is not UNSET:
            field_dict["step_id"] = step_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        job_id = d.pop("job_id", UNSET)

        step_het_component = d.pop("step_het_component", UNSET)

        step_id = d.pop("step_id", UNSET)

        v0039_slurm_step_id = cls(
            job_id=job_id,
            step_het_component=step_het_component,
            step_id=step_id,
        )

        v0039_slurm_step_id.additional_properties = d
        return v0039_slurm_step_id

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
