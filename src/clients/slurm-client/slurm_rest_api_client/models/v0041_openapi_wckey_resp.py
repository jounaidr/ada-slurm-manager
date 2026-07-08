from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v0041_openapi_wckey_resp_errors_item import V0041OpenapiWckeyRespErrorsItem
    from ..models.v0041_openapi_wckey_resp_meta import V0041OpenapiWckeyRespMeta
    from ..models.v0041_openapi_wckey_resp_warnings_item import V0041OpenapiWckeyRespWarningsItem
    from ..models.v0041_openapi_wckey_resp_wckeys_item import V0041OpenapiWckeyRespWckeysItem


T = TypeVar("T", bound="V0041OpenapiWckeyResp")


@_attrs_define
class V0041OpenapiWckeyResp:
    """
    Attributes:
        wckeys (list[V0041OpenapiWckeyRespWckeysItem]): wckeys
        meta (V0041OpenapiWckeyRespMeta | Unset): Slurm meta values
        errors (list[V0041OpenapiWckeyRespErrorsItem] | Unset): Query errors
        warnings (list[V0041OpenapiWckeyRespWarningsItem] | Unset): Query warnings
    """

    wckeys: list[V0041OpenapiWckeyRespWckeysItem]
    meta: V0041OpenapiWckeyRespMeta | Unset = UNSET
    errors: list[V0041OpenapiWckeyRespErrorsItem] | Unset = UNSET
    warnings: list[V0041OpenapiWckeyRespWarningsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        wckeys = []
        for wckeys_item_data in self.wckeys:
            wckeys_item = wckeys_item_data.to_dict()
            wckeys.append(wckeys_item)

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
                "wckeys": wckeys,
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
        from ..models.v0041_openapi_wckey_resp_errors_item import V0041OpenapiWckeyRespErrorsItem
        from ..models.v0041_openapi_wckey_resp_meta import V0041OpenapiWckeyRespMeta
        from ..models.v0041_openapi_wckey_resp_warnings_item import V0041OpenapiWckeyRespWarningsItem
        from ..models.v0041_openapi_wckey_resp_wckeys_item import V0041OpenapiWckeyRespWckeysItem

        d = dict(src_dict)
        wckeys = []
        _wckeys = d.pop("wckeys")
        for wckeys_item_data in _wckeys:
            wckeys_item = V0041OpenapiWckeyRespWckeysItem.from_dict(wckeys_item_data)

            wckeys.append(wckeys_item)

        _meta = d.pop("meta", UNSET)
        meta: V0041OpenapiWckeyRespMeta | Unset
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = V0041OpenapiWckeyRespMeta.from_dict(_meta)

        _errors = d.pop("errors", UNSET)
        errors: list[V0041OpenapiWckeyRespErrorsItem] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = V0041OpenapiWckeyRespErrorsItem.from_dict(errors_item_data)

                errors.append(errors_item)

        _warnings = d.pop("warnings", UNSET)
        warnings: list[V0041OpenapiWckeyRespWarningsItem] | Unset = UNSET
        if _warnings is not UNSET:
            warnings = []
            for warnings_item_data in _warnings:
                warnings_item = V0041OpenapiWckeyRespWarningsItem.from_dict(warnings_item_data)

                warnings.append(warnings_item)

        v0041_openapi_wckey_resp = cls(
            wckeys=wckeys,
            meta=meta,
            errors=errors,
            warnings=warnings,
        )

        v0041_openapi_wckey_resp.additional_properties = d
        return v0041_openapi_wckey_resp

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
