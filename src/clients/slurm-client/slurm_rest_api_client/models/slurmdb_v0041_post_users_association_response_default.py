from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.slurmdb_v0041_post_users_association_response_default_errors_item import (
        SlurmdbV0041PostUsersAssociationResponseDefaultErrorsItem,
    )
    from ..models.slurmdb_v0041_post_users_association_response_default_meta import (
        SlurmdbV0041PostUsersAssociationResponseDefaultMeta,
    )
    from ..models.slurmdb_v0041_post_users_association_response_default_warnings_item import (
        SlurmdbV0041PostUsersAssociationResponseDefaultWarningsItem,
    )


T = TypeVar("T", bound="SlurmdbV0041PostUsersAssociationResponseDefault")


@_attrs_define
class SlurmdbV0041PostUsersAssociationResponseDefault:
    """
    Attributes:
        added_users (str): added_users
        meta (SlurmdbV0041PostUsersAssociationResponseDefaultMeta | Unset): Slurm meta values
        errors (list[SlurmdbV0041PostUsersAssociationResponseDefaultErrorsItem] | Unset): Query errors
        warnings (list[SlurmdbV0041PostUsersAssociationResponseDefaultWarningsItem] | Unset): Query warnings
    """

    added_users: str
    meta: SlurmdbV0041PostUsersAssociationResponseDefaultMeta | Unset = UNSET
    errors: list[SlurmdbV0041PostUsersAssociationResponseDefaultErrorsItem] | Unset = UNSET
    warnings: list[SlurmdbV0041PostUsersAssociationResponseDefaultWarningsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        added_users = self.added_users

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
        field_dict.update(
            {
                "added_users": added_users,
            }
        )
        if meta is not UNSET:
            field_dict["meta"] = meta
        if errors is not UNSET:
            field_dict["errors"] = errors
        if warnings is not UNSET:
            field_dict["warnings"] = warnings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.slurmdb_v0041_post_users_association_response_default_errors_item import (
            SlurmdbV0041PostUsersAssociationResponseDefaultErrorsItem,
        )
        from ..models.slurmdb_v0041_post_users_association_response_default_meta import (
            SlurmdbV0041PostUsersAssociationResponseDefaultMeta,
        )
        from ..models.slurmdb_v0041_post_users_association_response_default_warnings_item import (
            SlurmdbV0041PostUsersAssociationResponseDefaultWarningsItem,
        )

        d = dict(src_dict)
        added_users = d.pop("added_users")

        _meta = d.pop("meta", UNSET)
        meta: SlurmdbV0041PostUsersAssociationResponseDefaultMeta | Unset
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = SlurmdbV0041PostUsersAssociationResponseDefaultMeta.from_dict(_meta)

        _errors = d.pop("errors", UNSET)
        errors: list[SlurmdbV0041PostUsersAssociationResponseDefaultErrorsItem] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = SlurmdbV0041PostUsersAssociationResponseDefaultErrorsItem.from_dict(errors_item_data)

                errors.append(errors_item)

        _warnings = d.pop("warnings", UNSET)
        warnings: list[SlurmdbV0041PostUsersAssociationResponseDefaultWarningsItem] | Unset = UNSET
        if _warnings is not UNSET:
            warnings = []
            for warnings_item_data in _warnings:
                warnings_item = SlurmdbV0041PostUsersAssociationResponseDefaultWarningsItem.from_dict(
                    warnings_item_data
                )

                warnings.append(warnings_item)

        slurmdb_v0041_post_users_association_response_default = cls(
            added_users=added_users,
            meta=meta,
            errors=errors,
            warnings=warnings,
        )

        slurmdb_v0041_post_users_association_response_default.additional_properties = d
        return slurmdb_v0041_post_users_association_response_default

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
