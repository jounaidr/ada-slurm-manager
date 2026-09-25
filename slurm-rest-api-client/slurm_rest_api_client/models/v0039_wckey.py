from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.v0039_wckey_flags_item import V0039WckeyFlagsItem
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v0039_accounting import V0039Accounting


T = TypeVar("T", bound="V0039Wckey")


@_attrs_define
class V0039Wckey:
    """
    Attributes:
        cluster (str):
        name (str):
        user (str):
        accounting (list[V0039Accounting] | Unset):
        id (int | Unset):
        flags (list[V0039WckeyFlagsItem] | Unset):
    """

    cluster: str
    name: str
    user: str
    accounting: list[V0039Accounting] | Unset = UNSET
    id: int | Unset = UNSET
    flags: list[V0039WckeyFlagsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cluster = self.cluster

        name = self.name

        user = self.user

        accounting: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.accounting, Unset):
            accounting = []
            for componentsschemasv0_0_39_accounting_list_item_data in self.accounting:
                componentsschemasv0_0_39_accounting_list_item = (
                    componentsschemasv0_0_39_accounting_list_item_data.to_dict()
                )
                accounting.append(componentsschemasv0_0_39_accounting_list_item)

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
        from ..models.v0039_accounting import V0039Accounting

        d = dict(src_dict)
        cluster = d.pop("cluster")

        name = d.pop("name")

        user = d.pop("user")

        _accounting = d.pop("accounting", UNSET)
        accounting: list[V0039Accounting] | Unset = UNSET
        if _accounting is not UNSET:
            accounting = []
            for componentsschemasv0_0_39_accounting_list_item_data in _accounting:
                componentsschemasv0_0_39_accounting_list_item = V0039Accounting.from_dict(
                    componentsschemasv0_0_39_accounting_list_item_data
                )

                accounting.append(componentsschemasv0_0_39_accounting_list_item)

        id = d.pop("id", UNSET)

        _flags = d.pop("flags", UNSET)
        flags: list[V0039WckeyFlagsItem] | Unset = UNSET
        if _flags is not UNSET:
            flags = []
            for flags_item_data in _flags:
                flags_item = V0039WckeyFlagsItem(flags_item_data)

                flags.append(flags_item)

        v0039_wckey = cls(
            cluster=cluster,
            name=name,
            user=user,
            accounting=accounting,
            id=id,
            flags=flags,
        )

        v0039_wckey.additional_properties = d
        return v0039_wckey

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
