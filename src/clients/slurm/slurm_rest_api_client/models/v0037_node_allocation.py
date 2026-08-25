from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v0037_node_allocation_cores import V0037NodeAllocationCores
    from ..models.v0037_node_allocation_cpus import V0037NodeAllocationCpus
    from ..models.v0037_node_allocation_sockets import V0037NodeAllocationSockets


T = TypeVar("T", bound="V0037NodeAllocation")


@_attrs_define
class V0037NodeAllocation:
    """
    Attributes:
        memory (int | Unset): amount of assigned job memory
        cpus (V0037NodeAllocationCpus | Unset): amount of assigned job CPUs
        sockets (V0037NodeAllocationSockets | Unset): assignment status of each socket by socket id
        cores (V0037NodeAllocationCores | Unset): assignment status of each core by core id
    """

    memory: int | Unset = UNSET
    cpus: V0037NodeAllocationCpus | Unset = UNSET
    sockets: V0037NodeAllocationSockets | Unset = UNSET
    cores: V0037NodeAllocationCores | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        memory = self.memory

        cpus: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cpus, Unset):
            cpus = self.cpus.to_dict()

        sockets: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sockets, Unset):
            sockets = self.sockets.to_dict()

        cores: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cores, Unset):
            cores = self.cores.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if memory is not UNSET:
            field_dict["memory"] = memory
        if cpus is not UNSET:
            field_dict["cpus"] = cpus
        if sockets is not UNSET:
            field_dict["sockets"] = sockets
        if cores is not UNSET:
            field_dict["cores"] = cores

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v0037_node_allocation_cores import V0037NodeAllocationCores
        from ..models.v0037_node_allocation_cpus import V0037NodeAllocationCpus
        from ..models.v0037_node_allocation_sockets import V0037NodeAllocationSockets

        d = dict(src_dict)
        memory = d.pop("memory", UNSET)

        _cpus = d.pop("cpus", UNSET)
        cpus: V0037NodeAllocationCpus | Unset
        if isinstance(_cpus, Unset):
            cpus = UNSET
        else:
            cpus = V0037NodeAllocationCpus.from_dict(_cpus)

        _sockets = d.pop("sockets", UNSET)
        sockets: V0037NodeAllocationSockets | Unset
        if isinstance(_sockets, Unset):
            sockets = UNSET
        else:
            sockets = V0037NodeAllocationSockets.from_dict(_sockets)

        _cores = d.pop("cores", UNSET)
        cores: V0037NodeAllocationCores | Unset
        if isinstance(_cores, Unset):
            cores = UNSET
        else:
            cores = V0037NodeAllocationCores.from_dict(_cores)

        v0037_node_allocation = cls(
            memory=memory,
            cpus=cpus,
            sockets=sockets,
            cores=cores,
        )

        v0037_node_allocation.additional_properties = d
        return v0037_node_allocation

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
