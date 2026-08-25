from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Dbv0038QosLimitsMaxWallClockPer")


@_attrs_define
class Dbv0038QosLimitsMaxWallClockPer:
    """Limit on wallclock per settings

    Attributes:
        qos (int | Unset): Max wallclock per QOS
        job (int | Unset): Max wallclock per job
    """

    qos: int | Unset = UNSET
    job: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        qos = self.qos

        job = self.job

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if qos is not UNSET:
            field_dict["qos"] = qos
        if job is not UNSET:
            field_dict["job"] = job

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        qos = d.pop("qos", UNSET)

        job = d.pop("job", UNSET)

        dbv_0038_qos_limits_max_wall_clock_per = cls(
            qos=qos,
            job=job,
        )

        dbv_0038_qos_limits_max_wall_clock_per.additional_properties = d
        return dbv_0038_qos_limits_max_wall_clock_per

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
