from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Dbv0038JobWckey")


@_attrs_define
class Dbv0038JobWckey:
    """Job assigned wckey details

    Attributes:
        wckey (str | Unset): Job assigned wckey
        flags (list[str] | Unset): wckey flags
    """

    wckey: str | Unset = UNSET
    flags: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        wckey = self.wckey

        flags: list[str] | Unset = UNSET
        if not isinstance(self.flags, Unset):
            flags = self.flags

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if wckey is not UNSET:
            field_dict["wckey"] = wckey
        if flags is not UNSET:
            field_dict["flags"] = flags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        wckey = d.pop("wckey", UNSET)

        flags = cast(list[str], d.pop("flags", UNSET))

        dbv_0038_job_wckey = cls(
            wckey=wckey,
            flags=flags,
        )

        dbv_0038_job_wckey.additional_properties = d
        return dbv_0038_job_wckey

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
