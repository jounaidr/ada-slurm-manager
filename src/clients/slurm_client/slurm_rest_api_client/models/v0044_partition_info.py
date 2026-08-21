from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.v0044_partition_info_select_type_item import V0044PartitionInfoSelectTypeItem
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v0044_partition_info_accounts import V0044PartitionInfoAccounts
    from ..models.v0044_partition_info_cpus import V0044PartitionInfoCpus
    from ..models.v0044_partition_info_defaults import V0044PartitionInfoDefaults
    from ..models.v0044_partition_info_groups import V0044PartitionInfoGroups
    from ..models.v0044_partition_info_maximums import V0044PartitionInfoMaximums
    from ..models.v0044_partition_info_minimums import V0044PartitionInfoMinimums
    from ..models.v0044_partition_info_nodes import V0044PartitionInfoNodes
    from ..models.v0044_partition_info_partition import V0044PartitionInfoPartition
    from ..models.v0044_partition_info_priority import V0044PartitionInfoPriority
    from ..models.v0044_partition_info_qos import V0044PartitionInfoQos
    from ..models.v0044_partition_info_timeouts import V0044PartitionInfoTimeouts
    from ..models.v0044_partition_info_tres import V0044PartitionInfoTres
    from ..models.v0044_uint_32_no_val_struct import V0044Uint32NoValStruct


T = TypeVar("T", bound="V0044PartitionInfo")


@_attrs_define
class V0044PartitionInfo:
    """
    Attributes:
        nodes (V0044PartitionInfoNodes | Unset):
        accounts (V0044PartitionInfoAccounts | Unset):
        groups (V0044PartitionInfoGroups | Unset):
        qos (V0044PartitionInfoQos | Unset):
        alternate (str | Unset): Alternate - Partition name of alternate partition to be used if the state of this
            partition is DRAIN or INACTIVE
        tres (V0044PartitionInfoTres | Unset):
        cluster (str | Unset): Cluster name
        select_type (list[V0044PartitionInfoSelectTypeItem] | Unset): Scheduler consumable resource selection type
        cpus (V0044PartitionInfoCpus | Unset):
        defaults (V0044PartitionInfoDefaults | Unset):
        grace_time (int | Unset): GraceTime - Grace time in seconds to be extended to a job which has been selected for
            preemption
        maximums (V0044PartitionInfoMaximums | Unset):
        minimums (V0044PartitionInfoMinimums | Unset):
        name (str | Unset): PartitionName - Name by which the partition may be referenced
        node_sets (str | Unset): NodeSets - Comma-separated list of nodesets which are associated with this partition
        priority (V0044PartitionInfoPriority | Unset):
        timeouts (V0044PartitionInfoTimeouts | Unset):
        topology (str | Unset): Topology - Name of the topology, defined in topology.yaml, used by jobs in this
            partition
        partition (V0044PartitionInfoPartition | Unset):
        suspend_time (V0044Uint32NoValStruct | Unset):
    """

    nodes: V0044PartitionInfoNodes | Unset = UNSET
    accounts: V0044PartitionInfoAccounts | Unset = UNSET
    groups: V0044PartitionInfoGroups | Unset = UNSET
    qos: V0044PartitionInfoQos | Unset = UNSET
    alternate: str | Unset = UNSET
    tres: V0044PartitionInfoTres | Unset = UNSET
    cluster: str | Unset = UNSET
    select_type: list[V0044PartitionInfoSelectTypeItem] | Unset = UNSET
    cpus: V0044PartitionInfoCpus | Unset = UNSET
    defaults: V0044PartitionInfoDefaults | Unset = UNSET
    grace_time: int | Unset = UNSET
    maximums: V0044PartitionInfoMaximums | Unset = UNSET
    minimums: V0044PartitionInfoMinimums | Unset = UNSET
    name: str | Unset = UNSET
    node_sets: str | Unset = UNSET
    priority: V0044PartitionInfoPriority | Unset = UNSET
    timeouts: V0044PartitionInfoTimeouts | Unset = UNSET
    topology: str | Unset = UNSET
    partition: V0044PartitionInfoPartition | Unset = UNSET
    suspend_time: V0044Uint32NoValStruct | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        nodes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.nodes, Unset):
            nodes = self.nodes.to_dict()

        accounts: dict[str, Any] | Unset = UNSET
        if not isinstance(self.accounts, Unset):
            accounts = self.accounts.to_dict()

        groups: dict[str, Any] | Unset = UNSET
        if not isinstance(self.groups, Unset):
            groups = self.groups.to_dict()

        qos: dict[str, Any] | Unset = UNSET
        if not isinstance(self.qos, Unset):
            qos = self.qos.to_dict()

        alternate = self.alternate

        tres: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tres, Unset):
            tres = self.tres.to_dict()

        cluster = self.cluster

        select_type: list[str] | Unset = UNSET
        if not isinstance(self.select_type, Unset):
            select_type = []
            for select_type_item_data in self.select_type:
                select_type_item = select_type_item_data.value
                select_type.append(select_type_item)

        cpus: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cpus, Unset):
            cpus = self.cpus.to_dict()

        defaults: dict[str, Any] | Unset = UNSET
        if not isinstance(self.defaults, Unset):
            defaults = self.defaults.to_dict()

        grace_time = self.grace_time

        maximums: dict[str, Any] | Unset = UNSET
        if not isinstance(self.maximums, Unset):
            maximums = self.maximums.to_dict()

        minimums: dict[str, Any] | Unset = UNSET
        if not isinstance(self.minimums, Unset):
            minimums = self.minimums.to_dict()

        name = self.name

        node_sets = self.node_sets

        priority: dict[str, Any] | Unset = UNSET
        if not isinstance(self.priority, Unset):
            priority = self.priority.to_dict()

        timeouts: dict[str, Any] | Unset = UNSET
        if not isinstance(self.timeouts, Unset):
            timeouts = self.timeouts.to_dict()

        topology = self.topology

        partition: dict[str, Any] | Unset = UNSET
        if not isinstance(self.partition, Unset):
            partition = self.partition.to_dict()

        suspend_time: dict[str, Any] | Unset = UNSET
        if not isinstance(self.suspend_time, Unset):
            suspend_time = self.suspend_time.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if nodes is not UNSET:
            field_dict["nodes"] = nodes
        if accounts is not UNSET:
            field_dict["accounts"] = accounts
        if groups is not UNSET:
            field_dict["groups"] = groups
        if qos is not UNSET:
            field_dict["qos"] = qos
        if alternate is not UNSET:
            field_dict["alternate"] = alternate
        if tres is not UNSET:
            field_dict["tres"] = tres
        if cluster is not UNSET:
            field_dict["cluster"] = cluster
        if select_type is not UNSET:
            field_dict["select_type"] = select_type
        if cpus is not UNSET:
            field_dict["cpus"] = cpus
        if defaults is not UNSET:
            field_dict["defaults"] = defaults
        if grace_time is not UNSET:
            field_dict["grace_time"] = grace_time
        if maximums is not UNSET:
            field_dict["maximums"] = maximums
        if minimums is not UNSET:
            field_dict["minimums"] = minimums
        if name is not UNSET:
            field_dict["name"] = name
        if node_sets is not UNSET:
            field_dict["node_sets"] = node_sets
        if priority is not UNSET:
            field_dict["priority"] = priority
        if timeouts is not UNSET:
            field_dict["timeouts"] = timeouts
        if topology is not UNSET:
            field_dict["topology"] = topology
        if partition is not UNSET:
            field_dict["partition"] = partition
        if suspend_time is not UNSET:
            field_dict["suspend_time"] = suspend_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v0044_partition_info_accounts import V0044PartitionInfoAccounts
        from ..models.v0044_partition_info_cpus import V0044PartitionInfoCpus
        from ..models.v0044_partition_info_defaults import V0044PartitionInfoDefaults
        from ..models.v0044_partition_info_groups import V0044PartitionInfoGroups
        from ..models.v0044_partition_info_maximums import V0044PartitionInfoMaximums
        from ..models.v0044_partition_info_minimums import V0044PartitionInfoMinimums
        from ..models.v0044_partition_info_nodes import V0044PartitionInfoNodes
        from ..models.v0044_partition_info_partition import V0044PartitionInfoPartition
        from ..models.v0044_partition_info_priority import V0044PartitionInfoPriority
        from ..models.v0044_partition_info_qos import V0044PartitionInfoQos
        from ..models.v0044_partition_info_timeouts import V0044PartitionInfoTimeouts
        from ..models.v0044_partition_info_tres import V0044PartitionInfoTres
        from ..models.v0044_uint_32_no_val_struct import V0044Uint32NoValStruct

        d = dict(src_dict)
        _nodes = d.pop("nodes", UNSET)
        nodes: V0044PartitionInfoNodes | Unset
        if isinstance(_nodes, Unset):
            nodes = UNSET
        else:
            nodes = V0044PartitionInfoNodes.from_dict(_nodes)

        _accounts = d.pop("accounts", UNSET)
        accounts: V0044PartitionInfoAccounts | Unset
        if isinstance(_accounts, Unset):
            accounts = UNSET
        else:
            accounts = V0044PartitionInfoAccounts.from_dict(_accounts)

        _groups = d.pop("groups", UNSET)
        groups: V0044PartitionInfoGroups | Unset
        if isinstance(_groups, Unset):
            groups = UNSET
        else:
            groups = V0044PartitionInfoGroups.from_dict(_groups)

        _qos = d.pop("qos", UNSET)
        qos: V0044PartitionInfoQos | Unset
        if isinstance(_qos, Unset):
            qos = UNSET
        else:
            qos = V0044PartitionInfoQos.from_dict(_qos)

        alternate = d.pop("alternate", UNSET)

        _tres = d.pop("tres", UNSET)
        tres: V0044PartitionInfoTres | Unset
        if isinstance(_tres, Unset):
            tres = UNSET
        else:
            tres = V0044PartitionInfoTres.from_dict(_tres)

        cluster = d.pop("cluster", UNSET)

        _select_type = d.pop("select_type", UNSET)
        select_type: list[V0044PartitionInfoSelectTypeItem] | Unset = UNSET
        if _select_type is not UNSET:
            select_type = []
            for select_type_item_data in _select_type:
                select_type_item = V0044PartitionInfoSelectTypeItem(select_type_item_data)

                select_type.append(select_type_item)

        _cpus = d.pop("cpus", UNSET)
        cpus: V0044PartitionInfoCpus | Unset
        if isinstance(_cpus, Unset):
            cpus = UNSET
        else:
            cpus = V0044PartitionInfoCpus.from_dict(_cpus)

        _defaults = d.pop("defaults", UNSET)
        defaults: V0044PartitionInfoDefaults | Unset
        if isinstance(_defaults, Unset):
            defaults = UNSET
        else:
            defaults = V0044PartitionInfoDefaults.from_dict(_defaults)

        grace_time = d.pop("grace_time", UNSET)

        _maximums = d.pop("maximums", UNSET)
        maximums: V0044PartitionInfoMaximums | Unset
        if isinstance(_maximums, Unset):
            maximums = UNSET
        else:
            maximums = V0044PartitionInfoMaximums.from_dict(_maximums)

        _minimums = d.pop("minimums", UNSET)
        minimums: V0044PartitionInfoMinimums | Unset
        if isinstance(_minimums, Unset):
            minimums = UNSET
        else:
            minimums = V0044PartitionInfoMinimums.from_dict(_minimums)

        name = d.pop("name", UNSET)

        node_sets = d.pop("node_sets", UNSET)

        _priority = d.pop("priority", UNSET)
        priority: V0044PartitionInfoPriority | Unset
        if isinstance(_priority, Unset):
            priority = UNSET
        else:
            priority = V0044PartitionInfoPriority.from_dict(_priority)

        _timeouts = d.pop("timeouts", UNSET)
        timeouts: V0044PartitionInfoTimeouts | Unset
        if isinstance(_timeouts, Unset):
            timeouts = UNSET
        else:
            timeouts = V0044PartitionInfoTimeouts.from_dict(_timeouts)

        topology = d.pop("topology", UNSET)

        _partition = d.pop("partition", UNSET)
        partition: V0044PartitionInfoPartition | Unset
        if isinstance(_partition, Unset):
            partition = UNSET
        else:
            partition = V0044PartitionInfoPartition.from_dict(_partition)

        _suspend_time = d.pop("suspend_time", UNSET)
        suspend_time: V0044Uint32NoValStruct | Unset
        if isinstance(_suspend_time, Unset):
            suspend_time = UNSET
        else:
            suspend_time = V0044Uint32NoValStruct.from_dict(_suspend_time)

        v0044_partition_info = cls(
            nodes=nodes,
            accounts=accounts,
            groups=groups,
            qos=qos,
            alternate=alternate,
            tres=tres,
            cluster=cluster,
            select_type=select_type,
            cpus=cpus,
            defaults=defaults,
            grace_time=grace_time,
            maximums=maximums,
            minimums=minimums,
            name=name,
            node_sets=node_sets,
            priority=priority,
            timeouts=timeouts,
            topology=topology,
            partition=partition,
            suspend_time=suspend_time,
        )

        v0044_partition_info.additional_properties = d
        return v0044_partition_info

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
