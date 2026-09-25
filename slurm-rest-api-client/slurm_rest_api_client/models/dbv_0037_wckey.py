from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Dbv0037Wckey")


@_attrs_define
class Dbv0037Wckey:
    """
    Attributes:
        accounts (list[str] | Unset): List of assigned accounts
        cluster (str | Unset): Cluster name
        id (int | Unset): wckey database unique id
        name (str | Unset): wckey name
        user (str | Unset): wckey user
        flags (list[str] | Unset): List of properties of wckey
    """

    accounts: list[str] | Unset = UNSET
    cluster: str | Unset = UNSET
    id: int | Unset = UNSET
    name: str | Unset = UNSET
    user: str | Unset = UNSET
    flags: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        accounts: list[str] | Unset = UNSET
        if not isinstance(self.accounts, Unset):
            accounts = self.accounts

        cluster = self.cluster

        id = self.id

        name = self.name

        user = self.user

        flags: list[str] | Unset = UNSET
        if not isinstance(self.flags, Unset):
            flags = self.flags

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if accounts is not UNSET:
            field_dict["accounts"] = accounts
        if cluster is not UNSET:
            field_dict["cluster"] = cluster
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if user is not UNSET:
            field_dict["user"] = user
        if flags is not UNSET:
            field_dict["flags"] = flags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        accounts = cast(list[str], d.pop("accounts", UNSET))

        cluster = d.pop("cluster", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        user = d.pop("user", UNSET)

        flags = cast(list[str], d.pop("flags", UNSET))

        dbv_0037_wckey = cls(
            accounts=accounts,
            cluster=cluster,
            id=id,
            name=name,
            user=user,
            flags=flags,
        )

        dbv_0037_wckey.additional_properties = d
        return dbv_0037_wckey

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
