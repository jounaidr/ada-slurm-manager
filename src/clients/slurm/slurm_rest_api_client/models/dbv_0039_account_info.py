from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dbv_0039_error import Dbv0039Error
    from ..models.dbv_0039_meta import Dbv0039Meta
    from ..models.dbv_0039_warning import Dbv0039Warning
    from ..models.v0039_account import V0039Account


T = TypeVar("T", bound="Dbv0039AccountInfo")


@_attrs_define
class Dbv0039AccountInfo:
    """
    Attributes:
        meta (Dbv0039Meta | Unset):
        errors (list[Dbv0039Error] | Unset): Slurm errors
        warnings (list[Dbv0039Warning] | Unset): Slurm warnings
        accounts (list[V0039Account] | Unset):
    """

    meta: Dbv0039Meta | Unset = UNSET
    errors: list[Dbv0039Error] | Unset = UNSET
    warnings: list[Dbv0039Warning] | Unset = UNSET
    accounts: list[V0039Account] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        meta: dict[str, Any] | Unset = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        errors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for componentsschemasdbv0_0_39_errors_item_data in self.errors:
                componentsschemasdbv0_0_39_errors_item = componentsschemasdbv0_0_39_errors_item_data.to_dict()
                errors.append(componentsschemasdbv0_0_39_errors_item)

        warnings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = []
            for componentsschemasdbv0_0_39_warnings_item_data in self.warnings:
                componentsschemasdbv0_0_39_warnings_item = componentsschemasdbv0_0_39_warnings_item_data.to_dict()
                warnings.append(componentsschemasdbv0_0_39_warnings_item)

        accounts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.accounts, Unset):
            accounts = []
            for componentsschemasv0_0_39_account_list_item_data in self.accounts:
                componentsschemasv0_0_39_account_list_item = componentsschemasv0_0_39_account_list_item_data.to_dict()
                accounts.append(componentsschemasv0_0_39_account_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if meta is not UNSET:
            field_dict["meta"] = meta
        if errors is not UNSET:
            field_dict["errors"] = errors
        if warnings is not UNSET:
            field_dict["warnings"] = warnings
        if accounts is not UNSET:
            field_dict["accounts"] = accounts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dbv_0039_error import Dbv0039Error
        from ..models.dbv_0039_meta import Dbv0039Meta
        from ..models.dbv_0039_warning import Dbv0039Warning
        from ..models.v0039_account import V0039Account

        d = dict(src_dict)
        _meta = d.pop("meta", UNSET)
        meta: Dbv0039Meta | Unset
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = Dbv0039Meta.from_dict(_meta)

        _errors = d.pop("errors", UNSET)
        errors: list[Dbv0039Error] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for componentsschemasdbv0_0_39_errors_item_data in _errors:
                componentsschemasdbv0_0_39_errors_item = Dbv0039Error.from_dict(
                    componentsschemasdbv0_0_39_errors_item_data
                )

                errors.append(componentsschemasdbv0_0_39_errors_item)

        _warnings = d.pop("warnings", UNSET)
        warnings: list[Dbv0039Warning] | Unset = UNSET
        if _warnings is not UNSET:
            warnings = []
            for componentsschemasdbv0_0_39_warnings_item_data in _warnings:
                componentsschemasdbv0_0_39_warnings_item = Dbv0039Warning.from_dict(
                    componentsschemasdbv0_0_39_warnings_item_data
                )

                warnings.append(componentsschemasdbv0_0_39_warnings_item)

        _accounts = d.pop("accounts", UNSET)
        accounts: list[V0039Account] | Unset = UNSET
        if _accounts is not UNSET:
            accounts = []
            for componentsschemasv0_0_39_account_list_item_data in _accounts:
                componentsschemasv0_0_39_account_list_item = V0039Account.from_dict(
                    componentsschemasv0_0_39_account_list_item_data
                )

                accounts.append(componentsschemasv0_0_39_account_list_item)

        dbv_0039_account_info = cls(
            meta=meta,
            errors=errors,
            warnings=warnings,
            accounts=accounts,
        )

        dbv_0039_account_info.additional_properties = d
        return dbv_0039_account_info

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
