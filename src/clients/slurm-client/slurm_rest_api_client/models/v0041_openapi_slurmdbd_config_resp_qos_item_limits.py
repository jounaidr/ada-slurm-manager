from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v0041_openapi_slurmdbd_config_resp_qos_item_limits_factor import (
        V0041OpenapiSlurmdbdConfigRespQosItemLimitsFactor,
    )
    from ..models.v0041_openapi_slurmdbd_config_resp_qos_item_limits_max import (
        V0041OpenapiSlurmdbdConfigRespQosItemLimitsMax,
    )
    from ..models.v0041_openapi_slurmdbd_config_resp_qos_item_limits_min import (
        V0041OpenapiSlurmdbdConfigRespQosItemLimitsMin,
    )


T = TypeVar("T", bound="V0041OpenapiSlurmdbdConfigRespQosItemLimits")


@_attrs_define
class V0041OpenapiSlurmdbdConfigRespQosItemLimits:
    """
    Attributes:
        grace_time (int | Unset): GraceTime
        max_ (V0041OpenapiSlurmdbdConfigRespQosItemLimitsMax | Unset):
        factor (V0041OpenapiSlurmdbdConfigRespQosItemLimitsFactor | Unset): LimitFactor
        min_ (V0041OpenapiSlurmdbdConfigRespQosItemLimitsMin | Unset):
    """

    grace_time: int | Unset = UNSET
    max_: V0041OpenapiSlurmdbdConfigRespQosItemLimitsMax | Unset = UNSET
    factor: V0041OpenapiSlurmdbdConfigRespQosItemLimitsFactor | Unset = UNSET
    min_: V0041OpenapiSlurmdbdConfigRespQosItemLimitsMin | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        grace_time = self.grace_time

        max_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.max_, Unset):
            max_ = self.max_.to_dict()

        factor: dict[str, Any] | Unset = UNSET
        if not isinstance(self.factor, Unset):
            factor = self.factor.to_dict()

        min_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.min_, Unset):
            min_ = self.min_.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if grace_time is not UNSET:
            field_dict["grace_time"] = grace_time
        if max_ is not UNSET:
            field_dict["max"] = max_
        if factor is not UNSET:
            field_dict["factor"] = factor
        if min_ is not UNSET:
            field_dict["min"] = min_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v0041_openapi_slurmdbd_config_resp_qos_item_limits_factor import (
            V0041OpenapiSlurmdbdConfigRespQosItemLimitsFactor,
        )
        from ..models.v0041_openapi_slurmdbd_config_resp_qos_item_limits_max import (
            V0041OpenapiSlurmdbdConfigRespQosItemLimitsMax,
        )
        from ..models.v0041_openapi_slurmdbd_config_resp_qos_item_limits_min import (
            V0041OpenapiSlurmdbdConfigRespQosItemLimitsMin,
        )

        d = dict(src_dict)
        grace_time = d.pop("grace_time", UNSET)

        _max_ = d.pop("max", UNSET)
        max_: V0041OpenapiSlurmdbdConfigRespQosItemLimitsMax | Unset
        if isinstance(_max_, Unset):
            max_ = UNSET
        else:
            max_ = V0041OpenapiSlurmdbdConfigRespQosItemLimitsMax.from_dict(_max_)

        _factor = d.pop("factor", UNSET)
        factor: V0041OpenapiSlurmdbdConfigRespQosItemLimitsFactor | Unset
        if isinstance(_factor, Unset):
            factor = UNSET
        else:
            factor = V0041OpenapiSlurmdbdConfigRespQosItemLimitsFactor.from_dict(_factor)

        _min_ = d.pop("min", UNSET)
        min_: V0041OpenapiSlurmdbdConfigRespQosItemLimitsMin | Unset
        if isinstance(_min_, Unset):
            min_ = UNSET
        else:
            min_ = V0041OpenapiSlurmdbdConfigRespQosItemLimitsMin.from_dict(_min_)

        v0041_openapi_slurmdbd_config_resp_qos_item_limits = cls(
            grace_time=grace_time,
            max_=max_,
            factor=factor,
            min_=min_,
        )

        v0041_openapi_slurmdbd_config_resp_qos_item_limits.additional_properties = d
        return v0041_openapi_slurmdbd_config_resp_qos_item_limits

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
