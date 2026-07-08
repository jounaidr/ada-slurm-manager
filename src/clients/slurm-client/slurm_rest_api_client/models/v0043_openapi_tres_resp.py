from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v0043_openapi_error import V0043OpenapiError
    from ..models.v0043_openapi_meta import V0043OpenapiMeta
    from ..models.v0043_openapi_warning import V0043OpenapiWarning
    from ..models.v0043_tres import V0043Tres


T = TypeVar("T", bound="V0043OpenapiTresResp")


@_attrs_define
class V0043OpenapiTresResp:
    """
    Attributes:
        tres (list[V0043Tres]):
        meta (V0043OpenapiMeta | Unset):
        errors (list[V0043OpenapiError] | Unset):
        warnings (list[V0043OpenapiWarning] | Unset):
    """

    tres: list[V0043Tres]
    meta: V0043OpenapiMeta | Unset = UNSET
    errors: list[V0043OpenapiError] | Unset = UNSET
    warnings: list[V0043OpenapiWarning] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tres = []
        for componentsschemasv0_0_43_tres_list_item_data in self.tres:
            componentsschemasv0_0_43_tres_list_item = componentsschemasv0_0_43_tres_list_item_data.to_dict()
            tres.append(componentsschemasv0_0_43_tres_list_item)

        meta: dict[str, Any] | Unset = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        errors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for componentsschemasv0_0_43_openapi_errors_item_data in self.errors:
                componentsschemasv0_0_43_openapi_errors_item = (
                    componentsschemasv0_0_43_openapi_errors_item_data.to_dict()
                )
                errors.append(componentsschemasv0_0_43_openapi_errors_item)

        warnings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = []
            for componentsschemasv0_0_43_openapi_warnings_item_data in self.warnings:
                componentsschemasv0_0_43_openapi_warnings_item = (
                    componentsschemasv0_0_43_openapi_warnings_item_data.to_dict()
                )
                warnings.append(componentsschemasv0_0_43_openapi_warnings_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "TRES": tres,
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
        from ..models.v0043_openapi_error import V0043OpenapiError
        from ..models.v0043_openapi_meta import V0043OpenapiMeta
        from ..models.v0043_openapi_warning import V0043OpenapiWarning
        from ..models.v0043_tres import V0043Tres

        d = dict(src_dict)
        tres = []
        _tres = d.pop("TRES")
        for componentsschemasv0_0_43_tres_list_item_data in _tres:
            componentsschemasv0_0_43_tres_list_item = V0043Tres.from_dict(componentsschemasv0_0_43_tres_list_item_data)

            tres.append(componentsschemasv0_0_43_tres_list_item)

        _meta = d.pop("meta", UNSET)
        meta: V0043OpenapiMeta | Unset
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = V0043OpenapiMeta.from_dict(_meta)

        _errors = d.pop("errors", UNSET)
        errors: list[V0043OpenapiError] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for componentsschemasv0_0_43_openapi_errors_item_data in _errors:
                componentsschemasv0_0_43_openapi_errors_item = V0043OpenapiError.from_dict(
                    componentsschemasv0_0_43_openapi_errors_item_data
                )

                errors.append(componentsschemasv0_0_43_openapi_errors_item)

        _warnings = d.pop("warnings", UNSET)
        warnings: list[V0043OpenapiWarning] | Unset = UNSET
        if _warnings is not UNSET:
            warnings = []
            for componentsschemasv0_0_43_openapi_warnings_item_data in _warnings:
                componentsschemasv0_0_43_openapi_warnings_item = V0043OpenapiWarning.from_dict(
                    componentsschemasv0_0_43_openapi_warnings_item_data
                )

                warnings.append(componentsschemasv0_0_43_openapi_warnings_item)

        v0043_openapi_tres_resp = cls(
            tres=tres,
            meta=meta,
            errors=errors,
            warnings=warnings,
        )

        v0043_openapi_tres_resp.additional_properties = d
        return v0043_openapi_tres_resp

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
