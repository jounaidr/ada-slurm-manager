from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v0038_node_allocation_sockets import V0038NodeAllocationSockets


T = TypeVar("T", bound="V0038NodeAllocation")


@_attrs_define
class V0038NodeAllocation:
    """
    Attributes:
        memory (int | Unset): amount of assigned job memory
        cpus (int | Unset): number of assigned job CPUs
        sockets (V0038NodeAllocationSockets | Unset): assignment status of each socket by numeric socket id
        nodename (str | Unset): node name
    """

    memory: int | Unset = UNSET
    cpus: int | Unset = UNSET
    sockets: V0038NodeAllocationSockets | Unset = UNSET
    nodename: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        memory = self.memory

        cpus = self.cpus

        sockets: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sockets, Unset):
            sockets = self.sockets.to_dict()

        nodename = self.nodename

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if memory is not UNSET:
            field_dict["memory"] = memory
        if cpus is not UNSET:
            field_dict["cpus"] = cpus
        if sockets is not UNSET:
            field_dict["sockets"] = sockets
        if nodename is not UNSET:
            field_dict["nodename"] = nodename

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v0038_node_allocation_sockets import V0038NodeAllocationSockets

        d = dict(src_dict)
        memory = d.pop("memory", UNSET)

        cpus = d.pop("cpus", UNSET)

        _sockets = d.pop("sockets", UNSET)
        sockets: V0038NodeAllocationSockets | Unset
        if isinstance(_sockets, Unset):
            sockets = UNSET
        else:
            sockets = V0038NodeAllocationSockets.from_dict(_sockets)

        nodename = d.pop("nodename", UNSET)

        v0038_node_allocation = cls(
            memory=memory,
            cpus=cpus,
            sockets=sockets,
            nodename=nodename,
        )

        v0038_node_allocation.additional_properties = d
        return v0038_node_allocation

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
