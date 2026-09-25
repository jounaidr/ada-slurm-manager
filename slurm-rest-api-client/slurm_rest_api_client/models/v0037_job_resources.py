from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v0037_node_allocation import V0037NodeAllocation


T = TypeVar("T", bound="V0037JobResources")


@_attrs_define
class V0037JobResources:
    """
    Attributes:
        nodes (str | Unset): list of assigned job nodes
        allocated_cpus (int | Unset): number of assigned job cpus
        allocated_hosts (int | Unset): number of assigned job hosts
        allocated_nodes (list[V0037NodeAllocation] | Unset): node allocations
    """

    nodes: str | Unset = UNSET
    allocated_cpus: int | Unset = UNSET
    allocated_hosts: int | Unset = UNSET
    allocated_nodes: list[V0037NodeAllocation] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        nodes = self.nodes

        allocated_cpus = self.allocated_cpus

        allocated_hosts = self.allocated_hosts

        allocated_nodes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.allocated_nodes, Unset):
            allocated_nodes = []
            for allocated_nodes_item_data in self.allocated_nodes:
                allocated_nodes_item = allocated_nodes_item_data.to_dict()
                allocated_nodes.append(allocated_nodes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if nodes is not UNSET:
            field_dict["nodes"] = nodes
        if allocated_cpus is not UNSET:
            field_dict["allocated_cpus"] = allocated_cpus
        if allocated_hosts is not UNSET:
            field_dict["allocated_hosts"] = allocated_hosts
        if allocated_nodes is not UNSET:
            field_dict["allocated_nodes"] = allocated_nodes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v0037_node_allocation import V0037NodeAllocation

        d = dict(src_dict)
        nodes = d.pop("nodes", UNSET)

        allocated_cpus = d.pop("allocated_cpus", UNSET)

        allocated_hosts = d.pop("allocated_hosts", UNSET)

        _allocated_nodes = d.pop("allocated_nodes", UNSET)
        allocated_nodes: list[V0037NodeAllocation] | Unset = UNSET
        if _allocated_nodes is not UNSET:
            allocated_nodes = []
            for allocated_nodes_item_data in _allocated_nodes:
                allocated_nodes_item = V0037NodeAllocation.from_dict(allocated_nodes_item_data)

                allocated_nodes.append(allocated_nodes_item)

        v0037_job_resources = cls(
            nodes=nodes,
            allocated_cpus=allocated_cpus,
            allocated_hosts=allocated_hosts,
            allocated_nodes=allocated_nodes,
        )

        v0037_job_resources.additional_properties = d
        return v0037_job_resources

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
