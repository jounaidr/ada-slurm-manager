from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v0044_uint_32_no_val_struct import V0044Uint32NoValStruct


T = TypeVar("T", bound="V0044SlurmStepId")


@_attrs_define
class V0044SlurmStepId:
    """
    Attributes:
        sluid (str | Unset): SLUID (Slurm Lexicographically-sortable Unique ID)
        job_id (V0044Uint32NoValStruct | Unset):
        step_het_component (V0044Uint32NoValStruct | Unset):
        step_id (str | Unset): Job step ID
    """

    sluid: str | Unset = UNSET
    job_id: V0044Uint32NoValStruct | Unset = UNSET
    step_het_component: V0044Uint32NoValStruct | Unset = UNSET
    step_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sluid = self.sluid

        job_id: dict[str, Any] | Unset = UNSET
        if not isinstance(self.job_id, Unset):
            job_id = self.job_id.to_dict()

        step_het_component: dict[str, Any] | Unset = UNSET
        if not isinstance(self.step_het_component, Unset):
            step_het_component = self.step_het_component.to_dict()

        step_id = self.step_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sluid is not UNSET:
            field_dict["sluid"] = sluid
        if job_id is not UNSET:
            field_dict["job_id"] = job_id
        if step_het_component is not UNSET:
            field_dict["step_het_component"] = step_het_component
        if step_id is not UNSET:
            field_dict["step_id"] = step_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v0044_uint_32_no_val_struct import V0044Uint32NoValStruct

        d = dict(src_dict)
        sluid = d.pop("sluid", UNSET)

        _job_id = d.pop("job_id", UNSET)
        job_id: V0044Uint32NoValStruct | Unset
        if isinstance(_job_id, Unset):
            job_id = UNSET
        else:
            job_id = V0044Uint32NoValStruct.from_dict(_job_id)

        _step_het_component = d.pop("step_het_component", UNSET)
        step_het_component: V0044Uint32NoValStruct | Unset
        if isinstance(_step_het_component, Unset):
            step_het_component = UNSET
        else:
            step_het_component = V0044Uint32NoValStruct.from_dict(_step_het_component)

        step_id = d.pop("step_id", UNSET)

        v0044_slurm_step_id = cls(
            sluid=sluid,
            job_id=job_id,
            step_het_component=step_het_component,
            step_id=step_id,
        )

        v0044_slurm_step_id.additional_properties = d
        return v0044_slurm_step_id

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
