from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.slurm_v0041_get_licenses_response_default_errors_item import (
        SlurmV0041GetLicensesResponseDefaultErrorsItem,
    )
    from ..models.slurm_v0041_get_licenses_response_default_last_update import (
        SlurmV0041GetLicensesResponseDefaultLastUpdate,
    )
    from ..models.slurm_v0041_get_licenses_response_default_licenses_item import (
        SlurmV0041GetLicensesResponseDefaultLicensesItem,
    )
    from ..models.slurm_v0041_get_licenses_response_default_meta import SlurmV0041GetLicensesResponseDefaultMeta
    from ..models.slurm_v0041_get_licenses_response_default_warnings_item import (
        SlurmV0041GetLicensesResponseDefaultWarningsItem,
    )


T = TypeVar("T", bound="SlurmV0041GetLicensesResponseDefault")


@_attrs_define
class SlurmV0041GetLicensesResponseDefault:
    """
    Attributes:
        licenses (list[SlurmV0041GetLicensesResponseDefaultLicensesItem]): List of licenses
        last_update (SlurmV0041GetLicensesResponseDefaultLastUpdate): Time of last licenses change (UNIX timestamp)
        meta (SlurmV0041GetLicensesResponseDefaultMeta | Unset): Slurm meta values
        errors (list[SlurmV0041GetLicensesResponseDefaultErrorsItem] | Unset): Query errors
        warnings (list[SlurmV0041GetLicensesResponseDefaultWarningsItem] | Unset): Query warnings
    """

    licenses: list[SlurmV0041GetLicensesResponseDefaultLicensesItem]
    last_update: SlurmV0041GetLicensesResponseDefaultLastUpdate
    meta: SlurmV0041GetLicensesResponseDefaultMeta | Unset = UNSET
    errors: list[SlurmV0041GetLicensesResponseDefaultErrorsItem] | Unset = UNSET
    warnings: list[SlurmV0041GetLicensesResponseDefaultWarningsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        licenses = []
        for licenses_item_data in self.licenses:
            licenses_item = licenses_item_data.to_dict()
            licenses.append(licenses_item)

        last_update = self.last_update.to_dict()

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
                "licenses": licenses,
                "last_update": last_update,
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
        from ..models.slurm_v0041_get_licenses_response_default_errors_item import (
            SlurmV0041GetLicensesResponseDefaultErrorsItem,
        )
        from ..models.slurm_v0041_get_licenses_response_default_last_update import (
            SlurmV0041GetLicensesResponseDefaultLastUpdate,
        )
        from ..models.slurm_v0041_get_licenses_response_default_licenses_item import (
            SlurmV0041GetLicensesResponseDefaultLicensesItem,
        )
        from ..models.slurm_v0041_get_licenses_response_default_meta import SlurmV0041GetLicensesResponseDefaultMeta
        from ..models.slurm_v0041_get_licenses_response_default_warnings_item import (
            SlurmV0041GetLicensesResponseDefaultWarningsItem,
        )

        d = dict(src_dict)
        licenses = []
        _licenses = d.pop("licenses")
        for licenses_item_data in _licenses:
            licenses_item = SlurmV0041GetLicensesResponseDefaultLicensesItem.from_dict(licenses_item_data)

            licenses.append(licenses_item)

        last_update = SlurmV0041GetLicensesResponseDefaultLastUpdate.from_dict(d.pop("last_update"))

        _meta = d.pop("meta", UNSET)
        meta: SlurmV0041GetLicensesResponseDefaultMeta | Unset
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = SlurmV0041GetLicensesResponseDefaultMeta.from_dict(_meta)

        _errors = d.pop("errors", UNSET)
        errors: list[SlurmV0041GetLicensesResponseDefaultErrorsItem] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = SlurmV0041GetLicensesResponseDefaultErrorsItem.from_dict(errors_item_data)

                errors.append(errors_item)

        _warnings = d.pop("warnings", UNSET)
        warnings: list[SlurmV0041GetLicensesResponseDefaultWarningsItem] | Unset = UNSET
        if _warnings is not UNSET:
            warnings = []
            for warnings_item_data in _warnings:
                warnings_item = SlurmV0041GetLicensesResponseDefaultWarningsItem.from_dict(warnings_item_data)

                warnings.append(warnings_item)

        slurm_v0041_get_licenses_response_default = cls(
            licenses=licenses,
            last_update=last_update,
            meta=meta,
            errors=errors,
            warnings=warnings,
        )

        slurm_v0041_get_licenses_response_default.additional_properties = d
        return slurm_v0041_get_licenses_response_default

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
