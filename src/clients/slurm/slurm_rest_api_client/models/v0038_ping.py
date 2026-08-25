from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.v0038_ping_ping import V0038PingPing
from ..types import UNSET, Unset

T = TypeVar("T", bound="V0038Ping")


@_attrs_define
class V0038Ping:
    """
    Attributes:
        hostname (str | Unset): slurm controller hostname
        ping (V0038PingPing | Unset): slurm controller host up
        mode (str | Unset): slurm controller mode
        status (int | Unset): slurm controller status
    """

    hostname: str | Unset = UNSET
    ping: V0038PingPing | Unset = UNSET
    mode: str | Unset = UNSET
    status: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hostname = self.hostname

        ping: str | Unset = UNSET
        if not isinstance(self.ping, Unset):
            ping = self.ping.value

        mode = self.mode

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hostname is not UNSET:
            field_dict["hostname"] = hostname
        if ping is not UNSET:
            field_dict["ping"] = ping
        if mode is not UNSET:
            field_dict["mode"] = mode
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        hostname = d.pop("hostname", UNSET)

        _ping = d.pop("ping", UNSET)
        ping: V0038PingPing | Unset
        if isinstance(_ping, Unset):
            ping = UNSET
        else:
            ping = V0038PingPing(_ping)

        mode = d.pop("mode", UNSET)

        status = d.pop("status", UNSET)

        v0038_ping = cls(
            hostname=hostname,
            ping=ping,
            mode=mode,
            status=status,
        )

        v0038_ping.additional_properties = d
        return v0038_ping

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
