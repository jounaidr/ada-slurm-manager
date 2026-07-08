from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.slurmdb_v0041_post_accounts_association_body_account import (
        SlurmdbV0041PostAccountsAssociationBodyAccount,
    )
    from ..models.slurmdb_v0041_post_accounts_association_body_association_condition import (
        SlurmdbV0041PostAccountsAssociationBodyAssociationCondition,
    )
    from ..models.slurmdb_v0041_post_accounts_association_body_errors_item import (
        SlurmdbV0041PostAccountsAssociationBodyErrorsItem,
    )
    from ..models.slurmdb_v0041_post_accounts_association_body_meta import SlurmdbV0041PostAccountsAssociationBodyMeta
    from ..models.slurmdb_v0041_post_accounts_association_body_warnings_item import (
        SlurmdbV0041PostAccountsAssociationBodyWarningsItem,
    )


T = TypeVar("T", bound="SlurmdbV0041PostAccountsAssociationBody")


@_attrs_define
class SlurmdbV0041PostAccountsAssociationBody:
    """
    Attributes:
        association_condition (SlurmdbV0041PostAccountsAssociationBodyAssociationCondition | Unset): CSV list of
            accounts, association limits and options, CSV list of clusters
        account (SlurmdbV0041PostAccountsAssociationBodyAccount | Unset): Account organization and description
        meta (SlurmdbV0041PostAccountsAssociationBodyMeta | Unset): Slurm meta values
        errors (list[SlurmdbV0041PostAccountsAssociationBodyErrorsItem] | Unset): Query errors
        warnings (list[SlurmdbV0041PostAccountsAssociationBodyWarningsItem] | Unset): Query warnings
    """

    association_condition: SlurmdbV0041PostAccountsAssociationBodyAssociationCondition | Unset = UNSET
    account: SlurmdbV0041PostAccountsAssociationBodyAccount | Unset = UNSET
    meta: SlurmdbV0041PostAccountsAssociationBodyMeta | Unset = UNSET
    errors: list[SlurmdbV0041PostAccountsAssociationBodyErrorsItem] | Unset = UNSET
    warnings: list[SlurmdbV0041PostAccountsAssociationBodyWarningsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        association_condition: dict[str, Any] | Unset = UNSET
        if not isinstance(self.association_condition, Unset):
            association_condition = self.association_condition.to_dict()

        account: dict[str, Any] | Unset = UNSET
        if not isinstance(self.account, Unset):
            account = self.account.to_dict()

        meta: dict[str, Any] | Unset = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        errors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()
                errors.append(errors_item)

        warnings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = []
            for warnings_item_data in self.warnings:
                warnings_item = warnings_item_data.to_dict()
                warnings.append(warnings_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if association_condition is not UNSET:
            field_dict["association_condition"] = association_condition
        if account is not UNSET:
            field_dict["account"] = account
        if meta is not UNSET:
            field_dict["meta"] = meta
        if errors is not UNSET:
            field_dict["errors"] = errors
        if warnings is not UNSET:
            field_dict["warnings"] = warnings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.slurmdb_v0041_post_accounts_association_body_account import (
            SlurmdbV0041PostAccountsAssociationBodyAccount,
        )
        from ..models.slurmdb_v0041_post_accounts_association_body_association_condition import (
            SlurmdbV0041PostAccountsAssociationBodyAssociationCondition,
        )
        from ..models.slurmdb_v0041_post_accounts_association_body_errors_item import (
            SlurmdbV0041PostAccountsAssociationBodyErrorsItem,
        )
        from ..models.slurmdb_v0041_post_accounts_association_body_meta import (
            SlurmdbV0041PostAccountsAssociationBodyMeta,
        )
        from ..models.slurmdb_v0041_post_accounts_association_body_warnings_item import (
            SlurmdbV0041PostAccountsAssociationBodyWarningsItem,
        )

        d = dict(src_dict)
        _association_condition = d.pop("association_condition", UNSET)
        association_condition: SlurmdbV0041PostAccountsAssociationBodyAssociationCondition | Unset
        if isinstance(_association_condition, Unset):
            association_condition = UNSET
        else:
            association_condition = SlurmdbV0041PostAccountsAssociationBodyAssociationCondition.from_dict(
                _association_condition
            )

        _account = d.pop("account", UNSET)
        account: SlurmdbV0041PostAccountsAssociationBodyAccount | Unset
        if isinstance(_account, Unset):
            account = UNSET
        else:
            account = SlurmdbV0041PostAccountsAssociationBodyAccount.from_dict(_account)

        _meta = d.pop("meta", UNSET)
        meta: SlurmdbV0041PostAccountsAssociationBodyMeta | Unset
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = SlurmdbV0041PostAccountsAssociationBodyMeta.from_dict(_meta)

        _errors = d.pop("errors", UNSET)
        errors: list[SlurmdbV0041PostAccountsAssociationBodyErrorsItem] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = SlurmdbV0041PostAccountsAssociationBodyErrorsItem.from_dict(errors_item_data)

                errors.append(errors_item)

        _warnings = d.pop("warnings", UNSET)
        warnings: list[SlurmdbV0041PostAccountsAssociationBodyWarningsItem] | Unset = UNSET
        if _warnings is not UNSET:
            warnings = []
            for warnings_item_data in _warnings:
                warnings_item = SlurmdbV0041PostAccountsAssociationBodyWarningsItem.from_dict(warnings_item_data)

                warnings.append(warnings_item)

        slurmdb_v0041_post_accounts_association_body = cls(
            association_condition=association_condition,
            account=account,
            meta=meta,
            errors=errors,
            warnings=warnings,
        )

        slurmdb_v0041_post_accounts_association_body.additional_properties = d
        return slurmdb_v0041_post_accounts_association_body

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
