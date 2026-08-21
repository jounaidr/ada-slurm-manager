from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.v0043_cluster_rec_flags_item import V0043ClusterRecFlagsItem
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v0043_cluster_rec_associations import V0043ClusterRecAssociations
    from ..models.v0043_cluster_rec_controller import V0043ClusterRecController
    from ..models.v0043_tres import V0043Tres


T = TypeVar("T", bound="V0043ClusterRec")


@_attrs_define
class V0043ClusterRec:
    """
    Attributes:
        controller (V0043ClusterRecController | Unset):
        flags (list[V0043ClusterRecFlagsItem] | Unset): Flags
        name (str | Unset): ClusterName
        nodes (str | Unset): Node names
        select_plugin (str | Unset):
        associations (V0043ClusterRecAssociations | Unset):
        rpc_version (int | Unset): RPC version used in the cluster
        tres (list[V0043Tres] | Unset):
    """

    controller: V0043ClusterRecController | Unset = UNSET
    flags: list[V0043ClusterRecFlagsItem] | Unset = UNSET
    name: str | Unset = UNSET
    nodes: str | Unset = UNSET
    select_plugin: str | Unset = UNSET
    associations: V0043ClusterRecAssociations | Unset = UNSET
    rpc_version: int | Unset = UNSET
    tres: list[V0043Tres] | Unset = UNSET
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
            for componentsschemasv0_0_43_tres_list_item_data in self.tres:
                componentsschemasv0_0_43_tres_list_item = componentsschemasv0_0_43_tres_list_item_data.to_dict()
                tres.append(componentsschemasv0_0_43_tres_list_item)

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
        from ..models.v0043_cluster_rec_associations import V0043ClusterRecAssociations
        from ..models.v0043_cluster_rec_controller import V0043ClusterRecController
        from ..models.v0043_tres import V0043Tres

        d = dict(src_dict)
        _controller = d.pop("controller", UNSET)
        controller: V0043ClusterRecController | Unset
        if isinstance(_controller, Unset):
            controller = UNSET
        else:
            controller = V0043ClusterRecController.from_dict(_controller)

        _flags = d.pop("flags", UNSET)
        flags: list[V0043ClusterRecFlagsItem] | Unset = UNSET
        if _flags is not UNSET:
            flags = []
            for flags_item_data in _flags:
                flags_item = V0043ClusterRecFlagsItem(flags_item_data)

                flags.append(flags_item)

        name = d.pop("name", UNSET)

        nodes = d.pop("nodes", UNSET)

        select_plugin = d.pop("select_plugin", UNSET)

        _associations = d.pop("associations", UNSET)
        associations: V0043ClusterRecAssociations | Unset
        if isinstance(_associations, Unset):
            associations = UNSET
        else:
            associations = V0043ClusterRecAssociations.from_dict(_associations)

        rpc_version = d.pop("rpc_version", UNSET)

        _tres = d.pop("tres", UNSET)
        tres: list[V0043Tres] | Unset = UNSET
        if _tres is not UNSET:
            tres = []
            for componentsschemasv0_0_43_tres_list_item_data in _tres:
                componentsschemasv0_0_43_tres_list_item = V0043Tres.from_dict(
                    componentsschemasv0_0_43_tres_list_item_data
                )

                tres.append(componentsschemasv0_0_43_tres_list_item)

        v0043_cluster_rec = cls(
            controller=controller,
            flags=flags,
            name=name,
            nodes=nodes,
            select_plugin=select_plugin,
            associations=associations,
            rpc_version=rpc_version,
            tres=tres,
        )

        v0043_cluster_rec.additional_properties = d
        return v0043_cluster_rec

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
