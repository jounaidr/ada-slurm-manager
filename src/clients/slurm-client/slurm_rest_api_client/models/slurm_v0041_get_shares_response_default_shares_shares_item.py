from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.slurm_v0041_get_shares_response_default_shares_shares_item_type_item import (
    SlurmV0041GetSharesResponseDefaultSharesSharesItemTypeItem,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.slurm_v0041_get_shares_response_default_shares_shares_item_fairshare import (
        SlurmV0041GetSharesResponseDefaultSharesSharesItemFairshare,
    )
    from ..models.slurm_v0041_get_shares_response_default_shares_shares_item_shares import (
        SlurmV0041GetSharesResponseDefaultSharesSharesItemShares,
    )
    from ..models.slurm_v0041_get_shares_response_default_shares_shares_item_shares_normalized import (
        SlurmV0041GetSharesResponseDefaultSharesSharesItemSharesNormalized,
    )
    from ..models.slurm_v0041_get_shares_response_default_shares_shares_item_tres import (
        SlurmV0041GetSharesResponseDefaultSharesSharesItemTres,
    )
    from ..models.slurm_v0041_get_shares_response_default_shares_shares_item_usage_normalized import (
        SlurmV0041GetSharesResponseDefaultSharesSharesItemUsageNormalized,
    )


T = TypeVar("T", bound="SlurmV0041GetSharesResponseDefaultSharesSharesItem")


@_attrs_define
class SlurmV0041GetSharesResponseDefaultSharesSharesItem:
    """
    Attributes:
        id (int | Unset): Association ID
        cluster (str | Unset): Cluster name
        name (str | Unset): Share name
        parent (str | Unset): Parent name
        partition (str | Unset): Partition name
        shares_normalized (SlurmV0041GetSharesResponseDefaultSharesSharesItemSharesNormalized | Unset): Normalized
            shares
        shares (SlurmV0041GetSharesResponseDefaultSharesSharesItemShares | Unset): Number of shares allocated
        tres (SlurmV0041GetSharesResponseDefaultSharesSharesItemTres | Unset):
        effective_usage (float | Unset): Effective, normalized usage
        usage_normalized (SlurmV0041GetSharesResponseDefaultSharesSharesItemUsageNormalized | Unset): Normalized usage
        usage (int | Unset): Measure of tresbillableunits usage
        fairshare (SlurmV0041GetSharesResponseDefaultSharesSharesItemFairshare | Unset):
        type_ (list[SlurmV0041GetSharesResponseDefaultSharesSharesItemTypeItem] | Unset): User or account association
    """

    id: int | Unset = UNSET
    cluster: str | Unset = UNSET
    name: str | Unset = UNSET
    parent: str | Unset = UNSET
    partition: str | Unset = UNSET
    shares_normalized: SlurmV0041GetSharesResponseDefaultSharesSharesItemSharesNormalized | Unset = UNSET
    shares: SlurmV0041GetSharesResponseDefaultSharesSharesItemShares | Unset = UNSET
    tres: SlurmV0041GetSharesResponseDefaultSharesSharesItemTres | Unset = UNSET
    effective_usage: float | Unset = UNSET
    usage_normalized: SlurmV0041GetSharesResponseDefaultSharesSharesItemUsageNormalized | Unset = UNSET
    usage: int | Unset = UNSET
    fairshare: SlurmV0041GetSharesResponseDefaultSharesSharesItemFairshare | Unset = UNSET
    type_: list[SlurmV0041GetSharesResponseDefaultSharesSharesItemTypeItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        cluster = self.cluster

        name = self.name

        parent = self.parent

        partition = self.partition

        shares_normalized: dict[str, Any] | Unset = UNSET
        if not isinstance(self.shares_normalized, Unset):
            shares_normalized = self.shares_normalized.to_dict()

        shares: dict[str, Any] | Unset = UNSET
        if not isinstance(self.shares, Unset):
            shares = self.shares.to_dict()

        tres: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tres, Unset):
            tres = self.tres.to_dict()

        effective_usage = self.effective_usage

        usage_normalized: dict[str, Any] | Unset = UNSET
        if not isinstance(self.usage_normalized, Unset):
            usage_normalized = self.usage_normalized.to_dict()

        usage = self.usage

        fairshare: dict[str, Any] | Unset = UNSET
        if not isinstance(self.fairshare, Unset):
            fairshare = self.fairshare.to_dict()

        type_: list[str] | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = []
            for type_item_data in self.type_:
                type_item = type_item_data.value
                type_.append(type_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if cluster is not UNSET:
            field_dict["cluster"] = cluster
        if name is not UNSET:
            field_dict["name"] = name
        if parent is not UNSET:
            field_dict["parent"] = parent
        if partition is not UNSET:
            field_dict["partition"] = partition
        if shares_normalized is not UNSET:
            field_dict["shares_normalized"] = shares_normalized
        if shares is not UNSET:
            field_dict["shares"] = shares
        if tres is not UNSET:
            field_dict["tres"] = tres
        if effective_usage is not UNSET:
            field_dict["effective_usage"] = effective_usage
        if usage_normalized is not UNSET:
            field_dict["usage_normalized"] = usage_normalized
        if usage is not UNSET:
            field_dict["usage"] = usage
        if fairshare is not UNSET:
            field_dict["fairshare"] = fairshare
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.slurm_v0041_get_shares_response_default_shares_shares_item_fairshare import (
            SlurmV0041GetSharesResponseDefaultSharesSharesItemFairshare,
        )
        from ..models.slurm_v0041_get_shares_response_default_shares_shares_item_shares import (
            SlurmV0041GetSharesResponseDefaultSharesSharesItemShares,
        )
        from ..models.slurm_v0041_get_shares_response_default_shares_shares_item_shares_normalized import (
            SlurmV0041GetSharesResponseDefaultSharesSharesItemSharesNormalized,
        )
        from ..models.slurm_v0041_get_shares_response_default_shares_shares_item_tres import (
            SlurmV0041GetSharesResponseDefaultSharesSharesItemTres,
        )
        from ..models.slurm_v0041_get_shares_response_default_shares_shares_item_usage_normalized import (
            SlurmV0041GetSharesResponseDefaultSharesSharesItemUsageNormalized,
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        cluster = d.pop("cluster", UNSET)

        name = d.pop("name", UNSET)

        parent = d.pop("parent", UNSET)

        partition = d.pop("partition", UNSET)

        _shares_normalized = d.pop("shares_normalized", UNSET)
        shares_normalized: SlurmV0041GetSharesResponseDefaultSharesSharesItemSharesNormalized | Unset
        if isinstance(_shares_normalized, Unset):
            shares_normalized = UNSET
        else:
            shares_normalized = SlurmV0041GetSharesResponseDefaultSharesSharesItemSharesNormalized.from_dict(
                _shares_normalized
            )

        _shares = d.pop("shares", UNSET)
        shares: SlurmV0041GetSharesResponseDefaultSharesSharesItemShares | Unset
        if isinstance(_shares, Unset):
            shares = UNSET
        else:
            shares = SlurmV0041GetSharesResponseDefaultSharesSharesItemShares.from_dict(_shares)

        _tres = d.pop("tres", UNSET)
        tres: SlurmV0041GetSharesResponseDefaultSharesSharesItemTres | Unset
        if isinstance(_tres, Unset):
            tres = UNSET
        else:
            tres = SlurmV0041GetSharesResponseDefaultSharesSharesItemTres.from_dict(_tres)

        effective_usage = d.pop("effective_usage", UNSET)

        _usage_normalized = d.pop("usage_normalized", UNSET)
        usage_normalized: SlurmV0041GetSharesResponseDefaultSharesSharesItemUsageNormalized | Unset
        if isinstance(_usage_normalized, Unset):
            usage_normalized = UNSET
        else:
            usage_normalized = SlurmV0041GetSharesResponseDefaultSharesSharesItemUsageNormalized.from_dict(
                _usage_normalized
            )

        usage = d.pop("usage", UNSET)

        _fairshare = d.pop("fairshare", UNSET)
        fairshare: SlurmV0041GetSharesResponseDefaultSharesSharesItemFairshare | Unset
        if isinstance(_fairshare, Unset):
            fairshare = UNSET
        else:
            fairshare = SlurmV0041GetSharesResponseDefaultSharesSharesItemFairshare.from_dict(_fairshare)

        _type_ = d.pop("type", UNSET)
        type_: list[SlurmV0041GetSharesResponseDefaultSharesSharesItemTypeItem] | Unset = UNSET
        if _type_ is not UNSET:
            type_ = []
            for type_item_data in _type_:
                type_item = SlurmV0041GetSharesResponseDefaultSharesSharesItemTypeItem(type_item_data)

                type_.append(type_item)

        slurm_v0041_get_shares_response_default_shares_shares_item = cls(
            id=id,
            cluster=cluster,
            name=name,
            parent=parent,
            partition=partition,
            shares_normalized=shares_normalized,
            shares=shares,
            tres=tres,
            effective_usage=effective_usage,
            usage_normalized=usage_normalized,
            usage=usage,
            fairshare=fairshare,
            type_=type_,
        )

        slurm_v0041_get_shares_response_default_shares_shares_item.additional_properties = d
        return slurm_v0041_get_shares_response_default_shares_shares_item

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
