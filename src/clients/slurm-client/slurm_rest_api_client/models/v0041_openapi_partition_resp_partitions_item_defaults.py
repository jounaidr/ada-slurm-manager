from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v0041_openapi_partition_resp_partitions_item_defaults_partition_memory_per_cpu import (
        V0041OpenapiPartitionRespPartitionsItemDefaultsPartitionMemoryPerCpu,
    )
    from ..models.v0041_openapi_partition_resp_partitions_item_defaults_partition_memory_per_node import (
        V0041OpenapiPartitionRespPartitionsItemDefaultsPartitionMemoryPerNode,
    )
    from ..models.v0041_openapi_partition_resp_partitions_item_defaults_time import (
        V0041OpenapiPartitionRespPartitionsItemDefaultsTime,
    )


T = TypeVar("T", bound="V0041OpenapiPartitionRespPartitionsItemDefaults")


@_attrs_define
class V0041OpenapiPartitionRespPartitionsItemDefaults:
    """
    Attributes:
        memory_per_cpu (int | Unset): DefMemPerCPU or DefMemPerNode
        partition_memory_per_cpu (V0041OpenapiPartitionRespPartitionsItemDefaultsPartitionMemoryPerCpu | Unset):
            DefMemPerCPU
        partition_memory_per_node (V0041OpenapiPartitionRespPartitionsItemDefaultsPartitionMemoryPerNode | Unset):
            DefMemPerNode
        time (V0041OpenapiPartitionRespPartitionsItemDefaultsTime | Unset): DefaultTime in minutes
        job (str | Unset): JobDefaults
    """

    memory_per_cpu: int | Unset = UNSET
    partition_memory_per_cpu: V0041OpenapiPartitionRespPartitionsItemDefaultsPartitionMemoryPerCpu | Unset = UNSET
    partition_memory_per_node: V0041OpenapiPartitionRespPartitionsItemDefaultsPartitionMemoryPerNode | Unset = UNSET
    time: V0041OpenapiPartitionRespPartitionsItemDefaultsTime | Unset = UNSET
    job: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        memory_per_cpu = self.memory_per_cpu

        partition_memory_per_cpu: dict[str, Any] | Unset = UNSET
        if not isinstance(self.partition_memory_per_cpu, Unset):
            partition_memory_per_cpu = self.partition_memory_per_cpu.to_dict()

        partition_memory_per_node: dict[str, Any] | Unset = UNSET
        if not isinstance(self.partition_memory_per_node, Unset):
            partition_memory_per_node = self.partition_memory_per_node.to_dict()

        time: dict[str, Any] | Unset = UNSET
        if not isinstance(self.time, Unset):
            time = self.time.to_dict()

        job = self.job

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if memory_per_cpu is not UNSET:
            field_dict["memory_per_cpu"] = memory_per_cpu
        if partition_memory_per_cpu is not UNSET:
            field_dict["partition_memory_per_cpu"] = partition_memory_per_cpu
        if partition_memory_per_node is not UNSET:
            field_dict["partition_memory_per_node"] = partition_memory_per_node
        if time is not UNSET:
            field_dict["time"] = time
        if job is not UNSET:
            field_dict["job"] = job

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v0041_openapi_partition_resp_partitions_item_defaults_partition_memory_per_cpu import (
            V0041OpenapiPartitionRespPartitionsItemDefaultsPartitionMemoryPerCpu,
        )
        from ..models.v0041_openapi_partition_resp_partitions_item_defaults_partition_memory_per_node import (
            V0041OpenapiPartitionRespPartitionsItemDefaultsPartitionMemoryPerNode,
        )
        from ..models.v0041_openapi_partition_resp_partitions_item_defaults_time import (
            V0041OpenapiPartitionRespPartitionsItemDefaultsTime,
        )

        d = dict(src_dict)
        memory_per_cpu = d.pop("memory_per_cpu", UNSET)

        _partition_memory_per_cpu = d.pop("partition_memory_per_cpu", UNSET)
        partition_memory_per_cpu: V0041OpenapiPartitionRespPartitionsItemDefaultsPartitionMemoryPerCpu | Unset
        if isinstance(_partition_memory_per_cpu, Unset):
            partition_memory_per_cpu = UNSET
        else:
            partition_memory_per_cpu = V0041OpenapiPartitionRespPartitionsItemDefaultsPartitionMemoryPerCpu.from_dict(
                _partition_memory_per_cpu
            )

        _partition_memory_per_node = d.pop("partition_memory_per_node", UNSET)
        partition_memory_per_node: V0041OpenapiPartitionRespPartitionsItemDefaultsPartitionMemoryPerNode | Unset
        if isinstance(_partition_memory_per_node, Unset):
            partition_memory_per_node = UNSET
        else:
            partition_memory_per_node = V0041OpenapiPartitionRespPartitionsItemDefaultsPartitionMemoryPerNode.from_dict(
                _partition_memory_per_node
            )

        _time = d.pop("time", UNSET)
        time: V0041OpenapiPartitionRespPartitionsItemDefaultsTime | Unset
        if isinstance(_time, Unset):
            time = UNSET
        else:
            time = V0041OpenapiPartitionRespPartitionsItemDefaultsTime.from_dict(_time)

        job = d.pop("job", UNSET)

        v0041_openapi_partition_resp_partitions_item_defaults = cls(
            memory_per_cpu=memory_per_cpu,
            partition_memory_per_cpu=partition_memory_per_cpu,
            partition_memory_per_node=partition_memory_per_node,
            time=time,
            job=job,
        )

        v0041_openapi_partition_resp_partitions_item_defaults.additional_properties = d
        return v0041_openapi_partition_resp_partitions_item_defaults

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
