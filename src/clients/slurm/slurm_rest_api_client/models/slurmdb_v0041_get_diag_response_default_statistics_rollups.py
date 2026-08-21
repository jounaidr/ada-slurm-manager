from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.slurmdb_v0041_get_diag_response_default_statistics_rollups_daily import (
        SlurmdbV0041GetDiagResponseDefaultStatisticsRollupsDaily,
    )
    from ..models.slurmdb_v0041_get_diag_response_default_statistics_rollups_hourly import (
        SlurmdbV0041GetDiagResponseDefaultStatisticsRollupsHourly,
    )
    from ..models.slurmdb_v0041_get_diag_response_default_statistics_rollups_monthly import (
        SlurmdbV0041GetDiagResponseDefaultStatisticsRollupsMonthly,
    )


T = TypeVar("T", bound="SlurmdbV0041GetDiagResponseDefaultStatisticsRollups")


@_attrs_define
class SlurmdbV0041GetDiagResponseDefaultStatisticsRollups:
    """Rollup statistics

    Attributes:
        hourly (SlurmdbV0041GetDiagResponseDefaultStatisticsRollupsHourly | Unset):
        daily (SlurmdbV0041GetDiagResponseDefaultStatisticsRollupsDaily | Unset):
        monthly (SlurmdbV0041GetDiagResponseDefaultStatisticsRollupsMonthly | Unset):
    """

    hourly: SlurmdbV0041GetDiagResponseDefaultStatisticsRollupsHourly | Unset = UNSET
    daily: SlurmdbV0041GetDiagResponseDefaultStatisticsRollupsDaily | Unset = UNSET
    monthly: SlurmdbV0041GetDiagResponseDefaultStatisticsRollupsMonthly | Unset = UNSET
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
        from ..models.slurmdb_v0041_get_diag_response_default_statistics_rollups_daily import (
            SlurmdbV0041GetDiagResponseDefaultStatisticsRollupsDaily,
        )
        from ..models.slurmdb_v0041_get_diag_response_default_statistics_rollups_hourly import (
            SlurmdbV0041GetDiagResponseDefaultStatisticsRollupsHourly,
        )
        from ..models.slurmdb_v0041_get_diag_response_default_statistics_rollups_monthly import (
            SlurmdbV0041GetDiagResponseDefaultStatisticsRollupsMonthly,
        )

        d = dict(src_dict)
        _hourly = d.pop("hourly", UNSET)
        hourly: SlurmdbV0041GetDiagResponseDefaultStatisticsRollupsHourly | Unset
        if isinstance(_hourly, Unset):
            hourly = UNSET
        else:
            hourly = SlurmdbV0041GetDiagResponseDefaultStatisticsRollupsHourly.from_dict(_hourly)

        _daily = d.pop("daily", UNSET)
        daily: SlurmdbV0041GetDiagResponseDefaultStatisticsRollupsDaily | Unset
        if isinstance(_daily, Unset):
            daily = UNSET
        else:
            daily = SlurmdbV0041GetDiagResponseDefaultStatisticsRollupsDaily.from_dict(_daily)

        _monthly = d.pop("monthly", UNSET)
        monthly: SlurmdbV0041GetDiagResponseDefaultStatisticsRollupsMonthly | Unset
        if isinstance(_monthly, Unset):
            monthly = UNSET
        else:
            monthly = SlurmdbV0041GetDiagResponseDefaultStatisticsRollupsMonthly.from_dict(_monthly)

        slurmdb_v0041_get_diag_response_default_statistics_rollups = cls(
            hourly=hourly,
            daily=daily,
            monthly=monthly,
        )

        slurmdb_v0041_get_diag_response_default_statistics_rollups.additional_properties = d
        return slurmdb_v0041_get_diag_response_default_statistics_rollups

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
