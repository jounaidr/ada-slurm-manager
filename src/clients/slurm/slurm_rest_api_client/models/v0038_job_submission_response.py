from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v0038_error import V0038Error
    from ..models.v0038_meta import V0038Meta


T = TypeVar("T", bound="V0038JobSubmissionResponse")


@_attrs_define
class V0038JobSubmissionResponse:
    """
    Attributes:
        meta (V0038Meta | Unset):
        errors (list[V0038Error] | Unset): slurm errors
        job_id (int | Unset): new job ID
        step_id (str | Unset): new job step ID
        job_submit_user_msg (str | Unset): Message to user from job_submit plugin
    """

    meta: V0038Meta | Unset = UNSET
    errors: list[V0038Error] | Unset = UNSET
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
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()
                errors.append(errors_item)

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
        if job_id is not UNSET:
            field_dict["job_id"] = job_id
        if step_id is not UNSET:
            field_dict["step_id"] = step_id
        if job_submit_user_msg is not UNSET:
            field_dict["job_submit_user_msg"] = job_submit_user_msg

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v0038_error import V0038Error
        from ..models.v0038_meta import V0038Meta

        d = dict(src_dict)
        _meta = d.pop("meta", UNSET)
        meta: V0038Meta | Unset
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = V0038Meta.from_dict(_meta)

        _errors = d.pop("errors", UNSET)
        errors: list[V0038Error] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = V0038Error.from_dict(errors_item_data)

                errors.append(errors_item)

        job_id = d.pop("job_id", UNSET)

        step_id = d.pop("step_id", UNSET)

        job_submit_user_msg = d.pop("job_submit_user_msg", UNSET)

        v0038_job_submission_response = cls(
            meta=meta,
            errors=errors,
            job_id=job_id,
            step_id=step_id,
            job_submit_user_msg=job_submit_user_msg,
        )

        v0038_job_submission_response.additional_properties = d
        return v0038_job_submission_response

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
