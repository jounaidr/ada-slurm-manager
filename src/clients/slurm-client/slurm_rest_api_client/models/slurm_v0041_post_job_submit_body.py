from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.slurm_v0041_post_job_submit_body_job import SlurmV0041PostJobSubmitBodyJob
    from ..models.slurm_v0041_post_job_submit_body_jobs_item import SlurmV0041PostJobSubmitBodyJobsItem


T = TypeVar("T", bound="SlurmV0041PostJobSubmitBody")


@_attrs_define
class SlurmV0041PostJobSubmitBody:
    """
    Attributes:
        script (str | Unset): Job batch script contents; Same as the script field in jobs[0] or job.
        jobs (list[SlurmV0041PostJobSubmitBodyJobsItem] | Unset): HetJob description
        job (SlurmV0041PostJobSubmitBodyJob | Unset): Job description
    """

    script: str | Unset = UNSET
    jobs: list[SlurmV0041PostJobSubmitBodyJobsItem] | Unset = UNSET
    job: SlurmV0041PostJobSubmitBodyJob | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        script = self.script

        jobs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.jobs, Unset):
            jobs = []
            for jobs_item_data in self.jobs:
                jobs_item = jobs_item_data.to_dict()
                jobs.append(jobs_item)

        job: dict[str, Any] | Unset = UNSET
        if not isinstance(self.job, Unset):
            job = self.job.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if script is not UNSET:
            field_dict["script"] = script
        if jobs is not UNSET:
            field_dict["jobs"] = jobs
        if job is not UNSET:
            field_dict["job"] = job

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.slurm_v0041_post_job_submit_body_job import SlurmV0041PostJobSubmitBodyJob
        from ..models.slurm_v0041_post_job_submit_body_jobs_item import SlurmV0041PostJobSubmitBodyJobsItem

        d = dict(src_dict)
        script = d.pop("script", UNSET)

        _jobs = d.pop("jobs", UNSET)
        jobs: list[SlurmV0041PostJobSubmitBodyJobsItem] | Unset = UNSET
        if _jobs is not UNSET:
            jobs = []
            for jobs_item_data in _jobs:
                jobs_item = SlurmV0041PostJobSubmitBodyJobsItem.from_dict(jobs_item_data)

                jobs.append(jobs_item)

        _job = d.pop("job", UNSET)
        job: SlurmV0041PostJobSubmitBodyJob | Unset
        if isinstance(_job, Unset):
            job = UNSET
        else:
            job = SlurmV0041PostJobSubmitBodyJob.from_dict(_job)

        slurm_v0041_post_job_submit_body = cls(
            script=script,
            jobs=jobs,
            job=job,
        )

        slurm_v0041_post_job_submit_body.additional_properties = d
        return slurm_v0041_post_job_submit_body

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
