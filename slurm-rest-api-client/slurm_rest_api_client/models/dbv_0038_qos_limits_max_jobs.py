from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dbv_0038_qos_limits_max_jobs_active_jobs import Dbv0038QosLimitsMaxJobsActiveJobs


T = TypeVar("T", bound="Dbv0038QosLimitsMaxJobs")


@_attrs_define
class Dbv0038QosLimitsMaxJobs:
    """Limits on jobs settings

    Attributes:
        active_jobs (Dbv0038QosLimitsMaxJobsActiveJobs | Unset): Limits on active jobs settings
    """

    active_jobs: Dbv0038QosLimitsMaxJobsActiveJobs | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        active_jobs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.active_jobs, Unset):
            active_jobs = self.active_jobs.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if active_jobs is not UNSET:
            field_dict["active_jobs"] = active_jobs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dbv_0038_qos_limits_max_jobs_active_jobs import Dbv0038QosLimitsMaxJobsActiveJobs

        d = dict(src_dict)
        _active_jobs = d.pop("active_jobs", UNSET)
        active_jobs: Dbv0038QosLimitsMaxJobsActiveJobs | Unset
        if isinstance(_active_jobs, Unset):
            active_jobs = UNSET
        else:
            active_jobs = Dbv0038QosLimitsMaxJobsActiveJobs.from_dict(_active_jobs)

        dbv_0038_qos_limits_max_jobs = cls(
            active_jobs=active_jobs,
        )

        dbv_0038_qos_limits_max_jobs.additional_properties = d
        return dbv_0038_qos_limits_max_jobs

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
