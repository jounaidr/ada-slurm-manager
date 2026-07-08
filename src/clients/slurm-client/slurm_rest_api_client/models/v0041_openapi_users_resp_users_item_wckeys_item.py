from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.v0041_openapi_users_resp_users_item_wckeys_item_flags_item import (
    V0041OpenapiUsersRespUsersItemWckeysItemFlagsItem,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v0041_openapi_users_resp_users_item_wckeys_item_accounting_item import (
        V0041OpenapiUsersRespUsersItemWckeysItemAccountingItem,
    )


T = TypeVar("T", bound="V0041OpenapiUsersRespUsersItemWckeysItem")


@_attrs_define
class V0041OpenapiUsersRespUsersItemWckeysItem:
    """
    Attributes:
        cluster (str): Cluster name
        name (str): WCKey name
        user (str): User name
        accounting (list[V0041OpenapiUsersRespUsersItemWckeysItemAccountingItem] | Unset): Accounting records containing
            related resource usage
        id (int | Unset): Unique ID for this user-cluster-wckey combination
        flags (list[V0041OpenapiUsersRespUsersItemWckeysItemFlagsItem] | Unset): Flags associated with the WCKey
    """

    cluster: str
    name: str
    user: str
    accounting: list[V0041OpenapiUsersRespUsersItemWckeysItemAccountingItem] | Unset = UNSET
    id: int | Unset = UNSET
    flags: list[V0041OpenapiUsersRespUsersItemWckeysItemFlagsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cluster = self.cluster

        name = self.name

        user = self.user

        accounting: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.accounting, Unset):
            accounting = []
            for accounting_item_data in self.accounting:
                accounting_item = accounting_item_data.to_dict()
                accounting.append(accounting_item)

        id = self.id

        flags: list[str] | Unset = UNSET
        if not isinstance(self.flags, Unset):
            flags = []
            for flags_item_data in self.flags:
                flags_item = flags_item_data.value
                flags.append(flags_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cluster": cluster,
                "name": name,
                "user": user,
            }
        )
        if accounting is not UNSET:
            field_dict["accounting"] = accounting
        if id is not UNSET:
            field_dict["id"] = id
        if flags is not UNSET:
            field_dict["flags"] = flags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v0041_openapi_users_resp_users_item_wckeys_item_accounting_item import (
            V0041OpenapiUsersRespUsersItemWckeysItemAccountingItem,
        )

        d = dict(src_dict)
        cluster = d.pop("cluster")

        name = d.pop("name")

        user = d.pop("user")

        _accounting = d.pop("accounting", UNSET)
        accounting: list[V0041OpenapiUsersRespUsersItemWckeysItemAccountingItem] | Unset = UNSET
        if _accounting is not UNSET:
            accounting = []
            for accounting_item_data in _accounting:
                accounting_item = V0041OpenapiUsersRespUsersItemWckeysItemAccountingItem.from_dict(accounting_item_data)

                accounting.append(accounting_item)

        id = d.pop("id", UNSET)

        _flags = d.pop("flags", UNSET)
        flags: list[V0041OpenapiUsersRespUsersItemWckeysItemFlagsItem] | Unset = UNSET
        if _flags is not UNSET:
            flags = []
            for flags_item_data in _flags:
                flags_item = V0041OpenapiUsersRespUsersItemWckeysItemFlagsItem(flags_item_data)

                flags.append(flags_item)

        v0041_openapi_users_resp_users_item_wckeys_item = cls(
            cluster=cluster,
            name=name,
            user=user,
            accounting=accounting,
            id=id,
            flags=flags,
        )

        v0041_openapi_users_resp_users_item_wckeys_item.additional_properties = d
        return v0041_openapi_users_resp_users_item_wckeys_item

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
