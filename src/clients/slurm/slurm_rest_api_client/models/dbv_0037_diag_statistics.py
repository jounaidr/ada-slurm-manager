from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dbv_0037_diag_statistics_rollups_item import Dbv0037DiagStatisticsRollupsItem
    from ..models.dbv_0037_diag_statistics_rp_cs_item import Dbv0037DiagStatisticsRPCsItem
    from ..models.dbv_0037_diag_statistics_users_item import Dbv0037DiagStatisticsUsersItem


T = TypeVar("T", bound="Dbv0037DiagStatistics")


@_attrs_define
class Dbv0037DiagStatistics:
    """dictionary of Slurmdb statistics

    Attributes:
        time_start (int | Unset): Unix timestamp of start time
        rollups (list[Dbv0037DiagStatisticsRollupsItem] | Unset):
        rp_cs (list[Dbv0037DiagStatisticsRPCsItem] | Unset):
        users (list[Dbv0037DiagStatisticsUsersItem] | Unset):
    """

    time_start: int | Unset = UNSET
    rollups: list[Dbv0037DiagStatisticsRollupsItem] | Unset = UNSET
    rp_cs: list[Dbv0037DiagStatisticsRPCsItem] | Unset = UNSET
    users: list[Dbv0037DiagStatisticsUsersItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        time_start = self.time_start

        rollups: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.rollups, Unset):
            rollups = []
            for rollups_item_data in self.rollups:
                rollups_item = rollups_item_data.to_dict()
                rollups.append(rollups_item)

        rp_cs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.rp_cs, Unset):
            rp_cs = []
            for rp_cs_item_data in self.rp_cs:
                rp_cs_item = rp_cs_item_data.to_dict()
                rp_cs.append(rp_cs_item)

        users: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.users, Unset):
            users = []
            for users_item_data in self.users:
                users_item = users_item_data.to_dict()
                users.append(users_item)

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
        from ..models.dbv_0037_diag_statistics_rollups_item import Dbv0037DiagStatisticsRollupsItem
        from ..models.dbv_0037_diag_statistics_rp_cs_item import Dbv0037DiagStatisticsRPCsItem
        from ..models.dbv_0037_diag_statistics_users_item import Dbv0037DiagStatisticsUsersItem

        d = dict(src_dict)
        time_start = d.pop("time_start", UNSET)

        _rollups = d.pop("rollups", UNSET)
        rollups: list[Dbv0037DiagStatisticsRollupsItem] | Unset = UNSET
        if _rollups is not UNSET:
            rollups = []
            for rollups_item_data in _rollups:
                rollups_item = Dbv0037DiagStatisticsRollupsItem.from_dict(rollups_item_data)

                rollups.append(rollups_item)

        _rp_cs = d.pop("RPCs", UNSET)
        rp_cs: list[Dbv0037DiagStatisticsRPCsItem] | Unset = UNSET
        if _rp_cs is not UNSET:
            rp_cs = []
            for rp_cs_item_data in _rp_cs:
                rp_cs_item = Dbv0037DiagStatisticsRPCsItem.from_dict(rp_cs_item_data)

                rp_cs.append(rp_cs_item)

        _users = d.pop("users", UNSET)
        users: list[Dbv0037DiagStatisticsUsersItem] | Unset = UNSET
        if _users is not UNSET:
            users = []
            for users_item_data in _users:
                users_item = Dbv0037DiagStatisticsUsersItem.from_dict(users_item_data)

                users.append(users_item)

        dbv_0037_diag_statistics = cls(
            time_start=time_start,
            rollups=rollups,
            rp_cs=rp_cs,
            users=users,
        )

        dbv_0037_diag_statistics.additional_properties = d
        return dbv_0037_diag_statistics

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
