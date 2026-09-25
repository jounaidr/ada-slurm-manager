from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Dbv0037AssociationShortInfo")


@_attrs_define
class Dbv0037AssociationShortInfo:
    """
    Attributes:
        account (str | Unset): Account name
        cluster (str | Unset): Cluster name
        partition (str | Unset): Partition name (optional)
        user (str | Unset): User name
    """

    account: str | Unset = UNSET
    cluster: str | Unset = UNSET
    partition: str | Unset = UNSET
    user: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account = self.account

        cluster = self.cluster

        partition = self.partition

        user = self.user

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account is not UNSET:
            field_dict["account"] = account
        if cluster is not UNSET:
            field_dict["cluster"] = cluster
        if partition is not UNSET:
            field_dict["partition"] = partition
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account = d.pop("account", UNSET)

        cluster = d.pop("cluster", UNSET)

        partition = d.pop("partition", UNSET)

        user = d.pop("user", UNSET)

        dbv_0037_association_short_info = cls(
            account=account,
            cluster=cluster,
            partition=partition,
            user=user,
        )

        dbv_0037_association_short_info.additional_properties = d
        return dbv_0037_association_short_info

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
