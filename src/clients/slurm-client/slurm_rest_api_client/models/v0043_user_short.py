from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.v0043_user_short_adminlevel_item import V0043UserShortAdminlevelItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="V0043UserShort")


@_attrs_define
class V0043UserShort:
    """
    Attributes:
        adminlevel (list[V0043UserShortAdminlevelItem] | Unset): AdminLevel granted to the user
        defaultaccount (str | Unset): Default account
        defaultwckey (str | Unset): Default WCKey
    """

    adminlevel: list[V0043UserShortAdminlevelItem] | Unset = UNSET
    defaultaccount: str | Unset = UNSET
    defaultwckey: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        adminlevel: list[str] | Unset = UNSET
        if not isinstance(self.adminlevel, Unset):
            adminlevel = []
            for adminlevel_item_data in self.adminlevel:
                adminlevel_item = adminlevel_item_data.value
                adminlevel.append(adminlevel_item)

        defaultaccount = self.defaultaccount

        defaultwckey = self.defaultwckey

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if adminlevel is not UNSET:
            field_dict["adminlevel"] = adminlevel
        if defaultaccount is not UNSET:
            field_dict["defaultaccount"] = defaultaccount
        if defaultwckey is not UNSET:
            field_dict["defaultwckey"] = defaultwckey

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _adminlevel = d.pop("adminlevel", UNSET)
        adminlevel: list[V0043UserShortAdminlevelItem] | Unset = UNSET
        if _adminlevel is not UNSET:
            adminlevel = []
            for adminlevel_item_data in _adminlevel:
                adminlevel_item = V0043UserShortAdminlevelItem(adminlevel_item_data)

                adminlevel.append(adminlevel_item)

        defaultaccount = d.pop("defaultaccount", UNSET)

        defaultwckey = d.pop("defaultwckey", UNSET)

        v0043_user_short = cls(
            adminlevel=adminlevel,
            defaultaccount=defaultaccount,
            defaultwckey=defaultwckey,
        )

        v0043_user_short.additional_properties = d
        return v0043_user_short

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
