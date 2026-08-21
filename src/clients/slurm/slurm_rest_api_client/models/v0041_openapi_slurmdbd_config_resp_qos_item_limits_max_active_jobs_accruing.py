from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="V0041OpenapiSlurmdbdConfigRespQosItemLimitsMaxActiveJobsAccruing")


@_attrs_define
class V0041OpenapiSlurmdbdConfigRespQosItemLimitsMaxActiveJobsAccruing:
    """GrpJobsAccrue

    Attributes:
        set_ (bool | Unset): True if number has been set; False if number is unset
        infinite (bool | Unset): True if number has been set to infinite; "set" and "number" will be ignored
        number (int | Unset): If "set" is True the number will be set with value; otherwise ignore number contents
    """

    set_: bool | Unset = UNSET
    infinite: bool | Unset = UNSET
    number: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        set_ = self.set_

        infinite = self.infinite

        number = self.number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if set_ is not UNSET:
            field_dict["set"] = set_
        if infinite is not UNSET:
            field_dict["infinite"] = infinite
        if number is not UNSET:
            field_dict["number"] = number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        set_ = d.pop("set", UNSET)

        infinite = d.pop("infinite", UNSET)

        number = d.pop("number", UNSET)

        v0041_openapi_slurmdbd_config_resp_qos_item_limits_max_active_jobs_accruing = cls(
            set_=set_,
            infinite=infinite,
            number=number,
        )

        v0041_openapi_slurmdbd_config_resp_qos_item_limits_max_active_jobs_accruing.additional_properties = d
        return v0041_openapi_slurmdbd_config_resp_qos_item_limits_max_active_jobs_accruing

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
