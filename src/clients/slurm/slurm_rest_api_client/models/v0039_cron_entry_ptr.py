from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.v0039_cron_entry_ptr_flags_item import V0039CronEntryPtrFlagsItem
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v0039_cron_entry_ptr_line import V0039CronEntryPtrLine


T = TypeVar("T", bound="V0039CronEntryPtr")


@_attrs_define
class V0039CronEntryPtr:
    """
    Attributes:
        flags (list[V0039CronEntryPtrFlagsItem] | Unset):
        minute (str | Unset):
        hour (str | Unset):
        day_of_month (str | Unset):
        month (str | Unset):
        day_of_week (str | Unset):
        specification (str | Unset):
        command (str | Unset):
        line (V0039CronEntryPtrLine | Unset):
    """

    flags: list[V0039CronEntryPtrFlagsItem] | Unset = UNSET
    minute: str | Unset = UNSET
    hour: str | Unset = UNSET
    day_of_month: str | Unset = UNSET
    month: str | Unset = UNSET
    day_of_week: str | Unset = UNSET
    specification: str | Unset = UNSET
    command: str | Unset = UNSET
    line: V0039CronEntryPtrLine | Unset = UNSET
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
        from ..models.v0039_cron_entry_ptr_line import V0039CronEntryPtrLine

        d = dict(src_dict)
        _flags = d.pop("flags", UNSET)
        flags: list[V0039CronEntryPtrFlagsItem] | Unset = UNSET
        if _flags is not UNSET:
            flags = []
            for flags_item_data in _flags:
                flags_item = V0039CronEntryPtrFlagsItem(flags_item_data)

                flags.append(flags_item)

        minute = d.pop("minute", UNSET)

        hour = d.pop("hour", UNSET)

        day_of_month = d.pop("day_of_month", UNSET)

        month = d.pop("month", UNSET)

        day_of_week = d.pop("day_of_week", UNSET)

        specification = d.pop("specification", UNSET)

        command = d.pop("command", UNSET)

        _line = d.pop("line", UNSET)
        line: V0039CronEntryPtrLine | Unset
        if isinstance(_line, Unset):
            line = UNSET
        else:
            line = V0039CronEntryPtrLine.from_dict(_line)

        v0039_cron_entry_ptr = cls(
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

        v0039_cron_entry_ptr.additional_properties = d
        return v0039_cron_entry_ptr

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
