from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.slurm_v0041_post_job_submit_body_job_crontab_flags_item import (
    SlurmV0041PostJobSubmitBodyJobCrontabFlagsItem,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.slurm_v0041_post_job_submit_body_job_crontab_line import SlurmV0041PostJobSubmitBodyJobCrontabLine


T = TypeVar("T", bound="SlurmV0041PostJobSubmitBodyJobCrontab")


@_attrs_define
class SlurmV0041PostJobSubmitBodyJobCrontab:
    """Specification for scrontab job

    Attributes:
        flags (list[SlurmV0041PostJobSubmitBodyJobCrontabFlagsItem] | Unset): Flags
        minute (str | Unset): Ranged string specifying eligible minute values (e.g. 0-10,50)
        hour (str | Unset): Ranged string specifying eligible hour values (e.g. 0-5,23)
        day_of_month (str | Unset): Ranged string specifying eligible day of month values (e.g. 0-10,29)
        month (str | Unset): Ranged string specifying eligible month values (e.g. 0-5,12)
        day_of_week (str | Unset): Ranged string specifying eligible day of week values (e.g.0-3,7)
        specification (str | Unset): Time specification (* means valid for all allowed values) - minute hour
            day_of_month month day_of_week
        command (str | Unset): Command to run
        line (SlurmV0041PostJobSubmitBodyJobCrontabLine | Unset):
    """

    flags: list[SlurmV0041PostJobSubmitBodyJobCrontabFlagsItem] | Unset = UNSET
    minute: str | Unset = UNSET
    hour: str | Unset = UNSET
    day_of_month: str | Unset = UNSET
    month: str | Unset = UNSET
    day_of_week: str | Unset = UNSET
    specification: str | Unset = UNSET
    command: str | Unset = UNSET
    line: SlurmV0041PostJobSubmitBodyJobCrontabLine | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        flags: list[str] | Unset = UNSET
        if not isinstance(self.flags, Unset):
            flags = []
            for flags_item_data in self.flags:
                flags_item = flags_item_data.value
                flags.append(flags_item)

        minute = self.minute

        hour = self.hour

        day_of_month = self.day_of_month

        month = self.month

        day_of_week = self.day_of_week

        specification = self.specification

        command = self.command

        line: dict[str, Any] | Unset = UNSET
        if not isinstance(self.line, Unset):
            line = self.line.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if flags is not UNSET:
            field_dict["flags"] = flags
        if minute is not UNSET:
            field_dict["minute"] = minute
        if hour is not UNSET:
            field_dict["hour"] = hour
        if day_of_month is not UNSET:
            field_dict["day_of_month"] = day_of_month
        if month is not UNSET:
            field_dict["month"] = month
        if day_of_week is not UNSET:
            field_dict["day_of_week"] = day_of_week
        if specification is not UNSET:
            field_dict["specification"] = specification
        if command is not UNSET:
            field_dict["command"] = command
        if line is not UNSET:
            field_dict["line"] = line

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.slurm_v0041_post_job_submit_body_job_crontab_line import SlurmV0041PostJobSubmitBodyJobCrontabLine

        d = dict(src_dict)
        _flags = d.pop("flags", UNSET)
        flags: list[SlurmV0041PostJobSubmitBodyJobCrontabFlagsItem] | Unset = UNSET
        if _flags is not UNSET:
            flags = []
            for flags_item_data in _flags:
                flags_item = SlurmV0041PostJobSubmitBodyJobCrontabFlagsItem(flags_item_data)

                flags.append(flags_item)

        minute = d.pop("minute", UNSET)

        hour = d.pop("hour", UNSET)

        day_of_month = d.pop("day_of_month", UNSET)

        month = d.pop("month", UNSET)

        day_of_week = d.pop("day_of_week", UNSET)

        specification = d.pop("specification", UNSET)

        command = d.pop("command", UNSET)

        _line = d.pop("line", UNSET)
        line: SlurmV0041PostJobSubmitBodyJobCrontabLine | Unset
        if isinstance(_line, Unset):
            line = UNSET
        else:
            line = SlurmV0041PostJobSubmitBodyJobCrontabLine.from_dict(_line)

        slurm_v0041_post_job_submit_body_job_crontab = cls(
            flags=flags,
            minute=minute,
            hour=hour,
            day_of_month=day_of_month,
            month=month,
            day_of_week=day_of_week,
            specification=specification,
            command=command,
            line=line,
        )

        slurm_v0041_post_job_submit_body_job_crontab.additional_properties = d
        return slurm_v0041_post_job_submit_body_job_crontab

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
