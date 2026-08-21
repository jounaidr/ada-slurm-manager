from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v0041_openapi_tres_resp_errors_item import V0041OpenapiTresRespErrorsItem
    from ..models.v0041_openapi_tres_resp_meta import V0041OpenapiTresRespMeta
    from ..models.v0041_openapi_tres_resp_tres_item import V0041OpenapiTresRespTRESItem
    from ..models.v0041_openapi_tres_resp_warnings_item import V0041OpenapiTresRespWarningsItem


T = TypeVar("T", bound="V0041OpenapiTresResp")


@_attrs_define
class V0041OpenapiTresResp:
    """
    Attributes:
        tres (list[V0041OpenapiTresRespTRESItem]): TRES
        meta (V0041OpenapiTresRespMeta | Unset): Slurm meta values
        errors (list[V0041OpenapiTresRespErrorsItem] | Unset): Query errors
        warnings (list[V0041OpenapiTresRespWarningsItem] | Unset): Query warnings
    """

    tres: list[V0041OpenapiTresRespTRESItem]
    meta: V0041OpenapiTresRespMeta | Unset = UNSET
    errors: list[V0041OpenapiTresRespErrorsItem] | Unset = UNSET
    warnings: list[V0041OpenapiTresRespWarningsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tres = []
        for tres_item_data in self.tres:
            tres_item = tres_item_data.to_dict()
            tres.append(tres_item)

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
        from ..models.v0041_openapi_tres_resp_errors_item import V0041OpenapiTresRespErrorsItem
        from ..models.v0041_openapi_tres_resp_meta import V0041OpenapiTresRespMeta
        from ..models.v0041_openapi_tres_resp_tres_item import V0041OpenapiTresRespTRESItem
        from ..models.v0041_openapi_tres_resp_warnings_item import V0041OpenapiTresRespWarningsItem

        d = dict(src_dict)
        tres = []
        _tres = d.pop("TRES")
        for tres_item_data in _tres:
            tres_item = V0041OpenapiTresRespTRESItem.from_dict(tres_item_data)

            tres.append(tres_item)

        _meta = d.pop("meta", UNSET)
        meta: V0041OpenapiTresRespMeta | Unset
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = V0041OpenapiTresRespMeta.from_dict(_meta)

        _errors = d.pop("errors", UNSET)
        errors: list[V0041OpenapiTresRespErrorsItem] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = V0041OpenapiTresRespErrorsItem.from_dict(errors_item_data)

                errors.append(errors_item)

        _warnings = d.pop("warnings", UNSET)
        warnings: list[V0041OpenapiTresRespWarningsItem] | Unset = UNSET
        if _warnings is not UNSET:
            warnings = []
            for warnings_item_data in _warnings:
                warnings_item = V0041OpenapiTresRespWarningsItem.from_dict(warnings_item_data)

                warnings.append(warnings_item)

        v0041_openapi_tres_resp = cls(
            tres=tres,
            meta=meta,
            errors=errors,
            warnings=warnings,
        )

        v0041_openapi_tres_resp.additional_properties = d
        return v0041_openapi_tres_resp

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
