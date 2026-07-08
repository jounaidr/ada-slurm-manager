from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.slurm_v0041_post_job_body_cpu_binding_flags_item import SlurmV0041PostJobBodyCpuBindingFlagsItem
from ..models.slurm_v0041_post_job_body_exclusive_item import SlurmV0041PostJobBodyExclusiveItem
from ..models.slurm_v0041_post_job_body_flags_item import SlurmV0041PostJobBodyFlagsItem
from ..models.slurm_v0041_post_job_body_kill_warning_flags_item import SlurmV0041PostJobBodyKillWarningFlagsItem
from ..models.slurm_v0041_post_job_body_mail_type_item import SlurmV0041PostJobBodyMailTypeItem
from ..models.slurm_v0041_post_job_body_memory_binding_type_item import SlurmV0041PostJobBodyMemoryBindingTypeItem
from ..models.slurm_v0041_post_job_body_open_mode_item import SlurmV0041PostJobBodyOpenModeItem
from ..models.slurm_v0041_post_job_body_profile_item import SlurmV0041PostJobBodyProfileItem
from ..models.slurm_v0041_post_job_body_shared_item import SlurmV0041PostJobBodySharedItem
from ..models.slurm_v0041_post_job_body_x11_item import SlurmV0041PostJobBodyX11Item
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.slurm_v0041_post_job_body_begin_time import SlurmV0041PostJobBodyBeginTime
    from ..models.slurm_v0041_post_job_body_crontab import SlurmV0041PostJobBodyCrontab
    from ..models.slurm_v0041_post_job_body_distribution_plane_size import SlurmV0041PostJobBodyDistributionPlaneSize
    from ..models.slurm_v0041_post_job_body_kill_warning_delay import SlurmV0041PostJobBodyKillWarningDelay
    from ..models.slurm_v0041_post_job_body_memory_per_cpu import SlurmV0041PostJobBodyMemoryPerCpu
    from ..models.slurm_v0041_post_job_body_memory_per_node import SlurmV0041PostJobBodyMemoryPerNode
    from ..models.slurm_v0041_post_job_body_priority import SlurmV0041PostJobBodyPriority
    from ..models.slurm_v0041_post_job_body_required_switches import SlurmV0041PostJobBodyRequiredSwitches
    from ..models.slurm_v0041_post_job_body_rlimits import SlurmV0041PostJobBodyRlimits
    from ..models.slurm_v0041_post_job_body_segment_size import SlurmV0041PostJobBodySegmentSize
    from ..models.slurm_v0041_post_job_body_time_limit import SlurmV0041PostJobBodyTimeLimit
    from ..models.slurm_v0041_post_job_body_time_minimum import SlurmV0041PostJobBodyTimeMinimum


T = TypeVar("T", bound="SlurmV0041PostJobBody")


@_attrs_define
class SlurmV0041PostJobBody:
    """
    Attributes:
        account (str | Unset): Account associated with the job
        account_gather_frequency (str | Unset): Job accounting and profiling sampling intervals in seconds
        admin_comment (str | Unset): Arbitrary comment made by administrator
        allocation_node_list (str | Unset): Local node making the resource allocation
        allocation_node_port (int | Unset): Port to send allocation confirmation to
        argv (list[str] | Unset): Arguments to the script
        array (str | Unset): Job array index value specification
        batch_features (str | Unset): Features required for batch script's node
        begin_time (SlurmV0041PostJobBodyBeginTime | Unset): Defer the allocation of the job until the specified time
            (UNIX timestamp)
        flags (list[SlurmV0041PostJobBodyFlagsItem] | Unset): Job flags
        burst_buffer (str | Unset): Burst buffer specifications
        clusters (str | Unset): Clusters that a federated job can run on
        cluster_constraint (str | Unset): Required features that a federated cluster must have to have a sibling job
            submitted to it
        comment (str | Unset): Arbitrary comment made by user
        contiguous (bool | Unset): True if job requires contiguous nodes
        container (str | Unset): Absolute path to OCI container bundle
        container_id (str | Unset): OCI container ID
        core_specification (int | Unset): Specialized core count
        thread_specification (int | Unset): Specialized thread count
        cpu_binding (str | Unset): Method for binding tasks to allocated CPUs
        cpu_binding_flags (list[SlurmV0041PostJobBodyCpuBindingFlagsItem] | Unset): Flags for CPU binding
        cpu_frequency (str | Unset): Requested CPU frequency range <p1>[-p2][:p3]
        cpus_per_tres (str | Unset): Semicolon delimited list of TRES=# values values indicating how many CPUs should be
            allocated for each specified TRES (currently only used for gres/gpu)
        crontab (SlurmV0041PostJobBodyCrontab | Unset): Specification for scrontab job
        deadline (int | Unset): Latest time that the job may start (UNIX timestamp)
        delay_boot (int | Unset): Number of seconds after job eligible start that nodes will be rebooted to satisfy
            feature specification
        dependency (str | Unset): Other jobs that must meet certain criteria before this job can start
        end_time (int | Unset): Expected end time (UNIX timestamp)
        environment (list[str] | Unset): Environment variables to be set for the job
        rlimits (SlurmV0041PostJobBodyRlimits | Unset):
        excluded_nodes (list[str] | Unset): Comma separated list of nodes that may not be used
        extra (str | Unset): Arbitrary string used for node filtering if extra constraints are enabled
        constraints (str | Unset): Comma separated list of features that are required
        group_id (str | Unset): Group ID of the user that owns the job
        hetjob_group (int | Unset): Unique sequence number applied to this component of the heterogeneous job
        immediate (bool | Unset): If true, exit if resources are not available within the time period specified
        job_id (int | Unset): Job ID
        kill_on_node_fail (bool | Unset): If true, kill job on node failure
        licenses (str | Unset): License(s) required by the job
        mail_type (list[SlurmV0041PostJobBodyMailTypeItem] | Unset): Mail event type(s)
        mail_user (str | Unset): User to receive email notifications
        mcs_label (str | Unset): Multi-Category Security label on the job
        memory_binding (str | Unset): Binding map for map/mask_cpu
        memory_binding_type (list[SlurmV0041PostJobBodyMemoryBindingTypeItem] | Unset): Method for binding tasks to
            memory
        memory_per_tres (str | Unset): Semicolon delimited list of TRES=# values indicating how much memory in megabytes
            should be allocated for each specified TRES (currently only used for gres/gpu)
        name (str | Unset): Job name
        network (str | Unset): Network specs for job step
        nice (int | Unset): Requested job priority change
        tasks (int | Unset): Number of tasks
        open_mode (list[SlurmV0041PostJobBodyOpenModeItem] | Unset): Open mode used for stdout and stderr files
        reserve_ports (int | Unset): Port to send various notification msg to
        overcommit (bool | Unset): Overcommit resources
        partition (str | Unset): Partition assigned to the job
        distribution_plane_size (SlurmV0041PostJobBodyDistributionPlaneSize | Unset): Plane size specification when
            distribution specifies plane
        power_flags (list[Any] | Unset):
        prefer (str | Unset): Comma separated list of features that are preferred but not required
        hold (bool | Unset): Hold (true) or release (false) job
        priority (SlurmV0041PostJobBodyPriority | Unset): Request specific job priority
        profile (list[SlurmV0041PostJobBodyProfileItem] | Unset): Profile used by the acct_gather_profile plugin
        qos (str | Unset): Quality of Service assigned to the job
        reboot (bool | Unset): Node reboot requested before start
        required_nodes (list[str] | Unset): Comma separated list of required nodes
        requeue (bool | Unset): Determines whether the job may be requeued
        reservation (str | Unset): Name of reservation to use
        resv_mpi_ports (int | Unset): Number of reserved communication ports; can only be used if slurmstepd step
            manager is enabled
        script (str | Unset): Job batch script; only the first component in a HetJob is populated or honored
        shared (list[SlurmV0041PostJobBodySharedItem] | Unset): How the job can share resources with other jobs, if at
            all
        exclusive (list[SlurmV0041PostJobBodyExclusiveItem] | Unset):
        oversubscribe (bool | Unset):
        site_factor (int | Unset): Site-specific priority factor
        spank_environment (list[str] | Unset): Environment variables for job prolog/epilog scripts as set by SPANK
            plugins
        distribution (str | Unset): Layout
        time_limit (SlurmV0041PostJobBodyTimeLimit | Unset): Maximum run time in minutes
        time_minimum (SlurmV0041PostJobBodyTimeMinimum | Unset): Minimum run time in minutes
        tres_bind (str | Unset): Task to TRES binding directives
        tres_freq (str | Unset): TRES frequency directives
        tres_per_job (str | Unset): Comma separated list of TRES=# values to be allocated for every job
        tres_per_node (str | Unset): Comma separated list of TRES=# values to be allocated for every node
        tres_per_socket (str | Unset): Comma separated list of TRES=# values to be allocated for every socket
        tres_per_task (str | Unset): Comma separated list of TRES=# values to be allocated for every task
        user_id (str | Unset): User ID that owns the job
        wait_all_nodes (bool | Unset): If true, wait to start until after all nodes have booted
        kill_warning_flags (list[SlurmV0041PostJobBodyKillWarningFlagsItem] | Unset): Flags related to job signals
        kill_warning_signal (str | Unset): Signal to send when approaching end time (e.g. "10" or "USR1")
        kill_warning_delay (SlurmV0041PostJobBodyKillWarningDelay | Unset): Number of seconds before end time to send
            the warning signal
        current_working_directory (str | Unset): Working directory to use for the job
        cpus_per_task (int | Unset): Number of CPUs required by each task
        minimum_cpus (int | Unset): Minimum number of CPUs required
        maximum_cpus (int | Unset): Maximum number of CPUs required
        nodes (str | Unset): Node count range specification (e.g. 1-15:4)
        minimum_nodes (int | Unset): Minimum node count
        maximum_nodes (int | Unset): Maximum node count
        minimum_boards_per_node (int | Unset): Boards per node required
        minimum_sockets_per_board (int | Unset): Sockets per board required
        sockets_per_node (int | Unset): Sockets per node required
        threads_per_core (int | Unset): Threads per core required
        tasks_per_node (int | Unset): Number of tasks to invoke on each node
        tasks_per_socket (int | Unset): Number of tasks to invoke on each socket
        tasks_per_core (int | Unset): Number of tasks to invoke on each core
        tasks_per_board (int | Unset): Number of tasks to invoke on each board
        ntasks_per_tres (int | Unset): Number of tasks that can access each GPU
        minimum_cpus_per_node (int | Unset): Minimum number of CPUs per node
        memory_per_cpu (SlurmV0041PostJobBodyMemoryPerCpu | Unset): Minimum memory in megabytes per allocated CPU
        memory_per_node (SlurmV0041PostJobBodyMemoryPerNode | Unset): Minimum memory in megabytes per allocated CPU
        temporary_disk_per_node (int | Unset): Minimum tmp disk space required per node
        selinux_context (str | Unset): SELinux context
        required_switches (SlurmV0041PostJobBodyRequiredSwitches | Unset): Maximum number of switches
        segment_size (SlurmV0041PostJobBodySegmentSize | Unset): Segment size for topology/block
        standard_error (str | Unset): Path to stderr file
        standard_input (str | Unset): Path to stdin file
        standard_output (str | Unset): Path to stdout file
        wait_for_switch (int | Unset): Maximum time to wait for switches in seconds
        wckey (str | Unset): Workload characterization key
        x11 (list[SlurmV0041PostJobBodyX11Item] | Unset): X11 forwarding options
        x11_magic_cookie (str | Unset): Magic cookie for X11 forwarding
        x11_target_host (str | Unset): Hostname or UNIX socket if x11_target_port=0
        x11_target_port (int | Unset): TCP port
    """

    account: str | Unset = UNSET
    account_gather_frequency: str | Unset = UNSET
    admin_comment: str | Unset = UNSET
    allocation_node_list: str | Unset = UNSET
    allocation_node_port: int | Unset = UNSET
    argv: list[str] | Unset = UNSET
    array: str | Unset = UNSET
    batch_features: str | Unset = UNSET
    begin_time: SlurmV0041PostJobBodyBeginTime | Unset = UNSET
    flags: list[SlurmV0041PostJobBodyFlagsItem] | Unset = UNSET
    burst_buffer: str | Unset = UNSET
    clusters: str | Unset = UNSET
    cluster_constraint: str | Unset = UNSET
    comment: str | Unset = UNSET
    contiguous: bool | Unset = UNSET
    container: str | Unset = UNSET
    container_id: str | Unset = UNSET
    core_specification: int | Unset = UNSET
    thread_specification: int | Unset = UNSET
    cpu_binding: str | Unset = UNSET
    cpu_binding_flags: list[SlurmV0041PostJobBodyCpuBindingFlagsItem] | Unset = UNSET
    cpu_frequency: str | Unset = UNSET
    cpus_per_tres: str | Unset = UNSET
    crontab: SlurmV0041PostJobBodyCrontab | Unset = UNSET
    deadline: int | Unset = UNSET
    delay_boot: int | Unset = UNSET
    dependency: str | Unset = UNSET
    end_time: int | Unset = UNSET
    environment: list[str] | Unset = UNSET
    rlimits: SlurmV0041PostJobBodyRlimits | Unset = UNSET
    excluded_nodes: list[str] | Unset = UNSET
    extra: str | Unset = UNSET
    constraints: str | Unset = UNSET
    group_id: str | Unset = UNSET
    hetjob_group: int | Unset = UNSET
    immediate: bool | Unset = UNSET
    job_id: int | Unset = UNSET
    kill_on_node_fail: bool | Unset = UNSET
    licenses: str | Unset = UNSET
    mail_type: list[SlurmV0041PostJobBodyMailTypeItem] | Unset = UNSET
    mail_user: str | Unset = UNSET
    mcs_label: str | Unset = UNSET
    memory_binding: str | Unset = UNSET
    memory_binding_type: list[SlurmV0041PostJobBodyMemoryBindingTypeItem] | Unset = UNSET
    memory_per_tres: str | Unset = UNSET
    name: str | Unset = UNSET
    network: str | Unset = UNSET
    nice: int | Unset = UNSET
    tasks: int | Unset = UNSET
    open_mode: list[SlurmV0041PostJobBodyOpenModeItem] | Unset = UNSET
    reserve_ports: int | Unset = UNSET
    overcommit: bool | Unset = UNSET
    partition: str | Unset = UNSET
    distribution_plane_size: SlurmV0041PostJobBodyDistributionPlaneSize | Unset = UNSET
    power_flags: list[Any] | Unset = UNSET
    prefer: str | Unset = UNSET
    hold: bool | Unset = UNSET
    priority: SlurmV0041PostJobBodyPriority | Unset = UNSET
    profile: list[SlurmV0041PostJobBodyProfileItem] | Unset = UNSET
    qos: str | Unset = UNSET
    reboot: bool | Unset = UNSET
    required_nodes: list[str] | Unset = UNSET
    requeue: bool | Unset = UNSET
    reservation: str | Unset = UNSET
    resv_mpi_ports: int | Unset = UNSET
    script: str | Unset = UNSET
    shared: list[SlurmV0041PostJobBodySharedItem] | Unset = UNSET
    exclusive: list[SlurmV0041PostJobBodyExclusiveItem] | Unset = UNSET
    oversubscribe: bool | Unset = UNSET
    site_factor: int | Unset = UNSET
    spank_environment: list[str] | Unset = UNSET
    distribution: str | Unset = UNSET
    time_limit: SlurmV0041PostJobBodyTimeLimit | Unset = UNSET
    time_minimum: SlurmV0041PostJobBodyTimeMinimum | Unset = UNSET
    tres_bind: str | Unset = UNSET
    tres_freq: str | Unset = UNSET
    tres_per_job: str | Unset = UNSET
    tres_per_node: str | Unset = UNSET
    tres_per_socket: str | Unset = UNSET
    tres_per_task: str | Unset = UNSET
    user_id: str | Unset = UNSET
    wait_all_nodes: bool | Unset = UNSET
    kill_warning_flags: list[SlurmV0041PostJobBodyKillWarningFlagsItem] | Unset = UNSET
    kill_warning_signal: str | Unset = UNSET
    kill_warning_delay: SlurmV0041PostJobBodyKillWarningDelay | Unset = UNSET
    current_working_directory: str | Unset = UNSET
    cpus_per_task: int | Unset = UNSET
    minimum_cpus: int | Unset = UNSET
    maximum_cpus: int | Unset = UNSET
    nodes: str | Unset = UNSET
    minimum_nodes: int | Unset = UNSET
    maximum_nodes: int | Unset = UNSET
    minimum_boards_per_node: int | Unset = UNSET
    minimum_sockets_per_board: int | Unset = UNSET
    sockets_per_node: int | Unset = UNSET
    threads_per_core: int | Unset = UNSET
    tasks_per_node: int | Unset = UNSET
    tasks_per_socket: int | Unset = UNSET
    tasks_per_core: int | Unset = UNSET
    tasks_per_board: int | Unset = UNSET
    ntasks_per_tres: int | Unset = UNSET
    minimum_cpus_per_node: int | Unset = UNSET
    memory_per_cpu: SlurmV0041PostJobBodyMemoryPerCpu | Unset = UNSET
    memory_per_node: SlurmV0041PostJobBodyMemoryPerNode | Unset = UNSET
    temporary_disk_per_node: int | Unset = UNSET
    selinux_context: str | Unset = UNSET
    required_switches: SlurmV0041PostJobBodyRequiredSwitches | Unset = UNSET
    segment_size: SlurmV0041PostJobBodySegmentSize | Unset = UNSET
    standard_error: str | Unset = UNSET
    standard_input: str | Unset = UNSET
    standard_output: str | Unset = UNSET
    wait_for_switch: int | Unset = UNSET
    wckey: str | Unset = UNSET
    x11: list[SlurmV0041PostJobBodyX11Item] | Unset = UNSET
    x11_magic_cookie: str | Unset = UNSET
    x11_target_host: str | Unset = UNSET
    x11_target_port: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account = self.account

        account_gather_frequency = self.account_gather_frequency

        admin_comment = self.admin_comment

        allocation_node_list = self.allocation_node_list

        allocation_node_port = self.allocation_node_port

        argv: list[str] | Unset = UNSET
        if not isinstance(self.argv, Unset):
            argv = self.argv

        array = self.array

        batch_features = self.batch_features

        begin_time: dict[str, Any] | Unset = UNSET
        if not isinstance(self.begin_time, Unset):
            begin_time = self.begin_time.to_dict()

        flags: list[str] | Unset = UNSET
        if not isinstance(self.flags, Unset):
            flags = []
            for flags_item_data in self.flags:
                flags_item = flags_item_data.value
                flags.append(flags_item)

        burst_buffer = self.burst_buffer

        clusters = self.clusters

        cluster_constraint = self.cluster_constraint

        comment = self.comment

        contiguous = self.contiguous

        container = self.container

        container_id = self.container_id

        core_specification = self.core_specification

        thread_specification = self.thread_specification

        cpu_binding = self.cpu_binding

        cpu_binding_flags: list[str] | Unset = UNSET
        if not isinstance(self.cpu_binding_flags, Unset):
            cpu_binding_flags = []
            for cpu_binding_flags_item_data in self.cpu_binding_flags:
                cpu_binding_flags_item = cpu_binding_flags_item_data.value
                cpu_binding_flags.append(cpu_binding_flags_item)

        cpu_frequency = self.cpu_frequency

        cpus_per_tres = self.cpus_per_tres

        crontab: dict[str, Any] | Unset = UNSET
        if not isinstance(self.crontab, Unset):
            crontab = self.crontab.to_dict()

        deadline = self.deadline

        delay_boot = self.delay_boot

        dependency = self.dependency

        end_time = self.end_time

        environment: list[str] | Unset = UNSET
        if not isinstance(self.environment, Unset):
            environment = self.environment

        rlimits: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rlimits, Unset):
            rlimits = self.rlimits.to_dict()

        excluded_nodes: list[str] | Unset = UNSET
        if not isinstance(self.excluded_nodes, Unset):
            excluded_nodes = self.excluded_nodes

        extra = self.extra

        constraints = self.constraints

        group_id = self.group_id

        hetjob_group = self.hetjob_group

        immediate = self.immediate

        job_id = self.job_id

        kill_on_node_fail = self.kill_on_node_fail

        licenses = self.licenses

        mail_type: list[str] | Unset = UNSET
        if not isinstance(self.mail_type, Unset):
            mail_type = []
            for mail_type_item_data in self.mail_type:
                mail_type_item = mail_type_item_data.value
                mail_type.append(mail_type_item)

        mail_user = self.mail_user

        mcs_label = self.mcs_label

        memory_binding = self.memory_binding

        memory_binding_type: list[str] | Unset = UNSET
        if not isinstance(self.memory_binding_type, Unset):
            memory_binding_type = []
            for memory_binding_type_item_data in self.memory_binding_type:
                memory_binding_type_item = memory_binding_type_item_data.value
                memory_binding_type.append(memory_binding_type_item)

        memory_per_tres = self.memory_per_tres

        name = self.name

        network = self.network

        nice = self.nice

        tasks = self.tasks

        open_mode: list[str] | Unset = UNSET
        if not isinstance(self.open_mode, Unset):
            open_mode = []
            for open_mode_item_data in self.open_mode:
                open_mode_item = open_mode_item_data.value
                open_mode.append(open_mode_item)

        reserve_ports = self.reserve_ports

        overcommit = self.overcommit

        partition = self.partition

        distribution_plane_size: dict[str, Any] | Unset = UNSET
        if not isinstance(self.distribution_plane_size, Unset):
            distribution_plane_size = self.distribution_plane_size.to_dict()

        power_flags: list[Any] | Unset = UNSET
        if not isinstance(self.power_flags, Unset):
            power_flags = self.power_flags

        prefer = self.prefer

        hold = self.hold

        priority: dict[str, Any] | Unset = UNSET
        if not isinstance(self.priority, Unset):
            priority = self.priority.to_dict()

        profile: list[str] | Unset = UNSET
        if not isinstance(self.profile, Unset):
            profile = []
            for profile_item_data in self.profile:
                profile_item = profile_item_data.value
                profile.append(profile_item)

        qos = self.qos

        reboot = self.reboot

        required_nodes: list[str] | Unset = UNSET
        if not isinstance(self.required_nodes, Unset):
            required_nodes = self.required_nodes

        requeue = self.requeue

        reservation = self.reservation

        resv_mpi_ports = self.resv_mpi_ports

        script = self.script

        shared: list[str] | Unset = UNSET
        if not isinstance(self.shared, Unset):
            shared = []
            for shared_item_data in self.shared:
                shared_item = shared_item_data.value
                shared.append(shared_item)

        exclusive: list[str] | Unset = UNSET
        if not isinstance(self.exclusive, Unset):
            exclusive = []
            for exclusive_item_data in self.exclusive:
                exclusive_item = exclusive_item_data.value
                exclusive.append(exclusive_item)

        oversubscribe = self.oversubscribe

        site_factor = self.site_factor

        spank_environment: list[str] | Unset = UNSET
        if not isinstance(self.spank_environment, Unset):
            spank_environment = self.spank_environment

        distribution = self.distribution

        time_limit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.time_limit, Unset):
            time_limit = self.time_limit.to_dict()

        time_minimum: dict[str, Any] | Unset = UNSET
        if not isinstance(self.time_minimum, Unset):
            time_minimum = self.time_minimum.to_dict()

        tres_bind = self.tres_bind

        tres_freq = self.tres_freq

        tres_per_job = self.tres_per_job

        tres_per_node = self.tres_per_node

        tres_per_socket = self.tres_per_socket

        tres_per_task = self.tres_per_task

        user_id = self.user_id

        wait_all_nodes = self.wait_all_nodes

        kill_warning_flags: list[str] | Unset = UNSET
        if not isinstance(self.kill_warning_flags, Unset):
            kill_warning_flags = []
            for kill_warning_flags_item_data in self.kill_warning_flags:
                kill_warning_flags_item = kill_warning_flags_item_data.value
                kill_warning_flags.append(kill_warning_flags_item)

        kill_warning_signal = self.kill_warning_signal

        kill_warning_delay: dict[str, Any] | Unset = UNSET
        if not isinstance(self.kill_warning_delay, Unset):
            kill_warning_delay = self.kill_warning_delay.to_dict()

        current_working_directory = self.current_working_directory

        cpus_per_task = self.cpus_per_task

        minimum_cpus = self.minimum_cpus

        maximum_cpus = self.maximum_cpus

        nodes = self.nodes

        minimum_nodes = self.minimum_nodes

        maximum_nodes = self.maximum_nodes

        minimum_boards_per_node = self.minimum_boards_per_node

        minimum_sockets_per_board = self.minimum_sockets_per_board

        sockets_per_node = self.sockets_per_node

        threads_per_core = self.threads_per_core

        tasks_per_node = self.tasks_per_node

        tasks_per_socket = self.tasks_per_socket

        tasks_per_core = self.tasks_per_core

        tasks_per_board = self.tasks_per_board

        ntasks_per_tres = self.ntasks_per_tres

        minimum_cpus_per_node = self.minimum_cpus_per_node

        memory_per_cpu: dict[str, Any] | Unset = UNSET
        if not isinstance(self.memory_per_cpu, Unset):
            memory_per_cpu = self.memory_per_cpu.to_dict()

        memory_per_node: dict[str, Any] | Unset = UNSET
        if not isinstance(self.memory_per_node, Unset):
            memory_per_node = self.memory_per_node.to_dict()

        temporary_disk_per_node = self.temporary_disk_per_node

        selinux_context = self.selinux_context

        required_switches: dict[str, Any] | Unset = UNSET
        if not isinstance(self.required_switches, Unset):
            required_switches = self.required_switches.to_dict()

        segment_size: dict[str, Any] | Unset = UNSET
        if not isinstance(self.segment_size, Unset):
            segment_size = self.segment_size.to_dict()

        standard_error = self.standard_error

        standard_input = self.standard_input

        standard_output = self.standard_output

        wait_for_switch = self.wait_for_switch

        wckey = self.wckey

        x11: list[str] | Unset = UNSET
        if not isinstance(self.x11, Unset):
            x11 = []
            for x11_item_data in self.x11:
                x11_item = x11_item_data.value
                x11.append(x11_item)

        x11_magic_cookie = self.x11_magic_cookie

        x11_target_host = self.x11_target_host

        x11_target_port = self.x11_target_port

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account is not UNSET:
            field_dict["account"] = account
        if account_gather_frequency is not UNSET:
            field_dict["account_gather_frequency"] = account_gather_frequency
        if admin_comment is not UNSET:
            field_dict["admin_comment"] = admin_comment
        if allocation_node_list is not UNSET:
            field_dict["allocation_node_list"] = allocation_node_list
        if allocation_node_port is not UNSET:
            field_dict["allocation_node_port"] = allocation_node_port
        if argv is not UNSET:
            field_dict["argv"] = argv
        if array is not UNSET:
            field_dict["array"] = array
        if batch_features is not UNSET:
            field_dict["batch_features"] = batch_features
        if begin_time is not UNSET:
            field_dict["begin_time"] = begin_time
        if flags is not UNSET:
            field_dict["flags"] = flags
        if burst_buffer is not UNSET:
            field_dict["burst_buffer"] = burst_buffer
        if clusters is not UNSET:
            field_dict["clusters"] = clusters
        if cluster_constraint is not UNSET:
            field_dict["cluster_constraint"] = cluster_constraint
        if comment is not UNSET:
            field_dict["comment"] = comment
        if contiguous is not UNSET:
            field_dict["contiguous"] = contiguous
        if container is not UNSET:
            field_dict["container"] = container
        if container_id is not UNSET:
            field_dict["container_id"] = container_id
        if core_specification is not UNSET:
            field_dict["core_specification"] = core_specification
        if thread_specification is not UNSET:
            field_dict["thread_specification"] = thread_specification
        if cpu_binding is not UNSET:
            field_dict["cpu_binding"] = cpu_binding
        if cpu_binding_flags is not UNSET:
            field_dict["cpu_binding_flags"] = cpu_binding_flags
        if cpu_frequency is not UNSET:
            field_dict["cpu_frequency"] = cpu_frequency
        if cpus_per_tres is not UNSET:
            field_dict["cpus_per_tres"] = cpus_per_tres
        if crontab is not UNSET:
            field_dict["crontab"] = crontab
        if deadline is not UNSET:
            field_dict["deadline"] = deadline
        if delay_boot is not UNSET:
            field_dict["delay_boot"] = delay_boot
        if dependency is not UNSET:
            field_dict["dependency"] = dependency
        if end_time is not UNSET:
            field_dict["end_time"] = end_time
        if environment is not UNSET:
            field_dict["environment"] = environment
        if rlimits is not UNSET:
            field_dict["rlimits"] = rlimits
        if excluded_nodes is not UNSET:
            field_dict["excluded_nodes"] = excluded_nodes
        if extra is not UNSET:
            field_dict["extra"] = extra
        if constraints is not UNSET:
            field_dict["constraints"] = constraints
        if group_id is not UNSET:
            field_dict["group_id"] = group_id
        if hetjob_group is not UNSET:
            field_dict["hetjob_group"] = hetjob_group
        if immediate is not UNSET:
            field_dict["immediate"] = immediate
        if job_id is not UNSET:
            field_dict["job_id"] = job_id
        if kill_on_node_fail is not UNSET:
            field_dict["kill_on_node_fail"] = kill_on_node_fail
        if licenses is not UNSET:
            field_dict["licenses"] = licenses
        if mail_type is not UNSET:
            field_dict["mail_type"] = mail_type
        if mail_user is not UNSET:
            field_dict["mail_user"] = mail_user
        if mcs_label is not UNSET:
            field_dict["mcs_label"] = mcs_label
        if memory_binding is not UNSET:
            field_dict["memory_binding"] = memory_binding
        if memory_binding_type is not UNSET:
            field_dict["memory_binding_type"] = memory_binding_type
        if memory_per_tres is not UNSET:
            field_dict["memory_per_tres"] = memory_per_tres
        if name is not UNSET:
            field_dict["name"] = name
        if network is not UNSET:
            field_dict["network"] = network
        if nice is not UNSET:
            field_dict["nice"] = nice
        if tasks is not UNSET:
            field_dict["tasks"] = tasks
        if open_mode is not UNSET:
            field_dict["open_mode"] = open_mode
        if reserve_ports is not UNSET:
            field_dict["reserve_ports"] = reserve_ports
        if overcommit is not UNSET:
            field_dict["overcommit"] = overcommit
        if partition is not UNSET:
            field_dict["partition"] = partition
        if distribution_plane_size is not UNSET:
            field_dict["distribution_plane_size"] = distribution_plane_size
        if power_flags is not UNSET:
            field_dict["power_flags"] = power_flags
        if prefer is not UNSET:
            field_dict["prefer"] = prefer
        if hold is not UNSET:
            field_dict["hold"] = hold
        if priority is not UNSET:
            field_dict["priority"] = priority
        if profile is not UNSET:
            field_dict["profile"] = profile
        if qos is not UNSET:
            field_dict["qos"] = qos
        if reboot is not UNSET:
            field_dict["reboot"] = reboot
        if required_nodes is not UNSET:
            field_dict["required_nodes"] = required_nodes
        if requeue is not UNSET:
            field_dict["requeue"] = requeue
        if reservation is not UNSET:
            field_dict["reservation"] = reservation
        if resv_mpi_ports is not UNSET:
            field_dict["resv_mpi_ports"] = resv_mpi_ports
        if script is not UNSET:
            field_dict["script"] = script
        if shared is not UNSET:
            field_dict["shared"] = shared
        if exclusive is not UNSET:
            field_dict["exclusive"] = exclusive
        if oversubscribe is not UNSET:
            field_dict["oversubscribe"] = oversubscribe
        if site_factor is not UNSET:
            field_dict["site_factor"] = site_factor
        if spank_environment is not UNSET:
            field_dict["spank_environment"] = spank_environment
        if distribution is not UNSET:
            field_dict["distribution"] = distribution
        if time_limit is not UNSET:
            field_dict["time_limit"] = time_limit
        if time_minimum is not UNSET:
            field_dict["time_minimum"] = time_minimum
        if tres_bind is not UNSET:
            field_dict["tres_bind"] = tres_bind
        if tres_freq is not UNSET:
            field_dict["tres_freq"] = tres_freq
        if tres_per_job is not UNSET:
            field_dict["tres_per_job"] = tres_per_job
        if tres_per_node is not UNSET:
            field_dict["tres_per_node"] = tres_per_node
        if tres_per_socket is not UNSET:
            field_dict["tres_per_socket"] = tres_per_socket
        if tres_per_task is not UNSET:
            field_dict["tres_per_task"] = tres_per_task
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if wait_all_nodes is not UNSET:
            field_dict["wait_all_nodes"] = wait_all_nodes
        if kill_warning_flags is not UNSET:
            field_dict["kill_warning_flags"] = kill_warning_flags
        if kill_warning_signal is not UNSET:
            field_dict["kill_warning_signal"] = kill_warning_signal
        if kill_warning_delay is not UNSET:
            field_dict["kill_warning_delay"] = kill_warning_delay
        if current_working_directory is not UNSET:
            field_dict["current_working_directory"] = current_working_directory
        if cpus_per_task is not UNSET:
            field_dict["cpus_per_task"] = cpus_per_task
        if minimum_cpus is not UNSET:
            field_dict["minimum_cpus"] = minimum_cpus
        if maximum_cpus is not UNSET:
            field_dict["maximum_cpus"] = maximum_cpus
        if nodes is not UNSET:
            field_dict["nodes"] = nodes
        if minimum_nodes is not UNSET:
            field_dict["minimum_nodes"] = minimum_nodes
        if maximum_nodes is not UNSET:
            field_dict["maximum_nodes"] = maximum_nodes
        if minimum_boards_per_node is not UNSET:
            field_dict["minimum_boards_per_node"] = minimum_boards_per_node
        if minimum_sockets_per_board is not UNSET:
            field_dict["minimum_sockets_per_board"] = minimum_sockets_per_board
        if sockets_per_node is not UNSET:
            field_dict["sockets_per_node"] = sockets_per_node
        if threads_per_core is not UNSET:
            field_dict["threads_per_core"] = threads_per_core
        if tasks_per_node is not UNSET:
            field_dict["tasks_per_node"] = tasks_per_node
        if tasks_per_socket is not UNSET:
            field_dict["tasks_per_socket"] = tasks_per_socket
        if tasks_per_core is not UNSET:
            field_dict["tasks_per_core"] = tasks_per_core
        if tasks_per_board is not UNSET:
            field_dict["tasks_per_board"] = tasks_per_board
        if ntasks_per_tres is not UNSET:
            field_dict["ntasks_per_tres"] = ntasks_per_tres
        if minimum_cpus_per_node is not UNSET:
            field_dict["minimum_cpus_per_node"] = minimum_cpus_per_node
        if memory_per_cpu is not UNSET:
            field_dict["memory_per_cpu"] = memory_per_cpu
        if memory_per_node is not UNSET:
            field_dict["memory_per_node"] = memory_per_node
        if temporary_disk_per_node is not UNSET:
            field_dict["temporary_disk_per_node"] = temporary_disk_per_node
        if selinux_context is not UNSET:
            field_dict["selinux_context"] = selinux_context
        if required_switches is not UNSET:
            field_dict["required_switches"] = required_switches
        if segment_size is not UNSET:
            field_dict["segment_size"] = segment_size
        if standard_error is not UNSET:
            field_dict["standard_error"] = standard_error
        if standard_input is not UNSET:
            field_dict["standard_input"] = standard_input
        if standard_output is not UNSET:
            field_dict["standard_output"] = standard_output
        if wait_for_switch is not UNSET:
            field_dict["wait_for_switch"] = wait_for_switch
        if wckey is not UNSET:
            field_dict["wckey"] = wckey
        if x11 is not UNSET:
            field_dict["x11"] = x11
        if x11_magic_cookie is not UNSET:
            field_dict["x11_magic_cookie"] = x11_magic_cookie
        if x11_target_host is not UNSET:
            field_dict["x11_target_host"] = x11_target_host
        if x11_target_port is not UNSET:
            field_dict["x11_target_port"] = x11_target_port

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.slurm_v0041_post_job_body_begin_time import SlurmV0041PostJobBodyBeginTime
        from ..models.slurm_v0041_post_job_body_crontab import SlurmV0041PostJobBodyCrontab
        from ..models.slurm_v0041_post_job_body_distribution_plane_size import (
            SlurmV0041PostJobBodyDistributionPlaneSize,
        )
        from ..models.slurm_v0041_post_job_body_kill_warning_delay import SlurmV0041PostJobBodyKillWarningDelay
        from ..models.slurm_v0041_post_job_body_memory_per_cpu import SlurmV0041PostJobBodyMemoryPerCpu
        from ..models.slurm_v0041_post_job_body_memory_per_node import SlurmV0041PostJobBodyMemoryPerNode
        from ..models.slurm_v0041_post_job_body_priority import SlurmV0041PostJobBodyPriority
        from ..models.slurm_v0041_post_job_body_required_switches import SlurmV0041PostJobBodyRequiredSwitches
        from ..models.slurm_v0041_post_job_body_rlimits import SlurmV0041PostJobBodyRlimits
        from ..models.slurm_v0041_post_job_body_segment_size import SlurmV0041PostJobBodySegmentSize
        from ..models.slurm_v0041_post_job_body_time_limit import SlurmV0041PostJobBodyTimeLimit
        from ..models.slurm_v0041_post_job_body_time_minimum import SlurmV0041PostJobBodyTimeMinimum

        d = dict(src_dict)
        account = d.pop("account", UNSET)

        account_gather_frequency = d.pop("account_gather_frequency", UNSET)

        admin_comment = d.pop("admin_comment", UNSET)

        allocation_node_list = d.pop("allocation_node_list", UNSET)

        allocation_node_port = d.pop("allocation_node_port", UNSET)

        argv = cast(list[str], d.pop("argv", UNSET))

        array = d.pop("array", UNSET)

        batch_features = d.pop("batch_features", UNSET)

        _begin_time = d.pop("begin_time", UNSET)
        begin_time: SlurmV0041PostJobBodyBeginTime | Unset
        if isinstance(_begin_time, Unset):
            begin_time = UNSET
        else:
            begin_time = SlurmV0041PostJobBodyBeginTime.from_dict(_begin_time)

        _flags = d.pop("flags", UNSET)
        flags: list[SlurmV0041PostJobBodyFlagsItem] | Unset = UNSET
        if _flags is not UNSET:
            flags = []
            for flags_item_data in _flags:
                flags_item = SlurmV0041PostJobBodyFlagsItem(flags_item_data)

                flags.append(flags_item)

        burst_buffer = d.pop("burst_buffer", UNSET)

        clusters = d.pop("clusters", UNSET)

        cluster_constraint = d.pop("cluster_constraint", UNSET)

        comment = d.pop("comment", UNSET)

        contiguous = d.pop("contiguous", UNSET)

        container = d.pop("container", UNSET)

        container_id = d.pop("container_id", UNSET)

        core_specification = d.pop("core_specification", UNSET)

        thread_specification = d.pop("thread_specification", UNSET)

        cpu_binding = d.pop("cpu_binding", UNSET)

        _cpu_binding_flags = d.pop("cpu_binding_flags", UNSET)
        cpu_binding_flags: list[SlurmV0041PostJobBodyCpuBindingFlagsItem] | Unset = UNSET
        if _cpu_binding_flags is not UNSET:
            cpu_binding_flags = []
            for cpu_binding_flags_item_data in _cpu_binding_flags:
                cpu_binding_flags_item = SlurmV0041PostJobBodyCpuBindingFlagsItem(cpu_binding_flags_item_data)

                cpu_binding_flags.append(cpu_binding_flags_item)

        cpu_frequency = d.pop("cpu_frequency", UNSET)

        cpus_per_tres = d.pop("cpus_per_tres", UNSET)

        _crontab = d.pop("crontab", UNSET)
        crontab: SlurmV0041PostJobBodyCrontab | Unset
        if isinstance(_crontab, Unset):
            crontab = UNSET
        else:
            crontab = SlurmV0041PostJobBodyCrontab.from_dict(_crontab)

        deadline = d.pop("deadline", UNSET)

        delay_boot = d.pop("delay_boot", UNSET)

        dependency = d.pop("dependency", UNSET)

        end_time = d.pop("end_time", UNSET)

        environment = cast(list[str], d.pop("environment", UNSET))

        _rlimits = d.pop("rlimits", UNSET)
        rlimits: SlurmV0041PostJobBodyRlimits | Unset
        if isinstance(_rlimits, Unset):
            rlimits = UNSET
        else:
            rlimits = SlurmV0041PostJobBodyRlimits.from_dict(_rlimits)

        excluded_nodes = cast(list[str], d.pop("excluded_nodes", UNSET))

        extra = d.pop("extra", UNSET)

        constraints = d.pop("constraints", UNSET)

        group_id = d.pop("group_id", UNSET)

        hetjob_group = d.pop("hetjob_group", UNSET)

        immediate = d.pop("immediate", UNSET)

        job_id = d.pop("job_id", UNSET)

        kill_on_node_fail = d.pop("kill_on_node_fail", UNSET)

        licenses = d.pop("licenses", UNSET)

        _mail_type = d.pop("mail_type", UNSET)
        mail_type: list[SlurmV0041PostJobBodyMailTypeItem] | Unset = UNSET
        if _mail_type is not UNSET:
            mail_type = []
            for mail_type_item_data in _mail_type:
                mail_type_item = SlurmV0041PostJobBodyMailTypeItem(mail_type_item_data)

                mail_type.append(mail_type_item)

        mail_user = d.pop("mail_user", UNSET)

        mcs_label = d.pop("mcs_label", UNSET)

        memory_binding = d.pop("memory_binding", UNSET)

        _memory_binding_type = d.pop("memory_binding_type", UNSET)
        memory_binding_type: list[SlurmV0041PostJobBodyMemoryBindingTypeItem] | Unset = UNSET
        if _memory_binding_type is not UNSET:
            memory_binding_type = []
            for memory_binding_type_item_data in _memory_binding_type:
                memory_binding_type_item = SlurmV0041PostJobBodyMemoryBindingTypeItem(memory_binding_type_item_data)

                memory_binding_type.append(memory_binding_type_item)

        memory_per_tres = d.pop("memory_per_tres", UNSET)

        name = d.pop("name", UNSET)

        network = d.pop("network", UNSET)

        nice = d.pop("nice", UNSET)

        tasks = d.pop("tasks", UNSET)

        _open_mode = d.pop("open_mode", UNSET)
        open_mode: list[SlurmV0041PostJobBodyOpenModeItem] | Unset = UNSET
        if _open_mode is not UNSET:
            open_mode = []
            for open_mode_item_data in _open_mode:
                open_mode_item = SlurmV0041PostJobBodyOpenModeItem(open_mode_item_data)

                open_mode.append(open_mode_item)

        reserve_ports = d.pop("reserve_ports", UNSET)

        overcommit = d.pop("overcommit", UNSET)

        partition = d.pop("partition", UNSET)

        _distribution_plane_size = d.pop("distribution_plane_size", UNSET)
        distribution_plane_size: SlurmV0041PostJobBodyDistributionPlaneSize | Unset
        if isinstance(_distribution_plane_size, Unset):
            distribution_plane_size = UNSET
        else:
            distribution_plane_size = SlurmV0041PostJobBodyDistributionPlaneSize.from_dict(_distribution_plane_size)

        power_flags = cast(list[Any], d.pop("power_flags", UNSET))

        prefer = d.pop("prefer", UNSET)

        hold = d.pop("hold", UNSET)

        _priority = d.pop("priority", UNSET)
        priority: SlurmV0041PostJobBodyPriority | Unset
        if isinstance(_priority, Unset):
            priority = UNSET
        else:
            priority = SlurmV0041PostJobBodyPriority.from_dict(_priority)

        _profile = d.pop("profile", UNSET)
        profile: list[SlurmV0041PostJobBodyProfileItem] | Unset = UNSET
        if _profile is not UNSET:
            profile = []
            for profile_item_data in _profile:
                profile_item = SlurmV0041PostJobBodyProfileItem(profile_item_data)

                profile.append(profile_item)

        qos = d.pop("qos", UNSET)

        reboot = d.pop("reboot", UNSET)

        required_nodes = cast(list[str], d.pop("required_nodes", UNSET))

        requeue = d.pop("requeue", UNSET)

        reservation = d.pop("reservation", UNSET)

        resv_mpi_ports = d.pop("resv_mpi_ports", UNSET)

        script = d.pop("script", UNSET)

        _shared = d.pop("shared", UNSET)
        shared: list[SlurmV0041PostJobBodySharedItem] | Unset = UNSET
        if _shared is not UNSET:
            shared = []
            for shared_item_data in _shared:
                shared_item = SlurmV0041PostJobBodySharedItem(shared_item_data)

                shared.append(shared_item)

        _exclusive = d.pop("exclusive", UNSET)
        exclusive: list[SlurmV0041PostJobBodyExclusiveItem] | Unset = UNSET
        if _exclusive is not UNSET:
            exclusive = []
            for exclusive_item_data in _exclusive:
                exclusive_item = SlurmV0041PostJobBodyExclusiveItem(exclusive_item_data)

                exclusive.append(exclusive_item)

        oversubscribe = d.pop("oversubscribe", UNSET)

        site_factor = d.pop("site_factor", UNSET)

        spank_environment = cast(list[str], d.pop("spank_environment", UNSET))

        distribution = d.pop("distribution", UNSET)

        _time_limit = d.pop("time_limit", UNSET)
        time_limit: SlurmV0041PostJobBodyTimeLimit | Unset
        if isinstance(_time_limit, Unset):
            time_limit = UNSET
        else:
            time_limit = SlurmV0041PostJobBodyTimeLimit.from_dict(_time_limit)

        _time_minimum = d.pop("time_minimum", UNSET)
        time_minimum: SlurmV0041PostJobBodyTimeMinimum | Unset
        if isinstance(_time_minimum, Unset):
            time_minimum = UNSET
        else:
            time_minimum = SlurmV0041PostJobBodyTimeMinimum.from_dict(_time_minimum)

        tres_bind = d.pop("tres_bind", UNSET)

        tres_freq = d.pop("tres_freq", UNSET)

        tres_per_job = d.pop("tres_per_job", UNSET)

        tres_per_node = d.pop("tres_per_node", UNSET)

        tres_per_socket = d.pop("tres_per_socket", UNSET)

        tres_per_task = d.pop("tres_per_task", UNSET)

        user_id = d.pop("user_id", UNSET)

        wait_all_nodes = d.pop("wait_all_nodes", UNSET)

        _kill_warning_flags = d.pop("kill_warning_flags", UNSET)
        kill_warning_flags: list[SlurmV0041PostJobBodyKillWarningFlagsItem] | Unset = UNSET
        if _kill_warning_flags is not UNSET:
            kill_warning_flags = []
            for kill_warning_flags_item_data in _kill_warning_flags:
                kill_warning_flags_item = SlurmV0041PostJobBodyKillWarningFlagsItem(kill_warning_flags_item_data)

                kill_warning_flags.append(kill_warning_flags_item)

        kill_warning_signal = d.pop("kill_warning_signal", UNSET)

        _kill_warning_delay = d.pop("kill_warning_delay", UNSET)
        kill_warning_delay: SlurmV0041PostJobBodyKillWarningDelay | Unset
        if isinstance(_kill_warning_delay, Unset):
            kill_warning_delay = UNSET
        else:
            kill_warning_delay = SlurmV0041PostJobBodyKillWarningDelay.from_dict(_kill_warning_delay)

        current_working_directory = d.pop("current_working_directory", UNSET)

        cpus_per_task = d.pop("cpus_per_task", UNSET)

        minimum_cpus = d.pop("minimum_cpus", UNSET)

        maximum_cpus = d.pop("maximum_cpus", UNSET)

        nodes = d.pop("nodes", UNSET)

        minimum_nodes = d.pop("minimum_nodes", UNSET)

        maximum_nodes = d.pop("maximum_nodes", UNSET)

        minimum_boards_per_node = d.pop("minimum_boards_per_node", UNSET)

        minimum_sockets_per_board = d.pop("minimum_sockets_per_board", UNSET)

        sockets_per_node = d.pop("sockets_per_node", UNSET)

        threads_per_core = d.pop("threads_per_core", UNSET)

        tasks_per_node = d.pop("tasks_per_node", UNSET)

        tasks_per_socket = d.pop("tasks_per_socket", UNSET)

        tasks_per_core = d.pop("tasks_per_core", UNSET)

        tasks_per_board = d.pop("tasks_per_board", UNSET)

        ntasks_per_tres = d.pop("ntasks_per_tres", UNSET)

        minimum_cpus_per_node = d.pop("minimum_cpus_per_node", UNSET)

        _memory_per_cpu = d.pop("memory_per_cpu", UNSET)
        memory_per_cpu: SlurmV0041PostJobBodyMemoryPerCpu | Unset
        if isinstance(_memory_per_cpu, Unset):
            memory_per_cpu = UNSET
        else:
            memory_per_cpu = SlurmV0041PostJobBodyMemoryPerCpu.from_dict(_memory_per_cpu)

        _memory_per_node = d.pop("memory_per_node", UNSET)
        memory_per_node: SlurmV0041PostJobBodyMemoryPerNode | Unset
        if isinstance(_memory_per_node, Unset):
            memory_per_node = UNSET
        else:
            memory_per_node = SlurmV0041PostJobBodyMemoryPerNode.from_dict(_memory_per_node)

        temporary_disk_per_node = d.pop("temporary_disk_per_node", UNSET)

        selinux_context = d.pop("selinux_context", UNSET)

        _required_switches = d.pop("required_switches", UNSET)
        required_switches: SlurmV0041PostJobBodyRequiredSwitches | Unset
        if isinstance(_required_switches, Unset):
            required_switches = UNSET
        else:
            required_switches = SlurmV0041PostJobBodyRequiredSwitches.from_dict(_required_switches)

        _segment_size = d.pop("segment_size", UNSET)
        segment_size: SlurmV0041PostJobBodySegmentSize | Unset
        if isinstance(_segment_size, Unset):
            segment_size = UNSET
        else:
            segment_size = SlurmV0041PostJobBodySegmentSize.from_dict(_segment_size)

        standard_error = d.pop("standard_error", UNSET)

        standard_input = d.pop("standard_input", UNSET)

        standard_output = d.pop("standard_output", UNSET)

        wait_for_switch = d.pop("wait_for_switch", UNSET)

        wckey = d.pop("wckey", UNSET)

        _x11 = d.pop("x11", UNSET)
        x11: list[SlurmV0041PostJobBodyX11Item] | Unset = UNSET
        if _x11 is not UNSET:
            x11 = []
            for x11_item_data in _x11:
                x11_item = SlurmV0041PostJobBodyX11Item(x11_item_data)

                x11.append(x11_item)

        x11_magic_cookie = d.pop("x11_magic_cookie", UNSET)

        x11_target_host = d.pop("x11_target_host", UNSET)

        x11_target_port = d.pop("x11_target_port", UNSET)

        slurm_v0041_post_job_body = cls(
            account=account,
            account_gather_frequency=account_gather_frequency,
            admin_comment=admin_comment,
            allocation_node_list=allocation_node_list,
            allocation_node_port=allocation_node_port,
            argv=argv,
            array=array,
            batch_features=batch_features,
            begin_time=begin_time,
            flags=flags,
            burst_buffer=burst_buffer,
            clusters=clusters,
            cluster_constraint=cluster_constraint,
            comment=comment,
            contiguous=contiguous,
            container=container,
            container_id=container_id,
            core_specification=core_specification,
            thread_specification=thread_specification,
            cpu_binding=cpu_binding,
            cpu_binding_flags=cpu_binding_flags,
            cpu_frequency=cpu_frequency,
            cpus_per_tres=cpus_per_tres,
            crontab=crontab,
            deadline=deadline,
            delay_boot=delay_boot,
            dependency=dependency,
            end_time=end_time,
            environment=environment,
            rlimits=rlimits,
            excluded_nodes=excluded_nodes,
            extra=extra,
            constraints=constraints,
            group_id=group_id,
            hetjob_group=hetjob_group,
            immediate=immediate,
            job_id=job_id,
            kill_on_node_fail=kill_on_node_fail,
            licenses=licenses,
            mail_type=mail_type,
            mail_user=mail_user,
            mcs_label=mcs_label,
            memory_binding=memory_binding,
            memory_binding_type=memory_binding_type,
            memory_per_tres=memory_per_tres,
            name=name,
            network=network,
            nice=nice,
            tasks=tasks,
            open_mode=open_mode,
            reserve_ports=reserve_ports,
            overcommit=overcommit,
            partition=partition,
            distribution_plane_size=distribution_plane_size,
            power_flags=power_flags,
            prefer=prefer,
            hold=hold,
            priority=priority,
            profile=profile,
            qos=qos,
            reboot=reboot,
            required_nodes=required_nodes,
            requeue=requeue,
            reservation=reservation,
            resv_mpi_ports=resv_mpi_ports,
            script=script,
            shared=shared,
            exclusive=exclusive,
            oversubscribe=oversubscribe,
            site_factor=site_factor,
            spank_environment=spank_environment,
            distribution=distribution,
            time_limit=time_limit,
            time_minimum=time_minimum,
            tres_bind=tres_bind,
            tres_freq=tres_freq,
            tres_per_job=tres_per_job,
            tres_per_node=tres_per_node,
            tres_per_socket=tres_per_socket,
            tres_per_task=tres_per_task,
            user_id=user_id,
            wait_all_nodes=wait_all_nodes,
            kill_warning_flags=kill_warning_flags,
            kill_warning_signal=kill_warning_signal,
            kill_warning_delay=kill_warning_delay,
            current_working_directory=current_working_directory,
            cpus_per_task=cpus_per_task,
            minimum_cpus=minimum_cpus,
            maximum_cpus=maximum_cpus,
            nodes=nodes,
            minimum_nodes=minimum_nodes,
            maximum_nodes=maximum_nodes,
            minimum_boards_per_node=minimum_boards_per_node,
            minimum_sockets_per_board=minimum_sockets_per_board,
            sockets_per_node=sockets_per_node,
            threads_per_core=threads_per_core,
            tasks_per_node=tasks_per_node,
            tasks_per_socket=tasks_per_socket,
            tasks_per_core=tasks_per_core,
            tasks_per_board=tasks_per_board,
            ntasks_per_tres=ntasks_per_tres,
            minimum_cpus_per_node=minimum_cpus_per_node,
            memory_per_cpu=memory_per_cpu,
            memory_per_node=memory_per_node,
            temporary_disk_per_node=temporary_disk_per_node,
            selinux_context=selinux_context,
            required_switches=required_switches,
            segment_size=segment_size,
            standard_error=standard_error,
            standard_input=standard_input,
            standard_output=standard_output,
            wait_for_switch=wait_for_switch,
            wckey=wckey,
            x11=x11,
            x11_magic_cookie=x11_magic_cookie,
            x11_target_host=x11_target_host,
            x11_target_port=x11_target_port,
        )

        slurm_v0041_post_job_body.additional_properties = d
        return slurm_v0041_post_job_body

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
