from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.slurm_v0041_get_shares_response_200_errors_item import SlurmV0041GetSharesResponse200ErrorsItem
    from ..models.slurm_v0041_get_shares_response_200_meta import SlurmV0041GetSharesResponse200Meta
    from ..models.slurm_v0041_get_shares_response_200_shares import SlurmV0041GetSharesResponse200Shares
    from ..models.slurm_v0041_get_shares_response_200_warnings_item import SlurmV0041GetSharesResponse200WarningsItem


T = TypeVar("T", bound="SlurmV0041GetSharesResponse200")


@_attrs_define
class SlurmV0041GetSharesResponse200:
    """
    Attributes:
        shares (SlurmV0041GetSharesResponse200Shares): fairshare info
        meta (SlurmV0041GetSharesResponse200Meta | Unset): Slurm meta values
        errors (list[SlurmV0041GetSharesResponse200ErrorsItem] | Unset): Query errors
        warnings (list[SlurmV0041GetSharesResponse200WarningsItem] | Unset): Query warnings
    """

    shares: SlurmV0041GetSharesResponse200Shares
    meta: SlurmV0041GetSharesResponse200Meta | Unset = UNSET
    errors: list[SlurmV0041GetSharesResponse200ErrorsItem] | Unset = UNSET
    warnings: list[SlurmV0041GetSharesResponse200WarningsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        shares = self.shares.to_dict()

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
                "shares": shares,
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
        from ..models.slurm_v0041_get_shares_response_200_errors_item import SlurmV0041GetSharesResponse200ErrorsItem
        from ..models.slurm_v0041_get_shares_response_200_meta import SlurmV0041GetSharesResponse200Meta
        from ..models.slurm_v0041_get_shares_response_200_shares import SlurmV0041GetSharesResponse200Shares
        from ..models.slurm_v0041_get_shares_response_200_warnings_item import (
            SlurmV0041GetSharesResponse200WarningsItem,
        )

        d = dict(src_dict)
        shares = SlurmV0041GetSharesResponse200Shares.from_dict(d.pop("shares"))

        _meta = d.pop("meta", UNSET)
        meta: SlurmV0041GetSharesResponse200Meta | Unset
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = SlurmV0041GetSharesResponse200Meta.from_dict(_meta)

        _errors = d.pop("errors", UNSET)
        errors: list[SlurmV0041GetSharesResponse200ErrorsItem] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = SlurmV0041GetSharesResponse200ErrorsItem.from_dict(errors_item_data)

                errors.append(errors_item)

        _warnings = d.pop("warnings", UNSET)
        warnings: list[SlurmV0041GetSharesResponse200WarningsItem] | Unset = UNSET
        if _warnings is not UNSET:
            warnings = []
            for warnings_item_data in _warnings:
                warnings_item = SlurmV0041GetSharesResponse200WarningsItem.from_dict(warnings_item_data)

                warnings.append(warnings_item)

        slurm_v0041_get_shares_response_200 = cls(
            shares=shares,
            meta=meta,
            errors=errors,
            warnings=warnings,
        )

        slurm_v0041_get_shares_response_200.additional_properties = d
        return slurm_v0041_get_shares_response_200

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
