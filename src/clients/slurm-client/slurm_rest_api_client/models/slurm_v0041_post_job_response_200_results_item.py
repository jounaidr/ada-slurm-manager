from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SlurmV0041PostJobResponse200ResultsItem")


@_attrs_define
class SlurmV0041PostJobResponse200ResultsItem:
    """
    Attributes:
        job_id (int | Unset): Job ID for updated job
        step_id (str | Unset): Step ID for updated job
        error (str | Unset): Verbose update status or error
        error_code (int | Unset): Verbose update status or error
        why (str | Unset): Update response message
    """

    job_id: int | Unset = UNSET
    step_id: str | Unset = UNSET
    error: str | Unset = UNSET
    error_code: int | Unset = UNSET
    why: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        job_id = self.job_id

        step_id = self.step_id

        error = self.error

        error_code = self.error_code

        why = self.why

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if job_id is not UNSET:
            field_dict["job_id"] = job_id
        if step_id is not UNSET:
            field_dict["step_id"] = step_id
        if error is not UNSET:
            field_dict["error"] = error
        if error_code is not UNSET:
            field_dict["error_code"] = error_code
        if why is not UNSET:
            field_dict["why"] = why

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        job_id = d.pop("job_id", UNSET)

        step_id = d.pop("step_id", UNSET)

        error = d.pop("error", UNSET)

        error_code = d.pop("error_code", UNSET)

        why = d.pop("why", UNSET)

        slurm_v0041_post_job_response_200_results_item = cls(
            job_id=job_id,
            step_id=step_id,
            error=error,
            error_code=error_code,
            why=why,
        )

        slurm_v0041_post_job_response_200_results_item.additional_properties = d
        return slurm_v0041_post_job_response_200_results_item

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
