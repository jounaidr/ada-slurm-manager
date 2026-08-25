from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Dbv0038AssociationUsage")


@_attrs_define
class Dbv0038AssociationUsage:
    """Association usage

    Attributes:
        accrue_job_count (int | Unset): Jobs accuring priority
        group_used_wallclock (float | Unset): Group used wallclock time (s)
        fairshare_factor (float | Unset): Fairshare factor
        fairshare_shares (int | Unset): Fairshare shares
        normalized_priority (int | Unset): Currently active jobs
        normalized_shares (float | Unset): Normalized shares
        effective_normalized_usage (float | Unset): Effective normalized usage
        raw_usage (int | Unset): Raw usage
        job_count (int | Unset): Total jobs submitted
        fairshare_level (float | Unset): Fairshare level
    """

    accrue_job_count: int | Unset = UNSET
    group_used_wallclock: float | Unset = UNSET
    fairshare_factor: float | Unset = UNSET
    fairshare_shares: int | Unset = UNSET
    normalized_priority: int | Unset = UNSET
    normalized_shares: float | Unset = UNSET
    effective_normalized_usage: float | Unset = UNSET
    raw_usage: int | Unset = UNSET
    job_count: int | Unset = UNSET
    fairshare_level: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        accrue_job_count = self.accrue_job_count

        group_used_wallclock = self.group_used_wallclock

        fairshare_factor = self.fairshare_factor

        fairshare_shares = self.fairshare_shares

        normalized_priority = self.normalized_priority

        normalized_shares = self.normalized_shares

        effective_normalized_usage = self.effective_normalized_usage

        raw_usage = self.raw_usage

        job_count = self.job_count

        fairshare_level = self.fairshare_level

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if accrue_job_count is not UNSET:
            field_dict["accrue_job_count"] = accrue_job_count
        if group_used_wallclock is not UNSET:
            field_dict["group_used_wallclock"] = group_used_wallclock
        if fairshare_factor is not UNSET:
            field_dict["fairshare_factor"] = fairshare_factor
        if fairshare_shares is not UNSET:
            field_dict["fairshare_shares"] = fairshare_shares
        if normalized_priority is not UNSET:
            field_dict["normalized_priority"] = normalized_priority
        if normalized_shares is not UNSET:
            field_dict["normalized_shares"] = normalized_shares
        if effective_normalized_usage is not UNSET:
            field_dict["effective_normalized_usage"] = effective_normalized_usage
        if raw_usage is not UNSET:
            field_dict["raw_usage"] = raw_usage
        if job_count is not UNSET:
            field_dict["job_count"] = job_count
        if fairshare_level is not UNSET:
            field_dict["fairshare_level"] = fairshare_level

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        accrue_job_count = d.pop("accrue_job_count", UNSET)

        group_used_wallclock = d.pop("group_used_wallclock", UNSET)

        fairshare_factor = d.pop("fairshare_factor", UNSET)

        fairshare_shares = d.pop("fairshare_shares", UNSET)

        normalized_priority = d.pop("normalized_priority", UNSET)

        normalized_shares = d.pop("normalized_shares", UNSET)

        effective_normalized_usage = d.pop("effective_normalized_usage", UNSET)

        raw_usage = d.pop("raw_usage", UNSET)

        job_count = d.pop("job_count", UNSET)

        fairshare_level = d.pop("fairshare_level", UNSET)

        dbv_0038_association_usage = cls(
            accrue_job_count=accrue_job_count,
            group_used_wallclock=group_used_wallclock,
            fairshare_factor=fairshare_factor,
            fairshare_shares=fairshare_shares,
            normalized_priority=normalized_priority,
            normalized_shares=normalized_shares,
            effective_normalized_usage=effective_normalized_usage,
            raw_usage=raw_usage,
            job_count=job_count,
            fairshare_level=fairshare_level,
        )

        dbv_0038_association_usage.additional_properties = d
        return dbv_0038_association_usage

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
