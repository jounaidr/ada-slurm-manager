from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.slurmdb_v0041_post_users_association_body_association_condition_association import (
        SlurmdbV0041PostUsersAssociationBodyAssociationConditionAssociation,
    )


T = TypeVar("T", bound="SlurmdbV0041PostUsersAssociationBodyAssociationCondition")


@_attrs_define
class SlurmdbV0041PostUsersAssociationBodyAssociationCondition:
    """Filters to select associations for users

    Attributes:
        users (list[str]): CSV users list
        accounts (list[str] | Unset): CSV accounts list
        association (SlurmdbV0041PostUsersAssociationBodyAssociationConditionAssociation | Unset): Association limits
            and options
        clusters (list[str] | Unset): CSV clusters list
        partitions (list[str] | Unset): CSV partitions list
        wckeys (list[str] | Unset): CSV WCKeys list
    """

    users: list[str]
    accounts: list[str] | Unset = UNSET
    association: SlurmdbV0041PostUsersAssociationBodyAssociationConditionAssociation | Unset = UNSET
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
        from ..models.slurmdb_v0041_post_users_association_body_association_condition_association import (
            SlurmdbV0041PostUsersAssociationBodyAssociationConditionAssociation,
        )

        d = dict(src_dict)
        users = cast(list[str], d.pop("users"))

        accounts = cast(list[str], d.pop("accounts", UNSET))

        _association = d.pop("association", UNSET)
        association: SlurmdbV0041PostUsersAssociationBodyAssociationConditionAssociation | Unset
        if isinstance(_association, Unset):
            association = UNSET
        else:
            association = SlurmdbV0041PostUsersAssociationBodyAssociationConditionAssociation.from_dict(_association)

        clusters = cast(list[str], d.pop("clusters", UNSET))

        partitions = cast(list[str], d.pop("partitions", UNSET))

        wckeys = cast(list[str], d.pop("wckeys", UNSET))

        slurmdb_v0041_post_users_association_body_association_condition = cls(
            users=users,
            accounts=accounts,
            association=association,
            clusters=clusters,
            partitions=partitions,
            wckeys=wckeys,
        )

        slurmdb_v0041_post_users_association_body_association_condition.additional_properties = d
        return slurmdb_v0041_post_users_association_body_association_condition

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
