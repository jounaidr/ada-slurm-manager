from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dbv_0037_qos_limits_min_tres import Dbv0037QosLimitsMinTres


T = TypeVar("T", bound="Dbv0037QosLimitsMin")


@_attrs_define
class Dbv0037QosLimitsMin:
    """Min limit settings

    Attributes:
        priority_threshold (int | Unset): Min priority threshold
        tres (Dbv0037QosLimitsMinTres | Unset): Min tres settings
    """

    priority_threshold: int | Unset = UNSET
    tres: Dbv0037QosLimitsMinTres | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        priority_threshold = self.priority_threshold

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
        from ..models.dbv_0037_qos_limits_min_tres import Dbv0037QosLimitsMinTres

        d = dict(src_dict)
        priority_threshold = d.pop("priority_threshold", UNSET)

        _tres = d.pop("tres", UNSET)
        tres: Dbv0037QosLimitsMinTres | Unset
        if isinstance(_tres, Unset):
            tres = UNSET
        else:
            tres = Dbv0037QosLimitsMinTres.from_dict(_tres)

        dbv_0037_qos_limits_min = cls(
            priority_threshold=priority_threshold,
            tres=tres,
        )

        dbv_0037_qos_limits_min.additional_properties = d
        return dbv_0037_qos_limits_min

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
