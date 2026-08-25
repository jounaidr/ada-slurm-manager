from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v0037_job_resources import V0037JobResources


T = TypeVar("T", bound="V0037JobResponseProperties")


@_attrs_define
class V0037JobResponseProperties:
    """
    Attributes:
        account (str | Unset): Charge resources used by this job to specified account
        accrue_time (int | Unset): time job is eligible for running
        admin_comment (str | Unset): administrator's arbitrary comment
        array_job_id (str | Unset): job_id of a job array or 0 if N/A
        array_task_id (str | Unset): task_id of a job array
        array_max_tasks (str | Unset): Maximum number of running array tasks
        array_task_string (str | Unset): string expression of task IDs in this record
        association_id (str | Unset): association id for job
        batch_features (str | Unset): features required for batch script's node
        batch_flag (bool | Unset): if batch: queued job with script
        batch_host (str | Unset): name of host running batch script
        flags (list[str] | Unset): Job flags
        burst_buffer (str | Unset): burst buffer specifications
        burst_buffer_state (str | Unset): burst buffer state info
        cluster (str | Unset): name of cluster that the job is on
        cluster_features (str | Unset): comma separated list of required cluster features
        command (str | Unset): command to be executed
        comment (str | Unset): arbitrary comment
        contiguous (bool | Unset): job requires contiguous nodes
        core_spec (str | Unset): specialized core count
        thread_spec (str | Unset): specialized thread count
        cores_per_socket (str | Unset): cores per socket required by job
        billable_tres (str | Unset): billable TRES
        cpus_per_task (str | Unset): number of processors required for each task
        cpu_frequency_minimum (str | Unset): Minimum cpu frequency
        cpu_frequency_maximum (str | Unset): Maximum cpu frequency
        cpu_frequency_governor (str | Unset): cpu frequency governor
        cpus_per_tres (str | Unset): semicolon delimited list of TRES=# values
        deadline (str | Unset): job start deadline
        delay_boot (str | Unset): command to be executed
        dependency (str | Unset): synchronize job execution with other jobs
        derived_exit_code (str | Unset): highest exit code of all job steps
        eligible_time (int | Unset): time job is eligible for running
        end_time (int | Unset): time of termination, actual or expected
        excluded_nodes (str | Unset): comma separated list of excluded nodes
        exit_code (int | Unset): exit code for job
        features (str | Unset): comma separated list of required features
        federation_origin (str | Unset): Origin cluster's name
        federation_siblings_active (str | Unset): string of active sibling names
        federation_siblings_viable (str | Unset): string of viable sibling names
        gres_detail (list[str] | Unset): Job flags
        group_id (str | Unset): group job submitted as
        job_id (str | Unset): job ID
        job_resources (V0037JobResources | Unset):
        job_state (str | Unset): state of the job
        last_sched_evaluation (str | Unset): last time job was evaluated for scheduling
        licenses (str | Unset): licenses required by the job
        max_cpus (str | Unset): maximum number of cpus usable by job
        max_nodes (str | Unset): maximum number of nodes usable by job
        mcs_label (str | Unset): mcs_label if mcs plugin in use
        memory_per_tres (str | Unset): semicolon delimited list of TRES=# values
        name (str | Unset): name of the job
        nodes (str | Unset): list of nodes allocated to job
        nice (str | Unset): requested priority change
        tasks_per_core (str | Unset): number of tasks to invoke on each core
        tasks_per_socket (str | Unset): number of tasks to invoke on each socket
        tasks_per_board (str | Unset): number of tasks to invoke on each board
        cpus (str | Unset): minimum number of cpus required by job
        node_count (str | Unset): minimum number of nodes required by job
        tasks (str | Unset): requested task count
        het_job_id (str | Unset): job ID of hetjob leader
        het_job_id_set (str | Unset): job IDs for all components
        het_job_offset (str | Unset): HetJob component offset from leader
        partition (str | Unset): name of assigned partition
        memory_per_node (str | Unset): minimum real memory per node
        memory_per_cpu (str | Unset): minimum real memory per cpu
        minimum_cpus_per_node (str | Unset): minimum # CPUs per node
        minimum_tmp_disk_per_node (str | Unset): minimum tmp disk per node
        preempt_time (int | Unset): preemption signal time
        pre_sus_time (int | Unset): time job ran prior to last suspend
        priority (str | Unset): relative priority of the job
        profile (list[str] | Unset): Job profiling requested
        qos (str | Unset): Quality of Service
        reboot (bool | Unset): node reboot requested before start
        required_nodes (str | Unset): comma separated list of required nodes
        requeue (bool | Unset): enable or disable job requeue option
        resize_time (int | Unset): time of latest size change
        restart_cnt (str | Unset): count of job restarts
        resv_name (str | Unset): reservation name
        shared (str | Unset): type and if job can share nodes with other jobs
        show_flags (list[str] | Unset): details requested
        sockets_per_board (str | Unset): sockets per board required by job
        sockets_per_node (str | Unset): sockets per node required by job
        start_time (int | Unset): time execution begins, actual or expected
        state_description (str | Unset): optional details for state_reason
        state_reason (str | Unset): reason job still pending or failed
        standard_error (str | Unset): pathname of job's stderr file
        standard_input (str | Unset): pathname of job's stdin file
        standard_output (str | Unset): pathname of job's stdout file
        submit_time (int | Unset): time of job submission
        suspend_time (int | Unset): time job last suspended or resumed
        system_comment (str | Unset): slurmctld's arbitrary comment
        time_limit (str | Unset): maximum run time in minutes
        time_minimum (str | Unset): minimum run time in minutes
        threads_per_core (str | Unset): threads per core required by job
        tres_bind (str | Unset): Task to TRES binding directives
        tres_freq (str | Unset): TRES frequency directives
        tres_per_job (str | Unset): semicolon delimited list of TRES=# values
        tres_per_node (str | Unset): semicolon delimited list of TRES=# values
        tres_per_socket (str | Unset): semicolon delimited list of TRES=# values
        tres_per_task (str | Unset): semicolon delimited list of TRES=# values
        tres_req_str (str | Unset): tres requested in the job
        tres_alloc_str (str | Unset): tres used in the job
        user_id (str | Unset): user id the job runs as
        user_name (str | Unset): user the job runs as
        wckey (str | Unset): wckey for job
        current_working_directory (str | Unset): pathname of working directory
    """

    account: str | Unset = UNSET
    accrue_time: int | Unset = UNSET
    admin_comment: str | Unset = UNSET
    array_job_id: str | Unset = UNSET
    array_task_id: str | Unset = UNSET
    array_max_tasks: str | Unset = UNSET
    array_task_string: str | Unset = UNSET
    association_id: str | Unset = UNSET
    batch_features: str | Unset = UNSET
    batch_flag: bool | Unset = UNSET
    batch_host: str | Unset = UNSET
    flags: list[str] | Unset = UNSET
    burst_buffer: str | Unset = UNSET
    burst_buffer_state: str | Unset = UNSET
    cluster: str | Unset = UNSET
    cluster_features: str | Unset = UNSET
    command: str | Unset = UNSET
    comment: str | Unset = UNSET
    contiguous: bool | Unset = UNSET
    core_spec: str | Unset = UNSET
    thread_spec: str | Unset = UNSET
    cores_per_socket: str | Unset = UNSET
    billable_tres: str | Unset = UNSET
    cpus_per_task: str | Unset = UNSET
    cpu_frequency_minimum: str | Unset = UNSET
    cpu_frequency_maximum: str | Unset = UNSET
    cpu_frequency_governor: str | Unset = UNSET
    cpus_per_tres: str | Unset = UNSET
    deadline: str | Unset = UNSET
    delay_boot: str | Unset = UNSET
    dependency: str | Unset = UNSET
    derived_exit_code: str | Unset = UNSET
    eligible_time: int | Unset = UNSET
    end_time: int | Unset = UNSET
    excluded_nodes: str | Unset = UNSET
    exit_code: int | Unset = UNSET
    features: str | Unset = UNSET
    federation_origin: str | Unset = UNSET
    federation_siblings_active: str | Unset = UNSET
    federation_siblings_viable: str | Unset = UNSET
    gres_detail: list[str] | Unset = UNSET
    group_id: str | Unset = UNSET
    job_id: str | Unset = UNSET
    job_resources: V0037JobResources | Unset = UNSET
    job_state: str | Unset = UNSET
    last_sched_evaluation: str | Unset = UNSET
    licenses: str | Unset = UNSET
    max_cpus: str | Unset = UNSET
    max_nodes: str | Unset = UNSET
    mcs_label: str | Unset = UNSET
    memory_per_tres: str | Unset = UNSET
    name: str | Unset = UNSET
    nodes: str | Unset = UNSET
    nice: str | Unset = UNSET
    tasks_per_core: str | Unset = UNSET
    tasks_per_socket: str | Unset = UNSET
    tasks_per_board: str | Unset = UNSET
    cpus: str | Unset = UNSET
    node_count: str | Unset = UNSET
    tasks: str | Unset = UNSET
    het_job_id: str | Unset = UNSET
    het_job_id_set: str | Unset = UNSET
    het_job_offset: str | Unset = UNSET
    partition: str | Unset = UNSET
    memory_per_node: str | Unset = UNSET
    memory_per_cpu: str | Unset = UNSET
    minimum_cpus_per_node: str | Unset = UNSET
    minimum_tmp_disk_per_node: str | Unset = UNSET
    preempt_time: int | Unset = UNSET
    pre_sus_time: int | Unset = UNSET
    priority: str | Unset = UNSET
    profile: list[str] | Unset = UNSET
    qos: str | Unset = UNSET
    reboot: bool | Unset = UNSET
    required_nodes: str | Unset = UNSET
    requeue: bool | Unset = UNSET
    resize_time: int | Unset = UNSET
    restart_cnt: str | Unset = UNSET
    resv_name: str | Unset = UNSET
    shared: str | Unset = UNSET
    show_flags: list[str] | Unset = UNSET
    sockets_per_board: str | Unset = UNSET
    sockets_per_node: str | Unset = UNSET
    start_time: int | Unset = UNSET
    state_description: str | Unset = UNSET
    state_reason: str | Unset = UNSET
    standard_error: str | Unset = UNSET
    standard_input: str | Unset = UNSET
    standard_output: str | Unset = UNSET
    submit_time: int | Unset = UNSET
    suspend_time: int | Unset = UNSET
    system_comment: str | Unset = UNSET
    time_limit: str | Unset = UNSET
    time_minimum: str | Unset = UNSET
    threads_per_core: str | Unset = UNSET
    tres_bind: str | Unset = UNSET
    tres_freq: str | Unset = UNSET
    tres_per_job: str | Unset = UNSET
    tres_per_node: str | Unset = UNSET
    tres_per_socket: str | Unset = UNSET
    tres_per_task: str | Unset = UNSET
    tres_req_str: str | Unset = UNSET
    tres_alloc_str: str | Unset = UNSET
    user_id: str | Unset = UNSET
    user_name: str | Unset = UNSET
    wckey: str | Unset = UNSET
    current_working_directory: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account = self.account

        accrue_time = self.accrue_time

        admin_comment = self.admin_comment

        array_job_id = self.array_job_id

        array_task_id = self.array_task_id

        array_max_tasks = self.array_max_tasks

        array_task_string = self.array_task_string

        association_id = self.association_id

        batch_features = self.batch_features

        batch_flag = self.batch_flag

        batch_host = self.batch_host

        flags: list[str] | Unset = UNSET
        if not isinstance(self.flags, Unset):
            flags = self.flags

        burst_buffer = self.burst_buffer

        burst_buffer_state = self.burst_buffer_state

        cluster = self.cluster

        cluster_features = self.cluster_features

        command = self.command

        comment = self.comment

        contiguous = self.contiguous

        core_spec = self.core_spec

        thread_spec = self.thread_spec

        cores_per_socket = self.cores_per_socket

        billable_tres = self.billable_tres

        cpus_per_task = self.cpus_per_task

        cpu_frequency_minimum = self.cpu_frequency_minimum

        cpu_frequency_maximum = self.cpu_frequency_maximum

        cpu_frequency_governor = self.cpu_frequency_governor

        cpus_per_tres = self.cpus_per_tres

        deadline = self.deadline

        delay_boot = self.delay_boot

        dependency = self.dependency

        derived_exit_code = self.derived_exit_code

        eligible_time = self.eligible_time

        end_time = self.end_time

        excluded_nodes = self.excluded_nodes

        exit_code = self.exit_code

        features = self.features

        federation_origin = self.federation_origin

        federation_siblings_active = self.federation_siblings_active

        federation_siblings_viable = self.federation_siblings_viable

        gres_detail: list[str] | Unset = UNSET
        if not isinstance(self.gres_detail, Unset):
            gres_detail = self.gres_detail

        group_id = self.group_id

        job_id = self.job_id

        job_resources: dict[str, Any] | Unset = UNSET
        if not isinstance(self.job_resources, Unset):
            job_resources = self.job_resources.to_dict()

        job_state = self.job_state

        last_sched_evaluation = self.last_sched_evaluation

        licenses = self.licenses

        max_cpus = self.max_cpus

        max_nodes = self.max_nodes

        mcs_label = self.mcs_label

        memory_per_tres = self.memory_per_tres

        name = self.name

        nodes = self.nodes

        nice = self.nice

        tasks_per_core = self.tasks_per_core

        tasks_per_socket = self.tasks_per_socket

        tasks_per_board = self.tasks_per_board

        cpus = self.cpus

        node_count = self.node_count

        tasks = self.tasks

        het_job_id = self.het_job_id

        het_job_id_set = self.het_job_id_set

        het_job_offset = self.het_job_offset

        partition = self.partition

        memory_per_node = self.memory_per_node

        memory_per_cpu = self.memory_per_cpu

        minimum_cpus_per_node = self.minimum_cpus_per_node

        minimum_tmp_disk_per_node = self.minimum_tmp_disk_per_node

        preempt_time = self.preempt_time

        pre_sus_time = self.pre_sus_time

        priority = self.priority

        profile: list[str] | Unset = UNSET
        if not isinstance(self.profile, Unset):
            profile = self.profile

        qos = self.qos

        reboot = self.reboot

        required_nodes = self.required_nodes

        requeue = self.requeue

        resize_time = self.resize_time

        restart_cnt = self.restart_cnt

        resv_name = self.resv_name

        shared = self.shared

        show_flags: list[str] | Unset = UNSET
        if not isinstance(self.show_flags, Unset):
            show_flags = self.show_flags

        sockets_per_board = self.sockets_per_board

        sockets_per_node = self.sockets_per_node

        start_time = self.start_time

        state_description = self.state_description

        state_reason = self.state_reason

        standard_error = self.standard_error

        standard_input = self.standard_input

        standard_output = self.standard_output

        submit_time = self.submit_time

        suspend_time = self.suspend_time

        system_comment = self.system_comment

        time_limit = self.time_limit

        time_minimum = self.time_minimum

        threads_per_core = self.threads_per_core

        tres_bind = self.tres_bind

        tres_freq = self.tres_freq

        tres_per_job = self.tres_per_job

        tres_per_node = self.tres_per_node

        tres_per_socket = self.tres_per_socket

        tres_per_task = self.tres_per_task

        tres_req_str = self.tres_req_str

        tres_alloc_str = self.tres_alloc_str

        user_id = self.user_id

        user_name = self.user_name

        wckey = self.wckey

        current_working_directory = self.current_working_directory

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account is not UNSET:
            field_dict["account"] = account
        if accrue_time is not UNSET:
            field_dict["accrue_time"] = accrue_time
        if admin_comment is not UNSET:
            field_dict["admin_comment"] = admin_comment
        if array_job_id is not UNSET:
            field_dict["array_job_id"] = array_job_id
        if array_task_id is not UNSET:
            field_dict["array_task_id"] = array_task_id
        if array_max_tasks is not UNSET:
            field_dict["array_max_tasks"] = array_max_tasks
        if array_task_string is not UNSET:
            field_dict["array_task_string"] = array_task_string
        if association_id is not UNSET:
            field_dict["association_id"] = association_id
        if batch_features is not UNSET:
            field_dict["batch_features"] = batch_features
        if batch_flag is not UNSET:
            field_dict["batch_flag"] = batch_flag
        if batch_host is not UNSET:
            field_dict["batch_host"] = batch_host
        if flags is not UNSET:
            field_dict["flags"] = flags
        if burst_buffer is not UNSET:
            field_dict["burst_buffer"] = burst_buffer
        if burst_buffer_state is not UNSET:
            field_dict["burst_buffer_state"] = burst_buffer_state
        if cluster is not UNSET:
            field_dict["cluster"] = cluster
        if cluster_features is not UNSET:
            field_dict["cluster_features"] = cluster_features
        if command is not UNSET:
            field_dict["command"] = command
        if comment is not UNSET:
            field_dict["comment"] = comment
        if contiguous is not UNSET:
            field_dict["contiguous"] = contiguous
        if core_spec is not UNSET:
            field_dict["core_spec"] = core_spec
        if thread_spec is not UNSET:
            field_dict["thread_spec"] = thread_spec
        if cores_per_socket is not UNSET:
            field_dict["cores_per_socket"] = cores_per_socket
        if billable_tres is not UNSET:
            field_dict["billable_tres"] = billable_tres
        if cpus_per_task is not UNSET:
            field_dict["cpus_per_task"] = cpus_per_task
        if cpu_frequency_minimum is not UNSET:
            field_dict["cpu_frequency_minimum"] = cpu_frequency_minimum
        if cpu_frequency_maximum is not UNSET:
            field_dict["cpu_frequency_maximum"] = cpu_frequency_maximum
        if cpu_frequency_governor is not UNSET:
            field_dict["cpu_frequency_governor"] = cpu_frequency_governor
        if cpus_per_tres is not UNSET:
            field_dict["cpus_per_tres"] = cpus_per_tres
        if deadline is not UNSET:
            field_dict["deadline"] = deadline
        if delay_boot is not UNSET:
            field_dict["delay_boot"] = delay_boot
        if dependency is not UNSET:
            field_dict["dependency"] = dependency
        if derived_exit_code is not UNSET:
            field_dict["derived_exit_code"] = derived_exit_code
        if eligible_time is not UNSET:
            field_dict["eligible_time"] = eligible_time
        if end_time is not UNSET:
            field_dict["end_time"] = end_time
        if excluded_nodes is not UNSET:
            field_dict["excluded_nodes"] = excluded_nodes
        if exit_code is not UNSET:
            field_dict["exit_code"] = exit_code
        if features is not UNSET:
            field_dict["features"] = features
        if federation_origin is not UNSET:
            field_dict["federation_origin"] = federation_origin
        if federation_siblings_active is not UNSET:
            field_dict["federation_siblings_active"] = federation_siblings_active
        if federation_siblings_viable is not UNSET:
            field_dict["federation_siblings_viable"] = federation_siblings_viable
        if gres_detail is not UNSET:
            field_dict["gres_detail"] = gres_detail
        if group_id is not UNSET:
            field_dict["group_id"] = group_id
        if job_id is not UNSET:
            field_dict["job_id"] = job_id
        if job_resources is not UNSET:
            field_dict["job_resources"] = job_resources
        if job_state is not UNSET:
            field_dict["job_state"] = job_state
        if last_sched_evaluation is not UNSET:
            field_dict["last_sched_evaluation"] = last_sched_evaluation
        if licenses is not UNSET:
            field_dict["licenses"] = licenses
        if max_cpus is not UNSET:
            field_dict["max_cpus"] = max_cpus
        if max_nodes is not UNSET:
            field_dict["max_nodes"] = max_nodes
        if mcs_label is not UNSET:
            field_dict["mcs_label"] = mcs_label
        if memory_per_tres is not UNSET:
            field_dict["memory_per_tres"] = memory_per_tres
        if name is not UNSET:
            field_dict["name"] = name
        if nodes is not UNSET:
            field_dict["nodes"] = nodes
        if nice is not UNSET:
            field_dict["nice"] = nice
        if tasks_per_core is not UNSET:
            field_dict["tasks_per_core"] = tasks_per_core
        if tasks_per_socket is not UNSET:
            field_dict["tasks_per_socket"] = tasks_per_socket
        if tasks_per_board is not UNSET:
            field_dict["tasks_per_board"] = tasks_per_board
        if cpus is not UNSET:
            field_dict["cpus"] = cpus
        if node_count is not UNSET:
            field_dict["node_count"] = node_count
        if tasks is not UNSET:
            field_dict["tasks"] = tasks
        if het_job_id is not UNSET:
            field_dict["het_job_id"] = het_job_id
        if het_job_id_set is not UNSET:
            field_dict["het_job_id_set"] = het_job_id_set
        if het_job_offset is not UNSET:
            field_dict["het_job_offset"] = het_job_offset
        if partition is not UNSET:
            field_dict["partition"] = partition
        if memory_per_node is not UNSET:
            field_dict["memory_per_node"] = memory_per_node
        if memory_per_cpu is not UNSET:
            field_dict["memory_per_cpu"] = memory_per_cpu
        if minimum_cpus_per_node is not UNSET:
            field_dict["minimum_cpus_per_node"] = minimum_cpus_per_node
        if minimum_tmp_disk_per_node is not UNSET:
            field_dict["minimum_tmp_disk_per_node"] = minimum_tmp_disk_per_node
        if preempt_time is not UNSET:
            field_dict["preempt_time"] = preempt_time
        if pre_sus_time is not UNSET:
            field_dict["pre_sus_time"] = pre_sus_time
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
        if resize_time is not UNSET:
            field_dict["resize_time"] = resize_time
        if restart_cnt is not UNSET:
            field_dict["restart_cnt"] = restart_cnt
        if resv_name is not UNSET:
            field_dict["resv_name"] = resv_name
        if shared is not UNSET:
            field_dict["shared"] = shared
        if show_flags is not UNSET:
            field_dict["show_flags"] = show_flags
        if sockets_per_board is not UNSET:
            field_dict["sockets_per_board"] = sockets_per_board
        if sockets_per_node is not UNSET:
            field_dict["sockets_per_node"] = sockets_per_node
        if start_time is not UNSET:
            field_dict["start_time"] = start_time
        if state_description is not UNSET:
            field_dict["state_description"] = state_description
        if state_reason is not UNSET:
            field_dict["state_reason"] = state_reason
        if standard_error is not UNSET:
            field_dict["standard_error"] = standard_error
        if standard_input is not UNSET:
            field_dict["standard_input"] = standard_input
        if standard_output is not UNSET:
            field_dict["standard_output"] = standard_output
        if submit_time is not UNSET:
            field_dict["submit_time"] = submit_time
        if suspend_time is not UNSET:
            field_dict["suspend_time"] = suspend_time
        if system_comment is not UNSET:
            field_dict["system_comment"] = system_comment
        if time_limit is not UNSET:
            field_dict["time_limit"] = time_limit
        if time_minimum is not UNSET:
            field_dict["time_minimum"] = time_minimum
        if threads_per_core is not UNSET:
            field_dict["threads_per_core"] = threads_per_core
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
        if tres_req_str is not UNSET:
            field_dict["tres_req_str"] = tres_req_str
        if tres_alloc_str is not UNSET:
            field_dict["tres_alloc_str"] = tres_alloc_str
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if user_name is not UNSET:
            field_dict["user_name"] = user_name
        if wckey is not UNSET:
            field_dict["wckey"] = wckey
        if current_working_directory is not UNSET:
            field_dict["current_working_directory"] = current_working_directory

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v0037_job_resources import V0037JobResources

        d = dict(src_dict)
        account = d.pop("account", UNSET)

        accrue_time = d.pop("accrue_time", UNSET)

        admin_comment = d.pop("admin_comment", UNSET)

        array_job_id = d.pop("array_job_id", UNSET)

        array_task_id = d.pop("array_task_id", UNSET)

        array_max_tasks = d.pop("array_max_tasks", UNSET)

        array_task_string = d.pop("array_task_string", UNSET)

        association_id = d.pop("association_id", UNSET)

        batch_features = d.pop("batch_features", UNSET)

        batch_flag = d.pop("batch_flag", UNSET)

        batch_host = d.pop("batch_host", UNSET)

        flags = cast(list[str], d.pop("flags", UNSET))

        burst_buffer = d.pop("burst_buffer", UNSET)

        burst_buffer_state = d.pop("burst_buffer_state", UNSET)

        cluster = d.pop("cluster", UNSET)

        cluster_features = d.pop("cluster_features", UNSET)

        command = d.pop("command", UNSET)

        comment = d.pop("comment", UNSET)

        contiguous = d.pop("contiguous", UNSET)

        core_spec = d.pop("core_spec", UNSET)

        thread_spec = d.pop("thread_spec", UNSET)

        cores_per_socket = d.pop("cores_per_socket", UNSET)

        billable_tres = d.pop("billable_tres", UNSET)

        cpus_per_task = d.pop("cpus_per_task", UNSET)

        cpu_frequency_minimum = d.pop("cpu_frequency_minimum", UNSET)

        cpu_frequency_maximum = d.pop("cpu_frequency_maximum", UNSET)

        cpu_frequency_governor = d.pop("cpu_frequency_governor", UNSET)

        cpus_per_tres = d.pop("cpus_per_tres", UNSET)

        deadline = d.pop("deadline", UNSET)

        delay_boot = d.pop("delay_boot", UNSET)

        dependency = d.pop("dependency", UNSET)

        derived_exit_code = d.pop("derived_exit_code", UNSET)

        eligible_time = d.pop("eligible_time", UNSET)

        end_time = d.pop("end_time", UNSET)

        excluded_nodes = d.pop("excluded_nodes", UNSET)

        exit_code = d.pop("exit_code", UNSET)

        features = d.pop("features", UNSET)

        federation_origin = d.pop("federation_origin", UNSET)

        federation_siblings_active = d.pop("federation_siblings_active", UNSET)

        federation_siblings_viable = d.pop("federation_siblings_viable", UNSET)

        gres_detail = cast(list[str], d.pop("gres_detail", UNSET))

        group_id = d.pop("group_id", UNSET)

        job_id = d.pop("job_id", UNSET)

        _job_resources = d.pop("job_resources", UNSET)
        job_resources: V0037JobResources | Unset
        if isinstance(_job_resources, Unset):
            job_resources = UNSET
        else:
            job_resources = V0037JobResources.from_dict(_job_resources)

        job_state = d.pop("job_state", UNSET)

        last_sched_evaluation = d.pop("last_sched_evaluation", UNSET)

        licenses = d.pop("licenses", UNSET)

        max_cpus = d.pop("max_cpus", UNSET)

        max_nodes = d.pop("max_nodes", UNSET)

        mcs_label = d.pop("mcs_label", UNSET)

        memory_per_tres = d.pop("memory_per_tres", UNSET)

        name = d.pop("name", UNSET)

        nodes = d.pop("nodes", UNSET)

        nice = d.pop("nice", UNSET)

        tasks_per_core = d.pop("tasks_per_core", UNSET)

        tasks_per_socket = d.pop("tasks_per_socket", UNSET)

        tasks_per_board = d.pop("tasks_per_board", UNSET)

        cpus = d.pop("cpus", UNSET)

        node_count = d.pop("node_count", UNSET)

        tasks = d.pop("tasks", UNSET)

        het_job_id = d.pop("het_job_id", UNSET)

        het_job_id_set = d.pop("het_job_id_set", UNSET)

        het_job_offset = d.pop("het_job_offset", UNSET)

        partition = d.pop("partition", UNSET)

        memory_per_node = d.pop("memory_per_node", UNSET)

        memory_per_cpu = d.pop("memory_per_cpu", UNSET)

        minimum_cpus_per_node = d.pop("minimum_cpus_per_node", UNSET)

        minimum_tmp_disk_per_node = d.pop("minimum_tmp_disk_per_node", UNSET)

        preempt_time = d.pop("preempt_time", UNSET)

        pre_sus_time = d.pop("pre_sus_time", UNSET)

        priority = d.pop("priority", UNSET)

        profile = cast(list[str], d.pop("profile", UNSET))

        qos = d.pop("qos", UNSET)

        reboot = d.pop("reboot", UNSET)

        required_nodes = d.pop("required_nodes", UNSET)

        requeue = d.pop("requeue", UNSET)

        resize_time = d.pop("resize_time", UNSET)

        restart_cnt = d.pop("restart_cnt", UNSET)

        resv_name = d.pop("resv_name", UNSET)

        shared = d.pop("shared", UNSET)

        show_flags = cast(list[str], d.pop("show_flags", UNSET))

        sockets_per_board = d.pop("sockets_per_board", UNSET)

        sockets_per_node = d.pop("sockets_per_node", UNSET)

        start_time = d.pop("start_time", UNSET)

        state_description = d.pop("state_description", UNSET)

        state_reason = d.pop("state_reason", UNSET)

        standard_error = d.pop("standard_error", UNSET)

        standard_input = d.pop("standard_input", UNSET)

        standard_output = d.pop("standard_output", UNSET)

        submit_time = d.pop("submit_time", UNSET)

        suspend_time = d.pop("suspend_time", UNSET)

        system_comment = d.pop("system_comment", UNSET)

        time_limit = d.pop("time_limit", UNSET)

        time_minimum = d.pop("time_minimum", UNSET)

        threads_per_core = d.pop("threads_per_core", UNSET)

        tres_bind = d.pop("tres_bind", UNSET)

        tres_freq = d.pop("tres_freq", UNSET)

        tres_per_job = d.pop("tres_per_job", UNSET)

        tres_per_node = d.pop("tres_per_node", UNSET)

        tres_per_socket = d.pop("tres_per_socket", UNSET)

        tres_per_task = d.pop("tres_per_task", UNSET)

        tres_req_str = d.pop("tres_req_str", UNSET)

        tres_alloc_str = d.pop("tres_alloc_str", UNSET)

        user_id = d.pop("user_id", UNSET)

        user_name = d.pop("user_name", UNSET)

        wckey = d.pop("wckey", UNSET)

        current_working_directory = d.pop("current_working_directory", UNSET)

        v0037_job_response_properties = cls(
            account=account,
            accrue_time=accrue_time,
            admin_comment=admin_comment,
            array_job_id=array_job_id,
            array_task_id=array_task_id,
            array_max_tasks=array_max_tasks,
            array_task_string=array_task_string,
            association_id=association_id,
            batch_features=batch_features,
            batch_flag=batch_flag,
            batch_host=batch_host,
            flags=flags,
            burst_buffer=burst_buffer,
            burst_buffer_state=burst_buffer_state,
            cluster=cluster,
            cluster_features=cluster_features,
            command=command,
            comment=comment,
            contiguous=contiguous,
            core_spec=core_spec,
            thread_spec=thread_spec,
            cores_per_socket=cores_per_socket,
            billable_tres=billable_tres,
            cpus_per_task=cpus_per_task,
            cpu_frequency_minimum=cpu_frequency_minimum,
            cpu_frequency_maximum=cpu_frequency_maximum,
            cpu_frequency_governor=cpu_frequency_governor,
            cpus_per_tres=cpus_per_tres,
            deadline=deadline,
            delay_boot=delay_boot,
            dependency=dependency,
            derived_exit_code=derived_exit_code,
            eligible_time=eligible_time,
            end_time=end_time,
            excluded_nodes=excluded_nodes,
            exit_code=exit_code,
            features=features,
            federation_origin=federation_origin,
            federation_siblings_active=federation_siblings_active,
            federation_siblings_viable=federation_siblings_viable,
            gres_detail=gres_detail,
            group_id=group_id,
            job_id=job_id,
            job_resources=job_resources,
            job_state=job_state,
            last_sched_evaluation=last_sched_evaluation,
            licenses=licenses,
            max_cpus=max_cpus,
            max_nodes=max_nodes,
            mcs_label=mcs_label,
            memory_per_tres=memory_per_tres,
            name=name,
            nodes=nodes,
            nice=nice,
            tasks_per_core=tasks_per_core,
            tasks_per_socket=tasks_per_socket,
            tasks_per_board=tasks_per_board,
            cpus=cpus,
            node_count=node_count,
            tasks=tasks,
            het_job_id=het_job_id,
            het_job_id_set=het_job_id_set,
            het_job_offset=het_job_offset,
            partition=partition,
            memory_per_node=memory_per_node,
            memory_per_cpu=memory_per_cpu,
            minimum_cpus_per_node=minimum_cpus_per_node,
            minimum_tmp_disk_per_node=minimum_tmp_disk_per_node,
            preempt_time=preempt_time,
            pre_sus_time=pre_sus_time,
            priority=priority,
            profile=profile,
            qos=qos,
            reboot=reboot,
            required_nodes=required_nodes,
            requeue=requeue,
            resize_time=resize_time,
            restart_cnt=restart_cnt,
            resv_name=resv_name,
            shared=shared,
            show_flags=show_flags,
            sockets_per_board=sockets_per_board,
            sockets_per_node=sockets_per_node,
            start_time=start_time,
            state_description=state_description,
            state_reason=state_reason,
            standard_error=standard_error,
            standard_input=standard_input,
            standard_output=standard_output,
            submit_time=submit_time,
            suspend_time=suspend_time,
            system_comment=system_comment,
            time_limit=time_limit,
            time_minimum=time_minimum,
            threads_per_core=threads_per_core,
            tres_bind=tres_bind,
            tres_freq=tres_freq,
            tres_per_job=tres_per_job,
            tres_per_node=tres_per_node,
            tres_per_socket=tres_per_socket,
            tres_per_task=tres_per_task,
            tres_req_str=tres_req_str,
            tres_alloc_str=tres_alloc_str,
            user_id=user_id,
            user_name=user_name,
            wckey=wckey,
            current_working_directory=current_working_directory,
        )

        v0037_job_response_properties.additional_properties = d
        return v0037_job_response_properties

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
