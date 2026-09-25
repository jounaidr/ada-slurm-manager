from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v0039_error import V0039Error
    from ..models.v0039_job_array_response_msg_ptr_item import V0039JobArrayResponseMsgPtrItem
    from ..models.v0039_meta import V0039Meta
    from ..models.v0039_warning import V0039Warning


T = TypeVar("T", bound="V0039JobUpdateResponse")


@_attrs_define
class V0039JobUpdateResponse:
    """
    Attributes:
        meta (V0039Meta | Unset):
        errors (list[V0039Error] | Unset): Slurm errors
        warnings (list[V0039Warning] | Unset): Slurm warnings
        results (list[V0039JobArrayResponseMsgPtrItem] | Unset): Result per ArrayJob
    """

    meta: V0039Meta | Unset = UNSET
    errors: list[V0039Error] | Unset = UNSET
    warnings: list[V0039Warning] | Unset = UNSET
    results: list[V0039JobArrayResponseMsgPtrItem] | Unset = UNSET
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

        results: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.results, Unset):
            results = []
            for componentsschemasv0_0_39_job_array_response_msg_ptr_item_data in self.results:
                componentsschemasv0_0_39_job_array_response_msg_ptr_item = (
                    componentsschemasv0_0_39_job_array_response_msg_ptr_item_data.to_dict()
                )
                results.append(componentsschemasv0_0_39_job_array_response_msg_ptr_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if meta is not UNSET:
            field_dict["meta"] = meta
        if errors is not UNSET:
            field_dict["errors"] = errors
        if warnings is not UNSET:
            field_dict["warnings"] = warnings
        if results is not UNSET:
            field_dict["results"] = results

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v0039_error import V0039Error
        from ..models.v0039_job_array_response_msg_ptr_item import V0039JobArrayResponseMsgPtrItem
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

        _results = d.pop("results", UNSET)
        results: list[V0039JobArrayResponseMsgPtrItem] | Unset = UNSET
        if _results is not UNSET:
            results = []
            for componentsschemasv0_0_39_job_array_response_msg_ptr_item_data in _results:
                componentsschemasv0_0_39_job_array_response_msg_ptr_item = V0039JobArrayResponseMsgPtrItem.from_dict(
                    componentsschemasv0_0_39_job_array_response_msg_ptr_item_data
                )

                results.append(componentsschemasv0_0_39_job_array_response_msg_ptr_item)

        v0039_job_update_response = cls(
            meta=meta,
            errors=errors,
            warnings=warnings,
            results=results,
        )

        v0039_job_update_response.additional_properties = d
        return v0039_job_update_response

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
