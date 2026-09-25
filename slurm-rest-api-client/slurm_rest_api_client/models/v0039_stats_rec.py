from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v0039_rollup_stats_ptr_item import V0039RollupStatsPtrItem
    from ..models.v0039_stats_rpc import V0039StatsRpc
    from ..models.v0039_stats_user import V0039StatsUser


T = TypeVar("T", bound="V0039StatsRec")


@_attrs_define
class V0039StatsRec:
    """
    Attributes:
        time_start (int | Unset):
        rollups (list[V0039RollupStatsPtrItem] | Unset): list of recorded rollup statistics
        rp_cs (list[V0039StatsRpc] | Unset):
        users (list[V0039StatsUser] | Unset):
    """

    time_start: int | Unset = UNSET
    rollups: list[V0039RollupStatsPtrItem] | Unset = UNSET
    rp_cs: list[V0039StatsRpc] | Unset = UNSET
    users: list[V0039StatsUser] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        time_start = self.time_start

        rollups: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.rollups, Unset):
            rollups = []
            for componentsschemasv0_0_39_rollup_stats_ptr_item_data in self.rollups:
                componentsschemasv0_0_39_rollup_stats_ptr_item = (
                    componentsschemasv0_0_39_rollup_stats_ptr_item_data.to_dict()
                )
                rollups.append(componentsschemasv0_0_39_rollup_stats_ptr_item)

        rp_cs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.rp_cs, Unset):
            rp_cs = []
            for componentsschemasv0_0_39_stats_rpc_list_item_data in self.rp_cs:
                componentsschemasv0_0_39_stats_rpc_list_item = (
                    componentsschemasv0_0_39_stats_rpc_list_item_data.to_dict()
                )
                rp_cs.append(componentsschemasv0_0_39_stats_rpc_list_item)

        users: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.users, Unset):
            users = []
            for componentsschemasv0_0_39_stats_user_list_item_data in self.users:
                componentsschemasv0_0_39_stats_user_list_item = (
                    componentsschemasv0_0_39_stats_user_list_item_data.to_dict()
                )
                users.append(componentsschemasv0_0_39_stats_user_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if time_start is not UNSET:
            field_dict["time_start"] = time_start
        if rollups is not UNSET:
            field_dict["rollups"] = rollups
        if rp_cs is not UNSET:
            field_dict["RPCs"] = rp_cs
        if users is not UNSET:
            field_dict["users"] = users

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v0039_rollup_stats_ptr_item import V0039RollupStatsPtrItem
        from ..models.v0039_stats_rpc import V0039StatsRpc
        from ..models.v0039_stats_user import V0039StatsUser

        d = dict(src_dict)
        time_start = d.pop("time_start", UNSET)

        _rollups = d.pop("rollups", UNSET)
        rollups: list[V0039RollupStatsPtrItem] | Unset = UNSET
        if _rollups is not UNSET:
            rollups = []
            for componentsschemasv0_0_39_rollup_stats_ptr_item_data in _rollups:
                componentsschemasv0_0_39_rollup_stats_ptr_item = V0039RollupStatsPtrItem.from_dict(
                    componentsschemasv0_0_39_rollup_stats_ptr_item_data
                )

                rollups.append(componentsschemasv0_0_39_rollup_stats_ptr_item)

        _rp_cs = d.pop("RPCs", UNSET)
        rp_cs: list[V0039StatsRpc] | Unset = UNSET
        if _rp_cs is not UNSET:
            rp_cs = []
            for componentsschemasv0_0_39_stats_rpc_list_item_data in _rp_cs:
                componentsschemasv0_0_39_stats_rpc_list_item = V0039StatsRpc.from_dict(
                    componentsschemasv0_0_39_stats_rpc_list_item_data
                )

                rp_cs.append(componentsschemasv0_0_39_stats_rpc_list_item)

        _users = d.pop("users", UNSET)
        users: list[V0039StatsUser] | Unset = UNSET
        if _users is not UNSET:
            users = []
            for componentsschemasv0_0_39_stats_user_list_item_data in _users:
                componentsschemasv0_0_39_stats_user_list_item = V0039StatsUser.from_dict(
                    componentsschemasv0_0_39_stats_user_list_item_data
                )

                users.append(componentsschemasv0_0_39_stats_user_list_item)

        v0039_stats_rec = cls(
            time_start=time_start,
            rollups=rollups,
            rp_cs=rp_cs,
            users=users,
        )

        v0039_stats_rec.additional_properties = d
        return v0039_stats_rec

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
