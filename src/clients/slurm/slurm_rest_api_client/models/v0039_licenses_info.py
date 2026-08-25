from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v0039_error import V0039Error
    from ..models.v0039_license import V0039License
    from ..models.v0039_meta import V0039Meta
    from ..models.v0039_warning import V0039Warning


T = TypeVar("T", bound="V0039LicensesInfo")


@_attrs_define
class V0039LicensesInfo:
    """
    Attributes:
        meta (V0039Meta | Unset):
        errors (list[V0039Error] | Unset): Slurm errors
        warnings (list[V0039Warning] | Unset): Slurm warnings
        licenses (list[V0039License] | Unset):
    """

    meta: V0039Meta | Unset = UNSET
    errors: list[V0039Error] | Unset = UNSET
    warnings: list[V0039Warning] | Unset = UNSET
    licenses: list[V0039License] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        meta: dict[str, Any] | Unset = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        errors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for componentsschemasv0_0_39_errors_item_data in self.errors:
                componentsschemasv0_0_39_errors_item = componentsschemasv0_0_39_errors_item_data.to_dict()
                errors.append(componentsschemasv0_0_39_errors_item)

        warnings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = []
            for componentsschemasv0_0_39_warnings_item_data in self.warnings:
                componentsschemasv0_0_39_warnings_item = componentsschemasv0_0_39_warnings_item_data.to_dict()
                warnings.append(componentsschemasv0_0_39_warnings_item)

        licenses: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.licenses, Unset):
            licenses = []
            for componentsschemasv0_0_39_licenses_item_data in self.licenses:
                componentsschemasv0_0_39_licenses_item = componentsschemasv0_0_39_licenses_item_data.to_dict()
                licenses.append(componentsschemasv0_0_39_licenses_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if meta is not UNSET:
            field_dict["meta"] = meta
        if errors is not UNSET:
            field_dict["errors"] = errors
        if warnings is not UNSET:
            field_dict["warnings"] = warnings
        if licenses is not UNSET:
            field_dict["licenses"] = licenses

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v0039_error import V0039Error
        from ..models.v0039_license import V0039License
        from ..models.v0039_meta import V0039Meta
        from ..models.v0039_warning import V0039Warning

        d = dict(src_dict)
        _meta = d.pop("meta", UNSET)
        meta: V0039Meta | Unset
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = V0039Meta.from_dict(_meta)

        _errors = d.pop("errors", UNSET)
        errors: list[V0039Error] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for componentsschemasv0_0_39_errors_item_data in _errors:
                componentsschemasv0_0_39_errors_item = V0039Error.from_dict(componentsschemasv0_0_39_errors_item_data)

                errors.append(componentsschemasv0_0_39_errors_item)

        _warnings = d.pop("warnings", UNSET)
        warnings: list[V0039Warning] | Unset = UNSET
        if _warnings is not UNSET:
            warnings = []
            for componentsschemasv0_0_39_warnings_item_data in _warnings:
                componentsschemasv0_0_39_warnings_item = V0039Warning.from_dict(
                    componentsschemasv0_0_39_warnings_item_data
                )

                warnings.append(componentsschemasv0_0_39_warnings_item)

        _licenses = d.pop("licenses", UNSET)
        licenses: list[V0039License] | Unset = UNSET
        if _licenses is not UNSET:
            licenses = []
            for componentsschemasv0_0_39_licenses_item_data in _licenses:
                componentsschemasv0_0_39_licenses_item = V0039License.from_dict(
                    componentsschemasv0_0_39_licenses_item_data
                )

                licenses.append(componentsschemasv0_0_39_licenses_item)

        v0039_licenses_info = cls(
            meta=meta,
            errors=errors,
            warnings=warnings,
            licenses=licenses,
        )

        v0039_licenses_info.additional_properties = d
        return v0039_licenses_info

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
