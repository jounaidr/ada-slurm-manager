from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v0041_openapi_slurmdbd_config_resp_qos_item_limits_min_tres_per_job_item import (
        V0041OpenapiSlurmdbdConfigRespQosItemLimitsMinTresPerJobItem,
    )


T = TypeVar("T", bound="V0041OpenapiSlurmdbdConfigRespQosItemLimitsMinTresPer")


@_attrs_define
class V0041OpenapiSlurmdbdConfigRespQosItemLimitsMinTresPer:
    """
    Attributes:
        job (list[V0041OpenapiSlurmdbdConfigRespQosItemLimitsMinTresPerJobItem] | Unset): MinTRES
    """

    job: list[V0041OpenapiSlurmdbdConfigRespQosItemLimitsMinTresPerJobItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        job: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.job, Unset):
            job = []
            for job_item_data in self.job:
                job_item = job_item_data.to_dict()
                job.append(job_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if job is not UNSET:
            field_dict["job"] = job

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v0041_openapi_slurmdbd_config_resp_qos_item_limits_min_tres_per_job_item import (
            V0041OpenapiSlurmdbdConfigRespQosItemLimitsMinTresPerJobItem,
        )

        d = dict(src_dict)
        _job = d.pop("job", UNSET)
        job: list[V0041OpenapiSlurmdbdConfigRespQosItemLimitsMinTresPerJobItem] | Unset = UNSET
        if _job is not UNSET:
            job = []
            for job_item_data in _job:
                job_item = V0041OpenapiSlurmdbdConfigRespQosItemLimitsMinTresPerJobItem.from_dict(job_item_data)

                job.append(job_item)

        v0041_openapi_slurmdbd_config_resp_qos_item_limits_min_tres_per = cls(
            job=job,
        )

        v0041_openapi_slurmdbd_config_resp_qos_item_limits_min_tres_per.additional_properties = d
        return v0041_openapi_slurmdbd_config_resp_qos_item_limits_min_tres_per

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
