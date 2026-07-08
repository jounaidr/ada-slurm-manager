from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.v0041_openapi_partition_resp_partitions_item_select_type_item import (
    V0041OpenapiPartitionRespPartitionsItemSelectTypeItem,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v0041_openapi_partition_resp_partitions_item_accounts import (
        V0041OpenapiPartitionRespPartitionsItemAccounts,
    )
    from ..models.v0041_openapi_partition_resp_partitions_item_cpus import V0041OpenapiPartitionRespPartitionsItemCpus
    from ..models.v0041_openapi_partition_resp_partitions_item_defaults import (
        V0041OpenapiPartitionRespPartitionsItemDefaults,
    )
    from ..models.v0041_openapi_partition_resp_partitions_item_groups import (
        V0041OpenapiPartitionRespPartitionsItemGroups,
    )
    from ..models.v0041_openapi_partition_resp_partitions_item_maximums import (
        V0041OpenapiPartitionRespPartitionsItemMaximums,
    )
    from ..models.v0041_openapi_partition_resp_partitions_item_minimums import (
        V0041OpenapiPartitionRespPartitionsItemMinimums,
    )
    from ..models.v0041_openapi_partition_resp_partitions_item_nodes import V0041OpenapiPartitionRespPartitionsItemNodes
    from ..models.v0041_openapi_partition_resp_partitions_item_partition import (
        V0041OpenapiPartitionRespPartitionsItemPartition,
    )
    from ..models.v0041_openapi_partition_resp_partitions_item_priority import (
        V0041OpenapiPartitionRespPartitionsItemPriority,
    )
    from ..models.v0041_openapi_partition_resp_partitions_item_qos import V0041OpenapiPartitionRespPartitionsItemQos
    from ..models.v0041_openapi_partition_resp_partitions_item_suspend_time import (
        V0041OpenapiPartitionRespPartitionsItemSuspendTime,
    )
    from ..models.v0041_openapi_partition_resp_partitions_item_timeouts import (
        V0041OpenapiPartitionRespPartitionsItemTimeouts,
    )
    from ..models.v0041_openapi_partition_resp_partitions_item_tres import V0041OpenapiPartitionRespPartitionsItemTres


T = TypeVar("T", bound="V0041OpenapiPartitionRespPartitionsItem")


@_attrs_define
class V0041OpenapiPartitionRespPartitionsItem:
    """
    Attributes:
        nodes (V0041OpenapiPartitionRespPartitionsItemNodes | Unset):
        accounts (V0041OpenapiPartitionRespPartitionsItemAccounts | Unset):
        groups (V0041OpenapiPartitionRespPartitionsItemGroups | Unset):
        qos (V0041OpenapiPartitionRespPartitionsItemQos | Unset):
        alternate (str | Unset): Alternate
        tres (V0041OpenapiPartitionRespPartitionsItemTres | Unset):
        cluster (str | Unset): Cluster name
        select_type (list[V0041OpenapiPartitionRespPartitionsItemSelectTypeItem] | Unset): Scheduler consumable resource
            selection type
        cpus (V0041OpenapiPartitionRespPartitionsItemCpus | Unset):
        defaults (V0041OpenapiPartitionRespPartitionsItemDefaults | Unset):
        grace_time (int | Unset): GraceTime
        maximums (V0041OpenapiPartitionRespPartitionsItemMaximums | Unset):
        minimums (V0041OpenapiPartitionRespPartitionsItemMinimums | Unset):
        name (str | Unset): PartitionName
        node_sets (str | Unset): NodeSets
        priority (V0041OpenapiPartitionRespPartitionsItemPriority | Unset):
        timeouts (V0041OpenapiPartitionRespPartitionsItemTimeouts | Unset):
        partition (V0041OpenapiPartitionRespPartitionsItemPartition | Unset):
        suspend_time (V0041OpenapiPartitionRespPartitionsItemSuspendTime | Unset): SuspendTime (GLOBAL if both set and
            infinite are false)
    """

    nodes: V0041OpenapiPartitionRespPartitionsItemNodes | Unset = UNSET
    accounts: V0041OpenapiPartitionRespPartitionsItemAccounts | Unset = UNSET
    groups: V0041OpenapiPartitionRespPartitionsItemGroups | Unset = UNSET
    qos: V0041OpenapiPartitionRespPartitionsItemQos | Unset = UNSET
    alternate: str | Unset = UNSET
    tres: V0041OpenapiPartitionRespPartitionsItemTres | Unset = UNSET
    cluster: str | Unset = UNSET
    select_type: list[V0041OpenapiPartitionRespPartitionsItemSelectTypeItem] | Unset = UNSET
    cpus: V0041OpenapiPartitionRespPartitionsItemCpus | Unset = UNSET
    defaults: V0041OpenapiPartitionRespPartitionsItemDefaults | Unset = UNSET
    grace_time: int | Unset = UNSET
    maximums: V0041OpenapiPartitionRespPartitionsItemMaximums | Unset = UNSET
    minimums: V0041OpenapiPartitionRespPartitionsItemMinimums | Unset = UNSET
    name: str | Unset = UNSET
    node_sets: str | Unset = UNSET
    priority: V0041OpenapiPartitionRespPartitionsItemPriority | Unset = UNSET
    timeouts: V0041OpenapiPartitionRespPartitionsItemTimeouts | Unset = UNSET
    partition: V0041OpenapiPartitionRespPartitionsItemPartition | Unset = UNSET
    suspend_time: V0041OpenapiPartitionRespPartitionsItemSuspendTime | Unset = UNSET
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
        if partition is not UNSET:
            field_dict["partition"] = partition
        if suspend_time is not UNSET:
            field_dict["suspend_time"] = suspend_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v0041_openapi_partition_resp_partitions_item_accounts import (
            V0041OpenapiPartitionRespPartitionsItemAccounts,
        )
        from ..models.v0041_openapi_partition_resp_partitions_item_cpus import (
            V0041OpenapiPartitionRespPartitionsItemCpus,
        )
        from ..models.v0041_openapi_partition_resp_partitions_item_defaults import (
            V0041OpenapiPartitionRespPartitionsItemDefaults,
        )
        from ..models.v0041_openapi_partition_resp_partitions_item_groups import (
            V0041OpenapiPartitionRespPartitionsItemGroups,
        )
        from ..models.v0041_openapi_partition_resp_partitions_item_maximums import (
            V0041OpenapiPartitionRespPartitionsItemMaximums,
        )
        from ..models.v0041_openapi_partition_resp_partitions_item_minimums import (
            V0041OpenapiPartitionRespPartitionsItemMinimums,
        )
        from ..models.v0041_openapi_partition_resp_partitions_item_nodes import (
            V0041OpenapiPartitionRespPartitionsItemNodes,
        )
        from ..models.v0041_openapi_partition_resp_partitions_item_partition import (
            V0041OpenapiPartitionRespPartitionsItemPartition,
        )
        from ..models.v0041_openapi_partition_resp_partitions_item_priority import (
            V0041OpenapiPartitionRespPartitionsItemPriority,
        )
        from ..models.v0041_openapi_partition_resp_partitions_item_qos import V0041OpenapiPartitionRespPartitionsItemQos
        from ..models.v0041_openapi_partition_resp_partitions_item_suspend_time import (
            V0041OpenapiPartitionRespPartitionsItemSuspendTime,
        )
        from ..models.v0041_openapi_partition_resp_partitions_item_timeouts import (
            V0041OpenapiPartitionRespPartitionsItemTimeouts,
        )
        from ..models.v0041_openapi_partition_resp_partitions_item_tres import (
            V0041OpenapiPartitionRespPartitionsItemTres,
        )

        d = dict(src_dict)
        _nodes = d.pop("nodes", UNSET)
        nodes: V0041OpenapiPartitionRespPartitionsItemNodes | Unset
        if isinstance(_nodes, Unset):
            nodes = UNSET
        else:
            nodes = V0041OpenapiPartitionRespPartitionsItemNodes.from_dict(_nodes)

        _accounts = d.pop("accounts", UNSET)
        accounts: V0041OpenapiPartitionRespPartitionsItemAccounts | Unset
        if isinstance(_accounts, Unset):
            accounts = UNSET
        else:
            accounts = V0041OpenapiPartitionRespPartitionsItemAccounts.from_dict(_accounts)

        _groups = d.pop("groups", UNSET)
        groups: V0041OpenapiPartitionRespPartitionsItemGroups | Unset
        if isinstance(_groups, Unset):
            groups = UNSET
        else:
            groups = V0041OpenapiPartitionRespPartitionsItemGroups.from_dict(_groups)

        _qos = d.pop("qos", UNSET)
        qos: V0041OpenapiPartitionRespPartitionsItemQos | Unset
        if isinstance(_qos, Unset):
            qos = UNSET
        else:
            qos = V0041OpenapiPartitionRespPartitionsItemQos.from_dict(_qos)

        alternate = d.pop("alternate", UNSET)

        _tres = d.pop("tres", UNSET)
        tres: V0041OpenapiPartitionRespPartitionsItemTres | Unset
        if isinstance(_tres, Unset):
            tres = UNSET
        else:
            tres = V0041OpenapiPartitionRespPartitionsItemTres.from_dict(_tres)

        cluster = d.pop("cluster", UNSET)

        _select_type = d.pop("select_type", UNSET)
        select_type: list[V0041OpenapiPartitionRespPartitionsItemSelectTypeItem] | Unset = UNSET
        if _select_type is not UNSET:
            select_type = []
            for select_type_item_data in _select_type:
                select_type_item = V0041OpenapiPartitionRespPartitionsItemSelectTypeItem(select_type_item_data)

                select_type.append(select_type_item)

        _cpus = d.pop("cpus", UNSET)
        cpus: V0041OpenapiPartitionRespPartitionsItemCpus | Unset
        if isinstance(_cpus, Unset):
            cpus = UNSET
        else:
            cpus = V0041OpenapiPartitionRespPartitionsItemCpus.from_dict(_cpus)

        _defaults = d.pop("defaults", UNSET)
        defaults: V0041OpenapiPartitionRespPartitionsItemDefaults | Unset
        if isinstance(_defaults, Unset):
            defaults = UNSET
        else:
            defaults = V0041OpenapiPartitionRespPartitionsItemDefaults.from_dict(_defaults)

        grace_time = d.pop("grace_time", UNSET)

        _maximums = d.pop("maximums", UNSET)
        maximums: V0041OpenapiPartitionRespPartitionsItemMaximums | Unset
        if isinstance(_maximums, Unset):
            maximums = UNSET
        else:
            maximums = V0041OpenapiPartitionRespPartitionsItemMaximums.from_dict(_maximums)

        _minimums = d.pop("minimums", UNSET)
        minimums: V0041OpenapiPartitionRespPartitionsItemMinimums | Unset
        if isinstance(_minimums, Unset):
            minimums = UNSET
        else:
            minimums = V0041OpenapiPartitionRespPartitionsItemMinimums.from_dict(_minimums)

        name = d.pop("name", UNSET)

        node_sets = d.pop("node_sets", UNSET)

        _priority = d.pop("priority", UNSET)
        priority: V0041OpenapiPartitionRespPartitionsItemPriority | Unset
        if isinstance(_priority, Unset):
            priority = UNSET
        else:
            priority = V0041OpenapiPartitionRespPartitionsItemPriority.from_dict(_priority)

        _timeouts = d.pop("timeouts", UNSET)
        timeouts: V0041OpenapiPartitionRespPartitionsItemTimeouts | Unset
        if isinstance(_timeouts, Unset):
            timeouts = UNSET
        else:
            timeouts = V0041OpenapiPartitionRespPartitionsItemTimeouts.from_dict(_timeouts)

        _partition = d.pop("partition", UNSET)
        partition: V0041OpenapiPartitionRespPartitionsItemPartition | Unset
        if isinstance(_partition, Unset):
            partition = UNSET
        else:
            partition = V0041OpenapiPartitionRespPartitionsItemPartition.from_dict(_partition)

        _suspend_time = d.pop("suspend_time", UNSET)
        suspend_time: V0041OpenapiPartitionRespPartitionsItemSuspendTime | Unset
        if isinstance(_suspend_time, Unset):
            suspend_time = UNSET
        else:
            suspend_time = V0041OpenapiPartitionRespPartitionsItemSuspendTime.from_dict(_suspend_time)

        v0041_openapi_partition_resp_partitions_item = cls(
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
            partition=partition,
            suspend_time=suspend_time,
        )

        v0041_openapi_partition_resp_partitions_item.additional_properties = d
        return v0041_openapi_partition_resp_partitions_item

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
