from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.slurmdb_v0041_post_users_association_body_user_adminlevel_item import (
    SlurmdbV0041PostUsersAssociationBodyUserAdminlevelItem,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SlurmdbV0041PostUsersAssociationBodyUser")


@_attrs_define
class SlurmdbV0041PostUsersAssociationBodyUser:
    """Admin level of user, DefaultAccount, DefaultWCKey

    Attributes:
        adminlevel (list[SlurmdbV0041PostUsersAssociationBodyUserAdminlevelItem] | Unset): AdminLevel granted to the
            user
        defaultaccount (str | Unset): Default account
        defaultwckey (str | Unset): Default WCKey
    """

    adminlevel: list[SlurmdbV0041PostUsersAssociationBodyUserAdminlevelItem] | Unset = UNSET
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
        adminlevel: list[SlurmdbV0041PostUsersAssociationBodyUserAdminlevelItem] | Unset = UNSET
        if _adminlevel is not UNSET:
            adminlevel = []
            for adminlevel_item_data in _adminlevel:
                adminlevel_item = SlurmdbV0041PostUsersAssociationBodyUserAdminlevelItem(adminlevel_item_data)

                adminlevel.append(adminlevel_item)

        defaultaccount = d.pop("defaultaccount", UNSET)

        defaultwckey = d.pop("defaultwckey", UNSET)

        slurmdb_v0041_post_users_association_body_user = cls(
            adminlevel=adminlevel,
            defaultaccount=defaultaccount,
            defaultwckey=defaultwckey,
        )

        slurmdb_v0041_post_users_association_body_user.additional_properties = d
        return slurmdb_v0041_post_users_association_body_user

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
