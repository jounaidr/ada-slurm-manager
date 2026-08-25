from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.v0039_cluster_rec_flags_item import V0039ClusterRecFlagsItem
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v0039_cluster_rec_associations import V0039ClusterRecAssociations
    from ..models.v0039_cluster_rec_controller import V0039ClusterRecController
    from ..models.v0039_tres import V0039Tres


T = TypeVar("T", bound="V0039ClusterRec")


@_attrs_define
class V0039ClusterRec:
    """
    Attributes:
        controller (V0039ClusterRecController | Unset):
        flags (list[V0039ClusterRecFlagsItem] | Unset):
        name (str | Unset):
        nodes (str | Unset):
        select_plugin (str | Unset):
        associations (V0039ClusterRecAssociations | Unset):
        rpc_version (int | Unset):
        tres (list[V0039Tres] | Unset):
    """

    controller: V0039ClusterRecController | Unset = UNSET
    flags: list[V0039ClusterRecFlagsItem] | Unset = UNSET
    name: str | Unset = UNSET
    nodes: str | Unset = UNSET
    select_plugin: str | Unset = UNSET
    associations: V0039ClusterRecAssociations | Unset = UNSET
    rpc_version: int | Unset = UNSET
    tres: list[V0039Tres] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        controller: dict[str, Any] | Unset = UNSET
        if not isinstance(self.controller, Unset):
            controller = self.controller.to_dict()

        flags: list[str] | Unset = UNSET
        if not isinstance(self.flags, Unset):
            flags = []
            for flags_item_data in self.flags:
                flags_item = flags_item_data.value
                flags.append(flags_item)

        name = self.name

        nodes = self.nodes

        select_plugin = self.select_plugin

        associations: dict[str, Any] | Unset = UNSET
        if not isinstance(self.associations, Unset):
            associations = self.associations.to_dict()

        rpc_version = self.rpc_version

        tres: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tres, Unset):
            tres = []
            for componentsschemasv0_0_39_tres_str_item_data in self.tres:
                componentsschemasv0_0_39_tres_str_item = componentsschemasv0_0_39_tres_str_item_data.to_dict()
                tres.append(componentsschemasv0_0_39_tres_str_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if controller is not UNSET:
            field_dict["controller"] = controller
        if flags is not UNSET:
            field_dict["flags"] = flags
        if name is not UNSET:
            field_dict["name"] = name
        if nodes is not UNSET:
            field_dict["nodes"] = nodes
        if select_plugin is not UNSET:
            field_dict["select_plugin"] = select_plugin
        if associations is not UNSET:
            field_dict["associations"] = associations
        if rpc_version is not UNSET:
            field_dict["rpc_version"] = rpc_version
        if tres is not UNSET:
            field_dict["tres"] = tres

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v0039_cluster_rec_associations import V0039ClusterRecAssociations
        from ..models.v0039_cluster_rec_controller import V0039ClusterRecController
        from ..models.v0039_tres import V0039Tres

        d = dict(src_dict)
        _controller = d.pop("controller", UNSET)
        controller: V0039ClusterRecController | Unset
        if isinstance(_controller, Unset):
            controller = UNSET
        else:
            controller = V0039ClusterRecController.from_dict(_controller)

        _flags = d.pop("flags", UNSET)
        flags: list[V0039ClusterRecFlagsItem] | Unset = UNSET
        if _flags is not UNSET:
            flags = []
            for flags_item_data in _flags:
                flags_item = V0039ClusterRecFlagsItem(flags_item_data)

                flags.append(flags_item)

        name = d.pop("name", UNSET)

        nodes = d.pop("nodes", UNSET)

        select_plugin = d.pop("select_plugin", UNSET)

        _associations = d.pop("associations", UNSET)
        associations: V0039ClusterRecAssociations | Unset
        if isinstance(_associations, Unset):
            associations = UNSET
        else:
            associations = V0039ClusterRecAssociations.from_dict(_associations)

        rpc_version = d.pop("rpc_version", UNSET)

        _tres = d.pop("tres", UNSET)
        tres: list[V0039Tres] | Unset = UNSET
        if _tres is not UNSET:
            tres = []
            for componentsschemasv0_0_39_tres_str_item_data in _tres:
                componentsschemasv0_0_39_tres_str_item = V0039Tres.from_dict(
                    componentsschemasv0_0_39_tres_str_item_data
                )

                tres.append(componentsschemasv0_0_39_tres_str_item)

        v0039_cluster_rec = cls(
            controller=controller,
            flags=flags,
            name=name,
            nodes=nodes,
            select_plugin=select_plugin,
            associations=associations,
            rpc_version=rpc_version,
            tres=tres,
        )

        v0039_cluster_rec.additional_properties = d
        return v0039_cluster_rec

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
