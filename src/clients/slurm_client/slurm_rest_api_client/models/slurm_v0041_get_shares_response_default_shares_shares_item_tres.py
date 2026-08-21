from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.slurm_v0041_get_shares_response_default_shares_shares_item_tres_group_minutes_item import (
        SlurmV0041GetSharesResponseDefaultSharesSharesItemTresGroupMinutesItem,
    )
    from ..models.slurm_v0041_get_shares_response_default_shares_shares_item_tres_run_seconds_item import (
        SlurmV0041GetSharesResponseDefaultSharesSharesItemTresRunSecondsItem,
    )
    from ..models.slurm_v0041_get_shares_response_default_shares_shares_item_tres_usage_item import (
        SlurmV0041GetSharesResponseDefaultSharesSharesItemTresUsageItem,
    )


T = TypeVar("T", bound="SlurmV0041GetSharesResponseDefaultSharesSharesItemTres")


@_attrs_define
class SlurmV0041GetSharesResponseDefaultSharesSharesItemTres:
    """
    Attributes:
        run_seconds (list[SlurmV0041GetSharesResponseDefaultSharesSharesItemTresRunSecondsItem] | Unset): Currently
            running tres-secs = grp_used_tres_run_secs
        group_minutes (list[SlurmV0041GetSharesResponseDefaultSharesSharesItemTresGroupMinutesItem] | Unset): TRES-
            minute limit
        usage (list[SlurmV0041GetSharesResponseDefaultSharesSharesItemTresUsageItem] | Unset): Measure of each TRES
            usage
    """

    run_seconds: list[SlurmV0041GetSharesResponseDefaultSharesSharesItemTresRunSecondsItem] | Unset = UNSET
    group_minutes: list[SlurmV0041GetSharesResponseDefaultSharesSharesItemTresGroupMinutesItem] | Unset = UNSET
    usage: list[SlurmV0041GetSharesResponseDefaultSharesSharesItemTresUsageItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        run_seconds: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.run_seconds, Unset):
            run_seconds = []
            for run_seconds_item_data in self.run_seconds:
                run_seconds_item = run_seconds_item_data.to_dict()
                run_seconds.append(run_seconds_item)

        group_minutes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.group_minutes, Unset):
            group_minutes = []
            for group_minutes_item_data in self.group_minutes:
                group_minutes_item = group_minutes_item_data.to_dict()
                group_minutes.append(group_minutes_item)

        usage: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.usage, Unset):
            usage = []
            for usage_item_data in self.usage:
                usage_item = usage_item_data.to_dict()
                usage.append(usage_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if run_seconds is not UNSET:
            field_dict["run_seconds"] = run_seconds
        if group_minutes is not UNSET:
            field_dict["group_minutes"] = group_minutes
        if usage is not UNSET:
            field_dict["usage"] = usage

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.slurm_v0041_get_shares_response_default_shares_shares_item_tres_group_minutes_item import (
            SlurmV0041GetSharesResponseDefaultSharesSharesItemTresGroupMinutesItem,
        )
        from ..models.slurm_v0041_get_shares_response_default_shares_shares_item_tres_run_seconds_item import (
            SlurmV0041GetSharesResponseDefaultSharesSharesItemTresRunSecondsItem,
        )
        from ..models.slurm_v0041_get_shares_response_default_shares_shares_item_tres_usage_item import (
            SlurmV0041GetSharesResponseDefaultSharesSharesItemTresUsageItem,
        )

        d = dict(src_dict)
        _run_seconds = d.pop("run_seconds", UNSET)
        run_seconds: list[SlurmV0041GetSharesResponseDefaultSharesSharesItemTresRunSecondsItem] | Unset = UNSET
        if _run_seconds is not UNSET:
            run_seconds = []
            for run_seconds_item_data in _run_seconds:
                run_seconds_item = SlurmV0041GetSharesResponseDefaultSharesSharesItemTresRunSecondsItem.from_dict(
                    run_seconds_item_data
                )

                run_seconds.append(run_seconds_item)

        _group_minutes = d.pop("group_minutes", UNSET)
        group_minutes: list[SlurmV0041GetSharesResponseDefaultSharesSharesItemTresGroupMinutesItem] | Unset = UNSET
        if _group_minutes is not UNSET:
            group_minutes = []
            for group_minutes_item_data in _group_minutes:
                group_minutes_item = SlurmV0041GetSharesResponseDefaultSharesSharesItemTresGroupMinutesItem.from_dict(
                    group_minutes_item_data
                )

                group_minutes.append(group_minutes_item)

        _usage = d.pop("usage", UNSET)
        usage: list[SlurmV0041GetSharesResponseDefaultSharesSharesItemTresUsageItem] | Unset = UNSET
        if _usage is not UNSET:
            usage = []
            for usage_item_data in _usage:
                usage_item = SlurmV0041GetSharesResponseDefaultSharesSharesItemTresUsageItem.from_dict(usage_item_data)

                usage.append(usage_item)

        slurm_v0041_get_shares_response_default_shares_shares_item_tres = cls(
            run_seconds=run_seconds,
            group_minutes=group_minutes,
            usage=usage,
        )

        slurm_v0041_get_shares_response_default_shares_shares_item_tres.additional_properties = d
        return slurm_v0041_get_shares_response_default_shares_shares_item_tres

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
