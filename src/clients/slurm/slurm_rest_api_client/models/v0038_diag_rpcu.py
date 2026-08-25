from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="V0038DiagRpcu")


@_attrs_define
class V0038DiagRpcu:
    """
    Attributes:
        user (str | Unset): user
        user_id (int | Unset): user id
        count (int | Unset): rpc count
        average_time (int | Unset): average time
        total_time (int | Unset): total time
    """

    user: str | Unset = UNSET
    user_id: int | Unset = UNSET
    count: int | Unset = UNSET
    average_time: int | Unset = UNSET
    total_time: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user = self.user

        user_id = self.user_id

        count = self.count

        average_time = self.average_time

        total_time = self.total_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user is not UNSET:
            field_dict["user"] = user
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if count is not UNSET:
            field_dict["count"] = count
        if average_time is not UNSET:
            field_dict["average_time"] = average_time
        if total_time is not UNSET:
            field_dict["total_time"] = total_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user = d.pop("user", UNSET)

        user_id = d.pop("user_id", UNSET)

        count = d.pop("count", UNSET)

        average_time = d.pop("average_time", UNSET)

        total_time = d.pop("total_time", UNSET)

        v0038_diag_rpcu = cls(
            user=user,
            user_id=user_id,
            count=count,
            average_time=average_time,
            total_time=total_time,
        )

        v0038_diag_rpcu.additional_properties = d
        return v0038_diag_rpcu

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
