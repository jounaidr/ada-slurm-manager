from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v0041_openapi_partition_resp_partitions_item_maximums_cpus_per_node import (
        V0041OpenapiPartitionRespPartitionsItemMaximumsCpusPerNode,
    )
    from ..models.v0041_openapi_partition_resp_partitions_item_maximums_cpus_per_socket import (
        V0041OpenapiPartitionRespPartitionsItemMaximumsCpusPerSocket,
    )
    from ..models.v0041_openapi_partition_resp_partitions_item_maximums_nodes import (
        V0041OpenapiPartitionRespPartitionsItemMaximumsNodes,
    )
    from ..models.v0041_openapi_partition_resp_partitions_item_maximums_over_time_limit import (
        V0041OpenapiPartitionRespPartitionsItemMaximumsOverTimeLimit,
    )
    from ..models.v0041_openapi_partition_resp_partitions_item_maximums_oversubscribe import (
        V0041OpenapiPartitionRespPartitionsItemMaximumsOversubscribe,
    )
    from ..models.v0041_openapi_partition_resp_partitions_item_maximums_partition_memory_per_cpu import (
        V0041OpenapiPartitionRespPartitionsItemMaximumsPartitionMemoryPerCpu,
    )
    from ..models.v0041_openapi_partition_resp_partitions_item_maximums_partition_memory_per_node import (
        V0041OpenapiPartitionRespPartitionsItemMaximumsPartitionMemoryPerNode,
    )
    from ..models.v0041_openapi_partition_resp_partitions_item_maximums_time import (
        V0041OpenapiPartitionRespPartitionsItemMaximumsTime,
    )


T = TypeVar("T", bound="V0041OpenapiPartitionRespPartitionsItemMaximums")


@_attrs_define
class V0041OpenapiPartitionRespPartitionsItemMaximums:
    """
    Attributes:
        cpus_per_node (V0041OpenapiPartitionRespPartitionsItemMaximumsCpusPerNode | Unset): MaxCPUsPerNode
        cpus_per_socket (V0041OpenapiPartitionRespPartitionsItemMaximumsCpusPerSocket | Unset): MaxCPUsPerSocket
        memory_per_cpu (int | Unset): MaxMemPerCPU or MaxMemPerNode
        partition_memory_per_cpu (V0041OpenapiPartitionRespPartitionsItemMaximumsPartitionMemoryPerCpu | Unset):
            MaxMemPerCPU
        partition_memory_per_node (V0041OpenapiPartitionRespPartitionsItemMaximumsPartitionMemoryPerNode | Unset):
            MaxMemPerNode
        nodes (V0041OpenapiPartitionRespPartitionsItemMaximumsNodes | Unset): MaxNodes
        shares (int | Unset): OverSubscribe
        oversubscribe (V0041OpenapiPartitionRespPartitionsItemMaximumsOversubscribe | Unset):
        time (V0041OpenapiPartitionRespPartitionsItemMaximumsTime | Unset): MaxTime
        over_time_limit (V0041OpenapiPartitionRespPartitionsItemMaximumsOverTimeLimit | Unset): OverTimeLimit
    """

    cpus_per_node: V0041OpenapiPartitionRespPartitionsItemMaximumsCpusPerNode | Unset = UNSET
    cpus_per_socket: V0041OpenapiPartitionRespPartitionsItemMaximumsCpusPerSocket | Unset = UNSET
    memory_per_cpu: int | Unset = UNSET
    partition_memory_per_cpu: V0041OpenapiPartitionRespPartitionsItemMaximumsPartitionMemoryPerCpu | Unset = UNSET
    partition_memory_per_node: V0041OpenapiPartitionRespPartitionsItemMaximumsPartitionMemoryPerNode | Unset = UNSET
    nodes: V0041OpenapiPartitionRespPartitionsItemMaximumsNodes | Unset = UNSET
    shares: int | Unset = UNSET
    oversubscribe: V0041OpenapiPartitionRespPartitionsItemMaximumsOversubscribe | Unset = UNSET
    time: V0041OpenapiPartitionRespPartitionsItemMaximumsTime | Unset = UNSET
    over_time_limit: V0041OpenapiPartitionRespPartitionsItemMaximumsOverTimeLimit | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cpus_per_node: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cpus_per_node, Unset):
            cpus_per_node = self.cpus_per_node.to_dict()

        cpus_per_socket: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cpus_per_socket, Unset):
            cpus_per_socket = self.cpus_per_socket.to_dict()

        memory_per_cpu = self.memory_per_cpu

        partition_memory_per_cpu: dict[str, Any] | Unset = UNSET
        if not isinstance(self.partition_memory_per_cpu, Unset):
            partition_memory_per_cpu = self.partition_memory_per_cpu.to_dict()

        partition_memory_per_node: dict[str, Any] | Unset = UNSET
        if not isinstance(self.partition_memory_per_node, Unset):
            partition_memory_per_node = self.partition_memory_per_node.to_dict()

        nodes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.nodes, Unset):
            nodes = self.nodes.to_dict()

        shares = self.shares

        oversubscribe: dict[str, Any] | Unset = UNSET
        if not isinstance(self.oversubscribe, Unset):
            oversubscribe = self.oversubscribe.to_dict()

        time: dict[str, Any] | Unset = UNSET
        if not isinstance(self.time, Unset):
            time = self.time.to_dict()

        over_time_limit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.over_time_limit, Unset):
            over_time_limit = self.over_time_limit.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cpus_per_node is not UNSET:
            field_dict["cpus_per_node"] = cpus_per_node
        if cpus_per_socket is not UNSET:
            field_dict["cpus_per_socket"] = cpus_per_socket
        if memory_per_cpu is not UNSET:
            field_dict["memory_per_cpu"] = memory_per_cpu
        if partition_memory_per_cpu is not UNSET:
            field_dict["partition_memory_per_cpu"] = partition_memory_per_cpu
        if partition_memory_per_node is not UNSET:
            field_dict["partition_memory_per_node"] = partition_memory_per_node
        if nodes is not UNSET:
            field_dict["nodes"] = nodes
        if shares is not UNSET:
            field_dict["shares"] = shares
        if oversubscribe is not UNSET:
            field_dict["oversubscribe"] = oversubscribe
        if time is not UNSET:
            field_dict["time"] = time
        if over_time_limit is not UNSET:
            field_dict["over_time_limit"] = over_time_limit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v0041_openapi_partition_resp_partitions_item_maximums_cpus_per_node import (
            V0041OpenapiPartitionRespPartitionsItemMaximumsCpusPerNode,
        )
        from ..models.v0041_openapi_partition_resp_partitions_item_maximums_cpus_per_socket import (
            V0041OpenapiPartitionRespPartitionsItemMaximumsCpusPerSocket,
        )
        from ..models.v0041_openapi_partition_resp_partitions_item_maximums_nodes import (
            V0041OpenapiPartitionRespPartitionsItemMaximumsNodes,
        )
        from ..models.v0041_openapi_partition_resp_partitions_item_maximums_over_time_limit import (
            V0041OpenapiPartitionRespPartitionsItemMaximumsOverTimeLimit,
        )
        from ..models.v0041_openapi_partition_resp_partitions_item_maximums_oversubscribe import (
            V0041OpenapiPartitionRespPartitionsItemMaximumsOversubscribe,
        )
        from ..models.v0041_openapi_partition_resp_partitions_item_maximums_partition_memory_per_cpu import (
            V0041OpenapiPartitionRespPartitionsItemMaximumsPartitionMemoryPerCpu,
        )
        from ..models.v0041_openapi_partition_resp_partitions_item_maximums_partition_memory_per_node import (
            V0041OpenapiPartitionRespPartitionsItemMaximumsPartitionMemoryPerNode,
        )
        from ..models.v0041_openapi_partition_resp_partitions_item_maximums_time import (
            V0041OpenapiPartitionRespPartitionsItemMaximumsTime,
        )

        d = dict(src_dict)
        _cpus_per_node = d.pop("cpus_per_node", UNSET)
        cpus_per_node: V0041OpenapiPartitionRespPartitionsItemMaximumsCpusPerNode | Unset
        if isinstance(_cpus_per_node, Unset):
            cpus_per_node = UNSET
        else:
            cpus_per_node = V0041OpenapiPartitionRespPartitionsItemMaximumsCpusPerNode.from_dict(_cpus_per_node)

        _cpus_per_socket = d.pop("cpus_per_socket", UNSET)
        cpus_per_socket: V0041OpenapiPartitionRespPartitionsItemMaximumsCpusPerSocket | Unset
        if isinstance(_cpus_per_socket, Unset):
            cpus_per_socket = UNSET
        else:
            cpus_per_socket = V0041OpenapiPartitionRespPartitionsItemMaximumsCpusPerSocket.from_dict(_cpus_per_socket)

        memory_per_cpu = d.pop("memory_per_cpu", UNSET)

        _partition_memory_per_cpu = d.pop("partition_memory_per_cpu", UNSET)
        partition_memory_per_cpu: V0041OpenapiPartitionRespPartitionsItemMaximumsPartitionMemoryPerCpu | Unset
        if isinstance(_partition_memory_per_cpu, Unset):
            partition_memory_per_cpu = UNSET
        else:
            partition_memory_per_cpu = V0041OpenapiPartitionRespPartitionsItemMaximumsPartitionMemoryPerCpu.from_dict(
                _partition_memory_per_cpu
            )

        _partition_memory_per_node = d.pop("partition_memory_per_node", UNSET)
        partition_memory_per_node: V0041OpenapiPartitionRespPartitionsItemMaximumsPartitionMemoryPerNode | Unset
        if isinstance(_partition_memory_per_node, Unset):
            partition_memory_per_node = UNSET
        else:
            partition_memory_per_node = V0041OpenapiPartitionRespPartitionsItemMaximumsPartitionMemoryPerNode.from_dict(
                _partition_memory_per_node
            )

        _nodes = d.pop("nodes", UNSET)
        nodes: V0041OpenapiPartitionRespPartitionsItemMaximumsNodes | Unset
        if isinstance(_nodes, Unset):
            nodes = UNSET
        else:
            nodes = V0041OpenapiPartitionRespPartitionsItemMaximumsNodes.from_dict(_nodes)

        shares = d.pop("shares", UNSET)

        _oversubscribe = d.pop("oversubscribe", UNSET)
        oversubscribe: V0041OpenapiPartitionRespPartitionsItemMaximumsOversubscribe | Unset
        if isinstance(_oversubscribe, Unset):
            oversubscribe = UNSET
        else:
            oversubscribe = V0041OpenapiPartitionRespPartitionsItemMaximumsOversubscribe.from_dict(_oversubscribe)

        _time = d.pop("time", UNSET)
        time: V0041OpenapiPartitionRespPartitionsItemMaximumsTime | Unset
        if isinstance(_time, Unset):
            time = UNSET
        else:
            time = V0041OpenapiPartitionRespPartitionsItemMaximumsTime.from_dict(_time)

        _over_time_limit = d.pop("over_time_limit", UNSET)
        over_time_limit: V0041OpenapiPartitionRespPartitionsItemMaximumsOverTimeLimit | Unset
        if isinstance(_over_time_limit, Unset):
            over_time_limit = UNSET
        else:
            over_time_limit = V0041OpenapiPartitionRespPartitionsItemMaximumsOverTimeLimit.from_dict(_over_time_limit)

        v0041_openapi_partition_resp_partitions_item_maximums = cls(
            cpus_per_node=cpus_per_node,
            cpus_per_socket=cpus_per_socket,
            memory_per_cpu=memory_per_cpu,
            partition_memory_per_cpu=partition_memory_per_cpu,
            partition_memory_per_node=partition_memory_per_node,
            nodes=nodes,
            shares=shares,
            oversubscribe=oversubscribe,
            time=time,
            over_time_limit=over_time_limit,
        )

        v0041_openapi_partition_resp_partitions_item_maximums.additional_properties = d
        return v0041_openapi_partition_resp_partitions_item_maximums

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
