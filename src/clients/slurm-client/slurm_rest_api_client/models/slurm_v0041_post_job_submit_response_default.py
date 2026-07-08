from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.slurm_v0041_post_job_submit_response_default_errors_item import (
        SlurmV0041PostJobSubmitResponseDefaultErrorsItem,
    )
    from ..models.slurm_v0041_post_job_submit_response_default_meta import SlurmV0041PostJobSubmitResponseDefaultMeta
    from ..models.slurm_v0041_post_job_submit_response_default_result import (
        SlurmV0041PostJobSubmitResponseDefaultResult,
    )
    from ..models.slurm_v0041_post_job_submit_response_default_warnings_item import (
        SlurmV0041PostJobSubmitResponseDefaultWarningsItem,
    )


T = TypeVar("T", bound="SlurmV0041PostJobSubmitResponseDefault")


@_attrs_define
class SlurmV0041PostJobSubmitResponseDefault:
    """
    Attributes:
        result (SlurmV0041PostJobSubmitResponseDefaultResult | Unset): Job submission
        job_id (int | Unset): Submitted Job ID
        step_id (str | Unset): Submitted Step ID
        job_submit_user_msg (str | Unset): Job submission user message
        meta (SlurmV0041PostJobSubmitResponseDefaultMeta | Unset): Slurm meta values
        errors (list[SlurmV0041PostJobSubmitResponseDefaultErrorsItem] | Unset): Query errors
        warnings (list[SlurmV0041PostJobSubmitResponseDefaultWarningsItem] | Unset): Query warnings
    """

    result: SlurmV0041PostJobSubmitResponseDefaultResult | Unset = UNSET
    job_id: int | Unset = UNSET
    step_id: str | Unset = UNSET
    job_submit_user_msg: str | Unset = UNSET
    meta: SlurmV0041PostJobSubmitResponseDefaultMeta | Unset = UNSET
    errors: list[SlurmV0041PostJobSubmitResponseDefaultErrorsItem] | Unset = UNSET
    warnings: list[SlurmV0041PostJobSubmitResponseDefaultWarningsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        result: dict[str, Any] | Unset = UNSET
        if not isinstance(self.result, Unset):
            result = self.result.to_dict()

        job_id = self.job_id

        step_id = self.step_id

        job_submit_user_msg = self.job_submit_user_msg

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
        field_dict.update({})
        if result is not UNSET:
            field_dict["result"] = result
        if job_id is not UNSET:
            field_dict["job_id"] = job_id
        if step_id is not UNSET:
            field_dict["step_id"] = step_id
        if job_submit_user_msg is not UNSET:
            field_dict["job_submit_user_msg"] = job_submit_user_msg
        if meta is not UNSET:
            field_dict["meta"] = meta
        if errors is not UNSET:
            field_dict["errors"] = errors
        if warnings is not UNSET:
            field_dict["warnings"] = warnings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.slurm_v0041_post_job_submit_response_default_errors_item import (
            SlurmV0041PostJobSubmitResponseDefaultErrorsItem,
        )
        from ..models.slurm_v0041_post_job_submit_response_default_meta import (
            SlurmV0041PostJobSubmitResponseDefaultMeta,
        )
        from ..models.slurm_v0041_post_job_submit_response_default_result import (
            SlurmV0041PostJobSubmitResponseDefaultResult,
        )
        from ..models.slurm_v0041_post_job_submit_response_default_warnings_item import (
            SlurmV0041PostJobSubmitResponseDefaultWarningsItem,
        )

        d = dict(src_dict)
        _result = d.pop("result", UNSET)
        result: SlurmV0041PostJobSubmitResponseDefaultResult | Unset
        if isinstance(_result, Unset):
            result = UNSET
        else:
            result = SlurmV0041PostJobSubmitResponseDefaultResult.from_dict(_result)

        job_id = d.pop("job_id", UNSET)

        step_id = d.pop("step_id", UNSET)

        job_submit_user_msg = d.pop("job_submit_user_msg", UNSET)

        _meta = d.pop("meta", UNSET)
        meta: SlurmV0041PostJobSubmitResponseDefaultMeta | Unset
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = SlurmV0041PostJobSubmitResponseDefaultMeta.from_dict(_meta)

        _errors = d.pop("errors", UNSET)
        errors: list[SlurmV0041PostJobSubmitResponseDefaultErrorsItem] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = SlurmV0041PostJobSubmitResponseDefaultErrorsItem.from_dict(errors_item_data)

                errors.append(errors_item)

        _warnings = d.pop("warnings", UNSET)
        warnings: list[SlurmV0041PostJobSubmitResponseDefaultWarningsItem] | Unset = UNSET
        if _warnings is not UNSET:
            warnings = []
            for warnings_item_data in _warnings:
                warnings_item = SlurmV0041PostJobSubmitResponseDefaultWarningsItem.from_dict(warnings_item_data)

                warnings.append(warnings_item)

        slurm_v0041_post_job_submit_response_default = cls(
            result=result,
            job_id=job_id,
            step_id=step_id,
            job_submit_user_msg=job_submit_user_msg,
            meta=meta,
            errors=errors,
            warnings=warnings,
        )

        slurm_v0041_post_job_submit_response_default.additional_properties = d
        return slurm_v0041_post_job_submit_response_default

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
