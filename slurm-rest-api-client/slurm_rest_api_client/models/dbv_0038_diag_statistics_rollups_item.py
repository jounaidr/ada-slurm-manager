from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Dbv0038DiagStatisticsRollupsItem")


@_attrs_define
class Dbv0038DiagStatisticsRollupsItem:
    """Rollup statistics

    Attributes:
        type_ (str | Unset): Type of rollup
        last_run (int | Unset): Timestamp of last rollup
        last_cycle (int | Unset): Timestamp of last cycle
        max_cycle (int | Unset): Max time of all cycles
        total_time (int | Unset): Total time (s) spent doing rollup
        mean_cycles (int | Unset): Average time (s) of cycle
    """

    type_: str | Unset = UNSET
    last_run: int | Unset = UNSET
    last_cycle: int | Unset = UNSET
    max_cycle: int | Unset = UNSET
    total_time: int | Unset = UNSET
    mean_cycles: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        last_run = self.last_run

        last_cycle = self.last_cycle

        max_cycle = self.max_cycle

        total_time = self.total_time

        mean_cycles = self.mean_cycles

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if last_run is not UNSET:
            field_dict["last_run"] = last_run
        if last_cycle is not UNSET:
            field_dict["last_cycle"] = last_cycle
        if max_cycle is not UNSET:
            field_dict["max_cycle"] = max_cycle
        if total_time is not UNSET:
            field_dict["total_time"] = total_time
        if mean_cycles is not UNSET:
            field_dict["mean_cycles"] = mean_cycles

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        last_run = d.pop("last_run", UNSET)

        last_cycle = d.pop("last_cycle", UNSET)

        max_cycle = d.pop("max_cycle", UNSET)

        total_time = d.pop("total_time", UNSET)

        mean_cycles = d.pop("mean_cycles", UNSET)

        dbv_0038_diag_statistics_rollups_item = cls(
            type_=type_,
            last_run=last_run,
            last_cycle=last_cycle,
            max_cycle=max_cycle,
            total_time=total_time,
            mean_cycles=mean_cycles,
        )

        dbv_0038_diag_statistics_rollups_item.additional_properties = d
        return dbv_0038_diag_statistics_rollups_item

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
