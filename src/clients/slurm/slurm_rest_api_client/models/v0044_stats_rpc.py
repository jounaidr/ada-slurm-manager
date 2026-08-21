from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v0044_stats_rpc_time import V0044StatsRpcTime


T = TypeVar("T", bound="V0044StatsRpc")


@_attrs_define
class V0044StatsRpc:
    """
    Attributes:
        rpc (str | Unset): RPC type
        count (int | Unset): Number of RPCs processed
        time (V0044StatsRpcTime | Unset):
    """

    rpc: str | Unset = UNSET
    count: int | Unset = UNSET
    time: V0044StatsRpcTime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rpc = self.rpc

        count = self.count

        time: dict[str, Any] | Unset = UNSET
        if not isinstance(self.time, Unset):
            time = self.time.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rpc is not UNSET:
            field_dict["rpc"] = rpc
        if count is not UNSET:
            field_dict["count"] = count
        if time is not UNSET:
            field_dict["time"] = time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v0044_stats_rpc_time import V0044StatsRpcTime

        d = dict(src_dict)
        rpc = d.pop("rpc", UNSET)

        count = d.pop("count", UNSET)

        _time = d.pop("time", UNSET)
        time: V0044StatsRpcTime | Unset
        if isinstance(_time, Unset):
            time = UNSET
        else:
            time = V0044StatsRpcTime.from_dict(_time)

        v0044_stats_rpc = cls(
            rpc=rpc,
            count=count,
            time=time,
        )

        v0044_stats_rpc.additional_properties = d
        return v0044_stats_rpc

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
