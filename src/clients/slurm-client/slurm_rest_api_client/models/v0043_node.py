from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.v0043_node_cert_flags_item import V0043NodeCertFlagsItem
from ..models.v0043_node_next_state_after_reboot_item import V0043NodeNextStateAfterRebootItem
from ..models.v0043_node_state_item import V0043NodeStateItem
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v0043_acct_gather_energy import V0043AcctGatherEnergy
    from ..models.v0043_node_external_sensors import V0043NodeExternalSensors
    from ..models.v0043_node_power import V0043NodePower
    from ..models.v0043_uint_64_no_val_struct import V0043Uint64NoValStruct


T = TypeVar("T", bound="V0043Node")


@_attrs_define
class V0043Node:
    """
    Attributes:
        architecture (str | Unset): Computer architecture
        burstbuffer_network_address (str | Unset): Alternate network path to be used for sbcast network traffic
        boards (int | Unset): Number of Baseboards in nodes with a baseboard controller
        boot_time (V0043Uint64NoValStruct | Unset):
        tls_cert_last_renewal (V0043Uint64NoValStruct | Unset):
        cert_flags (list[V0043NodeCertFlagsItem] | Unset): Certmgr status flags
        cluster_name (str | Unset): Cluster name (only set in federated environments)
        cores (int | Unset): Number of cores in a single physical processor socket
        specialized_cores (int | Unset): Number of cores reserved for system use
        cpu_binding (int | Unset): Default method for binding tasks to allocated CPUs
        cpu_load (int | Unset): CPU load as reported by the OS
        free_mem (V0043Uint64NoValStruct | Unset):
        cpus (int | Unset): Total CPUs, including cores and threads
        effective_cpus (int | Unset): Number of effective CPUs (excluding specialized CPUs)
        specialized_cpus (str | Unset): Abstract CPU IDs on this node reserved for exclusive use by slurmd and
            slurmstepd
        energy (V0043AcctGatherEnergy | Unset):
        external_sensors (V0043NodeExternalSensors | Unset):
        extra (str | Unset): Arbitrary string used for node filtering if extra constraints are enabled
        power (V0043NodePower | Unset):
        features (list[str] | Unset):
        active_features (list[str] | Unset):
        gpu_spec (str | Unset): CPU cores reserved for jobs that also use a GPU
        gres (str | Unset): Generic resources
        gres_drained (str | Unset): Drained generic resources
        gres_used (str | Unset): Generic resources currently in use
        instance_id (str | Unset): Cloud instance ID
        instance_type (str | Unset): Cloud instance type
        last_busy (V0043Uint64NoValStruct | Unset):
        mcs_label (str | Unset): Multi-Category Security label
        specialized_memory (int | Unset): Combined memory limit, in MB, for Slurm compute node daemons
        name (str | Unset): NodeName
        next_state_after_reboot (list[V0043NodeNextStateAfterRebootItem] | Unset): The state the node will be assigned
            after rebooting
        address (str | Unset): NodeAddr, used to establish a communication path
        hostname (str | Unset): NodeHostname
        state (list[V0043NodeStateItem] | Unset): Node state(s) applicable to this node
        operating_system (str | Unset): Operating system reported by the node
        owner (str | Unset): User allowed to run jobs on this node (unset if no restriction)
        partitions (list[str] | Unset):
        port (int | Unset): TCP port number of the slurmd
        real_memory (int | Unset): Total memory in MB on the node
        res_cores_per_gpu (int | Unset): Number of CPU cores per GPU restricted to GPU jobs
        comment (str | Unset): Arbitrary comment
        reason (str | Unset): Describes why the node is in a "DOWN", "DRAINED", "DRAINING", "FAILING" or "FAIL" state
        reason_changed_at (V0043Uint64NoValStruct | Unset):
        reason_set_by_user (str | Unset): User who set the reason
        resume_after (V0043Uint64NoValStruct | Unset):
        reservation (str | Unset): Name of reservation containing this node
        alloc_memory (int | Unset): Total memory in MB currently allocated for jobs
        alloc_cpus (int | Unset): Total number of CPUs currently allocated for jobs
        alloc_idle_cpus (int | Unset): Total number of idle CPUs
        tres_used (str | Unset): Trackable resources currently allocated for jobs
        tres_weighted (float | Unset): Ignored. Was weighted number of billable trackable resources allocated
        slurmd_start_time (V0043Uint64NoValStruct | Unset):
        sockets (int | Unset): Number of physical processor sockets/chips on the node
        threads (int | Unset): Number of logical threads in a single physical core
        temporary_disk (int | Unset): Total size in MB of temporary disk storage in TmpFS
        weight (int | Unset): Weight of the node for scheduling purposes
        topology (str | Unset): Topology
        tres (str | Unset): Configured trackable resources
        version (str | Unset): Slurmd version
    """

    architecture: str | Unset = UNSET
    burstbuffer_network_address: str | Unset = UNSET
    boards: int | Unset = UNSET
    boot_time: V0043Uint64NoValStruct | Unset = UNSET
    tls_cert_last_renewal: V0043Uint64NoValStruct | Unset = UNSET
    cert_flags: list[V0043NodeCertFlagsItem] | Unset = UNSET
    cluster_name: str | Unset = UNSET
    cores: int | Unset = UNSET
    specialized_cores: int | Unset = UNSET
    cpu_binding: int | Unset = UNSET
    cpu_load: int | Unset = UNSET
    free_mem: V0043Uint64NoValStruct | Unset = UNSET
    cpus: int | Unset = UNSET
    effective_cpus: int | Unset = UNSET
    specialized_cpus: str | Unset = UNSET
    energy: V0043AcctGatherEnergy | Unset = UNSET
    external_sensors: V0043NodeExternalSensors | Unset = UNSET
    extra: str | Unset = UNSET
    power: V0043NodePower | Unset = UNSET
    features: list[str] | Unset = UNSET
    active_features: list[str] | Unset = UNSET
    gpu_spec: str | Unset = UNSET
    gres: str | Unset = UNSET
    gres_drained: str | Unset = UNSET
    gres_used: str | Unset = UNSET
    instance_id: str | Unset = UNSET
    instance_type: str | Unset = UNSET
    last_busy: V0043Uint64NoValStruct | Unset = UNSET
    mcs_label: str | Unset = UNSET
    specialized_memory: int | Unset = UNSET
    name: str | Unset = UNSET
    next_state_after_reboot: list[V0043NodeNextStateAfterRebootItem] | Unset = UNSET
    address: str | Unset = UNSET
    hostname: str | Unset = UNSET
    state: list[V0043NodeStateItem] | Unset = UNSET
    operating_system: str | Unset = UNSET
    owner: str | Unset = UNSET
    partitions: list[str] | Unset = UNSET
    port: int | Unset = UNSET
    real_memory: int | Unset = UNSET
    res_cores_per_gpu: int | Unset = UNSET
    comment: str | Unset = UNSET
    reason: str | Unset = UNSET
    reason_changed_at: V0043Uint64NoValStruct | Unset = UNSET
    reason_set_by_user: str | Unset = UNSET
    resume_after: V0043Uint64NoValStruct | Unset = UNSET
    reservation: str | Unset = UNSET
    alloc_memory: int | Unset = UNSET
    alloc_cpus: int | Unset = UNSET
    alloc_idle_cpus: int | Unset = UNSET
    tres_used: str | Unset = UNSET
    tres_weighted: float | Unset = UNSET
    slurmd_start_time: V0043Uint64NoValStruct | Unset = UNSET
    sockets: int | Unset = UNSET
    threads: int | Unset = UNSET
    temporary_disk: int | Unset = UNSET
    weight: int | Unset = UNSET
    topology: str | Unset = UNSET
    tres: str | Unset = UNSET
    version: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        architecture = self.architecture

        burstbuffer_network_address = self.burstbuffer_network_address

        boards = self.boards

        boot_time: dict[str, Any] | Unset = UNSET
        if not isinstance(self.boot_time, Unset):
            boot_time = self.boot_time.to_dict()

        tls_cert_last_renewal: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tls_cert_last_renewal, Unset):
            tls_cert_last_renewal = self.tls_cert_last_renewal.to_dict()

        cert_flags: list[str] | Unset = UNSET
        if not isinstance(self.cert_flags, Unset):
            cert_flags = []
            for cert_flags_item_data in self.cert_flags:
                cert_flags_item = cert_flags_item_data.value
                cert_flags.append(cert_flags_item)

        cluster_name = self.cluster_name

        cores = self.cores

        specialized_cores = self.specialized_cores

        cpu_binding = self.cpu_binding

        cpu_load = self.cpu_load

        free_mem: dict[str, Any] | Unset = UNSET
        if not isinstance(self.free_mem, Unset):
            free_mem = self.free_mem.to_dict()

        cpus = self.cpus

        effective_cpus = self.effective_cpus

        specialized_cpus = self.specialized_cpus

        energy: dict[str, Any] | Unset = UNSET
        if not isinstance(self.energy, Unset):
            energy = self.energy.to_dict()

        external_sensors: dict[str, Any] | Unset = UNSET
        if not isinstance(self.external_sensors, Unset):
            external_sensors = self.external_sensors.to_dict()

        extra = self.extra

        power: dict[str, Any] | Unset = UNSET
        if not isinstance(self.power, Unset):
            power = self.power.to_dict()

        features: list[str] | Unset = UNSET
        if not isinstance(self.features, Unset):
            features = self.features

        active_features: list[str] | Unset = UNSET
        if not isinstance(self.active_features, Unset):
            active_features = self.active_features

        gpu_spec = self.gpu_spec

        gres = self.gres

        gres_drained = self.gres_drained

        gres_used = self.gres_used

        instance_id = self.instance_id

        instance_type = self.instance_type

        last_busy: dict[str, Any] | Unset = UNSET
        if not isinstance(self.last_busy, Unset):
            last_busy = self.last_busy.to_dict()

        mcs_label = self.mcs_label

        specialized_memory = self.specialized_memory

        name = self.name

        next_state_after_reboot: list[str] | Unset = UNSET
        if not isinstance(self.next_state_after_reboot, Unset):
            next_state_after_reboot = []
            for next_state_after_reboot_item_data in self.next_state_after_reboot:
                next_state_after_reboot_item = next_state_after_reboot_item_data.value
                next_state_after_reboot.append(next_state_after_reboot_item)

        address = self.address

        hostname = self.hostname

        state: list[str] | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = []
            for state_item_data in self.state:
                state_item = state_item_data.value
                state.append(state_item)

        operating_system = self.operating_system

        owner = self.owner

        partitions: list[str] | Unset = UNSET
        if not isinstance(self.partitions, Unset):
            partitions = self.partitions

        port = self.port

        real_memory = self.real_memory

        res_cores_per_gpu = self.res_cores_per_gpu

        comment = self.comment

        reason = self.reason

        reason_changed_at: dict[str, Any] | Unset = UNSET
        if not isinstance(self.reason_changed_at, Unset):
            reason_changed_at = self.reason_changed_at.to_dict()

        reason_set_by_user = self.reason_set_by_user

        resume_after: dict[str, Any] | Unset = UNSET
        if not isinstance(self.resume_after, Unset):
            resume_after = self.resume_after.to_dict()

        reservation = self.reservation

        alloc_memory = self.alloc_memory

        alloc_cpus = self.alloc_cpus

        alloc_idle_cpus = self.alloc_idle_cpus

        tres_used = self.tres_used

        tres_weighted = self.tres_weighted

        slurmd_start_time: dict[str, Any] | Unset = UNSET
        if not isinstance(self.slurmd_start_time, Unset):
            slurmd_start_time = self.slurmd_start_time.to_dict()

        sockets = self.sockets

        threads = self.threads

        temporary_disk = self.temporary_disk

        weight = self.weight

        topology = self.topology

        tres = self.tres

        version = self.version

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
        if tls_cert_last_renewal is not UNSET:
            field_dict["tls_cert_last_renewal"] = tls_cert_last_renewal
        if cert_flags is not UNSET:
            field_dict["cert_flags"] = cert_flags
        if cluster_name is not UNSET:
            field_dict["cluster_name"] = cluster_name
        if cores is not UNSET:
            field_dict["cores"] = cores
        if specialized_cores is not UNSET:
            field_dict["specialized_cores"] = specialized_cores
        if cpu_binding is not UNSET:
            field_dict["cpu_binding"] = cpu_binding
        if cpu_load is not UNSET:
            field_dict["cpu_load"] = cpu_load
        if free_mem is not UNSET:
            field_dict["free_mem"] = free_mem
        if cpus is not UNSET:
            field_dict["cpus"] = cpus
        if effective_cpus is not UNSET:
            field_dict["effective_cpus"] = effective_cpus
        if specialized_cpus is not UNSET:
            field_dict["specialized_cpus"] = specialized_cpus
        if energy is not UNSET:
            field_dict["energy"] = energy
        if external_sensors is not UNSET:
            field_dict["external_sensors"] = external_sensors
        if extra is not UNSET:
            field_dict["extra"] = extra
        if power is not UNSET:
            field_dict["power"] = power
        if features is not UNSET:
            field_dict["features"] = features
        if active_features is not UNSET:
            field_dict["active_features"] = active_features
        if gpu_spec is not UNSET:
            field_dict["gpu_spec"] = gpu_spec
        if gres is not UNSET:
            field_dict["gres"] = gres
        if gres_drained is not UNSET:
            field_dict["gres_drained"] = gres_drained
        if gres_used is not UNSET:
            field_dict["gres_used"] = gres_used
        if instance_id is not UNSET:
            field_dict["instance_id"] = instance_id
        if instance_type is not UNSET:
            field_dict["instance_type"] = instance_type
        if last_busy is not UNSET:
            field_dict["last_busy"] = last_busy
        if mcs_label is not UNSET:
            field_dict["mcs_label"] = mcs_label
        if specialized_memory is not UNSET:
            field_dict["specialized_memory"] = specialized_memory
        if name is not UNSET:
            field_dict["name"] = name
        if next_state_after_reboot is not UNSET:
            field_dict["next_state_after_reboot"] = next_state_after_reboot
        if address is not UNSET:
            field_dict["address"] = address
        if hostname is not UNSET:
            field_dict["hostname"] = hostname
        if state is not UNSET:
            field_dict["state"] = state
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
        if res_cores_per_gpu is not UNSET:
            field_dict["res_cores_per_gpu"] = res_cores_per_gpu
        if comment is not UNSET:
            field_dict["comment"] = comment
        if reason is not UNSET:
            field_dict["reason"] = reason
        if reason_changed_at is not UNSET:
            field_dict["reason_changed_at"] = reason_changed_at
        if reason_set_by_user is not UNSET:
            field_dict["reason_set_by_user"] = reason_set_by_user
        if resume_after is not UNSET:
            field_dict["resume_after"] = resume_after
        if reservation is not UNSET:
            field_dict["reservation"] = reservation
        if alloc_memory is not UNSET:
            field_dict["alloc_memory"] = alloc_memory
        if alloc_cpus is not UNSET:
            field_dict["alloc_cpus"] = alloc_cpus
        if alloc_idle_cpus is not UNSET:
            field_dict["alloc_idle_cpus"] = alloc_idle_cpus
        if tres_used is not UNSET:
            field_dict["tres_used"] = tres_used
        if tres_weighted is not UNSET:
            field_dict["tres_weighted"] = tres_weighted
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
        if topology is not UNSET:
            field_dict["topology"] = topology
        if tres is not UNSET:
            field_dict["tres"] = tres
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v0043_acct_gather_energy import V0043AcctGatherEnergy
        from ..models.v0043_node_external_sensors import V0043NodeExternalSensors
        from ..models.v0043_node_power import V0043NodePower
        from ..models.v0043_uint_64_no_val_struct import V0043Uint64NoValStruct

        d = dict(src_dict)
        architecture = d.pop("architecture", UNSET)

        burstbuffer_network_address = d.pop("burstbuffer_network_address", UNSET)

        boards = d.pop("boards", UNSET)

        _boot_time = d.pop("boot_time", UNSET)
        boot_time: V0043Uint64NoValStruct | Unset
        if isinstance(_boot_time, Unset):
            boot_time = UNSET
        else:
            boot_time = V0043Uint64NoValStruct.from_dict(_boot_time)

        _tls_cert_last_renewal = d.pop("tls_cert_last_renewal", UNSET)
        tls_cert_last_renewal: V0043Uint64NoValStruct | Unset
        if isinstance(_tls_cert_last_renewal, Unset):
            tls_cert_last_renewal = UNSET
        else:
            tls_cert_last_renewal = V0043Uint64NoValStruct.from_dict(_tls_cert_last_renewal)

        _cert_flags = d.pop("cert_flags", UNSET)
        cert_flags: list[V0043NodeCertFlagsItem] | Unset = UNSET
        if _cert_flags is not UNSET:
            cert_flags = []
            for cert_flags_item_data in _cert_flags:
                cert_flags_item = V0043NodeCertFlagsItem(cert_flags_item_data)

                cert_flags.append(cert_flags_item)

        cluster_name = d.pop("cluster_name", UNSET)

        cores = d.pop("cores", UNSET)

        specialized_cores = d.pop("specialized_cores", UNSET)

        cpu_binding = d.pop("cpu_binding", UNSET)

        cpu_load = d.pop("cpu_load", UNSET)

        _free_mem = d.pop("free_mem", UNSET)
        free_mem: V0043Uint64NoValStruct | Unset
        if isinstance(_free_mem, Unset):
            free_mem = UNSET
        else:
            free_mem = V0043Uint64NoValStruct.from_dict(_free_mem)

        cpus = d.pop("cpus", UNSET)

        effective_cpus = d.pop("effective_cpus", UNSET)

        specialized_cpus = d.pop("specialized_cpus", UNSET)

        _energy = d.pop("energy", UNSET)
        energy: V0043AcctGatherEnergy | Unset
        if isinstance(_energy, Unset):
            energy = UNSET
        else:
            energy = V0043AcctGatherEnergy.from_dict(_energy)

        _external_sensors = d.pop("external_sensors", UNSET)
        external_sensors: V0043NodeExternalSensors | Unset
        if isinstance(_external_sensors, Unset):
            external_sensors = UNSET
        else:
            external_sensors = V0043NodeExternalSensors.from_dict(_external_sensors)

        extra = d.pop("extra", UNSET)

        _power = d.pop("power", UNSET)
        power: V0043NodePower | Unset
        if isinstance(_power, Unset):
            power = UNSET
        else:
            power = V0043NodePower.from_dict(_power)

        features = cast(list[str], d.pop("features", UNSET))

        active_features = cast(list[str], d.pop("active_features", UNSET))

        gpu_spec = d.pop("gpu_spec", UNSET)

        gres = d.pop("gres", UNSET)

        gres_drained = d.pop("gres_drained", UNSET)

        gres_used = d.pop("gres_used", UNSET)

        instance_id = d.pop("instance_id", UNSET)

        instance_type = d.pop("instance_type", UNSET)

        _last_busy = d.pop("last_busy", UNSET)
        last_busy: V0043Uint64NoValStruct | Unset
        if isinstance(_last_busy, Unset):
            last_busy = UNSET
        else:
            last_busy = V0043Uint64NoValStruct.from_dict(_last_busy)

        mcs_label = d.pop("mcs_label", UNSET)

        specialized_memory = d.pop("specialized_memory", UNSET)

        name = d.pop("name", UNSET)

        _next_state_after_reboot = d.pop("next_state_after_reboot", UNSET)
        next_state_after_reboot: list[V0043NodeNextStateAfterRebootItem] | Unset = UNSET
        if _next_state_after_reboot is not UNSET:
            next_state_after_reboot = []
            for next_state_after_reboot_item_data in _next_state_after_reboot:
                next_state_after_reboot_item = V0043NodeNextStateAfterRebootItem(next_state_after_reboot_item_data)

                next_state_after_reboot.append(next_state_after_reboot_item)

        address = d.pop("address", UNSET)

        hostname = d.pop("hostname", UNSET)

        _state = d.pop("state", UNSET)
        state: list[V0043NodeStateItem] | Unset = UNSET
        if _state is not UNSET:
            state = []
            for state_item_data in _state:
                state_item = V0043NodeStateItem(state_item_data)

                state.append(state_item)

        operating_system = d.pop("operating_system", UNSET)

        owner = d.pop("owner", UNSET)

        partitions = cast(list[str], d.pop("partitions", UNSET))

        port = d.pop("port", UNSET)

        real_memory = d.pop("real_memory", UNSET)

        res_cores_per_gpu = d.pop("res_cores_per_gpu", UNSET)

        comment = d.pop("comment", UNSET)

        reason = d.pop("reason", UNSET)

        _reason_changed_at = d.pop("reason_changed_at", UNSET)
        reason_changed_at: V0043Uint64NoValStruct | Unset
        if isinstance(_reason_changed_at, Unset):
            reason_changed_at = UNSET
        else:
            reason_changed_at = V0043Uint64NoValStruct.from_dict(_reason_changed_at)

        reason_set_by_user = d.pop("reason_set_by_user", UNSET)

        _resume_after = d.pop("resume_after", UNSET)
        resume_after: V0043Uint64NoValStruct | Unset
        if isinstance(_resume_after, Unset):
            resume_after = UNSET
        else:
            resume_after = V0043Uint64NoValStruct.from_dict(_resume_after)

        reservation = d.pop("reservation", UNSET)

        alloc_memory = d.pop("alloc_memory", UNSET)

        alloc_cpus = d.pop("alloc_cpus", UNSET)

        alloc_idle_cpus = d.pop("alloc_idle_cpus", UNSET)

        tres_used = d.pop("tres_used", UNSET)

        tres_weighted = d.pop("tres_weighted", UNSET)

        _slurmd_start_time = d.pop("slurmd_start_time", UNSET)
        slurmd_start_time: V0043Uint64NoValStruct | Unset
        if isinstance(_slurmd_start_time, Unset):
            slurmd_start_time = UNSET
        else:
            slurmd_start_time = V0043Uint64NoValStruct.from_dict(_slurmd_start_time)

        sockets = d.pop("sockets", UNSET)

        threads = d.pop("threads", UNSET)

        temporary_disk = d.pop("temporary_disk", UNSET)

        weight = d.pop("weight", UNSET)

        topology = d.pop("topology", UNSET)

        tres = d.pop("tres", UNSET)

        version = d.pop("version", UNSET)

        v0043_node = cls(
            architecture=architecture,
            burstbuffer_network_address=burstbuffer_network_address,
            boards=boards,
            boot_time=boot_time,
            tls_cert_last_renewal=tls_cert_last_renewal,
            cert_flags=cert_flags,
            cluster_name=cluster_name,
            cores=cores,
            specialized_cores=specialized_cores,
            cpu_binding=cpu_binding,
            cpu_load=cpu_load,
            free_mem=free_mem,
            cpus=cpus,
            effective_cpus=effective_cpus,
            specialized_cpus=specialized_cpus,
            energy=energy,
            external_sensors=external_sensors,
            extra=extra,
            power=power,
            features=features,
            active_features=active_features,
            gpu_spec=gpu_spec,
            gres=gres,
            gres_drained=gres_drained,
            gres_used=gres_used,
            instance_id=instance_id,
            instance_type=instance_type,
            last_busy=last_busy,
            mcs_label=mcs_label,
            specialized_memory=specialized_memory,
            name=name,
            next_state_after_reboot=next_state_after_reboot,
            address=address,
            hostname=hostname,
            state=state,
            operating_system=operating_system,
            owner=owner,
            partitions=partitions,
            port=port,
            real_memory=real_memory,
            res_cores_per_gpu=res_cores_per_gpu,
            comment=comment,
            reason=reason,
            reason_changed_at=reason_changed_at,
            reason_set_by_user=reason_set_by_user,
            resume_after=resume_after,
            reservation=reservation,
            alloc_memory=alloc_memory,
            alloc_cpus=alloc_cpus,
            alloc_idle_cpus=alloc_idle_cpus,
            tres_used=tres_used,
            tres_weighted=tres_weighted,
            slurmd_start_time=slurmd_start_time,
            sockets=sockets,
            threads=threads,
            temporary_disk=temporary_disk,
            weight=weight,
            topology=topology,
            tres=tres,
            version=version,
        )

        v0043_node.additional_properties = d
        return v0043_node

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
