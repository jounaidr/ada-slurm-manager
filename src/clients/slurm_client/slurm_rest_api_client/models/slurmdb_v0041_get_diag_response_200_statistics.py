from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.slurmdb_v0041_get_diag_response_200_statistics_rollups import (
        SlurmdbV0041GetDiagResponse200StatisticsRollups,
    )
    from ..models.slurmdb_v0041_get_diag_response_200_statistics_rp_cs_item import (
        SlurmdbV0041GetDiagResponse200StatisticsRPCsItem,
    )
    from ..models.slurmdb_v0041_get_diag_response_200_statistics_users_item import (
        SlurmdbV0041GetDiagResponse200StatisticsUsersItem,
    )


T = TypeVar("T", bound="SlurmdbV0041GetDiagResponse200Statistics")


@_attrs_define
class SlurmdbV0041GetDiagResponse200Statistics:
    """statistics

    Attributes:
        time_start (int | Unset): When data collection started (UNIX timestamp)
        rollups (SlurmdbV0041GetDiagResponse200StatisticsRollups | Unset): Rollup statistics
        rp_cs (list[SlurmdbV0041GetDiagResponse200StatisticsRPCsItem] | Unset): List of RPCs sent to the slurmdbd
        users (list[SlurmdbV0041GetDiagResponse200StatisticsUsersItem] | Unset): List of users that issued RPCs
    """

    time_start: int | Unset = UNSET
    rollups: SlurmdbV0041GetDiagResponse200StatisticsRollups | Unset = UNSET
    rp_cs: list[SlurmdbV0041GetDiagResponse200StatisticsRPCsItem] | Unset = UNSET
    users: list[SlurmdbV0041GetDiagResponse200StatisticsUsersItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        time_start = self.time_start

        rollups: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rollups, Unset):
            rollups = self.rollups.to_dict()

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
        from ..models.slurmdb_v0041_get_diag_response_200_statistics_rollups import (
            SlurmdbV0041GetDiagResponse200StatisticsRollups,
        )
        from ..models.slurmdb_v0041_get_diag_response_200_statistics_rp_cs_item import (
            SlurmdbV0041GetDiagResponse200StatisticsRPCsItem,
        )
        from ..models.slurmdb_v0041_get_diag_response_200_statistics_users_item import (
            SlurmdbV0041GetDiagResponse200StatisticsUsersItem,
        )

        d = dict(src_dict)
        time_start = d.pop("time_start", UNSET)

        _rollups = d.pop("rollups", UNSET)
        rollups: SlurmdbV0041GetDiagResponse200StatisticsRollups | Unset
        if isinstance(_rollups, Unset):
            rollups = UNSET
        else:
            rollups = SlurmdbV0041GetDiagResponse200StatisticsRollups.from_dict(_rollups)

        _rp_cs = d.pop("RPCs", UNSET)
        rp_cs: list[SlurmdbV0041GetDiagResponse200StatisticsRPCsItem] | Unset = UNSET
        if _rp_cs is not UNSET:
            rp_cs = []
            for rp_cs_item_data in _rp_cs:
                rp_cs_item = SlurmdbV0041GetDiagResponse200StatisticsRPCsItem.from_dict(rp_cs_item_data)

                rp_cs.append(rp_cs_item)

        _users = d.pop("users", UNSET)
        users: list[SlurmdbV0041GetDiagResponse200StatisticsUsersItem] | Unset = UNSET
        if _users is not UNSET:
            users = []
            for users_item_data in _users:
                users_item = SlurmdbV0041GetDiagResponse200StatisticsUsersItem.from_dict(users_item_data)

                users.append(users_item)

        slurmdb_v0041_get_diag_response_200_statistics = cls(
            time_start=time_start,
            rollups=rollups,
            rp_cs=rp_cs,
            users=users,
        )

        slurmdb_v0041_get_diag_response_200_statistics.additional_properties = d
        return slurmdb_v0041_get_diag_response_200_statistics

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
