from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.v0041_openapi_job_info_resp_jobs_item_exclusive_item import V0041OpenapiJobInfoRespJobsItemExclusiveItem
from ..models.v0041_openapi_job_info_resp_jobs_item_flags_item import V0041OpenapiJobInfoRespJobsItemFlagsItem
from ..models.v0041_openapi_job_info_resp_jobs_item_job_state_item import V0041OpenapiJobInfoRespJobsItemJobStateItem
from ..models.v0041_openapi_job_info_resp_jobs_item_mail_type_item import V0041OpenapiJobInfoRespJobsItemMailTypeItem
from ..models.v0041_openapi_job_info_resp_jobs_item_profile_item import V0041OpenapiJobInfoRespJobsItemProfileItem
from ..models.v0041_openapi_job_info_resp_jobs_item_shared_item import V0041OpenapiJobInfoRespJobsItemSharedItem
from ..models.v0041_openapi_job_info_resp_jobs_item_show_flags_item import V0041OpenapiJobInfoRespJobsItemShowFlagsItem
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v0041_openapi_job_info_resp_jobs_item_accrue_time import V0041OpenapiJobInfoRespJobsItemAccrueTime
    from ..models.v0041_openapi_job_info_resp_jobs_item_array_job_id import V0041OpenapiJobInfoRespJobsItemArrayJobId
    from ..models.v0041_openapi_job_info_resp_jobs_item_array_max_tasks import (
        V0041OpenapiJobInfoRespJobsItemArrayMaxTasks,
    )
    from ..models.v0041_openapi_job_info_resp_jobs_item_array_task_id import V0041OpenapiJobInfoRespJobsItemArrayTaskId
    from ..models.v0041_openapi_job_info_resp_jobs_item_billable_tres import V0041OpenapiJobInfoRespJobsItemBillableTres
    from ..models.v0041_openapi_job_info_resp_jobs_item_cores_per_socket import (
        V0041OpenapiJobInfoRespJobsItemCoresPerSocket,
    )
    from ..models.v0041_openapi_job_info_resp_jobs_item_cpu_frequency_governor import (
        V0041OpenapiJobInfoRespJobsItemCpuFrequencyGovernor,
    )
    from ..models.v0041_openapi_job_info_resp_jobs_item_cpu_frequency_maximum import (
        V0041OpenapiJobInfoRespJobsItemCpuFrequencyMaximum,
    )
    from ..models.v0041_openapi_job_info_resp_jobs_item_cpu_frequency_minimum import (
        V0041OpenapiJobInfoRespJobsItemCpuFrequencyMinimum,
    )
    from ..models.v0041_openapi_job_info_resp_jobs_item_cpus import V0041OpenapiJobInfoRespJobsItemCpus
    from ..models.v0041_openapi_job_info_resp_jobs_item_cpus_per_task import V0041OpenapiJobInfoRespJobsItemCpusPerTask
    from ..models.v0041_openapi_job_info_resp_jobs_item_deadline import V0041OpenapiJobInfoRespJobsItemDeadline
    from ..models.v0041_openapi_job_info_resp_jobs_item_delay_boot import V0041OpenapiJobInfoRespJobsItemDelayBoot
    from ..models.v0041_openapi_job_info_resp_jobs_item_derived_exit_code import (
        V0041OpenapiJobInfoRespJobsItemDerivedExitCode,
    )
    from ..models.v0041_openapi_job_info_resp_jobs_item_eligible_time import V0041OpenapiJobInfoRespJobsItemEligibleTime
    from ..models.v0041_openapi_job_info_resp_jobs_item_end_time import V0041OpenapiJobInfoRespJobsItemEndTime
    from ..models.v0041_openapi_job_info_resp_jobs_item_exit_code import V0041OpenapiJobInfoRespJobsItemExitCode
    from ..models.v0041_openapi_job_info_resp_jobs_item_het_job_id import V0041OpenapiJobInfoRespJobsItemHetJobId
    from ..models.v0041_openapi_job_info_resp_jobs_item_het_job_offset import (
        V0041OpenapiJobInfoRespJobsItemHetJobOffset,
    )
    from ..models.v0041_openapi_job_info_resp_jobs_item_job_resources import V0041OpenapiJobInfoRespJobsItemJobResources
    from ..models.v0041_openapi_job_info_resp_jobs_item_last_sched_evaluation import (
        V0041OpenapiJobInfoRespJobsItemLastSchedEvaluation,
    )
    from ..models.v0041_openapi_job_info_resp_jobs_item_max_cpus import V0041OpenapiJobInfoRespJobsItemMaxCpus
    from ..models.v0041_openapi_job_info_resp_jobs_item_max_nodes import V0041OpenapiJobInfoRespJobsItemMaxNodes
    from ..models.v0041_openapi_job_info_resp_jobs_item_memory_per_cpu import (
        V0041OpenapiJobInfoRespJobsItemMemoryPerCpu,
    )
    from ..models.v0041_openapi_job_info_resp_jobs_item_memory_per_node import (
        V0041OpenapiJobInfoRespJobsItemMemoryPerNode,
    )
    from ..models.v0041_openapi_job_info_resp_jobs_item_minimum_cpus_per_node import (
        V0041OpenapiJobInfoRespJobsItemMinimumCpusPerNode,
    )
    from ..models.v0041_openapi_job_info_resp_jobs_item_minimum_tmp_disk_per_node import (
        V0041OpenapiJobInfoRespJobsItemMinimumTmpDiskPerNode,
    )
    from ..models.v0041_openapi_job_info_resp_jobs_item_node_count import V0041OpenapiJobInfoRespJobsItemNodeCount
    from ..models.v0041_openapi_job_info_resp_jobs_item_power import V0041OpenapiJobInfoRespJobsItemPower
    from ..models.v0041_openapi_job_info_resp_jobs_item_pre_sus_time import V0041OpenapiJobInfoRespJobsItemPreSusTime
    from ..models.v0041_openapi_job_info_resp_jobs_item_preempt_time import V0041OpenapiJobInfoRespJobsItemPreemptTime
    from ..models.v0041_openapi_job_info_resp_jobs_item_preemptable_time import (
        V0041OpenapiJobInfoRespJobsItemPreemptableTime,
    )
    from ..models.v0041_openapi_job_info_resp_jobs_item_priority import V0041OpenapiJobInfoRespJobsItemPriority
    from ..models.v0041_openapi_job_info_resp_jobs_item_resize_time import V0041OpenapiJobInfoRespJobsItemResizeTime
    from ..models.v0041_openapi_job_info_resp_jobs_item_sockets_per_node import (
        V0041OpenapiJobInfoRespJobsItemSocketsPerNode,
    )
    from ..models.v0041_openapi_job_info_resp_jobs_item_start_time import V0041OpenapiJobInfoRespJobsItemStartTime
    from ..models.v0041_openapi_job_info_resp_jobs_item_submit_time import V0041OpenapiJobInfoRespJobsItemSubmitTime
    from ..models.v0041_openapi_job_info_resp_jobs_item_suspend_time import V0041OpenapiJobInfoRespJobsItemSuspendTime
    from ..models.v0041_openapi_job_info_resp_jobs_item_tasks import V0041OpenapiJobInfoRespJobsItemTasks
    from ..models.v0041_openapi_job_info_resp_jobs_item_tasks_per_board import (
        V0041OpenapiJobInfoRespJobsItemTasksPerBoard,
    )
    from ..models.v0041_openapi_job_info_resp_jobs_item_tasks_per_core import (
        V0041OpenapiJobInfoRespJobsItemTasksPerCore,
    )
    from ..models.v0041_openapi_job_info_resp_jobs_item_tasks_per_node import (
        V0041OpenapiJobInfoRespJobsItemTasksPerNode,
    )
    from ..models.v0041_openapi_job_info_resp_jobs_item_tasks_per_socket import (
        V0041OpenapiJobInfoRespJobsItemTasksPerSocket,
    )
    from ..models.v0041_openapi_job_info_resp_jobs_item_tasks_per_tres import (
        V0041OpenapiJobInfoRespJobsItemTasksPerTres,
    )
    from ..models.v0041_openapi_job_info_resp_jobs_item_threads_per_core import (
        V0041OpenapiJobInfoRespJobsItemThreadsPerCore,
    )
    from ..models.v0041_openapi_job_info_resp_jobs_item_time_limit import V0041OpenapiJobInfoRespJobsItemTimeLimit
    from ..models.v0041_openapi_job_info_resp_jobs_item_time_minimum import V0041OpenapiJobInfoRespJobsItemTimeMinimum


T = TypeVar("T", bound="V0041OpenapiJobInfoRespJobsItem")


@_attrs_define
class V0041OpenapiJobInfoRespJobsItem:
    """
    Attributes:
        account (str | Unset): Account associated with the job
        accrue_time (V0041OpenapiJobInfoRespJobsItemAccrueTime | Unset): When the job started accruing age priority
            (UNIX timestamp)
        admin_comment (str | Unset): Arbitrary comment made by administrator
        allocating_node (str | Unset): Local node making the resource allocation
        array_job_id (V0041OpenapiJobInfoRespJobsItemArrayJobId | Unset): Job ID of job array, or 0 if N/A
        array_task_id (V0041OpenapiJobInfoRespJobsItemArrayTaskId | Unset): Task ID of this task in job array
        array_max_tasks (V0041OpenapiJobInfoRespJobsItemArrayMaxTasks | Unset): Maximum number of simultaneously running
            array tasks, 0 if no limit
        array_task_string (str | Unset): String expression of task IDs in this record
        association_id (int | Unset): Unique identifier for the association
        batch_features (str | Unset): Features required for batch script's node
        batch_flag (bool | Unset): True if batch job
        batch_host (str | Unset): Name of host running batch script
        flags (list[V0041OpenapiJobInfoRespJobsItemFlagsItem] | Unset): Job flags
        burst_buffer (str | Unset): Burst buffer specifications
        burst_buffer_state (str | Unset): Burst buffer state details
        cluster (str | Unset): Cluster name
        cluster_features (str | Unset): List of required cluster features
        command (str | Unset): Executed command
        comment (str | Unset): Arbitrary comment
        container (str | Unset): Absolute path to OCI container bundle
        container_id (str | Unset): OCI container ID
        contiguous (bool | Unset): True if job requires contiguous nodes
        core_spec (int | Unset): Specialized core count
        thread_spec (int | Unset): Specialized thread count
        cores_per_socket (V0041OpenapiJobInfoRespJobsItemCoresPerSocket | Unset): Cores per socket required
        billable_tres (V0041OpenapiJobInfoRespJobsItemBillableTres | Unset): Billable TRES
        cpus_per_task (V0041OpenapiJobInfoRespJobsItemCpusPerTask | Unset): Number of CPUs required by each task
        cpu_frequency_minimum (V0041OpenapiJobInfoRespJobsItemCpuFrequencyMinimum | Unset): Minimum CPU frequency
        cpu_frequency_maximum (V0041OpenapiJobInfoRespJobsItemCpuFrequencyMaximum | Unset): Maximum CPU frequency
        cpu_frequency_governor (V0041OpenapiJobInfoRespJobsItemCpuFrequencyGovernor | Unset): CPU frequency governor
        cpus_per_tres (str | Unset): Semicolon delimited list of TRES=# values indicating how many CPUs should be
            allocated for each specified TRES (currently only used for gres/gpu)
        cron (str | Unset): Time specification for scrontab job
        deadline (V0041OpenapiJobInfoRespJobsItemDeadline | Unset): Latest time that the job may start (UNIX timestamp)
        delay_boot (V0041OpenapiJobInfoRespJobsItemDelayBoot | Unset): Number of seconds after job eligible start that
            nodes will be rebooted to satisfy feature specification
        dependency (str | Unset): Other jobs that must meet certain criteria before this job can start
        derived_exit_code (V0041OpenapiJobInfoRespJobsItemDerivedExitCode | Unset): Highest exit code of all job steps
        eligible_time (V0041OpenapiJobInfoRespJobsItemEligibleTime | Unset): Time when the job became eligible to run
            (UNIX timestamp)
        end_time (V0041OpenapiJobInfoRespJobsItemEndTime | Unset): End time, real or expected (UNIX timestamp)
        excluded_nodes (str | Unset): Comma separated list of nodes that may not be used
        exit_code (V0041OpenapiJobInfoRespJobsItemExitCode | Unset): Exit code of the job
        extra (str | Unset): Arbitrary string used for node filtering if extra constraints are enabled
        failed_node (str | Unset): Name of node that caused job failure
        features (str | Unset): Comma separated list of features that are required
        federation_origin (str | Unset): Origin cluster's name (when using federation)
        federation_siblings_active (str | Unset): Active sibling job names
        federation_siblings_viable (str | Unset): Viable sibling job names
        gres_detail (list[str] | Unset): List of GRES index and counts allocated per node
        group_id (int | Unset): Group ID of the user that owns the job
        group_name (str | Unset): Group name of the user that owns the job
        het_job_id (V0041OpenapiJobInfoRespJobsItemHetJobId | Unset): Heterogeneous job ID, if applicable
        het_job_id_set (str | Unset): Job ID range for all heterogeneous job components
        het_job_offset (V0041OpenapiJobInfoRespJobsItemHetJobOffset | Unset): Unique sequence number applied to this
            component of the heterogeneous job
        job_id (int | Unset): Job ID
        job_resources (V0041OpenapiJobInfoRespJobsItemJobResources | Unset): Resources used by the job
        job_size_str (list[str] | Unset): Number of nodes (in a range) required for this job
        job_state (list[V0041OpenapiJobInfoRespJobsItemJobStateItem] | Unset): Current state
        last_sched_evaluation (V0041OpenapiJobInfoRespJobsItemLastSchedEvaluation | Unset): Last time job was evaluated
            for scheduling (UNIX timestamp)
        licenses (str | Unset): License(s) required by the job
        mail_type (list[V0041OpenapiJobInfoRespJobsItemMailTypeItem] | Unset): Mail event type(s)
        mail_user (str | Unset): User to receive email notifications
        max_cpus (V0041OpenapiJobInfoRespJobsItemMaxCpus | Unset): Maximum number of CPUs usable by the job
        max_nodes (V0041OpenapiJobInfoRespJobsItemMaxNodes | Unset): Maximum number of nodes usable by the job
        mcs_label (str | Unset): Multi-Category Security label on the job
        memory_per_tres (str | Unset): Semicolon delimited list of TRES=# values indicating how much memory in megabytes
            should be allocated for each specified TRES (currently only used for gres/gpu)
        name (str | Unset): Job name
        network (str | Unset): Network specs for the job
        nodes (str | Unset): Node(s) allocated to the job
        nice (int | Unset): Requested job priority change
        tasks_per_core (V0041OpenapiJobInfoRespJobsItemTasksPerCore | Unset): Number of tasks invoked on each core
        tasks_per_tres (V0041OpenapiJobInfoRespJobsItemTasksPerTres | Unset): Number of tasks that can assess each GPU
        tasks_per_node (V0041OpenapiJobInfoRespJobsItemTasksPerNode | Unset): Number of tasks invoked on each node
        tasks_per_socket (V0041OpenapiJobInfoRespJobsItemTasksPerSocket | Unset): Number of tasks invoked on each socket
        tasks_per_board (V0041OpenapiJobInfoRespJobsItemTasksPerBoard | Unset): Number of tasks invoked on each board
        cpus (V0041OpenapiJobInfoRespJobsItemCpus | Unset): Minimum number of CPUs required
        node_count (V0041OpenapiJobInfoRespJobsItemNodeCount | Unset): Minimum number of nodes required
        tasks (V0041OpenapiJobInfoRespJobsItemTasks | Unset): Number of tasks
        partition (str | Unset): Partition assigned to the job
        prefer (str | Unset): Feature(s) the job requested but that are not required
        memory_per_cpu (V0041OpenapiJobInfoRespJobsItemMemoryPerCpu | Unset): Minimum memory in megabytes per allocated
            CPU
        memory_per_node (V0041OpenapiJobInfoRespJobsItemMemoryPerNode | Unset): Minimum memory in megabytes per
            allocated node
        minimum_cpus_per_node (V0041OpenapiJobInfoRespJobsItemMinimumCpusPerNode | Unset): Minimum number of CPUs per
            node
        minimum_tmp_disk_per_node (V0041OpenapiJobInfoRespJobsItemMinimumTmpDiskPerNode | Unset): Minimum tmp disk space
            required per node
        power (V0041OpenapiJobInfoRespJobsItemPower | Unset):
        preempt_time (V0041OpenapiJobInfoRespJobsItemPreemptTime | Unset): Time job received preemption signal (UNIX
            timestamp)
        preemptable_time (V0041OpenapiJobInfoRespJobsItemPreemptableTime | Unset): Time job becomes eligible for
            preemption (UNIX timestamp)
        pre_sus_time (V0041OpenapiJobInfoRespJobsItemPreSusTime | Unset): Total run time prior to last suspend in
            seconds
        hold (bool | Unset): Hold (true) or release (false) job
        priority (V0041OpenapiJobInfoRespJobsItemPriority | Unset): Request specific job priority
        profile (list[V0041OpenapiJobInfoRespJobsItemProfileItem] | Unset): Profile used by the acct_gather_profile
            plugin
        qos (str | Unset): Quality of Service assigned to the job, if pending the QOS requested
        reboot (bool | Unset): Node reboot requested before start
        required_nodes (str | Unset): Comma separated list of required nodes
        minimum_switches (int | Unset): Maximum number of switches (the 'minimum' in the key is incorrect)
        requeue (bool | Unset): Determines whether the job may be requeued
        resize_time (V0041OpenapiJobInfoRespJobsItemResizeTime | Unset): Time of last size change (UNIX timestamp)
        restart_cnt (int | Unset): Number of job restarts
        resv_name (str | Unset): Name of reservation to use
        scheduled_nodes (str | Unset): List of nodes scheduled to be used for the job
        selinux_context (str | Unset): SELinux context
        shared (list[V0041OpenapiJobInfoRespJobsItemSharedItem] | Unset): How the job can share resources with other
            jobs, if at all
        exclusive (list[V0041OpenapiJobInfoRespJobsItemExclusiveItem] | Unset):
        oversubscribe (bool | Unset):
        show_flags (list[V0041OpenapiJobInfoRespJobsItemShowFlagsItem] | Unset):
        sockets_per_board (int | Unset): Number of sockets per board required
        sockets_per_node (V0041OpenapiJobInfoRespJobsItemSocketsPerNode | Unset): Number of sockets per node required
        start_time (V0041OpenapiJobInfoRespJobsItemStartTime | Unset): Time execution began, or is expected to begin
            (UNIX timestamp)
        state_description (str | Unset): Optional details for state_reason
        state_reason (str | Unset): Reason for current Pending or Failed state
        standard_error (str | Unset): Path to stderr file
        standard_input (str | Unset): Path to stdin file
        standard_output (str | Unset): Path to stdout file
        submit_time (V0041OpenapiJobInfoRespJobsItemSubmitTime | Unset): Time when the job was submitted (UNIX
            timestamp)
        suspend_time (V0041OpenapiJobInfoRespJobsItemSuspendTime | Unset): Time the job was last suspended or resumed
            (UNIX timestamp)
        system_comment (str | Unset): Arbitrary comment from slurmctld
        time_limit (V0041OpenapiJobInfoRespJobsItemTimeLimit | Unset): Maximum run time in minutes
        time_minimum (V0041OpenapiJobInfoRespJobsItemTimeMinimum | Unset): Minimum run time in minutes
        threads_per_core (V0041OpenapiJobInfoRespJobsItemThreadsPerCore | Unset): Number of processor threads per CPU
            core required
        tres_bind (str | Unset): Task to TRES binding directives
        tres_freq (str | Unset): TRES frequency directives
        tres_per_job (str | Unset): Comma separated list of TRES=# values to be allocated per job
        tres_per_node (str | Unset): Comma separated list of TRES=# values to be allocated per node
        tres_per_socket (str | Unset): Comma separated list of TRES=# values to be allocated per socket
        tres_per_task (str | Unset): Comma separated list of TRES=# values to be allocated per task
        tres_req_str (str | Unset): TRES requested by the job
        tres_alloc_str (str | Unset): TRES used by the job
        user_id (int | Unset): User ID that owns the job
        user_name (str | Unset): User name that owns the job
        maximum_switch_wait_time (int | Unset): Maximum time to wait for switches in seconds
        wckey (str | Unset): Workload characterization key
        current_working_directory (str | Unset): Working directory to use for the job
    """

    account: str | Unset = UNSET
    accrue_time: V0041OpenapiJobInfoRespJobsItemAccrueTime | Unset = UNSET
    admin_comment: str | Unset = UNSET
    allocating_node: str | Unset = UNSET
    array_job_id: V0041OpenapiJobInfoRespJobsItemArrayJobId | Unset = UNSET
    array_task_id: V0041OpenapiJobInfoRespJobsItemArrayTaskId | Unset = UNSET
    array_max_tasks: V0041OpenapiJobInfoRespJobsItemArrayMaxTasks | Unset = UNSET
    array_task_string: str | Unset = UNSET
    association_id: int | Unset = UNSET
    batch_features: str | Unset = UNSET
    batch_flag: bool | Unset = UNSET
    batch_host: str | Unset = UNSET
    flags: list[V0041OpenapiJobInfoRespJobsItemFlagsItem] | Unset = UNSET
    burst_buffer: str | Unset = UNSET
    burst_buffer_state: str | Unset = UNSET
    cluster: str | Unset = UNSET
    cluster_features: str | Unset = UNSET
    command: str | Unset = UNSET
    comment: str | Unset = UNSET
    container: str | Unset = UNSET
    container_id: str | Unset = UNSET
    contiguous: bool | Unset = UNSET
    core_spec: int | Unset = UNSET
    thread_spec: int | Unset = UNSET
    cores_per_socket: V0041OpenapiJobInfoRespJobsItemCoresPerSocket | Unset = UNSET
    billable_tres: V0041OpenapiJobInfoRespJobsItemBillableTres | Unset = UNSET
    cpus_per_task: V0041OpenapiJobInfoRespJobsItemCpusPerTask | Unset = UNSET
    cpu_frequency_minimum: V0041OpenapiJobInfoRespJobsItemCpuFrequencyMinimum | Unset = UNSET
    cpu_frequency_maximum: V0041OpenapiJobInfoRespJobsItemCpuFrequencyMaximum | Unset = UNSET
    cpu_frequency_governor: V0041OpenapiJobInfoRespJobsItemCpuFrequencyGovernor | Unset = UNSET
    cpus_per_tres: str | Unset = UNSET
    cron: str | Unset = UNSET
    deadline: V0041OpenapiJobInfoRespJobsItemDeadline | Unset = UNSET
    delay_boot: V0041OpenapiJobInfoRespJobsItemDelayBoot | Unset = UNSET
    dependency: str | Unset = UNSET
    derived_exit_code: V0041OpenapiJobInfoRespJobsItemDerivedExitCode | Unset = UNSET
    eligible_time: V0041OpenapiJobInfoRespJobsItemEligibleTime | Unset = UNSET
    end_time: V0041OpenapiJobInfoRespJobsItemEndTime | Unset = UNSET
    excluded_nodes: str | Unset = UNSET
    exit_code: V0041OpenapiJobInfoRespJobsItemExitCode | Unset = UNSET
    extra: str | Unset = UNSET
    failed_node: str | Unset = UNSET
    features: str | Unset = UNSET
    federation_origin: str | Unset = UNSET
    federation_siblings_active: str | Unset = UNSET
    federation_siblings_viable: str | Unset = UNSET
    gres_detail: list[str] | Unset = UNSET
    group_id: int | Unset = UNSET
    group_name: str | Unset = UNSET
    het_job_id: V0041OpenapiJobInfoRespJobsItemHetJobId | Unset = UNSET
    het_job_id_set: str | Unset = UNSET
    het_job_offset: V0041OpenapiJobInfoRespJobsItemHetJobOffset | Unset = UNSET
    job_id: int | Unset = UNSET
    job_resources: V0041OpenapiJobInfoRespJobsItemJobResources | Unset = UNSET
    job_size_str: list[str] | Unset = UNSET
    job_state: list[V0041OpenapiJobInfoRespJobsItemJobStateItem] | Unset = UNSET
    last_sched_evaluation: V0041OpenapiJobInfoRespJobsItemLastSchedEvaluation | Unset = UNSET
    licenses: str | Unset = UNSET
    mail_type: list[V0041OpenapiJobInfoRespJobsItemMailTypeItem] | Unset = UNSET
    mail_user: str | Unset = UNSET
    max_cpus: V0041OpenapiJobInfoRespJobsItemMaxCpus | Unset = UNSET
    max_nodes: V0041OpenapiJobInfoRespJobsItemMaxNodes | Unset = UNSET
    mcs_label: str | Unset = UNSET
    memory_per_tres: str | Unset = UNSET
    name: str | Unset = UNSET
    network: str | Unset = UNSET
    nodes: str | Unset = UNSET
    nice: int | Unset = UNSET
    tasks_per_core: V0041OpenapiJobInfoRespJobsItemTasksPerCore | Unset = UNSET
    tasks_per_tres: V0041OpenapiJobInfoRespJobsItemTasksPerTres | Unset = UNSET
    tasks_per_node: V0041OpenapiJobInfoRespJobsItemTasksPerNode | Unset = UNSET
    tasks_per_socket: V0041OpenapiJobInfoRespJobsItemTasksPerSocket | Unset = UNSET
    tasks_per_board: V0041OpenapiJobInfoRespJobsItemTasksPerBoard | Unset = UNSET
    cpus: V0041OpenapiJobInfoRespJobsItemCpus | Unset = UNSET
    node_count: V0041OpenapiJobInfoRespJobsItemNodeCount | Unset = UNSET
    tasks: V0041OpenapiJobInfoRespJobsItemTasks | Unset = UNSET
    partition: str | Unset = UNSET
    prefer: str | Unset = UNSET
    memory_per_cpu: V0041OpenapiJobInfoRespJobsItemMemoryPerCpu | Unset = UNSET
    memory_per_node: V0041OpenapiJobInfoRespJobsItemMemoryPerNode | Unset = UNSET
    minimum_cpus_per_node: V0041OpenapiJobInfoRespJobsItemMinimumCpusPerNode | Unset = UNSET
    minimum_tmp_disk_per_node: V0041OpenapiJobInfoRespJobsItemMinimumTmpDiskPerNode | Unset = UNSET
    power: V0041OpenapiJobInfoRespJobsItemPower | Unset = UNSET
    preempt_time: V0041OpenapiJobInfoRespJobsItemPreemptTime | Unset = UNSET
    preemptable_time: V0041OpenapiJobInfoRespJobsItemPreemptableTime | Unset = UNSET
    pre_sus_time: V0041OpenapiJobInfoRespJobsItemPreSusTime | Unset = UNSET
    hold: bool | Unset = UNSET
    priority: V0041OpenapiJobInfoRespJobsItemPriority | Unset = UNSET
    profile: list[V0041OpenapiJobInfoRespJobsItemProfileItem] | Unset = UNSET
    qos: str | Unset = UNSET
    reboot: bool | Unset = UNSET
    required_nodes: str | Unset = UNSET
    minimum_switches: int | Unset = UNSET
    requeue: bool | Unset = UNSET
    resize_time: V0041OpenapiJobInfoRespJobsItemResizeTime | Unset = UNSET
    restart_cnt: int | Unset = UNSET
    resv_name: str | Unset = UNSET
    scheduled_nodes: str | Unset = UNSET
    selinux_context: str | Unset = UNSET
    shared: list[V0041OpenapiJobInfoRespJobsItemSharedItem] | Unset = UNSET
    exclusive: list[V0041OpenapiJobInfoRespJobsItemExclusiveItem] | Unset = UNSET
    oversubscribe: bool | Unset = UNSET
    show_flags: list[V0041OpenapiJobInfoRespJobsItemShowFlagsItem] | Unset = UNSET
    sockets_per_board: int | Unset = UNSET
    sockets_per_node: V0041OpenapiJobInfoRespJobsItemSocketsPerNode | Unset = UNSET
    start_time: V0041OpenapiJobInfoRespJobsItemStartTime | Unset = UNSET
    state_description: str | Unset = UNSET
    state_reason: str | Unset = UNSET
    standard_error: str | Unset = UNSET
    standard_input: str | Unset = UNSET
    standard_output: str | Unset = UNSET
    submit_time: V0041OpenapiJobInfoRespJobsItemSubmitTime | Unset = UNSET
    suspend_time: V0041OpenapiJobInfoRespJobsItemSuspendTime | Unset = UNSET
    system_comment: str | Unset = UNSET
    time_limit: V0041OpenapiJobInfoRespJobsItemTimeLimit | Unset = UNSET
    time_minimum: V0041OpenapiJobInfoRespJobsItemTimeMinimum | Unset = UNSET
    threads_per_core: V0041OpenapiJobInfoRespJobsItemThreadsPerCore | Unset = UNSET
    tres_bind: str | Unset = UNSET
    tres_freq: str | Unset = UNSET
    tres_per_job: str | Unset = UNSET
    tres_per_node: str | Unset = UNSET
    tres_per_socket: str | Unset = UNSET
    tres_per_task: str | Unset = UNSET
    tres_req_str: str | Unset = UNSET
    tres_alloc_str: str | Unset = UNSET
    user_id: int | Unset = UNSET
    user_name: str | Unset = UNSET
    maximum_switch_wait_time: int | Unset = UNSET
    wckey: str | Unset = UNSET
    current_working_directory: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account = self.account

        accrue_time: dict[str, Any] | Unset = UNSET
        if not isinstance(self.accrue_time, Unset):
            accrue_time = self.accrue_time.to_dict()

        admin_comment = self.admin_comment

        allocating_node = self.allocating_node

        array_job_id: dict[str, Any] | Unset = UNSET
        if not isinstance(self.array_job_id, Unset):
            array_job_id = self.array_job_id.to_dict()

        array_task_id: dict[str, Any] | Unset = UNSET
        if not isinstance(self.array_task_id, Unset):
            array_task_id = self.array_task_id.to_dict()

        array_max_tasks: dict[str, Any] | Unset = UNSET
        if not isinstance(self.array_max_tasks, Unset):
            array_max_tasks = self.array_max_tasks.to_dict()

        array_task_string = self.array_task_string

        association_id = self.association_id

        batch_features = self.batch_features

        batch_flag = self.batch_flag

        batch_host = self.batch_host

        flags: list[str] | Unset = UNSET
        if not isinstance(self.flags, Unset):
            flags = []
            for flags_item_data in self.flags:
                flags_item = flags_item_data.value
                flags.append(flags_item)

        burst_buffer = self.burst_buffer

        burst_buffer_state = self.burst_buffer_state

        cluster = self.cluster

        cluster_features = self.cluster_features

        command = self.command

        comment = self.comment

        container = self.container

        container_id = self.container_id

        contiguous = self.contiguous

        core_spec = self.core_spec

        thread_spec = self.thread_spec

        cores_per_socket: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cores_per_socket, Unset):
            cores_per_socket = self.cores_per_socket.to_dict()

        billable_tres: dict[str, Any] | Unset = UNSET
        if not isinstance(self.billable_tres, Unset):
            billable_tres = self.billable_tres.to_dict()

        cpus_per_task: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cpus_per_task, Unset):
            cpus_per_task = self.cpus_per_task.to_dict()

        cpu_frequency_minimum: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cpu_frequency_minimum, Unset):
            cpu_frequency_minimum = self.cpu_frequency_minimum.to_dict()

        cpu_frequency_maximum: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cpu_frequency_maximum, Unset):
            cpu_frequency_maximum = self.cpu_frequency_maximum.to_dict()

        cpu_frequency_governor: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cpu_frequency_governor, Unset):
            cpu_frequency_governor = self.cpu_frequency_governor.to_dict()

        cpus_per_tres = self.cpus_per_tres

        cron = self.cron

        deadline: dict[str, Any] | Unset = UNSET
        if not isinstance(self.deadline, Unset):
            deadline = self.deadline.to_dict()

        delay_boot: dict[str, Any] | Unset = UNSET
        if not isinstance(self.delay_boot, Unset):
            delay_boot = self.delay_boot.to_dict()

        dependency = self.dependency

        derived_exit_code: dict[str, Any] | Unset = UNSET
        if not isinstance(self.derived_exit_code, Unset):
            derived_exit_code = self.derived_exit_code.to_dict()

        eligible_time: dict[str, Any] | Unset = UNSET
        if not isinstance(self.eligible_time, Unset):
            eligible_time = self.eligible_time.to_dict()

        end_time: dict[str, Any] | Unset = UNSET
        if not isinstance(self.end_time, Unset):
            end_time = self.end_time.to_dict()

        excluded_nodes = self.excluded_nodes

        exit_code: dict[str, Any] | Unset = UNSET
        if not isinstance(self.exit_code, Unset):
            exit_code = self.exit_code.to_dict()

        extra = self.extra

        failed_node = self.failed_node

        features = self.features

        federation_origin = self.federation_origin

        federation_siblings_active = self.federation_siblings_active

        federation_siblings_viable = self.federation_siblings_viable

        gres_detail: list[str] | Unset = UNSET
        if not isinstance(self.gres_detail, Unset):
            gres_detail = self.gres_detail

        group_id = self.group_id

        group_name = self.group_name

        het_job_id: dict[str, Any] | Unset = UNSET
        if not isinstance(self.het_job_id, Unset):
            het_job_id = self.het_job_id.to_dict()

        het_job_id_set = self.het_job_id_set

        het_job_offset: dict[str, Any] | Unset = UNSET
        if not isinstance(self.het_job_offset, Unset):
            het_job_offset = self.het_job_offset.to_dict()

        job_id = self.job_id

        job_resources: dict[str, Any] | Unset = UNSET
        if not isinstance(self.job_resources, Unset):
            job_resources = self.job_resources.to_dict()

        job_size_str: list[str] | Unset = UNSET
        if not isinstance(self.job_size_str, Unset):
            job_size_str = self.job_size_str

        job_state: list[str] | Unset = UNSET
        if not isinstance(self.job_state, Unset):
            job_state = []
            for job_state_item_data in self.job_state:
                job_state_item = job_state_item_data.value
                job_state.append(job_state_item)

        last_sched_evaluation: dict[str, Any] | Unset = UNSET
        if not isinstance(self.last_sched_evaluation, Unset):
            last_sched_evaluation = self.last_sched_evaluation.to_dict()

        licenses = self.licenses

        mail_type: list[str] | Unset = UNSET
        if not isinstance(self.mail_type, Unset):
            mail_type = []
            for mail_type_item_data in self.mail_type:
                mail_type_item = mail_type_item_data.value
                mail_type.append(mail_type_item)

        mail_user = self.mail_user

        max_cpus: dict[str, Any] | Unset = UNSET
        if not isinstance(self.max_cpus, Unset):
            max_cpus = self.max_cpus.to_dict()

        max_nodes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.max_nodes, Unset):
            max_nodes = self.max_nodes.to_dict()

        mcs_label = self.mcs_label

        memory_per_tres = self.memory_per_tres

        name = self.name

        network = self.network

        nodes = self.nodes

        nice = self.nice

        tasks_per_core: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tasks_per_core, Unset):
            tasks_per_core = self.tasks_per_core.to_dict()

        tasks_per_tres: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tasks_per_tres, Unset):
            tasks_per_tres = self.tasks_per_tres.to_dict()

        tasks_per_node: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tasks_per_node, Unset):
            tasks_per_node = self.tasks_per_node.to_dict()

        tasks_per_socket: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tasks_per_socket, Unset):
            tasks_per_socket = self.tasks_per_socket.to_dict()

        tasks_per_board: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tasks_per_board, Unset):
            tasks_per_board = self.tasks_per_board.to_dict()

        cpus: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cpus, Unset):
            cpus = self.cpus.to_dict()

        node_count: dict[str, Any] | Unset = UNSET
        if not isinstance(self.node_count, Unset):
            node_count = self.node_count.to_dict()

        tasks: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tasks, Unset):
            tasks = self.tasks.to_dict()

        partition = self.partition

        prefer = self.prefer

        memory_per_cpu: dict[str, Any] | Unset = UNSET
        if not isinstance(self.memory_per_cpu, Unset):
            memory_per_cpu = self.memory_per_cpu.to_dict()

        memory_per_node: dict[str, Any] | Unset = UNSET
        if not isinstance(self.memory_per_node, Unset):
            memory_per_node = self.memory_per_node.to_dict()

        minimum_cpus_per_node: dict[str, Any] | Unset = UNSET
        if not isinstance(self.minimum_cpus_per_node, Unset):
            minimum_cpus_per_node = self.minimum_cpus_per_node.to_dict()

        minimum_tmp_disk_per_node: dict[str, Any] | Unset = UNSET
        if not isinstance(self.minimum_tmp_disk_per_node, Unset):
            minimum_tmp_disk_per_node = self.minimum_tmp_disk_per_node.to_dict()

        power: dict[str, Any] | Unset = UNSET
        if not isinstance(self.power, Unset):
            power = self.power.to_dict()

        preempt_time: dict[str, Any] | Unset = UNSET
        if not isinstance(self.preempt_time, Unset):
            preempt_time = self.preempt_time.to_dict()

        preemptable_time: dict[str, Any] | Unset = UNSET
        if not isinstance(self.preemptable_time, Unset):
            preemptable_time = self.preemptable_time.to_dict()

        pre_sus_time: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pre_sus_time, Unset):
            pre_sus_time = self.pre_sus_time.to_dict()

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

        required_nodes = self.required_nodes

        minimum_switches = self.minimum_switches

        requeue = self.requeue

        resize_time: dict[str, Any] | Unset = UNSET
        if not isinstance(self.resize_time, Unset):
            resize_time = self.resize_time.to_dict()

        restart_cnt = self.restart_cnt

        resv_name = self.resv_name

        scheduled_nodes = self.scheduled_nodes

        selinux_context = self.selinux_context

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

        show_flags: list[str] | Unset = UNSET
        if not isinstance(self.show_flags, Unset):
            show_flags = []
            for show_flags_item_data in self.show_flags:
                show_flags_item = show_flags_item_data.value
                show_flags.append(show_flags_item)

        sockets_per_board = self.sockets_per_board

        sockets_per_node: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sockets_per_node, Unset):
            sockets_per_node = self.sockets_per_node.to_dict()

        start_time: dict[str, Any] | Unset = UNSET
        if not isinstance(self.start_time, Unset):
            start_time = self.start_time.to_dict()

        state_description = self.state_description

        state_reason = self.state_reason

        standard_error = self.standard_error

        standard_input = self.standard_input

        standard_output = self.standard_output

        submit_time: dict[str, Any] | Unset = UNSET
        if not isinstance(self.submit_time, Unset):
            submit_time = self.submit_time.to_dict()

        suspend_time: dict[str, Any] | Unset = UNSET
        if not isinstance(self.suspend_time, Unset):
            suspend_time = self.suspend_time.to_dict()

        system_comment = self.system_comment

        time_limit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.time_limit, Unset):
            time_limit = self.time_limit.to_dict()

        time_minimum: dict[str, Any] | Unset = UNSET
        if not isinstance(self.time_minimum, Unset):
            time_minimum = self.time_minimum.to_dict()

        threads_per_core: dict[str, Any] | Unset = UNSET
        if not isinstance(self.threads_per_core, Unset):
            threads_per_core = self.threads_per_core.to_dict()

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

        maximum_switch_wait_time = self.maximum_switch_wait_time

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
        if allocating_node is not UNSET:
            field_dict["allocating_node"] = allocating_node
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
        if container is not UNSET:
            field_dict["container"] = container
        if container_id is not UNSET:
            field_dict["container_id"] = container_id
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
        if cron is not UNSET:
            field_dict["cron"] = cron
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
        if extra is not UNSET:
            field_dict["extra"] = extra
        if failed_node is not UNSET:
            field_dict["failed_node"] = failed_node
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
        if group_name is not UNSET:
            field_dict["group_name"] = group_name
        if het_job_id is not UNSET:
            field_dict["het_job_id"] = het_job_id
        if het_job_id_set is not UNSET:
            field_dict["het_job_id_set"] = het_job_id_set
        if het_job_offset is not UNSET:
            field_dict["het_job_offset"] = het_job_offset
        if job_id is not UNSET:
            field_dict["job_id"] = job_id
        if job_resources is not UNSET:
            field_dict["job_resources"] = job_resources
        if job_size_str is not UNSET:
            field_dict["job_size_str"] = job_size_str
        if job_state is not UNSET:
            field_dict["job_state"] = job_state
        if last_sched_evaluation is not UNSET:
            field_dict["last_sched_evaluation"] = last_sched_evaluation
        if licenses is not UNSET:
            field_dict["licenses"] = licenses
        if mail_type is not UNSET:
            field_dict["mail_type"] = mail_type
        if mail_user is not UNSET:
            field_dict["mail_user"] = mail_user
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
        if network is not UNSET:
            field_dict["network"] = network
        if nodes is not UNSET:
            field_dict["nodes"] = nodes
        if nice is not UNSET:
            field_dict["nice"] = nice
        if tasks_per_core is not UNSET:
            field_dict["tasks_per_core"] = tasks_per_core
        if tasks_per_tres is not UNSET:
            field_dict["tasks_per_tres"] = tasks_per_tres
        if tasks_per_node is not UNSET:
            field_dict["tasks_per_node"] = tasks_per_node
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
        if partition is not UNSET:
            field_dict["partition"] = partition
        if prefer is not UNSET:
            field_dict["prefer"] = prefer
        if memory_per_cpu is not UNSET:
            field_dict["memory_per_cpu"] = memory_per_cpu
        if memory_per_node is not UNSET:
            field_dict["memory_per_node"] = memory_per_node
        if minimum_cpus_per_node is not UNSET:
            field_dict["minimum_cpus_per_node"] = minimum_cpus_per_node
        if minimum_tmp_disk_per_node is not UNSET:
            field_dict["minimum_tmp_disk_per_node"] = minimum_tmp_disk_per_node
        if power is not UNSET:
            field_dict["power"] = power
        if preempt_time is not UNSET:
            field_dict["preempt_time"] = preempt_time
        if preemptable_time is not UNSET:
            field_dict["preemptable_time"] = preemptable_time
        if pre_sus_time is not UNSET:
            field_dict["pre_sus_time"] = pre_sus_time
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
        if minimum_switches is not UNSET:
            field_dict["minimum_switches"] = minimum_switches
        if requeue is not UNSET:
            field_dict["requeue"] = requeue
        if resize_time is not UNSET:
            field_dict["resize_time"] = resize_time
        if restart_cnt is not UNSET:
            field_dict["restart_cnt"] = restart_cnt
        if resv_name is not UNSET:
            field_dict["resv_name"] = resv_name
        if scheduled_nodes is not UNSET:
            field_dict["scheduled_nodes"] = scheduled_nodes
        if selinux_context is not UNSET:
            field_dict["selinux_context"] = selinux_context
        if shared is not UNSET:
            field_dict["shared"] = shared
        if exclusive is not UNSET:
            field_dict["exclusive"] = exclusive
        if oversubscribe is not UNSET:
            field_dict["oversubscribe"] = oversubscribe
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
        if maximum_switch_wait_time is not UNSET:
            field_dict["maximum_switch_wait_time"] = maximum_switch_wait_time
        if wckey is not UNSET:
            field_dict["wckey"] = wckey
        if current_working_directory is not UNSET:
            field_dict["current_working_directory"] = current_working_directory

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v0041_openapi_job_info_resp_jobs_item_accrue_time import V0041OpenapiJobInfoRespJobsItemAccrueTime
        from ..models.v0041_openapi_job_info_resp_jobs_item_array_job_id import (
            V0041OpenapiJobInfoRespJobsItemArrayJobId,
        )
        from ..models.v0041_openapi_job_info_resp_jobs_item_array_max_tasks import (
            V0041OpenapiJobInfoRespJobsItemArrayMaxTasks,
        )
        from ..models.v0041_openapi_job_info_resp_jobs_item_array_task_id import (
            V0041OpenapiJobInfoRespJobsItemArrayTaskId,
        )
        from ..models.v0041_openapi_job_info_resp_jobs_item_billable_tres import (
            V0041OpenapiJobInfoRespJobsItemBillableTres,
        )
        from ..models.v0041_openapi_job_info_resp_jobs_item_cores_per_socket import (
            V0041OpenapiJobInfoRespJobsItemCoresPerSocket,
        )
        from ..models.v0041_openapi_job_info_resp_jobs_item_cpu_frequency_governor import (
            V0041OpenapiJobInfoRespJobsItemCpuFrequencyGovernor,
        )
        from ..models.v0041_openapi_job_info_resp_jobs_item_cpu_frequency_maximum import (
            V0041OpenapiJobInfoRespJobsItemCpuFrequencyMaximum,
        )
        from ..models.v0041_openapi_job_info_resp_jobs_item_cpu_frequency_minimum import (
            V0041OpenapiJobInfoRespJobsItemCpuFrequencyMinimum,
        )
        from ..models.v0041_openapi_job_info_resp_jobs_item_cpus import V0041OpenapiJobInfoRespJobsItemCpus
        from ..models.v0041_openapi_job_info_resp_jobs_item_cpus_per_task import (
            V0041OpenapiJobInfoRespJobsItemCpusPerTask,
        )
        from ..models.v0041_openapi_job_info_resp_jobs_item_deadline import V0041OpenapiJobInfoRespJobsItemDeadline
        from ..models.v0041_openapi_job_info_resp_jobs_item_delay_boot import V0041OpenapiJobInfoRespJobsItemDelayBoot
        from ..models.v0041_openapi_job_info_resp_jobs_item_derived_exit_code import (
            V0041OpenapiJobInfoRespJobsItemDerivedExitCode,
        )
        from ..models.v0041_openapi_job_info_resp_jobs_item_eligible_time import (
            V0041OpenapiJobInfoRespJobsItemEligibleTime,
        )
        from ..models.v0041_openapi_job_info_resp_jobs_item_end_time import V0041OpenapiJobInfoRespJobsItemEndTime
        from ..models.v0041_openapi_job_info_resp_jobs_item_exit_code import V0041OpenapiJobInfoRespJobsItemExitCode
        from ..models.v0041_openapi_job_info_resp_jobs_item_het_job_id import V0041OpenapiJobInfoRespJobsItemHetJobId
        from ..models.v0041_openapi_job_info_resp_jobs_item_het_job_offset import (
            V0041OpenapiJobInfoRespJobsItemHetJobOffset,
        )
        from ..models.v0041_openapi_job_info_resp_jobs_item_job_resources import (
            V0041OpenapiJobInfoRespJobsItemJobResources,
        )
        from ..models.v0041_openapi_job_info_resp_jobs_item_last_sched_evaluation import (
            V0041OpenapiJobInfoRespJobsItemLastSchedEvaluation,
        )
        from ..models.v0041_openapi_job_info_resp_jobs_item_max_cpus import V0041OpenapiJobInfoRespJobsItemMaxCpus
        from ..models.v0041_openapi_job_info_resp_jobs_item_max_nodes import V0041OpenapiJobInfoRespJobsItemMaxNodes
        from ..models.v0041_openapi_job_info_resp_jobs_item_memory_per_cpu import (
            V0041OpenapiJobInfoRespJobsItemMemoryPerCpu,
        )
        from ..models.v0041_openapi_job_info_resp_jobs_item_memory_per_node import (
            V0041OpenapiJobInfoRespJobsItemMemoryPerNode,
        )
        from ..models.v0041_openapi_job_info_resp_jobs_item_minimum_cpus_per_node import (
            V0041OpenapiJobInfoRespJobsItemMinimumCpusPerNode,
        )
        from ..models.v0041_openapi_job_info_resp_jobs_item_minimum_tmp_disk_per_node import (
            V0041OpenapiJobInfoRespJobsItemMinimumTmpDiskPerNode,
        )
        from ..models.v0041_openapi_job_info_resp_jobs_item_node_count import V0041OpenapiJobInfoRespJobsItemNodeCount
        from ..models.v0041_openapi_job_info_resp_jobs_item_power import V0041OpenapiJobInfoRespJobsItemPower
        from ..models.v0041_openapi_job_info_resp_jobs_item_pre_sus_time import (
            V0041OpenapiJobInfoRespJobsItemPreSusTime,
        )
        from ..models.v0041_openapi_job_info_resp_jobs_item_preempt_time import (
            V0041OpenapiJobInfoRespJobsItemPreemptTime,
        )
        from ..models.v0041_openapi_job_info_resp_jobs_item_preemptable_time import (
            V0041OpenapiJobInfoRespJobsItemPreemptableTime,
        )
        from ..models.v0041_openapi_job_info_resp_jobs_item_priority import V0041OpenapiJobInfoRespJobsItemPriority
        from ..models.v0041_openapi_job_info_resp_jobs_item_resize_time import V0041OpenapiJobInfoRespJobsItemResizeTime
        from ..models.v0041_openapi_job_info_resp_jobs_item_sockets_per_node import (
            V0041OpenapiJobInfoRespJobsItemSocketsPerNode,
        )
        from ..models.v0041_openapi_job_info_resp_jobs_item_start_time import V0041OpenapiJobInfoRespJobsItemStartTime
        from ..models.v0041_openapi_job_info_resp_jobs_item_submit_time import V0041OpenapiJobInfoRespJobsItemSubmitTime
        from ..models.v0041_openapi_job_info_resp_jobs_item_suspend_time import (
            V0041OpenapiJobInfoRespJobsItemSuspendTime,
        )
        from ..models.v0041_openapi_job_info_resp_jobs_item_tasks import V0041OpenapiJobInfoRespJobsItemTasks
        from ..models.v0041_openapi_job_info_resp_jobs_item_tasks_per_board import (
            V0041OpenapiJobInfoRespJobsItemTasksPerBoard,
        )
        from ..models.v0041_openapi_job_info_resp_jobs_item_tasks_per_core import (
            V0041OpenapiJobInfoRespJobsItemTasksPerCore,
        )
        from ..models.v0041_openapi_job_info_resp_jobs_item_tasks_per_node import (
            V0041OpenapiJobInfoRespJobsItemTasksPerNode,
        )
        from ..models.v0041_openapi_job_info_resp_jobs_item_tasks_per_socket import (
            V0041OpenapiJobInfoRespJobsItemTasksPerSocket,
        )
        from ..models.v0041_openapi_job_info_resp_jobs_item_tasks_per_tres import (
            V0041OpenapiJobInfoRespJobsItemTasksPerTres,
        )
        from ..models.v0041_openapi_job_info_resp_jobs_item_threads_per_core import (
            V0041OpenapiJobInfoRespJobsItemThreadsPerCore,
        )
        from ..models.v0041_openapi_job_info_resp_jobs_item_time_limit import V0041OpenapiJobInfoRespJobsItemTimeLimit
        from ..models.v0041_openapi_job_info_resp_jobs_item_time_minimum import (
            V0041OpenapiJobInfoRespJobsItemTimeMinimum,
        )

        d = dict(src_dict)
        account = d.pop("account", UNSET)

        _accrue_time = d.pop("accrue_time", UNSET)
        accrue_time: V0041OpenapiJobInfoRespJobsItemAccrueTime | Unset
        if isinstance(_accrue_time, Unset):
            accrue_time = UNSET
        else:
            accrue_time = V0041OpenapiJobInfoRespJobsItemAccrueTime.from_dict(_accrue_time)

        admin_comment = d.pop("admin_comment", UNSET)

        allocating_node = d.pop("allocating_node", UNSET)

        _array_job_id = d.pop("array_job_id", UNSET)
        array_job_id: V0041OpenapiJobInfoRespJobsItemArrayJobId | Unset
        if isinstance(_array_job_id, Unset):
            array_job_id = UNSET
        else:
            array_job_id = V0041OpenapiJobInfoRespJobsItemArrayJobId.from_dict(_array_job_id)

        _array_task_id = d.pop("array_task_id", UNSET)
        array_task_id: V0041OpenapiJobInfoRespJobsItemArrayTaskId | Unset
        if isinstance(_array_task_id, Unset):
            array_task_id = UNSET
        else:
            array_task_id = V0041OpenapiJobInfoRespJobsItemArrayTaskId.from_dict(_array_task_id)

        _array_max_tasks = d.pop("array_max_tasks", UNSET)
        array_max_tasks: V0041OpenapiJobInfoRespJobsItemArrayMaxTasks | Unset
        if isinstance(_array_max_tasks, Unset):
            array_max_tasks = UNSET
        else:
            array_max_tasks = V0041OpenapiJobInfoRespJobsItemArrayMaxTasks.from_dict(_array_max_tasks)

        array_task_string = d.pop("array_task_string", UNSET)

        association_id = d.pop("association_id", UNSET)

        batch_features = d.pop("batch_features", UNSET)

        batch_flag = d.pop("batch_flag", UNSET)

        batch_host = d.pop("batch_host", UNSET)

        _flags = d.pop("flags", UNSET)
        flags: list[V0041OpenapiJobInfoRespJobsItemFlagsItem] | Unset = UNSET
        if _flags is not UNSET:
            flags = []
            for flags_item_data in _flags:
                flags_item = V0041OpenapiJobInfoRespJobsItemFlagsItem(flags_item_data)

                flags.append(flags_item)

        burst_buffer = d.pop("burst_buffer", UNSET)

        burst_buffer_state = d.pop("burst_buffer_state", UNSET)

        cluster = d.pop("cluster", UNSET)

        cluster_features = d.pop("cluster_features", UNSET)

        command = d.pop("command", UNSET)

        comment = d.pop("comment", UNSET)

        container = d.pop("container", UNSET)

        container_id = d.pop("container_id", UNSET)

        contiguous = d.pop("contiguous", UNSET)

        core_spec = d.pop("core_spec", UNSET)

        thread_spec = d.pop("thread_spec", UNSET)

        _cores_per_socket = d.pop("cores_per_socket", UNSET)
        cores_per_socket: V0041OpenapiJobInfoRespJobsItemCoresPerSocket | Unset
        if isinstance(_cores_per_socket, Unset):
            cores_per_socket = UNSET
        else:
            cores_per_socket = V0041OpenapiJobInfoRespJobsItemCoresPerSocket.from_dict(_cores_per_socket)

        _billable_tres = d.pop("billable_tres", UNSET)
        billable_tres: V0041OpenapiJobInfoRespJobsItemBillableTres | Unset
        if isinstance(_billable_tres, Unset):
            billable_tres = UNSET
        else:
            billable_tres = V0041OpenapiJobInfoRespJobsItemBillableTres.from_dict(_billable_tres)

        _cpus_per_task = d.pop("cpus_per_task", UNSET)
        cpus_per_task: V0041OpenapiJobInfoRespJobsItemCpusPerTask | Unset
        if isinstance(_cpus_per_task, Unset):
            cpus_per_task = UNSET
        else:
            cpus_per_task = V0041OpenapiJobInfoRespJobsItemCpusPerTask.from_dict(_cpus_per_task)

        _cpu_frequency_minimum = d.pop("cpu_frequency_minimum", UNSET)
        cpu_frequency_minimum: V0041OpenapiJobInfoRespJobsItemCpuFrequencyMinimum | Unset
        if isinstance(_cpu_frequency_minimum, Unset):
            cpu_frequency_minimum = UNSET
        else:
            cpu_frequency_minimum = V0041OpenapiJobInfoRespJobsItemCpuFrequencyMinimum.from_dict(_cpu_frequency_minimum)

        _cpu_frequency_maximum = d.pop("cpu_frequency_maximum", UNSET)
        cpu_frequency_maximum: V0041OpenapiJobInfoRespJobsItemCpuFrequencyMaximum | Unset
        if isinstance(_cpu_frequency_maximum, Unset):
            cpu_frequency_maximum = UNSET
        else:
            cpu_frequency_maximum = V0041OpenapiJobInfoRespJobsItemCpuFrequencyMaximum.from_dict(_cpu_frequency_maximum)

        _cpu_frequency_governor = d.pop("cpu_frequency_governor", UNSET)
        cpu_frequency_governor: V0041OpenapiJobInfoRespJobsItemCpuFrequencyGovernor | Unset
        if isinstance(_cpu_frequency_governor, Unset):
            cpu_frequency_governor = UNSET
        else:
            cpu_frequency_governor = V0041OpenapiJobInfoRespJobsItemCpuFrequencyGovernor.from_dict(
                _cpu_frequency_governor
            )

        cpus_per_tres = d.pop("cpus_per_tres", UNSET)

        cron = d.pop("cron", UNSET)

        _deadline = d.pop("deadline", UNSET)
        deadline: V0041OpenapiJobInfoRespJobsItemDeadline | Unset
        if isinstance(_deadline, Unset):
            deadline = UNSET
        else:
            deadline = V0041OpenapiJobInfoRespJobsItemDeadline.from_dict(_deadline)

        _delay_boot = d.pop("delay_boot", UNSET)
        delay_boot: V0041OpenapiJobInfoRespJobsItemDelayBoot | Unset
        if isinstance(_delay_boot, Unset):
            delay_boot = UNSET
        else:
            delay_boot = V0041OpenapiJobInfoRespJobsItemDelayBoot.from_dict(_delay_boot)

        dependency = d.pop("dependency", UNSET)

        _derived_exit_code = d.pop("derived_exit_code", UNSET)
        derived_exit_code: V0041OpenapiJobInfoRespJobsItemDerivedExitCode | Unset
        if isinstance(_derived_exit_code, Unset):
            derived_exit_code = UNSET
        else:
            derived_exit_code = V0041OpenapiJobInfoRespJobsItemDerivedExitCode.from_dict(_derived_exit_code)

        _eligible_time = d.pop("eligible_time", UNSET)
        eligible_time: V0041OpenapiJobInfoRespJobsItemEligibleTime | Unset
        if isinstance(_eligible_time, Unset):
            eligible_time = UNSET
        else:
            eligible_time = V0041OpenapiJobInfoRespJobsItemEligibleTime.from_dict(_eligible_time)

        _end_time = d.pop("end_time", UNSET)
        end_time: V0041OpenapiJobInfoRespJobsItemEndTime | Unset
        if isinstance(_end_time, Unset):
            end_time = UNSET
        else:
            end_time = V0041OpenapiJobInfoRespJobsItemEndTime.from_dict(_end_time)

        excluded_nodes = d.pop("excluded_nodes", UNSET)

        _exit_code = d.pop("exit_code", UNSET)
        exit_code: V0041OpenapiJobInfoRespJobsItemExitCode | Unset
        if isinstance(_exit_code, Unset):
            exit_code = UNSET
        else:
            exit_code = V0041OpenapiJobInfoRespJobsItemExitCode.from_dict(_exit_code)

        extra = d.pop("extra", UNSET)

        failed_node = d.pop("failed_node", UNSET)

        features = d.pop("features", UNSET)

        federation_origin = d.pop("federation_origin", UNSET)

        federation_siblings_active = d.pop("federation_siblings_active", UNSET)

        federation_siblings_viable = d.pop("federation_siblings_viable", UNSET)

        gres_detail = cast(list[str], d.pop("gres_detail", UNSET))

        group_id = d.pop("group_id", UNSET)

        group_name = d.pop("group_name", UNSET)

        _het_job_id = d.pop("het_job_id", UNSET)
        het_job_id: V0041OpenapiJobInfoRespJobsItemHetJobId | Unset
        if isinstance(_het_job_id, Unset):
            het_job_id = UNSET
        else:
            het_job_id = V0041OpenapiJobInfoRespJobsItemHetJobId.from_dict(_het_job_id)

        het_job_id_set = d.pop("het_job_id_set", UNSET)

        _het_job_offset = d.pop("het_job_offset", UNSET)
        het_job_offset: V0041OpenapiJobInfoRespJobsItemHetJobOffset | Unset
        if isinstance(_het_job_offset, Unset):
            het_job_offset = UNSET
        else:
            het_job_offset = V0041OpenapiJobInfoRespJobsItemHetJobOffset.from_dict(_het_job_offset)

        job_id = d.pop("job_id", UNSET)

        _job_resources = d.pop("job_resources", UNSET)
        job_resources: V0041OpenapiJobInfoRespJobsItemJobResources | Unset
        if isinstance(_job_resources, Unset):
            job_resources = UNSET
        else:
            job_resources = V0041OpenapiJobInfoRespJobsItemJobResources.from_dict(_job_resources)

        job_size_str = cast(list[str], d.pop("job_size_str", UNSET))

        _job_state = d.pop("job_state", UNSET)
        job_state: list[V0041OpenapiJobInfoRespJobsItemJobStateItem] | Unset = UNSET
        if _job_state is not UNSET:
            job_state = []
            for job_state_item_data in _job_state:
                job_state_item = V0041OpenapiJobInfoRespJobsItemJobStateItem(job_state_item_data)

                job_state.append(job_state_item)

        _last_sched_evaluation = d.pop("last_sched_evaluation", UNSET)
        last_sched_evaluation: V0041OpenapiJobInfoRespJobsItemLastSchedEvaluation | Unset
        if isinstance(_last_sched_evaluation, Unset):
            last_sched_evaluation = UNSET
        else:
            last_sched_evaluation = V0041OpenapiJobInfoRespJobsItemLastSchedEvaluation.from_dict(_last_sched_evaluation)

        licenses = d.pop("licenses", UNSET)

        _mail_type = d.pop("mail_type", UNSET)
        mail_type: list[V0041OpenapiJobInfoRespJobsItemMailTypeItem] | Unset = UNSET
        if _mail_type is not UNSET:
            mail_type = []
            for mail_type_item_data in _mail_type:
                mail_type_item = V0041OpenapiJobInfoRespJobsItemMailTypeItem(mail_type_item_data)

                mail_type.append(mail_type_item)

        mail_user = d.pop("mail_user", UNSET)

        _max_cpus = d.pop("max_cpus", UNSET)
        max_cpus: V0041OpenapiJobInfoRespJobsItemMaxCpus | Unset
        if isinstance(_max_cpus, Unset):
            max_cpus = UNSET
        else:
            max_cpus = V0041OpenapiJobInfoRespJobsItemMaxCpus.from_dict(_max_cpus)

        _max_nodes = d.pop("max_nodes", UNSET)
        max_nodes: V0041OpenapiJobInfoRespJobsItemMaxNodes | Unset
        if isinstance(_max_nodes, Unset):
            max_nodes = UNSET
        else:
            max_nodes = V0041OpenapiJobInfoRespJobsItemMaxNodes.from_dict(_max_nodes)

        mcs_label = d.pop("mcs_label", UNSET)

        memory_per_tres = d.pop("memory_per_tres", UNSET)

        name = d.pop("name", UNSET)

        network = d.pop("network", UNSET)

        nodes = d.pop("nodes", UNSET)

        nice = d.pop("nice", UNSET)

        _tasks_per_core = d.pop("tasks_per_core", UNSET)
        tasks_per_core: V0041OpenapiJobInfoRespJobsItemTasksPerCore | Unset
        if isinstance(_tasks_per_core, Unset):
            tasks_per_core = UNSET
        else:
            tasks_per_core = V0041OpenapiJobInfoRespJobsItemTasksPerCore.from_dict(_tasks_per_core)

        _tasks_per_tres = d.pop("tasks_per_tres", UNSET)
        tasks_per_tres: V0041OpenapiJobInfoRespJobsItemTasksPerTres | Unset
        if isinstance(_tasks_per_tres, Unset):
            tasks_per_tres = UNSET
        else:
            tasks_per_tres = V0041OpenapiJobInfoRespJobsItemTasksPerTres.from_dict(_tasks_per_tres)

        _tasks_per_node = d.pop("tasks_per_node", UNSET)
        tasks_per_node: V0041OpenapiJobInfoRespJobsItemTasksPerNode | Unset
        if isinstance(_tasks_per_node, Unset):
            tasks_per_node = UNSET
        else:
            tasks_per_node = V0041OpenapiJobInfoRespJobsItemTasksPerNode.from_dict(_tasks_per_node)

        _tasks_per_socket = d.pop("tasks_per_socket", UNSET)
        tasks_per_socket: V0041OpenapiJobInfoRespJobsItemTasksPerSocket | Unset
        if isinstance(_tasks_per_socket, Unset):
            tasks_per_socket = UNSET
        else:
            tasks_per_socket = V0041OpenapiJobInfoRespJobsItemTasksPerSocket.from_dict(_tasks_per_socket)

        _tasks_per_board = d.pop("tasks_per_board", UNSET)
        tasks_per_board: V0041OpenapiJobInfoRespJobsItemTasksPerBoard | Unset
        if isinstance(_tasks_per_board, Unset):
            tasks_per_board = UNSET
        else:
            tasks_per_board = V0041OpenapiJobInfoRespJobsItemTasksPerBoard.from_dict(_tasks_per_board)

        _cpus = d.pop("cpus", UNSET)
        cpus: V0041OpenapiJobInfoRespJobsItemCpus | Unset
        if isinstance(_cpus, Unset):
            cpus = UNSET
        else:
            cpus = V0041OpenapiJobInfoRespJobsItemCpus.from_dict(_cpus)

        _node_count = d.pop("node_count", UNSET)
        node_count: V0041OpenapiJobInfoRespJobsItemNodeCount | Unset
        if isinstance(_node_count, Unset):
            node_count = UNSET
        else:
            node_count = V0041OpenapiJobInfoRespJobsItemNodeCount.from_dict(_node_count)

        _tasks = d.pop("tasks", UNSET)
        tasks: V0041OpenapiJobInfoRespJobsItemTasks | Unset
        if isinstance(_tasks, Unset):
            tasks = UNSET
        else:
            tasks = V0041OpenapiJobInfoRespJobsItemTasks.from_dict(_tasks)

        partition = d.pop("partition", UNSET)

        prefer = d.pop("prefer", UNSET)

        _memory_per_cpu = d.pop("memory_per_cpu", UNSET)
        memory_per_cpu: V0041OpenapiJobInfoRespJobsItemMemoryPerCpu | Unset
        if isinstance(_memory_per_cpu, Unset):
            memory_per_cpu = UNSET
        else:
            memory_per_cpu = V0041OpenapiJobInfoRespJobsItemMemoryPerCpu.from_dict(_memory_per_cpu)

        _memory_per_node = d.pop("memory_per_node", UNSET)
        memory_per_node: V0041OpenapiJobInfoRespJobsItemMemoryPerNode | Unset
        if isinstance(_memory_per_node, Unset):
            memory_per_node = UNSET
        else:
            memory_per_node = V0041OpenapiJobInfoRespJobsItemMemoryPerNode.from_dict(_memory_per_node)

        _minimum_cpus_per_node = d.pop("minimum_cpus_per_node", UNSET)
        minimum_cpus_per_node: V0041OpenapiJobInfoRespJobsItemMinimumCpusPerNode | Unset
        if isinstance(_minimum_cpus_per_node, Unset):
            minimum_cpus_per_node = UNSET
        else:
            minimum_cpus_per_node = V0041OpenapiJobInfoRespJobsItemMinimumCpusPerNode.from_dict(_minimum_cpus_per_node)

        _minimum_tmp_disk_per_node = d.pop("minimum_tmp_disk_per_node", UNSET)
        minimum_tmp_disk_per_node: V0041OpenapiJobInfoRespJobsItemMinimumTmpDiskPerNode | Unset
        if isinstance(_minimum_tmp_disk_per_node, Unset):
            minimum_tmp_disk_per_node = UNSET
        else:
            minimum_tmp_disk_per_node = V0041OpenapiJobInfoRespJobsItemMinimumTmpDiskPerNode.from_dict(
                _minimum_tmp_disk_per_node
            )

        _power = d.pop("power", UNSET)
        power: V0041OpenapiJobInfoRespJobsItemPower | Unset
        if isinstance(_power, Unset):
            power = UNSET
        else:
            power = V0041OpenapiJobInfoRespJobsItemPower.from_dict(_power)

        _preempt_time = d.pop("preempt_time", UNSET)
        preempt_time: V0041OpenapiJobInfoRespJobsItemPreemptTime | Unset
        if isinstance(_preempt_time, Unset):
            preempt_time = UNSET
        else:
            preempt_time = V0041OpenapiJobInfoRespJobsItemPreemptTime.from_dict(_preempt_time)

        _preemptable_time = d.pop("preemptable_time", UNSET)
        preemptable_time: V0041OpenapiJobInfoRespJobsItemPreemptableTime | Unset
        if isinstance(_preemptable_time, Unset):
            preemptable_time = UNSET
        else:
            preemptable_time = V0041OpenapiJobInfoRespJobsItemPreemptableTime.from_dict(_preemptable_time)

        _pre_sus_time = d.pop("pre_sus_time", UNSET)
        pre_sus_time: V0041OpenapiJobInfoRespJobsItemPreSusTime | Unset
        if isinstance(_pre_sus_time, Unset):
            pre_sus_time = UNSET
        else:
            pre_sus_time = V0041OpenapiJobInfoRespJobsItemPreSusTime.from_dict(_pre_sus_time)

        hold = d.pop("hold", UNSET)

        _priority = d.pop("priority", UNSET)
        priority: V0041OpenapiJobInfoRespJobsItemPriority | Unset
        if isinstance(_priority, Unset):
            priority = UNSET
        else:
            priority = V0041OpenapiJobInfoRespJobsItemPriority.from_dict(_priority)

        _profile = d.pop("profile", UNSET)
        profile: list[V0041OpenapiJobInfoRespJobsItemProfileItem] | Unset = UNSET
        if _profile is not UNSET:
            profile = []
            for profile_item_data in _profile:
                profile_item = V0041OpenapiJobInfoRespJobsItemProfileItem(profile_item_data)

                profile.append(profile_item)

        qos = d.pop("qos", UNSET)

        reboot = d.pop("reboot", UNSET)

        required_nodes = d.pop("required_nodes", UNSET)

        minimum_switches = d.pop("minimum_switches", UNSET)

        requeue = d.pop("requeue", UNSET)

        _resize_time = d.pop("resize_time", UNSET)
        resize_time: V0041OpenapiJobInfoRespJobsItemResizeTime | Unset
        if isinstance(_resize_time, Unset):
            resize_time = UNSET
        else:
            resize_time = V0041OpenapiJobInfoRespJobsItemResizeTime.from_dict(_resize_time)

        restart_cnt = d.pop("restart_cnt", UNSET)

        resv_name = d.pop("resv_name", UNSET)

        scheduled_nodes = d.pop("scheduled_nodes", UNSET)

        selinux_context = d.pop("selinux_context", UNSET)

        _shared = d.pop("shared", UNSET)
        shared: list[V0041OpenapiJobInfoRespJobsItemSharedItem] | Unset = UNSET
        if _shared is not UNSET:
            shared = []
            for shared_item_data in _shared:
                shared_item = V0041OpenapiJobInfoRespJobsItemSharedItem(shared_item_data)

                shared.append(shared_item)

        _exclusive = d.pop("exclusive", UNSET)
        exclusive: list[V0041OpenapiJobInfoRespJobsItemExclusiveItem] | Unset = UNSET
        if _exclusive is not UNSET:
            exclusive = []
            for exclusive_item_data in _exclusive:
                exclusive_item = V0041OpenapiJobInfoRespJobsItemExclusiveItem(exclusive_item_data)

                exclusive.append(exclusive_item)

        oversubscribe = d.pop("oversubscribe", UNSET)

        _show_flags = d.pop("show_flags", UNSET)
        show_flags: list[V0041OpenapiJobInfoRespJobsItemShowFlagsItem] | Unset = UNSET
        if _show_flags is not UNSET:
            show_flags = []
            for show_flags_item_data in _show_flags:
                show_flags_item = V0041OpenapiJobInfoRespJobsItemShowFlagsItem(show_flags_item_data)

                show_flags.append(show_flags_item)

        sockets_per_board = d.pop("sockets_per_board", UNSET)

        _sockets_per_node = d.pop("sockets_per_node", UNSET)
        sockets_per_node: V0041OpenapiJobInfoRespJobsItemSocketsPerNode | Unset
        if isinstance(_sockets_per_node, Unset):
            sockets_per_node = UNSET
        else:
            sockets_per_node = V0041OpenapiJobInfoRespJobsItemSocketsPerNode.from_dict(_sockets_per_node)

        _start_time = d.pop("start_time", UNSET)
        start_time: V0041OpenapiJobInfoRespJobsItemStartTime | Unset
        if isinstance(_start_time, Unset):
            start_time = UNSET
        else:
            start_time = V0041OpenapiJobInfoRespJobsItemStartTime.from_dict(_start_time)

        state_description = d.pop("state_description", UNSET)

        state_reason = d.pop("state_reason", UNSET)

        standard_error = d.pop("standard_error", UNSET)

        standard_input = d.pop("standard_input", UNSET)

        standard_output = d.pop("standard_output", UNSET)

        _submit_time = d.pop("submit_time", UNSET)
        submit_time: V0041OpenapiJobInfoRespJobsItemSubmitTime | Unset
        if isinstance(_submit_time, Unset):
            submit_time = UNSET
        else:
            submit_time = V0041OpenapiJobInfoRespJobsItemSubmitTime.from_dict(_submit_time)

        _suspend_time = d.pop("suspend_time", UNSET)
        suspend_time: V0041OpenapiJobInfoRespJobsItemSuspendTime | Unset
        if isinstance(_suspend_time, Unset):
            suspend_time = UNSET
        else:
            suspend_time = V0041OpenapiJobInfoRespJobsItemSuspendTime.from_dict(_suspend_time)

        system_comment = d.pop("system_comment", UNSET)

        _time_limit = d.pop("time_limit", UNSET)
        time_limit: V0041OpenapiJobInfoRespJobsItemTimeLimit | Unset
        if isinstance(_time_limit, Unset):
            time_limit = UNSET
        else:
            time_limit = V0041OpenapiJobInfoRespJobsItemTimeLimit.from_dict(_time_limit)

        _time_minimum = d.pop("time_minimum", UNSET)
        time_minimum: V0041OpenapiJobInfoRespJobsItemTimeMinimum | Unset
        if isinstance(_time_minimum, Unset):
            time_minimum = UNSET
        else:
            time_minimum = V0041OpenapiJobInfoRespJobsItemTimeMinimum.from_dict(_time_minimum)

        _threads_per_core = d.pop("threads_per_core", UNSET)
        threads_per_core: V0041OpenapiJobInfoRespJobsItemThreadsPerCore | Unset
        if isinstance(_threads_per_core, Unset):
            threads_per_core = UNSET
        else:
            threads_per_core = V0041OpenapiJobInfoRespJobsItemThreadsPerCore.from_dict(_threads_per_core)

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

        maximum_switch_wait_time = d.pop("maximum_switch_wait_time", UNSET)

        wckey = d.pop("wckey", UNSET)

        current_working_directory = d.pop("current_working_directory", UNSET)

        v0041_openapi_job_info_resp_jobs_item = cls(
            account=account,
            accrue_time=accrue_time,
            admin_comment=admin_comment,
            allocating_node=allocating_node,
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
            container=container,
            container_id=container_id,
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
            cron=cron,
            deadline=deadline,
            delay_boot=delay_boot,
            dependency=dependency,
            derived_exit_code=derived_exit_code,
            eligible_time=eligible_time,
            end_time=end_time,
            excluded_nodes=excluded_nodes,
            exit_code=exit_code,
            extra=extra,
            failed_node=failed_node,
            features=features,
            federation_origin=federation_origin,
            federation_siblings_active=federation_siblings_active,
            federation_siblings_viable=federation_siblings_viable,
            gres_detail=gres_detail,
            group_id=group_id,
            group_name=group_name,
            het_job_id=het_job_id,
            het_job_id_set=het_job_id_set,
            het_job_offset=het_job_offset,
            job_id=job_id,
            job_resources=job_resources,
            job_size_str=job_size_str,
            job_state=job_state,
            last_sched_evaluation=last_sched_evaluation,
            licenses=licenses,
            mail_type=mail_type,
            mail_user=mail_user,
            max_cpus=max_cpus,
            max_nodes=max_nodes,
            mcs_label=mcs_label,
            memory_per_tres=memory_per_tres,
            name=name,
            network=network,
            nodes=nodes,
            nice=nice,
            tasks_per_core=tasks_per_core,
            tasks_per_tres=tasks_per_tres,
            tasks_per_node=tasks_per_node,
            tasks_per_socket=tasks_per_socket,
            tasks_per_board=tasks_per_board,
            cpus=cpus,
            node_count=node_count,
            tasks=tasks,
            partition=partition,
            prefer=prefer,
            memory_per_cpu=memory_per_cpu,
            memory_per_node=memory_per_node,
            minimum_cpus_per_node=minimum_cpus_per_node,
            minimum_tmp_disk_per_node=minimum_tmp_disk_per_node,
            power=power,
            preempt_time=preempt_time,
            preemptable_time=preemptable_time,
            pre_sus_time=pre_sus_time,
            hold=hold,
            priority=priority,
            profile=profile,
            qos=qos,
            reboot=reboot,
            required_nodes=required_nodes,
            minimum_switches=minimum_switches,
            requeue=requeue,
            resize_time=resize_time,
            restart_cnt=restart_cnt,
            resv_name=resv_name,
            scheduled_nodes=scheduled_nodes,
            selinux_context=selinux_context,
            shared=shared,
            exclusive=exclusive,
            oversubscribe=oversubscribe,
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
            maximum_switch_wait_time=maximum_switch_wait_time,
            wckey=wckey,
            current_working_directory=current_working_directory,
        )

        v0041_openapi_job_info_resp_jobs_item.additional_properties = d
        return v0041_openapi_job_info_resp_jobs_item

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
