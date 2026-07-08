from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.v0041_openapi_partition_resp_partitions_item_maximums_oversubscribe_flags_item import (
    V0041OpenapiPartitionRespPartitionsItemMaximumsOversubscribeFlagsItem,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="V0041OpenapiPartitionRespPartitionsItemMaximumsOversubscribe")


@_attrs_define
class V0041OpenapiPartitionRespPartitionsItemMaximumsOversubscribe:
    """
    Attributes:
        jobs (int | Unset): Maximum number of jobs allowed to oversubscribe resources
        flags (list[V0041OpenapiPartitionRespPartitionsItemMaximumsOversubscribeFlagsItem] | Unset): Flags applicable to
            the OverSubscribe setting
    """

    jobs: int | Unset = UNSET
    flags: list[V0041OpenapiPartitionRespPartitionsItemMaximumsOversubscribeFlagsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        jobs = self.jobs

        flags: list[str] | Unset = UNSET
        if not isinstance(self.flags, Unset):
            flags = []
            for flags_item_data in self.flags:
                flags_item = flags_item_data.value
                flags.append(flags_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if jobs is not UNSET:
            field_dict["jobs"] = jobs
        if flags is not UNSET:
            field_dict["flags"] = flags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        jobs = d.pop("jobs", UNSET)

        _flags = d.pop("flags", UNSET)
        flags: list[V0041OpenapiPartitionRespPartitionsItemMaximumsOversubscribeFlagsItem] | Unset = UNSET
        if _flags is not UNSET:
            flags = []
            for flags_item_data in _flags:
                flags_item = V0041OpenapiPartitionRespPartitionsItemMaximumsOversubscribeFlagsItem(flags_item_data)

                flags.append(flags_item)

        v0041_openapi_partition_resp_partitions_item_maximums_oversubscribe = cls(
            jobs=jobs,
            flags=flags,
        )

        v0041_openapi_partition_resp_partitions_item_maximums_oversubscribe.additional_properties = d
        return v0041_openapi_partition_resp_partitions_item_maximums_oversubscribe

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
