from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v0043_job_array_response_msg_entry import V0043JobArrayResponseMsgEntry
    from ..models.v0043_openapi_error import V0043OpenapiError
    from ..models.v0043_openapi_meta import V0043OpenapiMeta
    from ..models.v0043_openapi_warning import V0043OpenapiWarning


T = TypeVar("T", bound="V0043OpenapiJobPostResponse")


@_attrs_define
class V0043OpenapiJobPostResponse:
    """
    Attributes:
        results (list[V0043JobArrayResponseMsgEntry] | Unset):
        meta (V0043OpenapiMeta | Unset):
        errors (list[V0043OpenapiError] | Unset):
        warnings (list[V0043OpenapiWarning] | Unset):
    """

    results: list[V0043JobArrayResponseMsgEntry] | Unset = UNSET
    meta: V0043OpenapiMeta | Unset = UNSET
    errors: list[V0043OpenapiError] | Unset = UNSET
    warnings: list[V0043OpenapiWarning] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        results: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.results, Unset):
            results = []
            for componentsschemasv0_0_43_job_array_response_array_item_data in self.results:
                componentsschemasv0_0_43_job_array_response_array_item = (
                    componentsschemasv0_0_43_job_array_response_array_item_data.to_dict()
                )
                results.append(componentsschemasv0_0_43_job_array_response_array_item)

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
        field_dict.update({})
        if results is not UNSET:
            field_dict["results"] = results
        if meta is not UNSET:
            field_dict["meta"] = meta
        if errors is not UNSET:
            field_dict["errors"] = errors
        if warnings is not UNSET:
            field_dict["warnings"] = warnings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v0043_job_array_response_msg_entry import V0043JobArrayResponseMsgEntry
        from ..models.v0043_openapi_error import V0043OpenapiError
        from ..models.v0043_openapi_meta import V0043OpenapiMeta
        from ..models.v0043_openapi_warning import V0043OpenapiWarning

        d = dict(src_dict)
        _results = d.pop("results", UNSET)
        results: list[V0043JobArrayResponseMsgEntry] | Unset = UNSET
        if _results is not UNSET:
            results = []
            for componentsschemasv0_0_43_job_array_response_array_item_data in _results:
                componentsschemasv0_0_43_job_array_response_array_item = V0043JobArrayResponseMsgEntry.from_dict(
                    componentsschemasv0_0_43_job_array_response_array_item_data
                )

                results.append(componentsschemasv0_0_43_job_array_response_array_item)

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

        v0043_openapi_job_post_response = cls(
            results=results,
            meta=meta,
            errors=errors,
            warnings=warnings,
        )

        v0043_openapi_job_post_response.additional_properties = d
        return v0043_openapi_job_post_response

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
