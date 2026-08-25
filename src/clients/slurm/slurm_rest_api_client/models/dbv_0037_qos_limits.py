from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dbv_0037_qos_limits_max import Dbv0037QosLimitsMax
    from ..models.dbv_0037_qos_limits_min import Dbv0037QosLimitsMin


T = TypeVar("T", bound="Dbv0037QosLimits")


@_attrs_define
class Dbv0037QosLimits:
    """Assigned limits

    Attributes:
        factor (float | Unset): factor to apply to TRES count for associations using this QOS
        max_ (Dbv0037QosLimitsMax | Unset): Limits on max settings
        min_ (Dbv0037QosLimitsMin | Unset): Min limit settings
    """

    factor: float | Unset = UNSET
    max_: Dbv0037QosLimitsMax | Unset = UNSET
    min_: Dbv0037QosLimitsMin | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        factor = self.factor

        max_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.max_, Unset):
            max_ = self.max_.to_dict()

        min_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.min_, Unset):
            min_ = self.min_.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if factor is not UNSET:
            field_dict["factor"] = factor
        if max_ is not UNSET:
            field_dict["max"] = max_
        if min_ is not UNSET:
            field_dict["min"] = min_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dbv_0037_qos_limits_max import Dbv0037QosLimitsMax
        from ..models.dbv_0037_qos_limits_min import Dbv0037QosLimitsMin

        d = dict(src_dict)
        factor = d.pop("factor", UNSET)

        _max_ = d.pop("max", UNSET)
        max_: Dbv0037QosLimitsMax | Unset
        if isinstance(_max_, Unset):
            max_ = UNSET
        else:
            max_ = Dbv0037QosLimitsMax.from_dict(_max_)

        _min_ = d.pop("min", UNSET)
        min_: Dbv0037QosLimitsMin | Unset
        if isinstance(_min_, Unset):
            min_ = UNSET
        else:
            min_ = Dbv0037QosLimitsMin.from_dict(_min_)

        dbv_0037_qos_limits = cls(
            factor=factor,
            max_=max_,
            min_=min_,
        )

        dbv_0037_qos_limits.additional_properties = d
        return dbv_0037_qos_limits

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
