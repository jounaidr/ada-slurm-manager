from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.slurmdb_v0041_post_accounts_association_body_association_condition_association import (
        SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociation,
    )


T = TypeVar("T", bound="SlurmdbV0041PostAccountsAssociationBodyAssociationCondition")


@_attrs_define
class SlurmdbV0041PostAccountsAssociationBodyAssociationCondition:
    """CSV list of accounts, association limits and options, CSV list of clusters

    Attributes:
        accounts (list[str]): CSV accounts list
        association (SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociation | Unset): Association limits
            and options
        clusters (list[str] | Unset): CSV clusters list
    """

    accounts: list[str]
    association: SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociation | Unset = UNSET
    clusters: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        accounts = self.accounts

        association: dict[str, Any] | Unset = UNSET
        if not isinstance(self.association, Unset):
            association = self.association.to_dict()

        clusters: list[str] | Unset = UNSET
        if not isinstance(self.clusters, Unset):
            clusters = self.clusters

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accounts": accounts,
            }
        )
        if association is not UNSET:
            field_dict["association"] = association
        if clusters is not UNSET:
            field_dict["clusters"] = clusters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.slurmdb_v0041_post_accounts_association_body_association_condition_association import (
            SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociation,
        )

        d = dict(src_dict)
        accounts = cast(list[str], d.pop("accounts"))

        _association = d.pop("association", UNSET)
        association: SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociation | Unset
        if isinstance(_association, Unset):
            association = UNSET
        else:
            association = SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociation.from_dict(_association)

        clusters = cast(list[str], d.pop("clusters", UNSET))

        slurmdb_v0041_post_accounts_association_body_association_condition = cls(
            accounts=accounts,
            association=association,
            clusters=clusters,
        )

        slurmdb_v0041_post_accounts_association_body_association_condition.additional_properties = d
        return slurmdb_v0041_post_accounts_association_body_association_condition

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
