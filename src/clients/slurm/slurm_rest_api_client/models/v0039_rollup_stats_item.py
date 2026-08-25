from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.v0039_rollup_stats_item_type import V0039RollupStatsItemType
from ..types import UNSET, Unset

T = TypeVar("T", bound="V0039RollupStatsItem")


@_attrs_define
class V0039RollupStatsItem:
    """recorded rollup statistics

    Attributes:
        type_ (V0039RollupStatsItemType | Unset): type
        last_run (int | Unset): Last time rollup ran (UNIX timestamp)
        max_cycle (int | Unset): longest rollup time (seconds)
        total_time (int | Unset): total time spent doing rollups (seconds)
        total_cycles (int | Unset): number of rollups since last_run
        mean_cycles (int | Unset): average time for rollup (seconds)
    """

    type_: V0039RollupStatsItemType | Unset = UNSET
    last_run: int | Unset = UNSET
    max_cycle: int | Unset = UNSET
    total_time: int | Unset = UNSET
    total_cycles: int | Unset = UNSET
    mean_cycles: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        last_run = self.last_run

        max_cycle = self.max_cycle

        total_time = self.total_time

        total_cycles = self.total_cycles

        mean_cycles = self.mean_cycles

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if last_run is not UNSET:
            field_dict["last run"] = last_run
        if max_cycle is not UNSET:
            field_dict["max_cycle"] = max_cycle
        if total_time is not UNSET:
            field_dict["total_time"] = total_time
        if total_cycles is not UNSET:
            field_dict["total_cycles"] = total_cycles
        if mean_cycles is not UNSET:
            field_dict["mean_cycles"] = mean_cycles

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: V0039RollupStatsItemType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = V0039RollupStatsItemType(_type_)

        last_run = d.pop("last run", UNSET)

        max_cycle = d.pop("max_cycle", UNSET)

        total_time = d.pop("total_time", UNSET)

        total_cycles = d.pop("total_cycles", UNSET)

        mean_cycles = d.pop("mean_cycles", UNSET)

        v0039_rollup_stats_item = cls(
            type_=type_,
            last_run=last_run,
            max_cycle=max_cycle,
            total_time=total_time,
            total_cycles=total_cycles,
            mean_cycles=mean_cycles,
        )

        v0039_rollup_stats_item.additional_properties = d
        return v0039_rollup_stats_item

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
