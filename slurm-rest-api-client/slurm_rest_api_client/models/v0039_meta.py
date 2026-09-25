from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v0039_meta_plugin import V0039MetaPlugin
    from ..models.v0039_meta_slurm import V0039MetaSlurm


T = TypeVar("T", bound="V0039Meta")


@_attrs_define
class V0039Meta:
    """
    Attributes:
        plugin (V0039MetaPlugin | Unset):
        slurm (V0039MetaSlurm | Unset): Slurm information
    """

    plugin: V0039MetaPlugin | Unset = UNSET
    slurm: V0039MetaSlurm | Unset = UNSET
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
        from ..models.v0039_meta_plugin import V0039MetaPlugin
        from ..models.v0039_meta_slurm import V0039MetaSlurm

        d = dict(src_dict)
        _plugin = d.pop("plugin", UNSET)
        plugin: V0039MetaPlugin | Unset
        if isinstance(_plugin, Unset):
            plugin = UNSET
        else:
            plugin = V0039MetaPlugin.from_dict(_plugin)

        _slurm = d.pop("Slurm", UNSET)
        slurm: V0039MetaSlurm | Unset
        if isinstance(_slurm, Unset):
            slurm = UNSET
        else:
            slurm = V0039MetaSlurm.from_dict(_slurm)

        v0039_meta = cls(
            plugin=plugin,
            slurm=slurm,
        )

        v0039_meta.additional_properties = d
        return v0039_meta

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
