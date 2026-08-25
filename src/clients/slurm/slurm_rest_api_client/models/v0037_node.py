from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="V0037Node")


@_attrs_define
class V0037Node:
    """
    Attributes:
        architecture (str | Unset): computer architecture
        burstbuffer_network_address (str | Unset): BcastAddr
        boards (int | Unset): total number of boards per node
        boot_time (int | Unset): timestamp of node boot
        cores (int | Unset): number of cores per socket
        cpu_binding (int | Unset): Default task binding
        cpu_load (int | Unset): CPU load * 100
        free_memory (int | Unset): free memory in MiB
        cpus (int | Unset): configured count of cpus running on the node
        features (str | Unset):
        active_features (str | Unset): list of a node's available features
        gres (str | Unset): list of a node's generic resources
        gres_drained (str | Unset): list of drained GRES
        gres_used (str | Unset): list of GRES in current use
        mcs_label (str | Unset): mcs label if mcs plugin in use
        name (str | Unset): node name to slurm
        next_state_after_reboot (str | Unset): state after reboot
        next_state_after_reboot_flags (list[str] | Unset): node state flags
        address (str | Unset): state after reboot
        hostname (str | Unset): node's hostname
        state (str | Unset): current node state
        state_flags (list[str] | Unset): node state flags
        operating_system (str | Unset): operating system
        owner (str | Unset): User allowed to use this node
        partitions (list[str] | Unset): assigned partitions
        port (int | Unset): TCP port number of the slurmd
        real_memory (int | Unset): configured MB of real memory on the node
        reason (str | Unset): reason for node being DOWN or DRAINING
        reason_changed_at (int | Unset): Time stamp when reason was set
        reason_set_by_user (str | Unset): User that set the reason
        slurmd_start_time (int | Unset): timestamp of slurmd startup
        sockets (int | Unset): total number of sockets per node
        threads (int | Unset): number of threads per core
        temporary_disk (int | Unset): configured MB of total disk in TMP_FS
        weight (int | Unset): arbitrary priority of node for scheduling
        tres (str | Unset): TRES on node
        tres_used (str | Unset): TRES used on node
        tres_weighted (float | Unset): TRES weight used on node
        slurmd_version (str | Unset): Slurmd version
        alloc_cpus (int | Unset): Allocated CPUs
        idle_cpus (int | Unset): Idle CPUs
        alloc_memory (int | Unset): Allocated memory (MB)
    """

    architecture: str | Unset = UNSET
    burstbuffer_network_address: str | Unset = UNSET
    boards: int | Unset = UNSET
    boot_time: int | Unset = UNSET
    cores: int | Unset = UNSET
    cpu_binding: int | Unset = UNSET
    cpu_load: int | Unset = UNSET
    free_memory: int | Unset = UNSET
    cpus: int | Unset = UNSET
    features: str | Unset = UNSET
    active_features: str | Unset = UNSET
    gres: str | Unset = UNSET
    gres_drained: str | Unset = UNSET
    gres_used: str | Unset = UNSET
    mcs_label: str | Unset = UNSET
    name: str | Unset = UNSET
    next_state_after_reboot: str | Unset = UNSET
    next_state_after_reboot_flags: list[str] | Unset = UNSET
    address: str | Unset = UNSET
    hostname: str | Unset = UNSET
    state: str | Unset = UNSET
    state_flags: list[str] | Unset = UNSET
    operating_system: str | Unset = UNSET
    owner: str | Unset = UNSET
    partitions: list[str] | Unset = UNSET
    port: int | Unset = UNSET
    real_memory: int | Unset = UNSET
    reason: str | Unset = UNSET
    reason_changed_at: int | Unset = UNSET
    reason_set_by_user: str | Unset = UNSET
    slurmd_start_time: int | Unset = UNSET
    sockets: int | Unset = UNSET
    threads: int | Unset = UNSET
    temporary_disk: int | Unset = UNSET
    weight: int | Unset = UNSET
    tres: str | Unset = UNSET
    tres_used: str | Unset = UNSET
    tres_weighted: float | Unset = UNSET
    slurmd_version: str | Unset = UNSET
    alloc_cpus: int | Unset = UNSET
    idle_cpus: int | Unset = UNSET
    alloc_memory: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        architecture = self.architecture

        burstbuffer_network_address = self.burstbuffer_network_address

        boards = self.boards

        boot_time = self.boot_time

        cores = self.cores

        cpu_binding = self.cpu_binding

        cpu_load = self.cpu_load

        free_memory = self.free_memory

        cpus = self.cpus

        features = self.features

        active_features = self.active_features

        gres = self.gres

        gres_drained = self.gres_drained

        gres_used = self.gres_used

        mcs_label = self.mcs_label

        name = self.name

        next_state_after_reboot = self.next_state_after_reboot

        next_state_after_reboot_flags: list[str] | Unset = UNSET
        if not isinstance(self.next_state_after_reboot_flags, Unset):
            next_state_after_reboot_flags = self.next_state_after_reboot_flags

        address = self.address

        hostname = self.hostname

        state = self.state

        state_flags: list[str] | Unset = UNSET
        if not isinstance(self.state_flags, Unset):
            state_flags = self.state_flags

        operating_system = self.operating_system

        owner = self.owner

        partitions: list[str] | Unset = UNSET
        if not isinstance(self.partitions, Unset):
            partitions = self.partitions

        port = self.port

        real_memory = self.real_memory

        reason = self.reason

        reason_changed_at = self.reason_changed_at

        reason_set_by_user = self.reason_set_by_user

        slurmd_start_time = self.slurmd_start_time

        sockets = self.sockets

        threads = self.threads

        temporary_disk = self.temporary_disk

        weight = self.weight

        tres = self.tres

        tres_used = self.tres_used

        tres_weighted = self.tres_weighted

        slurmd_version = self.slurmd_version

        alloc_cpus = self.alloc_cpus

        idle_cpus = self.idle_cpus

        alloc_memory = self.alloc_memory

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if architecture is not UNSET:
            field_dict["architecture"] = architecture
        if burstbuffer_network_address is not UNSET:
            field_dict["burstbuffer_network_address"] = burstbuffer_network_address
        if boards is not UNSET:
            field_dict["boards"] = boards
        if boot_time is not UNSET:
            field_dict["boot_time"] = boot_time
        if cores is not UNSET:
            field_dict["cores"] = cores
        if cpu_binding is not UNSET:
            field_dict["cpu_binding"] = cpu_binding
        if cpu_load is not UNSET:
            field_dict["cpu_load"] = cpu_load
        if free_memory is not UNSET:
            field_dict["free_memory"] = free_memory
        if cpus is not UNSET:
            field_dict["cpus"] = cpus
        if features is not UNSET:
            field_dict["features"] = features
        if active_features is not UNSET:
            field_dict["active_features"] = active_features
        if gres is not UNSET:
            field_dict["gres"] = gres
        if gres_drained is not UNSET:
            field_dict["gres_drained"] = gres_drained
        if gres_used is not UNSET:
            field_dict["gres_used"] = gres_used
        if mcs_label is not UNSET:
            field_dict["mcs_label"] = mcs_label
        if name is not UNSET:
            field_dict["name"] = name
        if next_state_after_reboot is not UNSET:
            field_dict["next_state_after_reboot"] = next_state_after_reboot
        if next_state_after_reboot_flags is not UNSET:
            field_dict["next_state_after_reboot_flags"] = next_state_after_reboot_flags
        if address is not UNSET:
            field_dict["address"] = address
        if hostname is not UNSET:
            field_dict["hostname"] = hostname
        if state is not UNSET:
            field_dict["state"] = state
        if state_flags is not UNSET:
            field_dict["state_flags"] = state_flags
        if operating_system is not UNSET:
            field_dict["operating_system"] = operating_system
        if owner is not UNSET:
            field_dict["owner"] = owner
        if partitions is not UNSET:
            field_dict["partitions"] = partitions
        if port is not UNSET:
            field_dict["port"] = port
        if real_memory is not UNSET:
            field_dict["real_memory"] = real_memory
        if reason is not UNSET:
            field_dict["reason"] = reason
        if reason_changed_at is not UNSET:
            field_dict["reason_changed_at"] = reason_changed_at
        if reason_set_by_user is not UNSET:
            field_dict["reason_set_by_user"] = reason_set_by_user
        if slurmd_start_time is not UNSET:
            field_dict["slurmd_start_time"] = slurmd_start_time
        if sockets is not UNSET:
            field_dict["sockets"] = sockets
        if threads is not UNSET:
            field_dict["threads"] = threads
        if temporary_disk is not UNSET:
            field_dict["temporary_disk"] = temporary_disk
        if weight is not UNSET:
            field_dict["weight"] = weight
        if tres is not UNSET:
            field_dict["tres"] = tres
        if tres_used is not UNSET:
            field_dict["tres_used"] = tres_used
        if tres_weighted is not UNSET:
            field_dict["tres_weighted"] = tres_weighted
        if slurmd_version is not UNSET:
            field_dict["slurmd_version"] = slurmd_version
        if alloc_cpus is not UNSET:
            field_dict["alloc_cpus"] = alloc_cpus
        if idle_cpus is not UNSET:
            field_dict["idle_cpus"] = idle_cpus
        if alloc_memory is not UNSET:
            field_dict["alloc_memory"] = alloc_memory

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        architecture = d.pop("architecture", UNSET)

        burstbuffer_network_address = d.pop("burstbuffer_network_address", UNSET)

        boards = d.pop("boards", UNSET)

        boot_time = d.pop("boot_time", UNSET)

        cores = d.pop("cores", UNSET)

        cpu_binding = d.pop("cpu_binding", UNSET)

        cpu_load = d.pop("cpu_load", UNSET)

        free_memory = d.pop("free_memory", UNSET)

        cpus = d.pop("cpus", UNSET)

        features = d.pop("features", UNSET)

        active_features = d.pop("active_features", UNSET)

        gres = d.pop("gres", UNSET)

        gres_drained = d.pop("gres_drained", UNSET)

        gres_used = d.pop("gres_used", UNSET)

        mcs_label = d.pop("mcs_label", UNSET)

        name = d.pop("name", UNSET)

        next_state_after_reboot = d.pop("next_state_after_reboot", UNSET)

        next_state_after_reboot_flags = cast(list[str], d.pop("next_state_after_reboot_flags", UNSET))

        address = d.pop("address", UNSET)

        hostname = d.pop("hostname", UNSET)

        state = d.pop("state", UNSET)

        state_flags = cast(list[str], d.pop("state_flags", UNSET))

        operating_system = d.pop("operating_system", UNSET)

        owner = d.pop("owner", UNSET)

        partitions = cast(list[str], d.pop("partitions", UNSET))

        port = d.pop("port", UNSET)

        real_memory = d.pop("real_memory", UNSET)

        reason = d.pop("reason", UNSET)

        reason_changed_at = d.pop("reason_changed_at", UNSET)

        reason_set_by_user = d.pop("reason_set_by_user", UNSET)

        slurmd_start_time = d.pop("slurmd_start_time", UNSET)

        sockets = d.pop("sockets", UNSET)

        threads = d.pop("threads", UNSET)

        temporary_disk = d.pop("temporary_disk", UNSET)

        weight = d.pop("weight", UNSET)

        tres = d.pop("tres", UNSET)

        tres_used = d.pop("tres_used", UNSET)

        tres_weighted = d.pop("tres_weighted", UNSET)

        slurmd_version = d.pop("slurmd_version", UNSET)

        alloc_cpus = d.pop("alloc_cpus", UNSET)

        idle_cpus = d.pop("idle_cpus", UNSET)

        alloc_memory = d.pop("alloc_memory", UNSET)

        v0037_node = cls(
            architecture=architecture,
            burstbuffer_network_address=burstbuffer_network_address,
            boards=boards,
            boot_time=boot_time,
            cores=cores,
            cpu_binding=cpu_binding,
            cpu_load=cpu_load,
            free_memory=free_memory,
            cpus=cpus,
            features=features,
            active_features=active_features,
            gres=gres,
            gres_drained=gres_drained,
            gres_used=gres_used,
            mcs_label=mcs_label,
            name=name,
            next_state_after_reboot=next_state_after_reboot,
            next_state_after_reboot_flags=next_state_after_reboot_flags,
            address=address,
            hostname=hostname,
            state=state,
            state_flags=state_flags,
            operating_system=operating_system,
            owner=owner,
            partitions=partitions,
            port=port,
            real_memory=real_memory,
            reason=reason,
            reason_changed_at=reason_changed_at,
            reason_set_by_user=reason_set_by_user,
            slurmd_start_time=slurmd_start_time,
            sockets=sockets,
            threads=threads,
            temporary_disk=temporary_disk,
            weight=weight,
            tres=tres,
            tres_used=tres_used,
            tres_weighted=tres_weighted,
            slurmd_version=slurmd_version,
            alloc_cpus=alloc_cpus,
            idle_cpus=idle_cpus,
            alloc_memory=alloc_memory,
        )

        v0037_node.additional_properties = d
        return v0037_node

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
