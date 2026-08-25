from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Dbv0038QosLimitsMaxJobsActiveJobsPer")


@_attrs_define
class Dbv0038QosLimitsMaxJobsActiveJobsPer:
    """Limits on active jobs per settings

    Attributes:
        account (int | Unset): Max jobs per account
        user (int | Unset): Max jobs per user
    """

    account: int | Unset = UNSET
    user: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account = self.account

        user = self.user

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account is not UNSET:
            field_dict["account"] = account
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account = d.pop("account", UNSET)

        user = d.pop("user", UNSET)

        dbv_0038_qos_limits_max_jobs_active_jobs_per = cls(
            account=account,
            user=user,
        )

        dbv_0038_qos_limits_max_jobs_active_jobs_per.additional_properties = d
        return dbv_0038_qos_limits_max_jobs_active_jobs_per

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
