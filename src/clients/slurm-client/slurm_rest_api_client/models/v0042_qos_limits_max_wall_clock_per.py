from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v0042_uint_32_no_val_struct import V0042Uint32NoValStruct


T = TypeVar("T", bound="V0042QosLimitsMaxWallClockPer")


@_attrs_define
class V0042QosLimitsMaxWallClockPer:
    """
    Attributes:
        qos (V0042Uint32NoValStruct | Unset):
        job (V0042Uint32NoValStruct | Unset):
    """

    qos: V0042Uint32NoValStruct | Unset = UNSET
    job: V0042Uint32NoValStruct | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        qos: dict[str, Any] | Unset = UNSET
        if not isinstance(self.qos, Unset):
            qos = self.qos.to_dict()

        job: dict[str, Any] | Unset = UNSET
        if not isinstance(self.job, Unset):
            job = self.job.to_dict()

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
        from ..models.v0042_uint_32_no_val_struct import V0042Uint32NoValStruct

        d = dict(src_dict)
        _qos = d.pop("qos", UNSET)
        qos: V0042Uint32NoValStruct | Unset
        if isinstance(_qos, Unset):
            qos = UNSET
        else:
            qos = V0042Uint32NoValStruct.from_dict(_qos)

        _job = d.pop("job", UNSET)
        job: V0042Uint32NoValStruct | Unset
        if isinstance(_job, Unset):
            job = UNSET
        else:
            job = V0042Uint32NoValStruct.from_dict(_job)

        v0042_qos_limits_max_wall_clock_per = cls(
            qos=qos,
            job=job,
        )

        v0042_qos_limits_max_wall_clock_per.additional_properties = d
        return v0042_qos_limits_max_wall_clock_per

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
