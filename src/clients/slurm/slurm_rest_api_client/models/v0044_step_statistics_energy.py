from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v0044_uint_64_no_val_struct import V0044Uint64NoValStruct


T = TypeVar("T", bound="V0044StepStatisticsEnergy")


@_attrs_define
class V0044StepStatisticsEnergy:
    """
    Attributes:
        consumed (V0044Uint64NoValStruct | Unset):
    """

    consumed: V0044Uint64NoValStruct | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        consumed: dict[str, Any] | Unset = UNSET
        if not isinstance(self.consumed, Unset):
            consumed = self.consumed.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if consumed is not UNSET:
            field_dict["consumed"] = consumed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v0044_uint_64_no_val_struct import V0044Uint64NoValStruct

        d = dict(src_dict)
        _consumed = d.pop("consumed", UNSET)
        consumed: V0044Uint64NoValStruct | Unset
        if isinstance(_consumed, Unset):
            consumed = UNSET
        else:
            consumed = V0044Uint64NoValStruct.from_dict(_consumed)

        v0044_step_statistics_energy = cls(
            consumed=consumed,
        )

        v0044_step_statistics_energy.additional_properties = d
        return v0044_step_statistics_energy

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
