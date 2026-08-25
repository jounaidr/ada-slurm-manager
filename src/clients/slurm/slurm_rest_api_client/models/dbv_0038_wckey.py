from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dbv_0038_accounting import Dbv0038Accounting


T = TypeVar("T", bound="Dbv0038Wckey")


@_attrs_define
class Dbv0038Wckey:
    """
    Attributes:
        cluster (str | Unset): Cluster name
        id (int | Unset): wckey database unique id
        name (str | Unset): wckey name
        user (str | Unset): wckey user
        flags (list[str] | Unset): List of properties of wckey
        accounting (list[Dbv0038Accounting] | Unset): List of accounting records
    """

    cluster: str | Unset = UNSET
    id: int | Unset = UNSET
    name: str | Unset = UNSET
    user: str | Unset = UNSET
    flags: list[str] | Unset = UNSET
    accounting: list[Dbv0038Accounting] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cluster = self.cluster

        id = self.id

        name = self.name

        user = self.user

        flags: list[str] | Unset = UNSET
        if not isinstance(self.flags, Unset):
            flags = self.flags

        accounting: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.accounting, Unset):
            accounting = []
            for accounting_item_data in self.accounting:
                accounting_item = accounting_item_data.to_dict()
                accounting.append(accounting_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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
        if accounting is not UNSET:
            field_dict["accounting"] = accounting

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dbv_0038_accounting import Dbv0038Accounting

        d = dict(src_dict)
        cluster = d.pop("cluster", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        user = d.pop("user", UNSET)

        flags = cast(list[str], d.pop("flags", UNSET))

        _accounting = d.pop("accounting", UNSET)
        accounting: list[Dbv0038Accounting] | Unset = UNSET
        if _accounting is not UNSET:
            accounting = []
            for accounting_item_data in _accounting:
                accounting_item = Dbv0038Accounting.from_dict(accounting_item_data)

                accounting.append(accounting_item)

        dbv_0038_wckey = cls(
            cluster=cluster,
            id=id,
            name=name,
            user=user,
            flags=flags,
            accounting=accounting,
        )

        dbv_0038_wckey.additional_properties = d
        return dbv_0038_wckey

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
