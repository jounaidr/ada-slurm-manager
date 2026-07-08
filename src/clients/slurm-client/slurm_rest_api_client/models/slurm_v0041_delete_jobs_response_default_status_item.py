from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.slurm_v0041_delete_jobs_response_default_status_item_error import (
        SlurmV0041DeleteJobsResponseDefaultStatusItemError,
    )
    from ..models.slurm_v0041_delete_jobs_response_default_status_item_federation import (
        SlurmV0041DeleteJobsResponseDefaultStatusItemFederation,
    )
    from ..models.slurm_v0041_delete_jobs_response_default_status_item_job_id import (
        SlurmV0041DeleteJobsResponseDefaultStatusItemJobId,
    )


T = TypeVar("T", bound="SlurmV0041DeleteJobsResponseDefaultStatusItem")


@_attrs_define
class SlurmV0041DeleteJobsResponseDefaultStatusItem:
    """List of jobs signal responses

    Attributes:
        step_id (str): Job or Step ID that signaling failed
        job_id (SlurmV0041DeleteJobsResponseDefaultStatusItemJobId): Job ID that signaling failed
        error (SlurmV0041DeleteJobsResponseDefaultStatusItemError | Unset):
        federation (SlurmV0041DeleteJobsResponseDefaultStatusItemFederation | Unset):
    """

    step_id: str
    job_id: SlurmV0041DeleteJobsResponseDefaultStatusItemJobId
    error: SlurmV0041DeleteJobsResponseDefaultStatusItemError | Unset = UNSET
    federation: SlurmV0041DeleteJobsResponseDefaultStatusItemFederation | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        step_id = self.step_id

        job_id = self.job_id.to_dict()

        error: dict[str, Any] | Unset = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()

        federation: dict[str, Any] | Unset = UNSET
        if not isinstance(self.federation, Unset):
            federation = self.federation.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "step_id": step_id,
                "job_id": job_id,
            }
        )
        if error is not UNSET:
            field_dict["error"] = error
        if federation is not UNSET:
            field_dict["federation"] = federation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.slurm_v0041_delete_jobs_response_default_status_item_error import (
            SlurmV0041DeleteJobsResponseDefaultStatusItemError,
        )
        from ..models.slurm_v0041_delete_jobs_response_default_status_item_federation import (
            SlurmV0041DeleteJobsResponseDefaultStatusItemFederation,
        )
        from ..models.slurm_v0041_delete_jobs_response_default_status_item_job_id import (
            SlurmV0041DeleteJobsResponseDefaultStatusItemJobId,
        )

        d = dict(src_dict)
        step_id = d.pop("step_id")

        job_id = SlurmV0041DeleteJobsResponseDefaultStatusItemJobId.from_dict(d.pop("job_id"))

        _error = d.pop("error", UNSET)
        error: SlurmV0041DeleteJobsResponseDefaultStatusItemError | Unset
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = SlurmV0041DeleteJobsResponseDefaultStatusItemError.from_dict(_error)

        _federation = d.pop("federation", UNSET)
        federation: SlurmV0041DeleteJobsResponseDefaultStatusItemFederation | Unset
        if isinstance(_federation, Unset):
            federation = UNSET
        else:
            federation = SlurmV0041DeleteJobsResponseDefaultStatusItemFederation.from_dict(_federation)

        slurm_v0041_delete_jobs_response_default_status_item = cls(
            step_id=step_id,
            job_id=job_id,
            error=error,
            federation=federation,
        )

        slurm_v0041_delete_jobs_response_default_status_item.additional_properties = d
        return slurm_v0041_delete_jobs_response_default_status_item

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
