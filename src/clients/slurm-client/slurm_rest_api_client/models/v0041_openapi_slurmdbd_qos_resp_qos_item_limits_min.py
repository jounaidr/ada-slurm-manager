from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v0041_openapi_slurmdbd_qos_resp_qos_item_limits_min_priority_threshold import (
        V0041OpenapiSlurmdbdQosRespQosItemLimitsMinPriorityThreshold,
    )
    from ..models.v0041_openapi_slurmdbd_qos_resp_qos_item_limits_min_tres import (
        V0041OpenapiSlurmdbdQosRespQosItemLimitsMinTres,
    )


T = TypeVar("T", bound="V0041OpenapiSlurmdbdQosRespQosItemLimitsMin")


@_attrs_define
class V0041OpenapiSlurmdbdQosRespQosItemLimitsMin:
    """
    Attributes:
        priority_threshold (V0041OpenapiSlurmdbdQosRespQosItemLimitsMinPriorityThreshold | Unset): MinPrioThreshold
        tres (V0041OpenapiSlurmdbdQosRespQosItemLimitsMinTres | Unset):
    """

    priority_threshold: V0041OpenapiSlurmdbdQosRespQosItemLimitsMinPriorityThreshold | Unset = UNSET
    tres: V0041OpenapiSlurmdbdQosRespQosItemLimitsMinTres | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        priority_threshold: dict[str, Any] | Unset = UNSET
        if not isinstance(self.priority_threshold, Unset):
            priority_threshold = self.priority_threshold.to_dict()

        tres: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tres, Unset):
            tres = self.tres.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if priority_threshold is not UNSET:
            field_dict["priority_threshold"] = priority_threshold
        if tres is not UNSET:
            field_dict["tres"] = tres

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v0041_openapi_slurmdbd_qos_resp_qos_item_limits_min_priority_threshold import (
            V0041OpenapiSlurmdbdQosRespQosItemLimitsMinPriorityThreshold,
        )
        from ..models.v0041_openapi_slurmdbd_qos_resp_qos_item_limits_min_tres import (
            V0041OpenapiSlurmdbdQosRespQosItemLimitsMinTres,
        )

        d = dict(src_dict)
        _priority_threshold = d.pop("priority_threshold", UNSET)
        priority_threshold: V0041OpenapiSlurmdbdQosRespQosItemLimitsMinPriorityThreshold | Unset
        if isinstance(_priority_threshold, Unset):
            priority_threshold = UNSET
        else:
            priority_threshold = V0041OpenapiSlurmdbdQosRespQosItemLimitsMinPriorityThreshold.from_dict(
                _priority_threshold
            )

        _tres = d.pop("tres", UNSET)
        tres: V0041OpenapiSlurmdbdQosRespQosItemLimitsMinTres | Unset
        if isinstance(_tres, Unset):
            tres = UNSET
        else:
            tres = V0041OpenapiSlurmdbdQosRespQosItemLimitsMinTres.from_dict(_tres)

        v0041_openapi_slurmdbd_qos_resp_qos_item_limits_min = cls(
            priority_threshold=priority_threshold,
            tres=tres,
        )

        v0041_openapi_slurmdbd_qos_resp_qos_item_limits_min.additional_properties = d
        return v0041_openapi_slurmdbd_qos_resp_qos_item_limits_min

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
