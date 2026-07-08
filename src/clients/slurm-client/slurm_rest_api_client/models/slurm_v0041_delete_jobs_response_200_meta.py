from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.slurm_v0041_delete_jobs_response_200_meta_client import SlurmV0041DeleteJobsResponse200MetaClient
    from ..models.slurm_v0041_delete_jobs_response_200_meta_plugin import SlurmV0041DeleteJobsResponse200MetaPlugin
    from ..models.slurm_v0041_delete_jobs_response_200_meta_slurm import SlurmV0041DeleteJobsResponse200MetaSlurm


T = TypeVar("T", bound="SlurmV0041DeleteJobsResponse200Meta")


@_attrs_define
class SlurmV0041DeleteJobsResponse200Meta:
    """Slurm meta values

    Attributes:
        plugin (SlurmV0041DeleteJobsResponse200MetaPlugin | Unset):
        client (SlurmV0041DeleteJobsResponse200MetaClient | Unset):
        command (list[str] | Unset): CLI command (if applicable)
        slurm (SlurmV0041DeleteJobsResponse200MetaSlurm | Unset):
    """

    plugin: SlurmV0041DeleteJobsResponse200MetaPlugin | Unset = UNSET
    client: SlurmV0041DeleteJobsResponse200MetaClient | Unset = UNSET
    command: list[str] | Unset = UNSET
    slurm: SlurmV0041DeleteJobsResponse200MetaSlurm | Unset = UNSET
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
        from ..models.slurm_v0041_delete_jobs_response_200_meta_client import SlurmV0041DeleteJobsResponse200MetaClient
        from ..models.slurm_v0041_delete_jobs_response_200_meta_plugin import SlurmV0041DeleteJobsResponse200MetaPlugin
        from ..models.slurm_v0041_delete_jobs_response_200_meta_slurm import SlurmV0041DeleteJobsResponse200MetaSlurm

        d = dict(src_dict)
        _plugin = d.pop("plugin", UNSET)
        plugin: SlurmV0041DeleteJobsResponse200MetaPlugin | Unset
        if isinstance(_plugin, Unset):
            plugin = UNSET
        else:
            plugin = SlurmV0041DeleteJobsResponse200MetaPlugin.from_dict(_plugin)

        _client = d.pop("client", UNSET)
        client: SlurmV0041DeleteJobsResponse200MetaClient | Unset
        if isinstance(_client, Unset):
            client = UNSET
        else:
            client = SlurmV0041DeleteJobsResponse200MetaClient.from_dict(_client)

        command = cast(list[str], d.pop("command", UNSET))

        _slurm = d.pop("slurm", UNSET)
        slurm: SlurmV0041DeleteJobsResponse200MetaSlurm | Unset
        if isinstance(_slurm, Unset):
            slurm = UNSET
        else:
            slurm = SlurmV0041DeleteJobsResponse200MetaSlurm.from_dict(_slurm)

        slurm_v0041_delete_jobs_response_200_meta = cls(
            plugin=plugin,
            client=client,
            command=command,
            slurm=slurm,
        )

        slurm_v0041_delete_jobs_response_200_meta.additional_properties = d
        return slurm_v0041_delete_jobs_response_200_meta

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
