from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v0039_error import V0039Error
    from ..models.v0039_meta import V0039Meta
    from ..models.v0039_warning import V0039Warning


T = TypeVar("T", bound="V0039JobSubmissionResponse")


@_attrs_define
class V0039JobSubmissionResponse:
    """
    Attributes:
        meta (V0039Meta | Unset):
        errors (list[V0039Error] | Unset): Slurm errors
        warnings (list[V0039Warning] | Unset): Slurm warnings
        job_id (int | Unset): new job ID
        step_id (str | Unset): new job step ID
        job_submit_user_msg (str | Unset): Message to user from job_submit plugin
    """

    meta: V0039Meta | Unset = UNSET
    errors: list[V0039Error] | Unset = UNSET
    warnings: list[V0039Warning] | Unset = UNSET
    job_id: int | Unset = UNSET
    step_id: str | Unset = UNSET
    job_submit_user_msg: str | Unset = UNSET
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

        job_id = self.job_id

        step_id = self.step_id

        job_submit_user_msg = self.job_submit_user_msg

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if meta is not UNSET:
            field_dict["meta"] = meta
        if errors is not UNSET:
            field_dict["errors"] = errors
        if warnings is not UNSET:
            field_dict["warnings"] = warnings
        if job_id is not UNSET:
            field_dict["job_id"] = job_id
        if step_id is not UNSET:
            field_dict["step_id"] = step_id
        if job_submit_user_msg is not UNSET:
            field_dict["job_submit_user_msg"] = job_submit_user_msg

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v0039_error import V0039Error
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

        job_id = d.pop("job_id", UNSET)

        step_id = d.pop("step_id", UNSET)

        job_submit_user_msg = d.pop("job_submit_user_msg", UNSET)

        v0039_job_submission_response = cls(
            meta=meta,
            errors=errors,
            warnings=warnings,
            job_id=job_id,
            step_id=step_id,
            job_submit_user_msg=job_submit_user_msg,
        )

        v0039_job_submission_response.additional_properties = d
        return v0039_job_submission_response

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
