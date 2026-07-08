from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.slurmdb_v0041_get_diag_response_default_statistics_users_item_time import (
        SlurmdbV0041GetDiagResponseDefaultStatisticsUsersItemTime,
    )


T = TypeVar("T", bound="SlurmdbV0041GetDiagResponseDefaultStatisticsUsersItem")


@_attrs_define
class SlurmdbV0041GetDiagResponseDefaultStatisticsUsersItem:
    """
    Attributes:
        user (str | Unset): User ID
        count (int | Unset): Number of RPCs processed
        time (SlurmdbV0041GetDiagResponseDefaultStatisticsUsersItemTime | Unset):
    """

    user: str | Unset = UNSET
    count: int | Unset = UNSET
    time: SlurmdbV0041GetDiagResponseDefaultStatisticsUsersItemTime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user = self.user

        count = self.count

        time: dict[str, Any] | Unset = UNSET
        if not isinstance(self.time, Unset):
            time = self.time.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user is not UNSET:
            field_dict["user"] = user
        if count is not UNSET:
            field_dict["count"] = count
        if time is not UNSET:
            field_dict["time"] = time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.slurmdb_v0041_get_diag_response_default_statistics_users_item_time import (
            SlurmdbV0041GetDiagResponseDefaultStatisticsUsersItemTime,
        )

        d = dict(src_dict)
        user = d.pop("user", UNSET)

        count = d.pop("count", UNSET)

        _time = d.pop("time", UNSET)
        time: SlurmdbV0041GetDiagResponseDefaultStatisticsUsersItemTime | Unset
        if isinstance(_time, Unset):
            time = UNSET
        else:
            time = SlurmdbV0041GetDiagResponseDefaultStatisticsUsersItemTime.from_dict(_time)

        slurmdb_v0041_get_diag_response_default_statistics_users_item = cls(
            user=user,
            count=count,
            time=time,
        )

        slurmdb_v0041_get_diag_response_default_statistics_users_item.additional_properties = d
        return slurmdb_v0041_get_diag_response_default_statistics_users_item

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
