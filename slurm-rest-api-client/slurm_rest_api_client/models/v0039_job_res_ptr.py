from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="V0039JobResPtr")


@_attrs_define
class V0039JobResPtr:
    """
    Attributes:
        nodes (str | Unset):
        allocated_cores (int | Unset):
        allocated_cpus (int | Unset):
        allocated_hosts (int | Unset):
        allocated_nodes (list[Any] | Unset): job node resources
    """

    nodes: str | Unset = UNSET
    allocated_cores: int | Unset = UNSET
    allocated_cpus: int | Unset = UNSET
    allocated_hosts: int | Unset = UNSET
    allocated_nodes: list[Any] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        nodes = self.nodes

        allocated_cores = self.allocated_cores

        allocated_cpus = self.allocated_cpus

        allocated_hosts = self.allocated_hosts

        allocated_nodes: list[Any] | Unset = UNSET
        if not isinstance(self.allocated_nodes, Unset):
            allocated_nodes = self.allocated_nodes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if nodes is not UNSET:
            field_dict["nodes"] = nodes
        if allocated_cores is not UNSET:
            field_dict["allocated_cores"] = allocated_cores
        if allocated_cpus is not UNSET:
            field_dict["allocated_cpus"] = allocated_cpus
        if allocated_hosts is not UNSET:
            field_dict["allocated_hosts"] = allocated_hosts
        if allocated_nodes is not UNSET:
            field_dict["allocated_nodes"] = allocated_nodes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        nodes = d.pop("nodes", UNSET)

        allocated_cores = d.pop("allocated_cores", UNSET)

        allocated_cpus = d.pop("allocated_cpus", UNSET)

        allocated_hosts = d.pop("allocated_hosts", UNSET)

        allocated_nodes = cast(list[Any], d.pop("allocated_nodes", UNSET))

        v0039_job_res_ptr = cls(
            nodes=nodes,
            allocated_cores=allocated_cores,
            allocated_cpus=allocated_cpus,
            allocated_hosts=allocated_hosts,
            allocated_nodes=allocated_nodes,
        )

        v0039_job_res_ptr.additional_properties = d
        return v0039_job_res_ptr

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
