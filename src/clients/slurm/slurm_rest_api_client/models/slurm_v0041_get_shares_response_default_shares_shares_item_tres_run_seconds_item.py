from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.slurm_v0041_get_shares_response_default_shares_shares_item_tres_run_seconds_item_value import (
        SlurmV0041GetSharesResponseDefaultSharesSharesItemTresRunSecondsItemValue,
    )


T = TypeVar("T", bound="SlurmV0041GetSharesResponseDefaultSharesSharesItemTresRunSecondsItem")


@_attrs_define
class SlurmV0041GetSharesResponseDefaultSharesSharesItemTresRunSecondsItem:
    """
    Attributes:
        name (str | Unset): TRES name
        value (SlurmV0041GetSharesResponseDefaultSharesSharesItemTresRunSecondsItemValue | Unset): TRES value
    """

    name: str | Unset = UNSET
    value: SlurmV0041GetSharesResponseDefaultSharesSharesItemTresRunSecondsItemValue | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.slurm_v0041_get_shares_response_default_shares_shares_item_tres_run_seconds_item_value import (
            SlurmV0041GetSharesResponseDefaultSharesSharesItemTresRunSecondsItemValue,
        )

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        _value = d.pop("value", UNSET)
        value: SlurmV0041GetSharesResponseDefaultSharesSharesItemTresRunSecondsItemValue | Unset
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = SlurmV0041GetSharesResponseDefaultSharesSharesItemTresRunSecondsItemValue.from_dict(_value)

        slurm_v0041_get_shares_response_default_shares_shares_item_tres_run_seconds_item = cls(
            name=name,
            value=value,
        )

        slurm_v0041_get_shares_response_default_shares_shares_item_tres_run_seconds_item.additional_properties = d
        return slurm_v0041_get_shares_response_default_shares_shares_item_tres_run_seconds_item

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
