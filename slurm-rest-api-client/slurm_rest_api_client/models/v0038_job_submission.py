from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v0038_job_properties import V0038JobProperties


T = TypeVar("T", bound="V0038JobSubmission")


@_attrs_define
class V0038JobSubmission:
    """
    Attributes:
        script (str): Executable script (full contents) to run in batch step
        job (V0038JobProperties | Unset):
        jobs (list[V0038JobProperties] | Unset): Properties of an HetJob
    """

    script: str
    job: V0038JobProperties | Unset = UNSET
    jobs: list[V0038JobProperties] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        script = self.script

        job: dict[str, Any] | Unset = UNSET
        if not isinstance(self.job, Unset):
            job = self.job.to_dict()

        jobs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.jobs, Unset):
            jobs = []
            for jobs_item_data in self.jobs:
                jobs_item = jobs_item_data.to_dict()
                jobs.append(jobs_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "script": script,
            }
        )
        if job is not UNSET:
            field_dict["job"] = job
        if jobs is not UNSET:
            field_dict["jobs"] = jobs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v0038_job_properties import V0038JobProperties

        d = dict(src_dict)
        script = d.pop("script")

        _job = d.pop("job", UNSET)
        job: V0038JobProperties | Unset
        if isinstance(_job, Unset):
            job = UNSET
        else:
            job = V0038JobProperties.from_dict(_job)

        _jobs = d.pop("jobs", UNSET)
        jobs: list[V0038JobProperties] | Unset = UNSET
        if _jobs is not UNSET:
            jobs = []
            for jobs_item_data in _jobs:
                jobs_item = V0038JobProperties.from_dict(jobs_item_data)

                jobs.append(jobs_item)

        v0038_job_submission = cls(
            script=script,
            job=job,
            jobs=jobs,
        )

        v0038_job_submission.additional_properties = d
        return v0038_job_submission

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
