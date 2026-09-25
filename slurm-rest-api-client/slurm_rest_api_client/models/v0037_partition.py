from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="V0037Partition")


@_attrs_define
class V0037Partition:
    """
    Attributes:
        flags (list[str] | Unset): partition options
        preemption_mode (list[str] | Unset): preemption type
        allowed_allocation_nodes (str | Unset): list names of allowed allocating nodes
        allowed_accounts (str | Unset): comma delimited list of accounts
        allowed_groups (str | Unset): comma delimited list of groups
        allowed_qos (str | Unset): comma delimited list of qos
        alternative (str | Unset): name of alternate partition
        billing_weights (str | Unset): TRES billing weights
        default_memory_per_cpu (int | Unset): default MB memory per allocated CPU
        default_time_limit (int | Unset): default time limit (minutes)
        denied_accounts (str | Unset): comma delimited list of denied accounts
        denied_qos (str | Unset): comma delimited list of denied qos
        preemption_grace_time (int | Unset): preemption grace time (seconds)
        maximum_cpus_per_node (int | Unset): maximum allocated CPUs per node
        maximum_memory_per_node (int | Unset): maximum memory per allocated CPU (MiB)
        maximum_nodes_per_job (int | Unset): Max nodes per job
        max_time_limit (int | Unset): Max time limit per job
        min_nodes_per_job (int | Unset): Min number of nodes per job
        name (str | Unset): Partition name
        nodes (str | Unset): list names of nodes in partition
        over_time_limit (int | Unset): job's time limit can be exceeded by this number of minutes before cancellation
        priority_job_factor (int | Unset): job priority weight factor
        priority_tier (int | Unset): tier for scheduling and preemption
        qos (str | Unset): partition QOS name
        state (str | Unset): Partition state
        total_cpus (int | Unset): Total cpus in partition
        total_nodes (int | Unset): Total number of nodes in partition
        tres (str | Unset): configured TRES in partition
    """

    flags: list[str] | Unset = UNSET
    preemption_mode: list[str] | Unset = UNSET
    allowed_allocation_nodes: str | Unset = UNSET
    allowed_accounts: str | Unset = UNSET
    allowed_groups: str | Unset = UNSET
    allowed_qos: str | Unset = UNSET
    alternative: str | Unset = UNSET
    billing_weights: str | Unset = UNSET
    default_memory_per_cpu: int | Unset = UNSET
    default_time_limit: int | Unset = UNSET
    denied_accounts: str | Unset = UNSET
    denied_qos: str | Unset = UNSET
    preemption_grace_time: int | Unset = UNSET
    maximum_cpus_per_node: int | Unset = UNSET
    maximum_memory_per_node: int | Unset = UNSET
    maximum_nodes_per_job: int | Unset = UNSET
    max_time_limit: int | Unset = UNSET
    min_nodes_per_job: int | Unset = UNSET
    name: str | Unset = UNSET
    nodes: str | Unset = UNSET
    over_time_limit: int | Unset = UNSET
    priority_job_factor: int | Unset = UNSET
    priority_tier: int | Unset = UNSET
    qos: str | Unset = UNSET
    state: str | Unset = UNSET
    total_cpus: int | Unset = UNSET
    total_nodes: int | Unset = UNSET
    tres: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        flags: list[str] | Unset = UNSET
        if not isinstance(self.flags, Unset):
            flags = self.flags

        preemption_mode: list[str] | Unset = UNSET
        if not isinstance(self.preemption_mode, Unset):
            preemption_mode = self.preemption_mode

        allowed_allocation_nodes = self.allowed_allocation_nodes

        allowed_accounts = self.allowed_accounts

        allowed_groups = self.allowed_groups

        allowed_qos = self.allowed_qos

        alternative = self.alternative

        billing_weights = self.billing_weights

        default_memory_per_cpu = self.default_memory_per_cpu

        default_time_limit = self.default_time_limit

        denied_accounts = self.denied_accounts

        denied_qos = self.denied_qos

        preemption_grace_time = self.preemption_grace_time

        maximum_cpus_per_node = self.maximum_cpus_per_node

        maximum_memory_per_node = self.maximum_memory_per_node

        maximum_nodes_per_job = self.maximum_nodes_per_job

        max_time_limit = self.max_time_limit

        min_nodes_per_job = self.min_nodes_per_job

        name = self.name

        nodes = self.nodes

        over_time_limit = self.over_time_limit

        priority_job_factor = self.priority_job_factor

        priority_tier = self.priority_tier

        qos = self.qos

        state = self.state

        total_cpus = self.total_cpus

        total_nodes = self.total_nodes

        tres = self.tres

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if flags is not UNSET:
            field_dict["flags"] = flags
        if preemption_mode is not UNSET:
            field_dict["preemption_mode"] = preemption_mode
        if allowed_allocation_nodes is not UNSET:
            field_dict["allowed_allocation_nodes"] = allowed_allocation_nodes
        if allowed_accounts is not UNSET:
            field_dict["allowed_accounts"] = allowed_accounts
        if allowed_groups is not UNSET:
            field_dict["allowed_groups"] = allowed_groups
        if allowed_qos is not UNSET:
            field_dict["allowed_qos"] = allowed_qos
        if alternative is not UNSET:
            field_dict["alternative"] = alternative
        if billing_weights is not UNSET:
            field_dict["billing_weights"] = billing_weights
        if default_memory_per_cpu is not UNSET:
            field_dict["default_memory_per_cpu"] = default_memory_per_cpu
        if default_time_limit is not UNSET:
            field_dict["default_time_limit"] = default_time_limit
        if denied_accounts is not UNSET:
            field_dict["denied_accounts"] = denied_accounts
        if denied_qos is not UNSET:
            field_dict["denied_qos"] = denied_qos
        if preemption_grace_time is not UNSET:
            field_dict["preemption_grace_time"] = preemption_grace_time
        if maximum_cpus_per_node is not UNSET:
            field_dict["maximum_cpus_per_node"] = maximum_cpus_per_node
        if maximum_memory_per_node is not UNSET:
            field_dict["maximum_memory_per_node"] = maximum_memory_per_node
        if maximum_nodes_per_job is not UNSET:
            field_dict["maximum_nodes_per_job"] = maximum_nodes_per_job
        if max_time_limit is not UNSET:
            field_dict["max_time_limit"] = max_time_limit
        if min_nodes_per_job is not UNSET:
            field_dict["min_nodes_per_job"] = min_nodes_per_job
        if name is not UNSET:
            field_dict["name"] = name
        if nodes is not UNSET:
            field_dict["nodes"] = nodes
        if over_time_limit is not UNSET:
            field_dict["over_time_limit"] = over_time_limit
        if priority_job_factor is not UNSET:
            field_dict["priority_job_factor"] = priority_job_factor
        if priority_tier is not UNSET:
            field_dict["priority_tier"] = priority_tier
        if qos is not UNSET:
            field_dict["qos"] = qos
        if state is not UNSET:
            field_dict["state"] = state
        if total_cpus is not UNSET:
            field_dict["total_cpus"] = total_cpus
        if total_nodes is not UNSET:
            field_dict["total_nodes"] = total_nodes
        if tres is not UNSET:
            field_dict["tres"] = tres

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        flags = cast(list[str], d.pop("flags", UNSET))

        preemption_mode = cast(list[str], d.pop("preemption_mode", UNSET))

        allowed_allocation_nodes = d.pop("allowed_allocation_nodes", UNSET)

        allowed_accounts = d.pop("allowed_accounts", UNSET)

        allowed_groups = d.pop("allowed_groups", UNSET)

        allowed_qos = d.pop("allowed_qos", UNSET)

        alternative = d.pop("alternative", UNSET)

        billing_weights = d.pop("billing_weights", UNSET)

        default_memory_per_cpu = d.pop("default_memory_per_cpu", UNSET)

        default_time_limit = d.pop("default_time_limit", UNSET)

        denied_accounts = d.pop("denied_accounts", UNSET)

        denied_qos = d.pop("denied_qos", UNSET)

        preemption_grace_time = d.pop("preemption_grace_time", UNSET)

        maximum_cpus_per_node = d.pop("maximum_cpus_per_node", UNSET)

        maximum_memory_per_node = d.pop("maximum_memory_per_node", UNSET)

        maximum_nodes_per_job = d.pop("maximum_nodes_per_job", UNSET)

        max_time_limit = d.pop("max_time_limit", UNSET)

        min_nodes_per_job = d.pop("min_nodes_per_job", UNSET)

        name = d.pop("name", UNSET)

        nodes = d.pop("nodes", UNSET)

        over_time_limit = d.pop("over_time_limit", UNSET)

        priority_job_factor = d.pop("priority_job_factor", UNSET)

        priority_tier = d.pop("priority_tier", UNSET)

        qos = d.pop("qos", UNSET)

        state = d.pop("state", UNSET)

        total_cpus = d.pop("total_cpus", UNSET)

        total_nodes = d.pop("total_nodes", UNSET)

        tres = d.pop("tres", UNSET)

        v0037_partition = cls(
            flags=flags,
            preemption_mode=preemption_mode,
            allowed_allocation_nodes=allowed_allocation_nodes,
            allowed_accounts=allowed_accounts,
            allowed_groups=allowed_groups,
            allowed_qos=allowed_qos,
            alternative=alternative,
            billing_weights=billing_weights,
            default_memory_per_cpu=default_memory_per_cpu,
            default_time_limit=default_time_limit,
            denied_accounts=denied_accounts,
            denied_qos=denied_qos,
            preemption_grace_time=preemption_grace_time,
            maximum_cpus_per_node=maximum_cpus_per_node,
            maximum_memory_per_node=maximum_memory_per_node,
            maximum_nodes_per_job=maximum_nodes_per_job,
            max_time_limit=max_time_limit,
            min_nodes_per_job=min_nodes_per_job,
            name=name,
            nodes=nodes,
            over_time_limit=over_time_limit,
            priority_job_factor=priority_job_factor,
            priority_tier=priority_tier,
            qos=qos,
            state=state,
            total_cpus=total_cpus,
            total_nodes=total_nodes,
            tres=tres,
        )

        v0037_partition.additional_properties = d
        return v0037_partition

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
