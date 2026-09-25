from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dbv_0038_cluster_info_associations import Dbv0038ClusterInfoAssociations
    from ..models.dbv_0038_cluster_info_controller import Dbv0038ClusterInfoController
    from ..models.dbv_0038_response_tres import Dbv0038ResponseTres


T = TypeVar("T", bound="Dbv0038ClusterInfo")


@_attrs_define
class Dbv0038ClusterInfo:
    """
    Attributes:
        controller (Dbv0038ClusterInfoController | Unset): Information about controller
        flags (list[str] | Unset): List of properties of cluster
        name (str | Unset): Cluster name
        nodes (str | Unset): Assigned nodes
        select_plugin (str | Unset): Configured select plugin
        associations (Dbv0038ClusterInfoAssociations | Unset): Information about associations
        rpc_version (int | Unset): Number rpc version
        tres (list[Dbv0038ResponseTres] | Unset): List of TRES in cluster
    """

    controller: Dbv0038ClusterInfoController | Unset = UNSET
    flags: list[str] | Unset = UNSET
    name: str | Unset = UNSET
    nodes: str | Unset = UNSET
    select_plugin: str | Unset = UNSET
    associations: Dbv0038ClusterInfoAssociations | Unset = UNSET
    rpc_version: int | Unset = UNSET
    tres: list[Dbv0038ResponseTres] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        controller: dict[str, Any] | Unset = UNSET
        if not isinstance(self.controller, Unset):
            controller = self.controller.to_dict()

        flags: list[str] | Unset = UNSET
        if not isinstance(self.flags, Unset):
            flags = self.flags

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
            for tres_item_data in self.tres:
                tres_item = tres_item_data.to_dict()
                tres.append(tres_item)

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
        from ..models.dbv_0038_cluster_info_associations import Dbv0038ClusterInfoAssociations
        from ..models.dbv_0038_cluster_info_controller import Dbv0038ClusterInfoController
        from ..models.dbv_0038_response_tres import Dbv0038ResponseTres

        d = dict(src_dict)
        _controller = d.pop("controller", UNSET)
        controller: Dbv0038ClusterInfoController | Unset
        if isinstance(_controller, Unset):
            controller = UNSET
        else:
            controller = Dbv0038ClusterInfoController.from_dict(_controller)

        flags = cast(list[str], d.pop("flags", UNSET))

        name = d.pop("name", UNSET)

        nodes = d.pop("nodes", UNSET)

        select_plugin = d.pop("select_plugin", UNSET)

        _associations = d.pop("associations", UNSET)
        associations: Dbv0038ClusterInfoAssociations | Unset
        if isinstance(_associations, Unset):
            associations = UNSET
        else:
            associations = Dbv0038ClusterInfoAssociations.from_dict(_associations)

        rpc_version = d.pop("rpc_version", UNSET)

        _tres = d.pop("tres", UNSET)
        tres: list[Dbv0038ResponseTres] | Unset = UNSET
        if _tres is not UNSET:
            tres = []
            for tres_item_data in _tres:
                tres_item = Dbv0038ResponseTres.from_dict(tres_item_data)

                tres.append(tres_item)

        dbv_0038_cluster_info = cls(
            controller=controller,
            flags=flags,
            name=name,
            nodes=nodes,
            select_plugin=select_plugin,
            associations=associations,
            rpc_version=rpc_version,
            tres=tres,
        )

        dbv_0038_cluster_info.additional_properties = d
        return dbv_0038_cluster_info

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
