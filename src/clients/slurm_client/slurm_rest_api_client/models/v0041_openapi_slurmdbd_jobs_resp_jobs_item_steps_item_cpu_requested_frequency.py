from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v0041_openapi_slurmdbd_jobs_resp_jobs_item_steps_item_cpu_requested_frequency_max import (
        V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemCPURequestedFrequencyMax,
    )
    from ..models.v0041_openapi_slurmdbd_jobs_resp_jobs_item_steps_item_cpu_requested_frequency_min import (
        V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemCPURequestedFrequencyMin,
    )


T = TypeVar("T", bound="V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemCPURequestedFrequency")


@_attrs_define
class V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemCPURequestedFrequency:
    """
    Attributes:
        min_ (V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemCPURequestedFrequencyMin | Unset): Minimum requested CPU
            frequency in kHz
        max_ (V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemCPURequestedFrequencyMax | Unset): Maximum requested CPU
            frequency in kHz
    """

    min_: V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemCPURequestedFrequencyMin | Unset = UNSET
    max_: V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemCPURequestedFrequencyMax | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        min_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.min_, Unset):
            min_ = self.min_.to_dict()

        max_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.max_, Unset):
            max_ = self.max_.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if min_ is not UNSET:
            field_dict["min"] = min_
        if max_ is not UNSET:
            field_dict["max"] = max_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v0041_openapi_slurmdbd_jobs_resp_jobs_item_steps_item_cpu_requested_frequency_max import (
            V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemCPURequestedFrequencyMax,
        )
        from ..models.v0041_openapi_slurmdbd_jobs_resp_jobs_item_steps_item_cpu_requested_frequency_min import (
            V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemCPURequestedFrequencyMin,
        )

        d = dict(src_dict)
        _min_ = d.pop("min", UNSET)
        min_: V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemCPURequestedFrequencyMin | Unset
        if isinstance(_min_, Unset):
            min_ = UNSET
        else:
            min_ = V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemCPURequestedFrequencyMin.from_dict(_min_)

        _max_ = d.pop("max", UNSET)
        max_: V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemCPURequestedFrequencyMax | Unset
        if isinstance(_max_, Unset):
            max_ = UNSET
        else:
            max_ = V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemCPURequestedFrequencyMax.from_dict(_max_)

        v0041_openapi_slurmdbd_jobs_resp_jobs_item_steps_item_cpu_requested_frequency = cls(
            min_=min_,
            max_=max_,
        )

        v0041_openapi_slurmdbd_jobs_resp_jobs_item_steps_item_cpu_requested_frequency.additional_properties = d
        return v0041_openapi_slurmdbd_jobs_resp_jobs_item_steps_item_cpu_requested_frequency

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
