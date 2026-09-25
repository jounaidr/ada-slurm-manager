from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dbv_0038_qos_limits import Dbv0038QosLimits
    from ..models.dbv_0038_qos_preempt import Dbv0038QosPreempt


T = TypeVar("T", bound="Dbv0038Qos")


@_attrs_define
class Dbv0038Qos:
    """QOS description

    Attributes:
        description (str | Unset): QOS description
        flags (list[str] | Unset): List of properties of QOS
        id (str | Unset): Database id
        limits (Dbv0038QosLimits | Unset): Assigned limits
        preempt (Dbv0038QosPreempt | Unset): Preemption settings
        priority (int | Unset): QOS priority
        usage_factor (float | Unset): Usage factor
        usage_threshold (float | Unset): Usage threshold
        name (str | Unset): Assigned name of QOS
    """

    description: str | Unset = UNSET
    flags: list[str] | Unset = UNSET
    id: str | Unset = UNSET
    limits: Dbv0038QosLimits | Unset = UNSET
    preempt: Dbv0038QosPreempt | Unset = UNSET
    priority: int | Unset = UNSET
    usage_factor: float | Unset = UNSET
    usage_threshold: float | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        flags: list[str] | Unset = UNSET
        if not isinstance(self.flags, Unset):
            flags = self.flags

        id = self.id

        limits: dict[str, Any] | Unset = UNSET
        if not isinstance(self.limits, Unset):
            limits = self.limits.to_dict()

        preempt: dict[str, Any] | Unset = UNSET
        if not isinstance(self.preempt, Unset):
            preempt = self.preempt.to_dict()

        priority = self.priority

        usage_factor = self.usage_factor

        usage_threshold = self.usage_threshold

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if flags is not UNSET:
            field_dict["flags"] = flags
        if id is not UNSET:
            field_dict["id"] = id
        if limits is not UNSET:
            field_dict["limits"] = limits
        if preempt is not UNSET:
            field_dict["preempt"] = preempt
        if priority is not UNSET:
            field_dict["priority"] = priority
        if usage_factor is not UNSET:
            field_dict["usage_factor"] = usage_factor
        if usage_threshold is not UNSET:
            field_dict["usage_threshold"] = usage_threshold
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dbv_0038_qos_limits import Dbv0038QosLimits
        from ..models.dbv_0038_qos_preempt import Dbv0038QosPreempt

        d = dict(src_dict)
        description = d.pop("description", UNSET)

        flags = cast(list[str], d.pop("flags", UNSET))

        id = d.pop("id", UNSET)

        _limits = d.pop("limits", UNSET)
        limits: Dbv0038QosLimits | Unset
        if isinstance(_limits, Unset):
            limits = UNSET
        else:
            limits = Dbv0038QosLimits.from_dict(_limits)

        _preempt = d.pop("preempt", UNSET)
        preempt: Dbv0038QosPreempt | Unset
        if isinstance(_preempt, Unset):
            preempt = UNSET
        else:
            preempt = Dbv0038QosPreempt.from_dict(_preempt)

        priority = d.pop("priority", UNSET)

        usage_factor = d.pop("usage_factor", UNSET)

        usage_threshold = d.pop("usage_threshold", UNSET)

        name = d.pop("name", UNSET)

        dbv_0038_qos = cls(
            description=description,
            flags=flags,
            id=id,
            limits=limits,
            preempt=preempt,
            priority=priority,
            usage_factor=usage_factor,
            usage_threshold=usage_threshold,
            name=name,
        )

        dbv_0038_qos.additional_properties = d
        return dbv_0038_qos

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
