from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dbv_0038_qos_limits_max_tres_minutes import Dbv0038QosLimitsMaxTresMinutes
    from ..models.dbv_0038_qos_limits_max_tres_per import Dbv0038QosLimitsMaxTresPer


T = TypeVar("T", bound="Dbv0038QosLimitsMaxTres")


@_attrs_define
class Dbv0038QosLimitsMaxTres:
    """Limits on TRES

    Attributes:
        minutes (Dbv0038QosLimitsMaxTresMinutes | Unset): Max TRES minutes settings
        per (Dbv0038QosLimitsMaxTresPer | Unset): Max TRES per settings
    """

    minutes: Dbv0038QosLimitsMaxTresMinutes | Unset = UNSET
    per: Dbv0038QosLimitsMaxTresPer | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        minutes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.minutes, Unset):
            minutes = self.minutes.to_dict()

        per: dict[str, Any] | Unset = UNSET
        if not isinstance(self.per, Unset):
            per = self.per.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if minutes is not UNSET:
            field_dict["minutes"] = minutes
        if per is not UNSET:
            field_dict["per"] = per

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dbv_0038_qos_limits_max_tres_minutes import Dbv0038QosLimitsMaxTresMinutes
        from ..models.dbv_0038_qos_limits_max_tres_per import Dbv0038QosLimitsMaxTresPer

        d = dict(src_dict)
        _minutes = d.pop("minutes", UNSET)
        minutes: Dbv0038QosLimitsMaxTresMinutes | Unset
        if isinstance(_minutes, Unset):
            minutes = UNSET
        else:
            minutes = Dbv0038QosLimitsMaxTresMinutes.from_dict(_minutes)

        _per = d.pop("per", UNSET)
        per: Dbv0038QosLimitsMaxTresPer | Unset
        if isinstance(_per, Unset):
            per = UNSET
        else:
            per = Dbv0038QosLimitsMaxTresPer.from_dict(_per)

        dbv_0038_qos_limits_max_tres = cls(
            minutes=minutes,
            per=per,
        )

        dbv_0038_qos_limits_max_tres.additional_properties = d
        return dbv_0038_qos_limits_max_tres

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
