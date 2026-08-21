from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.slurm_v0041_post_job_allocate_body_hetjob_item import SlurmV0041PostJobAllocateBodyHetjobItem
    from ..models.slurm_v0041_post_job_allocate_body_job import SlurmV0041PostJobAllocateBodyJob


T = TypeVar("T", bound="SlurmV0041PostJobAllocateBody")


@_attrs_define
class SlurmV0041PostJobAllocateBody:
    """
    Attributes:
        hetjob (list[SlurmV0041PostJobAllocateBodyHetjobItem] | Unset): HetJob description
        job (SlurmV0041PostJobAllocateBodyJob | Unset): Job description
    """

    hetjob: list[SlurmV0041PostJobAllocateBodyHetjobItem] | Unset = UNSET
    job: SlurmV0041PostJobAllocateBodyJob | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hetjob: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.hetjob, Unset):
            hetjob = []
            for hetjob_item_data in self.hetjob:
                hetjob_item = hetjob_item_data.to_dict()
                hetjob.append(hetjob_item)

        job: dict[str, Any] | Unset = UNSET
        if not isinstance(self.job, Unset):
            job = self.job.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hetjob is not UNSET:
            field_dict["hetjob"] = hetjob
        if job is not UNSET:
            field_dict["job"] = job

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.slurm_v0041_post_job_allocate_body_hetjob_item import SlurmV0041PostJobAllocateBodyHetjobItem
        from ..models.slurm_v0041_post_job_allocate_body_job import SlurmV0041PostJobAllocateBodyJob

        d = dict(src_dict)
        _hetjob = d.pop("hetjob", UNSET)
        hetjob: list[SlurmV0041PostJobAllocateBodyHetjobItem] | Unset = UNSET
        if _hetjob is not UNSET:
            hetjob = []
            for hetjob_item_data in _hetjob:
                hetjob_item = SlurmV0041PostJobAllocateBodyHetjobItem.from_dict(hetjob_item_data)

                hetjob.append(hetjob_item)

        _job = d.pop("job", UNSET)
        job: SlurmV0041PostJobAllocateBodyJob | Unset
        if isinstance(_job, Unset):
            job = UNSET
        else:
            job = SlurmV0041PostJobAllocateBodyJob.from_dict(_job)

        slurm_v0041_post_job_allocate_body = cls(
            hetjob=hetjob,
            job=job,
        )

        slurm_v0041_post_job_allocate_body.additional_properties = d
        return slurm_v0041_post_job_allocate_body

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
