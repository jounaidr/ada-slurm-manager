from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v0044_node_gres_layout import V0044NodeGresLayout
    from ..models.v0044_uint_32_no_val_struct import V0044Uint32NoValStruct


T = TypeVar("T", bound="V0044NodeResourceLayout")


@_attrs_define
class V0044NodeResourceLayout:
    """
    Attributes:
        node (str): Node name
        sockets_per_node (int | Unset): Sockets per node
        cores_per_socket (int | Unset): Cores per socket
        mem_alloc (int | Unset): Allocated memory
        core_bitmap (str | Unset): Abstract core bitmap
        channel (V0044Uint32NoValStruct | Unset):
        gres (list[V0044NodeGresLayout] | Unset):
    """

    node: str
    sockets_per_node: int | Unset = UNSET
    cores_per_socket: int | Unset = UNSET
    mem_alloc: int | Unset = UNSET
    core_bitmap: str | Unset = UNSET
    channel: V0044Uint32NoValStruct | Unset = UNSET
    gres: list[V0044NodeGresLayout] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        node = self.node

        sockets_per_node = self.sockets_per_node

        cores_per_socket = self.cores_per_socket

        mem_alloc = self.mem_alloc

        core_bitmap = self.core_bitmap

        channel: dict[str, Any] | Unset = UNSET
        if not isinstance(self.channel, Unset):
            channel = self.channel.to_dict()

        gres: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.gres, Unset):
            gres = []
            for componentsschemasv0_0_44_node_gres_layout_list_item_data in self.gres:
                componentsschemasv0_0_44_node_gres_layout_list_item = (
                    componentsschemasv0_0_44_node_gres_layout_list_item_data.to_dict()
                )
                gres.append(componentsschemasv0_0_44_node_gres_layout_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "node": node,
            }
        )
        if sockets_per_node is not UNSET:
            field_dict["sockets_per_node"] = sockets_per_node
        if cores_per_socket is not UNSET:
            field_dict["cores_per_socket"] = cores_per_socket
        if mem_alloc is not UNSET:
            field_dict["mem_alloc"] = mem_alloc
        if core_bitmap is not UNSET:
            field_dict["core_bitmap"] = core_bitmap
        if channel is not UNSET:
            field_dict["channel"] = channel
        if gres is not UNSET:
            field_dict["gres"] = gres

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v0044_node_gres_layout import V0044NodeGresLayout
        from ..models.v0044_uint_32_no_val_struct import V0044Uint32NoValStruct

        d = dict(src_dict)
        node = d.pop("node")

        sockets_per_node = d.pop("sockets_per_node", UNSET)

        cores_per_socket = d.pop("cores_per_socket", UNSET)

        mem_alloc = d.pop("mem_alloc", UNSET)

        core_bitmap = d.pop("core_bitmap", UNSET)

        _channel = d.pop("channel", UNSET)
        channel: V0044Uint32NoValStruct | Unset
        if isinstance(_channel, Unset):
            channel = UNSET
        else:
            channel = V0044Uint32NoValStruct.from_dict(_channel)

        _gres = d.pop("gres", UNSET)
        gres: list[V0044NodeGresLayout] | Unset = UNSET
        if _gres is not UNSET:
            gres = []
            for componentsschemasv0_0_44_node_gres_layout_list_item_data in _gres:
                componentsschemasv0_0_44_node_gres_layout_list_item = V0044NodeGresLayout.from_dict(
                    componentsschemasv0_0_44_node_gres_layout_list_item_data
                )

                gres.append(componentsschemasv0_0_44_node_gres_layout_list_item)

        v0044_node_resource_layout = cls(
            node=node,
            sockets_per_node=sockets_per_node,
            cores_per_socket=cores_per_socket,
            mem_alloc=mem_alloc,
            core_bitmap=core_bitmap,
            channel=channel,
            gres=gres,
        )

        v0044_node_resource_layout.additional_properties = d
        return v0044_node_resource_layout

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
