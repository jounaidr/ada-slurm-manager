from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v0038_node_allocation_sockets_cores import V0038NodeAllocationSocketsCores


T = TypeVar("T", bound="V0038NodeAllocationSockets")


@_attrs_define
class V0038NodeAllocationSockets:
    """assignment status of each socket by numeric socket id

    Attributes:
        cores (V0038NodeAllocationSocketsCores | Unset): assignment status of each core by core id in each socket
    """

    cores: V0038NodeAllocationSocketsCores | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cores: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cores, Unset):
            cores = self.cores.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cores is not UNSET:
            field_dict["cores"] = cores

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v0038_node_allocation_sockets_cores import V0038NodeAllocationSocketsCores

        d = dict(src_dict)
        _cores = d.pop("cores", UNSET)
        cores: V0038NodeAllocationSocketsCores | Unset
        if isinstance(_cores, Unset):
            cores = UNSET
        else:
            cores = V0038NodeAllocationSocketsCores.from_dict(_cores)

        v0038_node_allocation_sockets = cls(
            cores=cores,
        )

        v0038_node_allocation_sockets.additional_properties = d
        return v0038_node_allocation_sockets

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
