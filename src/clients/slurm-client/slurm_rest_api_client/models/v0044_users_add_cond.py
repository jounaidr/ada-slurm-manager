from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v0044_assoc_rec_set import V0044AssocRecSet


T = TypeVar("T", bound="V0044UsersAddCond")


@_attrs_define
class V0044UsersAddCond:
    """
    Attributes:
        users (list[str]):
        accounts (list[str] | Unset):
        association (V0044AssocRecSet | Unset):
        clusters (list[str] | Unset):
        partitions (list[str] | Unset):
        wckeys (list[str] | Unset):
    """

    users: list[str]
    accounts: list[str] | Unset = UNSET
    association: V0044AssocRecSet | Unset = UNSET
    clusters: list[str] | Unset = UNSET
    partitions: list[str] | Unset = UNSET
    wckeys: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        users = self.users

        accounts: list[str] | Unset = UNSET
        if not isinstance(self.accounts, Unset):
            accounts = self.accounts

        association: dict[str, Any] | Unset = UNSET
        if not isinstance(self.association, Unset):
            association = self.association.to_dict()

        clusters: list[str] | Unset = UNSET
        if not isinstance(self.clusters, Unset):
            clusters = self.clusters

        partitions: list[str] | Unset = UNSET
        if not isinstance(self.partitions, Unset):
            partitions = self.partitions

        wckeys: list[str] | Unset = UNSET
        if not isinstance(self.wckeys, Unset):
            wckeys = self.wckeys

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "users": users,
            }
        )
        if accounts is not UNSET:
            field_dict["accounts"] = accounts
        if association is not UNSET:
            field_dict["association"] = association
        if clusters is not UNSET:
            field_dict["clusters"] = clusters
        if partitions is not UNSET:
            field_dict["partitions"] = partitions
        if wckeys is not UNSET:
            field_dict["wckeys"] = wckeys

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v0044_assoc_rec_set import V0044AssocRecSet

        d = dict(src_dict)
        users = cast(list[str], d.pop("users"))

        accounts = cast(list[str], d.pop("accounts", UNSET))

        _association = d.pop("association", UNSET)
        association: V0044AssocRecSet | Unset
        if isinstance(_association, Unset):
            association = UNSET
        else:
            association = V0044AssocRecSet.from_dict(_association)

        clusters = cast(list[str], d.pop("clusters", UNSET))

        partitions = cast(list[str], d.pop("partitions", UNSET))

        wckeys = cast(list[str], d.pop("wckeys", UNSET))

        v0044_users_add_cond = cls(
            users=users,
            accounts=accounts,
            association=association,
            clusters=clusters,
            partitions=partitions,
            wckeys=wckeys,
        )

        v0044_users_add_cond.additional_properties = d
        return v0044_users_add_cond

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
