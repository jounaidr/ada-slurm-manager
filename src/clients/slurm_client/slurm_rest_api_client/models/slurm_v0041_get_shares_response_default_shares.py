from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.slurm_v0041_get_shares_response_default_shares_shares_item import (
        SlurmV0041GetSharesResponseDefaultSharesSharesItem,
    )


T = TypeVar("T", bound="SlurmV0041GetSharesResponseDefaultShares")


@_attrs_define
class SlurmV0041GetSharesResponseDefaultShares:
    """fairshare info

    Attributes:
        shares (list[SlurmV0041GetSharesResponseDefaultSharesSharesItem] | Unset): Association shares
        total_shares (int | Unset): Total number of shares
    """

    shares: list[SlurmV0041GetSharesResponseDefaultSharesSharesItem] | Unset = UNSET
    total_shares: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        shares: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.shares, Unset):
            shares = []
            for shares_item_data in self.shares:
                shares_item = shares_item_data.to_dict()
                shares.append(shares_item)

        total_shares = self.total_shares

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if shares is not UNSET:
            field_dict["shares"] = shares
        if total_shares is not UNSET:
            field_dict["total_shares"] = total_shares

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.slurm_v0041_get_shares_response_default_shares_shares_item import (
            SlurmV0041GetSharesResponseDefaultSharesSharesItem,
        )

        d = dict(src_dict)
        _shares = d.pop("shares", UNSET)
        shares: list[SlurmV0041GetSharesResponseDefaultSharesSharesItem] | Unset = UNSET
        if _shares is not UNSET:
            shares = []
            for shares_item_data in _shares:
                shares_item = SlurmV0041GetSharesResponseDefaultSharesSharesItem.from_dict(shares_item_data)

                shares.append(shares_item)

        total_shares = d.pop("total_shares", UNSET)

        slurm_v0041_get_shares_response_default_shares = cls(
            shares=shares,
            total_shares=total_shares,
        )

        slurm_v0041_get_shares_response_default_shares.additional_properties = d
        return slurm_v0041_get_shares_response_default_shares

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
