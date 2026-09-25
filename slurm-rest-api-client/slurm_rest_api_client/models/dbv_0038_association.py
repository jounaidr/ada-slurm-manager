from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dbv_0038_association_default import Dbv0038AssociationDefault
    from ..models.dbv_0038_association_max import Dbv0038AssociationMax
    from ..models.dbv_0038_association_min import Dbv0038AssociationMin
    from ..models.dbv_0038_association_usage import Dbv0038AssociationUsage


T = TypeVar("T", bound="Dbv0038Association")


@_attrs_define
class Dbv0038Association:
    """Association description

    Attributes:
        account (str | Unset): Assigned account
        cluster (str | Unset): Assigned cluster
        default (Dbv0038AssociationDefault | Unset): Default settings
        flags (list[str] | Unset): List of properties of association
        max_ (Dbv0038AssociationMax | Unset): Max settings
        min_ (Dbv0038AssociationMin | Unset): Min settings
        parent_account (str | Unset): Parent account name
        partition (str | Unset): Assigned partition
        priority (int | Unset): Assigned priority
        shares_raw (int | Unset): Raw fairshare shares
        usage (Dbv0038AssociationUsage | Unset): Association usage
        user (str | Unset): Assigned user
        qos (list[str] | Unset): Assigned QOS
    """

    account: str | Unset = UNSET
    cluster: str | Unset = UNSET
    default: Dbv0038AssociationDefault | Unset = UNSET
    flags: list[str] | Unset = UNSET
    max_: Dbv0038AssociationMax | Unset = UNSET
    min_: Dbv0038AssociationMin | Unset = UNSET
    parent_account: str | Unset = UNSET
    partition: str | Unset = UNSET
    priority: int | Unset = UNSET
    shares_raw: int | Unset = UNSET
    usage: Dbv0038AssociationUsage | Unset = UNSET
    user: str | Unset = UNSET
    qos: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account = self.account

        cluster = self.cluster

        default: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default, Unset):
            default = self.default.to_dict()

        flags: list[str] | Unset = UNSET
        if not isinstance(self.flags, Unset):
            flags = self.flags

        max_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.max_, Unset):
            max_ = self.max_.to_dict()

        min_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.min_, Unset):
            min_ = self.min_.to_dict()

        parent_account = self.parent_account

        partition = self.partition

        priority = self.priority

        shares_raw = self.shares_raw

        usage: dict[str, Any] | Unset = UNSET
        if not isinstance(self.usage, Unset):
            usage = self.usage.to_dict()

        user = self.user

        qos: list[str] | Unset = UNSET
        if not isinstance(self.qos, Unset):
            qos = self.qos

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account is not UNSET:
            field_dict["account"] = account
        if cluster is not UNSET:
            field_dict["cluster"] = cluster
        if default is not UNSET:
            field_dict["default"] = default
        if flags is not UNSET:
            field_dict["flags"] = flags
        if max_ is not UNSET:
            field_dict["max"] = max_
        if min_ is not UNSET:
            field_dict["min"] = min_
        if parent_account is not UNSET:
            field_dict["parent_account"] = parent_account
        if partition is not UNSET:
            field_dict["partition"] = partition
        if priority is not UNSET:
            field_dict["priority"] = priority
        if shares_raw is not UNSET:
            field_dict["shares_raw"] = shares_raw
        if usage is not UNSET:
            field_dict["usage"] = usage
        if user is not UNSET:
            field_dict["user"] = user
        if qos is not UNSET:
            field_dict["QOS"] = qos

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dbv_0038_association_default import Dbv0038AssociationDefault
        from ..models.dbv_0038_association_max import Dbv0038AssociationMax
        from ..models.dbv_0038_association_min import Dbv0038AssociationMin
        from ..models.dbv_0038_association_usage import Dbv0038AssociationUsage

        d = dict(src_dict)
        account = d.pop("account", UNSET)

        cluster = d.pop("cluster", UNSET)

        _default = d.pop("default", UNSET)
        default: Dbv0038AssociationDefault | Unset
        if isinstance(_default, Unset):
            default = UNSET
        else:
            default = Dbv0038AssociationDefault.from_dict(_default)

        flags = cast(list[str], d.pop("flags", UNSET))

        _max_ = d.pop("max", UNSET)
        max_: Dbv0038AssociationMax | Unset
        if isinstance(_max_, Unset):
            max_ = UNSET
        else:
            max_ = Dbv0038AssociationMax.from_dict(_max_)

        _min_ = d.pop("min", UNSET)
        min_: Dbv0038AssociationMin | Unset
        if isinstance(_min_, Unset):
            min_ = UNSET
        else:
            min_ = Dbv0038AssociationMin.from_dict(_min_)

        parent_account = d.pop("parent_account", UNSET)

        partition = d.pop("partition", UNSET)

        priority = d.pop("priority", UNSET)

        shares_raw = d.pop("shares_raw", UNSET)

        _usage = d.pop("usage", UNSET)
        usage: Dbv0038AssociationUsage | Unset
        if isinstance(_usage, Unset):
            usage = UNSET
        else:
            usage = Dbv0038AssociationUsage.from_dict(_usage)

        user = d.pop("user", UNSET)

        qos = cast(list[str], d.pop("QOS", UNSET))

        dbv_0038_association = cls(
            account=account,
            cluster=cluster,
            default=default,
            flags=flags,
            max_=max_,
            min_=min_,
            parent_account=parent_account,
            partition=partition,
            priority=priority,
            shares_raw=shares_raw,
            usage=usage,
            user=user,
            qos=qos,
        )

        dbv_0038_association.additional_properties = d
        return dbv_0038_association

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
