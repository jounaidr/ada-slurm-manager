from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SlurmdbV0041GetDiagResponseDefaultStatisticsUsersItemTime")


@_attrs_define
class SlurmdbV0041GetDiagResponseDefaultStatisticsUsersItemTime:
    """
    Attributes:
        average (int | Unset): Average RPC processing time in microseconds
        total (int | Unset): Total RPC processing time in microseconds
    """

    average: int | Unset = UNSET
    total: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        average = self.average

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if average is not UNSET:
            field_dict["average"] = average
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        average = d.pop("average", UNSET)

        total = d.pop("total", UNSET)

        slurmdb_v0041_get_diag_response_default_statistics_users_item_time = cls(
            average=average,
            total=total,
        )

        slurmdb_v0041_get_diag_response_default_statistics_users_item_time.additional_properties = d
        return slurmdb_v0041_get_diag_response_default_statistics_users_item_time

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
