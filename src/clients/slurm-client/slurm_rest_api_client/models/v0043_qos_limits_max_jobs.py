from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v0043_qos_limits_max_jobs_active_jobs import V0043QosLimitsMaxJobsActiveJobs
    from ..models.v0043_qos_limits_max_jobs_per import V0043QosLimitsMaxJobsPer
    from ..models.v0043_uint_32_no_val_struct import V0043Uint32NoValStruct


T = TypeVar("T", bound="V0043QosLimitsMaxJobs")


@_attrs_define
class V0043QosLimitsMaxJobs:
    """
    Attributes:
        count (V0043Uint32NoValStruct | Unset):
        active_jobs (V0043QosLimitsMaxJobsActiveJobs | Unset):
        per (V0043QosLimitsMaxJobsPer | Unset):
    """

    count: V0043Uint32NoValStruct | Unset = UNSET
    active_jobs: V0043QosLimitsMaxJobsActiveJobs | Unset = UNSET
    per: V0043QosLimitsMaxJobsPer | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count: dict[str, Any] | Unset = UNSET
        if not isinstance(self.count, Unset):
            count = self.count.to_dict()

        active_jobs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.active_jobs, Unset):
            active_jobs = self.active_jobs.to_dict()

        per: dict[str, Any] | Unset = UNSET
        if not isinstance(self.per, Unset):
            per = self.per.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if count is not UNSET:
            field_dict["count"] = count
        if active_jobs is not UNSET:
            field_dict["active_jobs"] = active_jobs
        if per is not UNSET:
            field_dict["per"] = per

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v0043_qos_limits_max_jobs_active_jobs import V0043QosLimitsMaxJobsActiveJobs
        from ..models.v0043_qos_limits_max_jobs_per import V0043QosLimitsMaxJobsPer
        from ..models.v0043_uint_32_no_val_struct import V0043Uint32NoValStruct

        d = dict(src_dict)
        _count = d.pop("count", UNSET)
        count: V0043Uint32NoValStruct | Unset
        if isinstance(_count, Unset):
            count = UNSET
        else:
            count = V0043Uint32NoValStruct.from_dict(_count)

        _active_jobs = d.pop("active_jobs", UNSET)
        active_jobs: V0043QosLimitsMaxJobsActiveJobs | Unset
        if isinstance(_active_jobs, Unset):
            active_jobs = UNSET
        else:
            active_jobs = V0043QosLimitsMaxJobsActiveJobs.from_dict(_active_jobs)

        _per = d.pop("per", UNSET)
        per: V0043QosLimitsMaxJobsPer | Unset
        if isinstance(_per, Unset):
            per = UNSET
        else:
            per = V0043QosLimitsMaxJobsPer.from_dict(_per)

        v0043_qos_limits_max_jobs = cls(
            count=count,
            active_jobs=active_jobs,
            per=per,
        )

        v0043_qos_limits_max_jobs.additional_properties = d
        return v0043_qos_limits_max_jobs

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
