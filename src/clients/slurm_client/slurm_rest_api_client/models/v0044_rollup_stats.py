from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v0044_rollup_stats_daily import V0044RollupStatsDaily
    from ..models.v0044_rollup_stats_hourly import V0044RollupStatsHourly
    from ..models.v0044_rollup_stats_monthly import V0044RollupStatsMonthly


T = TypeVar("T", bound="V0044RollupStats")


@_attrs_define
class V0044RollupStats:
    """
    Attributes:
        hourly (V0044RollupStatsHourly | Unset):
        daily (V0044RollupStatsDaily | Unset):
        monthly (V0044RollupStatsMonthly | Unset):
    """

    hourly: V0044RollupStatsHourly | Unset = UNSET
    daily: V0044RollupStatsDaily | Unset = UNSET
    monthly: V0044RollupStatsMonthly | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hourly: dict[str, Any] | Unset = UNSET
        if not isinstance(self.hourly, Unset):
            hourly = self.hourly.to_dict()

        daily: dict[str, Any] | Unset = UNSET
        if not isinstance(self.daily, Unset):
            daily = self.daily.to_dict()

        monthly: dict[str, Any] | Unset = UNSET
        if not isinstance(self.monthly, Unset):
            monthly = self.monthly.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hourly is not UNSET:
            field_dict["hourly"] = hourly
        if daily is not UNSET:
            field_dict["daily"] = daily
        if monthly is not UNSET:
            field_dict["monthly"] = monthly

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v0044_rollup_stats_daily import V0044RollupStatsDaily
        from ..models.v0044_rollup_stats_hourly import V0044RollupStatsHourly
        from ..models.v0044_rollup_stats_monthly import V0044RollupStatsMonthly

        d = dict(src_dict)
        _hourly = d.pop("hourly", UNSET)
        hourly: V0044RollupStatsHourly | Unset
        if isinstance(_hourly, Unset):
            hourly = UNSET
        else:
            hourly = V0044RollupStatsHourly.from_dict(_hourly)

        _daily = d.pop("daily", UNSET)
        daily: V0044RollupStatsDaily | Unset
        if isinstance(_daily, Unset):
            daily = UNSET
        else:
            daily = V0044RollupStatsDaily.from_dict(_daily)

        _monthly = d.pop("monthly", UNSET)
        monthly: V0044RollupStatsMonthly | Unset
        if isinstance(_monthly, Unset):
            monthly = UNSET
        else:
            monthly = V0044RollupStatsMonthly.from_dict(_monthly)

        v0044_rollup_stats = cls(
            hourly=hourly,
            daily=daily,
            monthly=monthly,
        )

        v0044_rollup_stats.additional_properties = d
        return v0044_rollup_stats

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
