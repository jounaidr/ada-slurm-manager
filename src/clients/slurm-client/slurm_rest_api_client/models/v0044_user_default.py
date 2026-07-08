from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="V0044UserDefault")


@_attrs_define
class V0044UserDefault:
    """
    Attributes:
        qos (int | Unset): Default QOS
        account (str | Unset): Default account
        wckey (str | Unset): Default WCKey
    """

    qos: int | Unset = UNSET
    account: str | Unset = UNSET
    wckey: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        qos = self.qos

        account = self.account

        wckey = self.wckey

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if qos is not UNSET:
            field_dict["qos"] = qos
        if account is not UNSET:
            field_dict["account"] = account
        if wckey is not UNSET:
            field_dict["wckey"] = wckey

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        qos = d.pop("qos", UNSET)

        account = d.pop("account", UNSET)

        wckey = d.pop("wckey", UNSET)

        v0044_user_default = cls(
            qos=qos,
            account=account,
            wckey=wckey,
        )

        v0044_user_default.additional_properties = d
        return v0044_user_default

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
