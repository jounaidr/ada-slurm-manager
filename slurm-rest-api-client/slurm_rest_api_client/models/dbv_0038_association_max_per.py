from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dbv_0038_association_max_per_account import Dbv0038AssociationMaxPerAccount


T = TypeVar("T", bound="Dbv0038AssociationMaxPer")


@_attrs_define
class Dbv0038AssociationMaxPer:
    """Max per settings

    Attributes:
        account (Dbv0038AssociationMaxPerAccount | Unset): Max per accounting settings
    """

    account: Dbv0038AssociationMaxPerAccount | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account: dict[str, Any] | Unset = UNSET
        if not isinstance(self.account, Unset):
            account = self.account.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account is not UNSET:
            field_dict["account"] = account

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dbv_0038_association_max_per_account import Dbv0038AssociationMaxPerAccount

        d = dict(src_dict)
        _account = d.pop("account", UNSET)
        account: Dbv0038AssociationMaxPerAccount | Unset
        if isinstance(_account, Unset):
            account = UNSET
        else:
            account = Dbv0038AssociationMaxPerAccount.from_dict(_account)

        dbv_0038_association_max_per = cls(
            account=account,
        )

        dbv_0038_association_max_per.additional_properties = d
        return dbv_0038_association_max_per

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
