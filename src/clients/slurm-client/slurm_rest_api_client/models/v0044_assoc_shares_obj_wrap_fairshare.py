from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v0044_float_64_no_val_struct import V0044Float64NoValStruct


T = TypeVar("T", bound="V0044AssocSharesObjWrapFairshare")


@_attrs_define
class V0044AssocSharesObjWrapFairshare:
    """
    Attributes:
        factor (V0044Float64NoValStruct | Unset):
        level (V0044Float64NoValStruct | Unset):
    """

    factor: V0044Float64NoValStruct | Unset = UNSET
    level: V0044Float64NoValStruct | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        factor: dict[str, Any] | Unset = UNSET
        if not isinstance(self.factor, Unset):
            factor = self.factor.to_dict()

        level: dict[str, Any] | Unset = UNSET
        if not isinstance(self.level, Unset):
            level = self.level.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if factor is not UNSET:
            field_dict["factor"] = factor
        if level is not UNSET:
            field_dict["level"] = level

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v0044_float_64_no_val_struct import V0044Float64NoValStruct

        d = dict(src_dict)
        _factor = d.pop("factor", UNSET)
        factor: V0044Float64NoValStruct | Unset
        if isinstance(_factor, Unset):
            factor = UNSET
        else:
            factor = V0044Float64NoValStruct.from_dict(_factor)

        _level = d.pop("level", UNSET)
        level: V0044Float64NoValStruct | Unset
        if isinstance(_level, Unset):
            level = UNSET
        else:
            level = V0044Float64NoValStruct.from_dict(_level)

        v0044_assoc_shares_obj_wrap_fairshare = cls(
            factor=factor,
            level=level,
        )

        v0044_assoc_shares_obj_wrap_fairshare.additional_properties = d
        return v0044_assoc_shares_obj_wrap_fairshare

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
