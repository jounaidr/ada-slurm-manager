from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SlurmV0041GetSharesResponse200SharesSharesItemFairshare")


@_attrs_define
class SlurmV0041GetSharesResponse200SharesSharesItemFairshare:
    """
    Attributes:
        factor (float | Unset): Fairshare factor
        level (float | Unset): Fairshare factor at this level; stored on an assoc as a long double, but that is not
            needed for display in sshare
    """

    factor: float | Unset = UNSET
    level: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        factor = self.factor

        level = self.level

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
        d = dict(src_dict)
        factor = d.pop("factor", UNSET)

        level = d.pop("level", UNSET)

        slurm_v0041_get_shares_response_200_shares_shares_item_fairshare = cls(
            factor=factor,
            level=level,
        )

        slurm_v0041_get_shares_response_200_shares_shares_item_fairshare.additional_properties = d
        return slurm_v0041_get_shares_response_200_shares_shares_item_fairshare

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
