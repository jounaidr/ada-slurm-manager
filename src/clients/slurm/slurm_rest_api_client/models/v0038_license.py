from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="V0038License")


@_attrs_define
class V0038License:
    """
    Attributes:
        license_name (str | Unset): name of license
        total (int | Unset): total number of licenses
        used (int | Unset): number of licenses in use
        free (int | Unset): number of licenses available
        reserved (int | Unset): number of licenses reserved
        remote (bool | Unset): license is remote
    """

    license_name: str | Unset = UNSET
    total: int | Unset = UNSET
    used: int | Unset = UNSET
    free: int | Unset = UNSET
    reserved: int | Unset = UNSET
    remote: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        license_name = self.license_name

        total = self.total

        used = self.used

        free = self.free

        reserved = self.reserved

        remote = self.remote

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if license_name is not UNSET:
            field_dict["LicenseName"] = license_name
        if total is not UNSET:
            field_dict["Total"] = total
        if used is not UNSET:
            field_dict["Used"] = used
        if free is not UNSET:
            field_dict["Free"] = free
        if reserved is not UNSET:
            field_dict["Reserved"] = reserved
        if remote is not UNSET:
            field_dict["Remote"] = remote

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        license_name = d.pop("LicenseName", UNSET)

        total = d.pop("Total", UNSET)

        used = d.pop("Used", UNSET)

        free = d.pop("Free", UNSET)

        reserved = d.pop("Reserved", UNSET)

        remote = d.pop("Remote", UNSET)

        v0038_license = cls(
            license_name=license_name,
            total=total,
            used=used,
            free=free,
            reserved=reserved,
            remote=remote,
        )

        v0038_license.additional_properties = d
        return v0038_license

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
