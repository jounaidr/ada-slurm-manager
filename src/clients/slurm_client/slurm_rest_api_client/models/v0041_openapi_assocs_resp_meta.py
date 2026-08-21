from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v0041_openapi_assocs_resp_meta_client import V0041OpenapiAssocsRespMetaClient
    from ..models.v0041_openapi_assocs_resp_meta_plugin import V0041OpenapiAssocsRespMetaPlugin
    from ..models.v0041_openapi_assocs_resp_meta_slurm import V0041OpenapiAssocsRespMetaSlurm


T = TypeVar("T", bound="V0041OpenapiAssocsRespMeta")


@_attrs_define
class V0041OpenapiAssocsRespMeta:
    """Slurm meta values

    Attributes:
        plugin (V0041OpenapiAssocsRespMetaPlugin | Unset):
        client (V0041OpenapiAssocsRespMetaClient | Unset):
        command (list[str] | Unset): CLI command (if applicable)
        slurm (V0041OpenapiAssocsRespMetaSlurm | Unset):
    """

    plugin: V0041OpenapiAssocsRespMetaPlugin | Unset = UNSET
    client: V0041OpenapiAssocsRespMetaClient | Unset = UNSET
    command: list[str] | Unset = UNSET
    slurm: V0041OpenapiAssocsRespMetaSlurm | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        plugin: dict[str, Any] | Unset = UNSET
        if not isinstance(self.plugin, Unset):
            plugin = self.plugin.to_dict()

        client: dict[str, Any] | Unset = UNSET
        if not isinstance(self.client, Unset):
            client = self.client.to_dict()

        command: list[str] | Unset = UNSET
        if not isinstance(self.command, Unset):
            command = self.command

        slurm: dict[str, Any] | Unset = UNSET
        if not isinstance(self.slurm, Unset):
            slurm = self.slurm.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if plugin is not UNSET:
            field_dict["plugin"] = plugin
        if client is not UNSET:
            field_dict["client"] = client
        if command is not UNSET:
            field_dict["command"] = command
        if slurm is not UNSET:
            field_dict["slurm"] = slurm

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v0041_openapi_assocs_resp_meta_client import V0041OpenapiAssocsRespMetaClient
        from ..models.v0041_openapi_assocs_resp_meta_plugin import V0041OpenapiAssocsRespMetaPlugin
        from ..models.v0041_openapi_assocs_resp_meta_slurm import V0041OpenapiAssocsRespMetaSlurm

        d = dict(src_dict)
        _plugin = d.pop("plugin", UNSET)
        plugin: V0041OpenapiAssocsRespMetaPlugin | Unset
        if isinstance(_plugin, Unset):
            plugin = UNSET
        else:
            plugin = V0041OpenapiAssocsRespMetaPlugin.from_dict(_plugin)

        _client = d.pop("client", UNSET)
        client: V0041OpenapiAssocsRespMetaClient | Unset
        if isinstance(_client, Unset):
            client = UNSET
        else:
            client = V0041OpenapiAssocsRespMetaClient.from_dict(_client)

        command = cast(list[str], d.pop("command", UNSET))

        _slurm = d.pop("slurm", UNSET)
        slurm: V0041OpenapiAssocsRespMetaSlurm | Unset
        if isinstance(_slurm, Unset):
            slurm = UNSET
        else:
            slurm = V0041OpenapiAssocsRespMetaSlurm.from_dict(_slurm)

        v0041_openapi_assocs_resp_meta = cls(
            plugin=plugin,
            client=client,
            command=command,
            slurm=slurm,
        )

        v0041_openapi_assocs_resp_meta.additional_properties = d
        return v0041_openapi_assocs_resp_meta

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
