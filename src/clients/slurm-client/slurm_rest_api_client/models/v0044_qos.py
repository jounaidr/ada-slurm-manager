from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.v0044_qos_flags_item import V0044QosFlagsItem
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v0044_float_64_no_val_struct import V0044Float64NoValStruct
    from ..models.v0044_qos_limits import V0044QosLimits
    from ..models.v0044_qos_preempt import V0044QosPreempt
    from ..models.v0044_uint_32_no_val_struct import V0044Uint32NoValStruct


T = TypeVar("T", bound="V0044Qos")


@_attrs_define
class V0044Qos:
    """
    Attributes:
        description (str | Unset): Arbitrary description
        flags (list[V0044QosFlagsItem] | Unset): Flags, to avoid modifying current values specify NOT_SET
        id (int | Unset): Unique ID
        limits (V0044QosLimits | Unset):
        name (str | Unset): Name
        preempt (V0044QosPreempt | Unset):
        priority (V0044Uint32NoValStruct | Unset):
        usage_factor (V0044Float64NoValStruct | Unset):
        usage_threshold (V0044Float64NoValStruct | Unset):
    """

    description: str | Unset = UNSET
    flags: list[V0044QosFlagsItem] | Unset = UNSET
    id: int | Unset = UNSET
    limits: V0044QosLimits | Unset = UNSET
    name: str | Unset = UNSET
    preempt: V0044QosPreempt | Unset = UNSET
    priority: V0044Uint32NoValStruct | Unset = UNSET
    usage_factor: V0044Float64NoValStruct | Unset = UNSET
    usage_threshold: V0044Float64NoValStruct | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        flags: list[str] | Unset = UNSET
        if not isinstance(self.flags, Unset):
            flags = []
            for flags_item_data in self.flags:
                flags_item = flags_item_data.value
                flags.append(flags_item)

        id = self.id

        limits: dict[str, Any] | Unset = UNSET
        if not isinstance(self.limits, Unset):
            limits = self.limits.to_dict()

        name = self.name

        preempt: dict[str, Any] | Unset = UNSET
        if not isinstance(self.preempt, Unset):
            preempt = self.preempt.to_dict()

        priority: dict[str, Any] | Unset = UNSET
        if not isinstance(self.priority, Unset):
            priority = self.priority.to_dict()

        usage_factor: dict[str, Any] | Unset = UNSET
        if not isinstance(self.usage_factor, Unset):
            usage_factor = self.usage_factor.to_dict()

        usage_threshold: dict[str, Any] | Unset = UNSET
        if not isinstance(self.usage_threshold, Unset):
            usage_threshold = self.usage_threshold.to_dict()

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
        if name is not UNSET:
            field_dict["name"] = name
        if preempt is not UNSET:
            field_dict["preempt"] = preempt
        if priority is not UNSET:
            field_dict["priority"] = priority
        if usage_factor is not UNSET:
            field_dict["usage_factor"] = usage_factor
        if usage_threshold is not UNSET:
            field_dict["usage_threshold"] = usage_threshold

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v0044_float_64_no_val_struct import V0044Float64NoValStruct
        from ..models.v0044_qos_limits import V0044QosLimits
        from ..models.v0044_qos_preempt import V0044QosPreempt
        from ..models.v0044_uint_32_no_val_struct import V0044Uint32NoValStruct

        d = dict(src_dict)
        description = d.pop("description", UNSET)

        _flags = d.pop("flags", UNSET)
        flags: list[V0044QosFlagsItem] | Unset = UNSET
        if _flags is not UNSET:
            flags = []
            for flags_item_data in _flags:
                flags_item = V0044QosFlagsItem(flags_item_data)

                flags.append(flags_item)

        id = d.pop("id", UNSET)

        _limits = d.pop("limits", UNSET)
        limits: V0044QosLimits | Unset
        if isinstance(_limits, Unset):
            limits = UNSET
        else:
            limits = V0044QosLimits.from_dict(_limits)

        name = d.pop("name", UNSET)

        _preempt = d.pop("preempt", UNSET)
        preempt: V0044QosPreempt | Unset
        if isinstance(_preempt, Unset):
            preempt = UNSET
        else:
            preempt = V0044QosPreempt.from_dict(_preempt)

        _priority = d.pop("priority", UNSET)
        priority: V0044Uint32NoValStruct | Unset
        if isinstance(_priority, Unset):
            priority = UNSET
        else:
            priority = V0044Uint32NoValStruct.from_dict(_priority)

        _usage_factor = d.pop("usage_factor", UNSET)
        usage_factor: V0044Float64NoValStruct | Unset
        if isinstance(_usage_factor, Unset):
            usage_factor = UNSET
        else:
            usage_factor = V0044Float64NoValStruct.from_dict(_usage_factor)

        _usage_threshold = d.pop("usage_threshold", UNSET)
        usage_threshold: V0044Float64NoValStruct | Unset
        if isinstance(_usage_threshold, Unset):
            usage_threshold = UNSET
        else:
            usage_threshold = V0044Float64NoValStruct.from_dict(_usage_threshold)

        v0044_qos = cls(
            description=description,
            flags=flags,
            id=id,
            limits=limits,
            name=name,
            preempt=preempt,
            priority=priority,
            usage_factor=usage_factor,
            usage_threshold=usage_threshold,
        )

        v0044_qos.additional_properties = d
        return v0044_qos

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
