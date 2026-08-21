from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v0041_openapi_slurmdbd_qos_resp_qos_item_limits_max_active_jobs_accruing import (
        V0041OpenapiSlurmdbdQosRespQosItemLimitsMaxActiveJobsAccruing,
    )
    from ..models.v0041_openapi_slurmdbd_qos_resp_qos_item_limits_max_active_jobs_count import (
        V0041OpenapiSlurmdbdQosRespQosItemLimitsMaxActiveJobsCount,
    )


T = TypeVar("T", bound="V0041OpenapiSlurmdbdQosRespQosItemLimitsMaxActiveJobs")


@_attrs_define
class V0041OpenapiSlurmdbdQosRespQosItemLimitsMaxActiveJobs:
    """
    Attributes:
        accruing (V0041OpenapiSlurmdbdQosRespQosItemLimitsMaxActiveJobsAccruing | Unset): GrpJobsAccrue
        count (V0041OpenapiSlurmdbdQosRespQosItemLimitsMaxActiveJobsCount | Unset): GrpJobs
    """

    accruing: V0041OpenapiSlurmdbdQosRespQosItemLimitsMaxActiveJobsAccruing | Unset = UNSET
    count: V0041OpenapiSlurmdbdQosRespQosItemLimitsMaxActiveJobsCount | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        accruing: dict[str, Any] | Unset = UNSET
        if not isinstance(self.accruing, Unset):
            accruing = self.accruing.to_dict()

        count: dict[str, Any] | Unset = UNSET
        if not isinstance(self.count, Unset):
            count = self.count.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if accruing is not UNSET:
            field_dict["accruing"] = accruing
        if count is not UNSET:
            field_dict["count"] = count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v0041_openapi_slurmdbd_qos_resp_qos_item_limits_max_active_jobs_accruing import (
            V0041OpenapiSlurmdbdQosRespQosItemLimitsMaxActiveJobsAccruing,
        )
        from ..models.v0041_openapi_slurmdbd_qos_resp_qos_item_limits_max_active_jobs_count import (
            V0041OpenapiSlurmdbdQosRespQosItemLimitsMaxActiveJobsCount,
        )

        d = dict(src_dict)
        _accruing = d.pop("accruing", UNSET)
        accruing: V0041OpenapiSlurmdbdQosRespQosItemLimitsMaxActiveJobsAccruing | Unset
        if isinstance(_accruing, Unset):
            accruing = UNSET
        else:
            accruing = V0041OpenapiSlurmdbdQosRespQosItemLimitsMaxActiveJobsAccruing.from_dict(_accruing)

        _count = d.pop("count", UNSET)
        count: V0041OpenapiSlurmdbdQosRespQosItemLimitsMaxActiveJobsCount | Unset
        if isinstance(_count, Unset):
            count = UNSET
        else:
            count = V0041OpenapiSlurmdbdQosRespQosItemLimitsMaxActiveJobsCount.from_dict(_count)

        v0041_openapi_slurmdbd_qos_resp_qos_item_limits_max_active_jobs = cls(
            accruing=accruing,
            count=count,
        )

        v0041_openapi_slurmdbd_qos_resp_qos_item_limits_max_active_jobs.additional_properties = d
        return v0041_openapi_slurmdbd_qos_resp_qos_item_limits_max_active_jobs

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
