from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SlurmdbV0041GetDiagResponse200StatisticsRollupsHourlyDuration")


@_attrs_define
class SlurmdbV0041GetDiagResponse200StatisticsRollupsHourlyDuration:
    """
    Attributes:
        last (int | Unset): Total time spent doing last daily rollup (seconds)
        max_ (int | Unset): Longest hourly rollup time (seconds)
        time (int | Unset): Total time spent doing hourly rollups (seconds)
    """

    last: int | Unset = UNSET
    max_: int | Unset = UNSET
    time: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        last = self.last

        max_ = self.max_

        time = self.time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if last is not UNSET:
            field_dict["last"] = last
        if max_ is not UNSET:
            field_dict["max"] = max_
        if time is not UNSET:
            field_dict["time"] = time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        last = d.pop("last", UNSET)

        max_ = d.pop("max", UNSET)

        time = d.pop("time", UNSET)

        slurmdb_v0041_get_diag_response_200_statistics_rollups_hourly_duration = cls(
            last=last,
            max_=max_,
            time=time,
        )

        slurmdb_v0041_get_diag_response_200_statistics_rollups_hourly_duration.additional_properties = d
        return slurmdb_v0041_get_diag_response_200_statistics_rollups_hourly_duration

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
