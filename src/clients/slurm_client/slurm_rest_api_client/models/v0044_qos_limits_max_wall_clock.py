from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v0044_qos_limits_max_wall_clock_per import V0044QosLimitsMaxWallClockPer


T = TypeVar("T", bound="V0044QosLimitsMaxWallClock")


@_attrs_define
class V0044QosLimitsMaxWallClock:
    """
    Attributes:
        per (V0044QosLimitsMaxWallClockPer | Unset):
    """

    per: V0044QosLimitsMaxWallClockPer | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        per: dict[str, Any] | Unset = UNSET
        if not isinstance(self.per, Unset):
            per = self.per.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if per is not UNSET:
            field_dict["per"] = per

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v0044_qos_limits_max_wall_clock_per import V0044QosLimitsMaxWallClockPer

        d = dict(src_dict)
        _per = d.pop("per", UNSET)
        per: V0044QosLimitsMaxWallClockPer | Unset
        if isinstance(_per, Unset):
            per = UNSET
        else:
            per = V0044QosLimitsMaxWallClockPer.from_dict(_per)

        v0044_qos_limits_max_wall_clock = cls(
            per=per,
        )

        v0044_qos_limits_max_wall_clock.additional_properties = d
        return v0044_qos_limits_max_wall_clock

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
