from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dbv_0038_meta_plugin import Dbv0038MetaPlugin
    from ..models.dbv_0038_meta_slurm import Dbv0038MetaSlurm


T = TypeVar("T", bound="Dbv0038Meta")


@_attrs_define
class Dbv0038Meta:
    """
    Attributes:
        plugin (Dbv0038MetaPlugin | Unset):
        slurm (Dbv0038MetaSlurm | Unset): Slurm information
    """

    plugin: Dbv0038MetaPlugin | Unset = UNSET
    slurm: Dbv0038MetaSlurm | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        plugin: dict[str, Any] | Unset = UNSET
        if not isinstance(self.plugin, Unset):
            plugin = self.plugin.to_dict()

        slurm: dict[str, Any] | Unset = UNSET
        if not isinstance(self.slurm, Unset):
            slurm = self.slurm.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if plugin is not UNSET:
            field_dict["plugin"] = plugin
        if slurm is not UNSET:
            field_dict["Slurm"] = slurm

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dbv_0038_meta_plugin import Dbv0038MetaPlugin
        from ..models.dbv_0038_meta_slurm import Dbv0038MetaSlurm

        d = dict(src_dict)
        _plugin = d.pop("plugin", UNSET)
        plugin: Dbv0038MetaPlugin | Unset
        if isinstance(_plugin, Unset):
            plugin = UNSET
        else:
            plugin = Dbv0038MetaPlugin.from_dict(_plugin)

        _slurm = d.pop("Slurm", UNSET)
        slurm: Dbv0038MetaSlurm | Unset
        if isinstance(_slurm, Unset):
            slurm = UNSET
        else:
            slurm = Dbv0038MetaSlurm.from_dict(_slurm)

        dbv_0038_meta = cls(
            plugin=plugin,
            slurm=slurm,
        )

        dbv_0038_meta.additional_properties = d
        return dbv_0038_meta

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
