from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v0044_job_modify import V0044JobModify
    from ..models.v0044_openapi_error import V0044OpenapiError
    from ..models.v0044_openapi_meta import V0044OpenapiMeta
    from ..models.v0044_openapi_warning import V0044OpenapiWarning


T = TypeVar("T", bound="V0044OpenapiJobModifyReq")


@_attrs_define
class V0044OpenapiJobModifyReq:
    """
    Attributes:
        job_id_list (list[str] | Unset):
        job_rec (V0044JobModify | Unset):
        meta (V0044OpenapiMeta | Unset):
        errors (list[V0044OpenapiError] | Unset):
        warnings (list[V0044OpenapiWarning] | Unset):
    """

    job_id_list: list[str] | Unset = UNSET
    job_rec: V0044JobModify | Unset = UNSET
    meta: V0044OpenapiMeta | Unset = UNSET
    errors: list[V0044OpenapiError] | Unset = UNSET
    warnings: list[V0044OpenapiWarning] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        job_id_list: list[str] | Unset = UNSET
        if not isinstance(self.job_id_list, Unset):
            job_id_list = self.job_id_list

        job_rec: dict[str, Any] | Unset = UNSET
        if not isinstance(self.job_rec, Unset):
            job_rec = self.job_rec.to_dict()

        meta: dict[str, Any] | Unset = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        errors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for componentsschemasv0_0_44_openapi_errors_item_data in self.errors:
                componentsschemasv0_0_44_openapi_errors_item = (
                    componentsschemasv0_0_44_openapi_errors_item_data.to_dict()
                )
                errors.append(componentsschemasv0_0_44_openapi_errors_item)

        warnings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = []
            for componentsschemasv0_0_44_openapi_warnings_item_data in self.warnings:
                componentsschemasv0_0_44_openapi_warnings_item = (
                    componentsschemasv0_0_44_openapi_warnings_item_data.to_dict()
                )
                warnings.append(componentsschemasv0_0_44_openapi_warnings_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if job_id_list is not UNSET:
            field_dict["job_id_list"] = job_id_list
        if job_rec is not UNSET:
            field_dict["job_rec"] = job_rec
        if meta is not UNSET:
            field_dict["meta"] = meta
        if errors is not UNSET:
            field_dict["errors"] = errors
        if warnings is not UNSET:
            field_dict["warnings"] = warnings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v0044_job_modify import V0044JobModify
        from ..models.v0044_openapi_error import V0044OpenapiError
        from ..models.v0044_openapi_meta import V0044OpenapiMeta
        from ..models.v0044_openapi_warning import V0044OpenapiWarning

        d = dict(src_dict)
        job_id_list = cast(list[str], d.pop("job_id_list", UNSET))

        _job_rec = d.pop("job_rec", UNSET)
        job_rec: V0044JobModify | Unset
        if isinstance(_job_rec, Unset):
            job_rec = UNSET
        else:
            job_rec = V0044JobModify.from_dict(_job_rec)

        _meta = d.pop("meta", UNSET)
        meta: V0044OpenapiMeta | Unset
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = V0044OpenapiMeta.from_dict(_meta)

        _errors = d.pop("errors", UNSET)
        errors: list[V0044OpenapiError] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for componentsschemasv0_0_44_openapi_errors_item_data in _errors:
                componentsschemasv0_0_44_openapi_errors_item = V0044OpenapiError.from_dict(
                    componentsschemasv0_0_44_openapi_errors_item_data
                )

                errors.append(componentsschemasv0_0_44_openapi_errors_item)

        _warnings = d.pop("warnings", UNSET)
        warnings: list[V0044OpenapiWarning] | Unset = UNSET
        if _warnings is not UNSET:
            warnings = []
            for componentsschemasv0_0_44_openapi_warnings_item_data in _warnings:
                componentsschemasv0_0_44_openapi_warnings_item = V0044OpenapiWarning.from_dict(
                    componentsschemasv0_0_44_openapi_warnings_item_data
                )

                warnings.append(componentsschemasv0_0_44_openapi_warnings_item)

        v0044_openapi_job_modify_req = cls(
            job_id_list=job_id_list,
            job_rec=job_rec,
            meta=meta,
            errors=errors,
            warnings=warnings,
        )

        v0044_openapi_job_modify_req.additional_properties = d
        return v0044_openapi_job_modify_req

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
