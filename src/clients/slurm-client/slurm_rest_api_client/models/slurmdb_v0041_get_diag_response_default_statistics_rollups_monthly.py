from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.slurmdb_v0041_get_diag_response_default_statistics_rollups_monthly_duration import (
        SlurmdbV0041GetDiagResponseDefaultStatisticsRollupsMonthlyDuration,
    )


T = TypeVar("T", bound="SlurmdbV0041GetDiagResponseDefaultStatisticsRollupsMonthly")


@_attrs_define
class SlurmdbV0041GetDiagResponseDefaultStatisticsRollupsMonthly:
    """
    Attributes:
        count (int | Unset): Number of monthly rollups since last_run
        last_run (int | Unset): Last time monthly rollup ran (UNIX timestamp)
        duration (SlurmdbV0041GetDiagResponseDefaultStatisticsRollupsMonthlyDuration | Unset):
    """

    count: int | Unset = UNSET
    last_run: int | Unset = UNSET
    duration: SlurmdbV0041GetDiagResponseDefaultStatisticsRollupsMonthlyDuration | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        last_run = self.last_run

        duration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.duration, Unset):
            duration = self.duration.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if count is not UNSET:
            field_dict["count"] = count
        if last_run is not UNSET:
            field_dict["last_run"] = last_run
        if duration is not UNSET:
            field_dict["duration"] = duration

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.slurmdb_v0041_get_diag_response_default_statistics_rollups_monthly_duration import (
            SlurmdbV0041GetDiagResponseDefaultStatisticsRollupsMonthlyDuration,
        )

        d = dict(src_dict)
        count = d.pop("count", UNSET)

        last_run = d.pop("last_run", UNSET)

        _duration = d.pop("duration", UNSET)
        duration: SlurmdbV0041GetDiagResponseDefaultStatisticsRollupsMonthlyDuration | Unset
        if isinstance(_duration, Unset):
            duration = UNSET
        else:
            duration = SlurmdbV0041GetDiagResponseDefaultStatisticsRollupsMonthlyDuration.from_dict(_duration)

        slurmdb_v0041_get_diag_response_default_statistics_rollups_monthly = cls(
            count=count,
            last_run=last_run,
            duration=duration,
        )

        slurmdb_v0041_get_diag_response_default_statistics_rollups_monthly.additional_properties = d
        return slurmdb_v0041_get_diag_response_default_statistics_rollups_monthly

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
