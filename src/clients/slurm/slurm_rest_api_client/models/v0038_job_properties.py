from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.v0038_job_properties_exclusive import V0038JobPropertiesExclusive
from ..models.v0038_job_properties_gres_flags import V0038JobPropertiesGresFlags
from ..models.v0038_job_properties_open_mode import V0038JobPropertiesOpenMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v0038_job_properties_environment import V0038JobPropertiesEnvironment


T = TypeVar("T", bound="V0038JobProperties")


@_attrs_define
class V0038JobProperties:
    """
    Attributes:
        environment (V0038JobPropertiesEnvironment): Dictionary of environment entries.
        account (str | Unset): Charge resources used by this job to specified account.
        account_gather_frequency (str | Unset): Define the job accounting and profiling sampling intervals.
        argv (list[str] | Unset): Arguments to the script.
        array (str | Unset): Submit a job array, multiple jobs to be executed with identical parameters. The indexes
            specification identifies what array index values should be used.
        batch_features (str | Unset): features required for batch script's node
        begin_time (int | Unset): Submit the batch script to the Slurm controller immediately, like normal, but tell the
            controller to defer the allocation of the job until the specified time.
        burst_buffer (str | Unset): Burst buffer specification.
        cluster_constraint (str | Unset): Specifies features that a federated cluster must have to have a sibling job
            submitted to it.
        comment (str | Unset): An arbitrary comment.
        constraints (str | Unset): node features required by job.
        container (str | Unset): absolute path to OCI container bundle
        core_specification (int | Unset): Count of specialized threads per node reserved by the job for system
            operations and not used by the application.
        cores_per_socket (int | Unset): Restrict node selection to nodes with at least the specified number of cores per
            socket.
        cpu_binding (str | Unset): Cpu binding
        cpu_binding_hint (str | Unset): Cpu binding hint
        cpu_frequency (str | Unset): Request that job steps initiated by srun commands inside this sbatch script be run
            at some requested frequency if possible, on the CPUs selected for the step on the compute node(s).
        cpus_per_gpu (str | Unset): Number of CPUs requested per allocated GPU.
        cpus_per_task (int | Unset): Advise the Slurm controller that ensuing job steps will require ncpus number of
            processors per task.
        current_working_directory (str | Unset): Instruct Slurm to connect the batch script's standard output directly
            to the file name.
        deadline (str | Unset): Remove the job if no ending is possible before this deadline (start > (deadline -
            time[-min])).
        delay_boot (int | Unset): Do not reboot nodes in order to satisfied this job's feature specification if the job
            has been eligible to run for less than this time period.
        dependency (str | Unset): Defer the start of this job until the specified dependencies have been satisfied
            completed.
        distribution (str | Unset): Specify alternate distribution methods for remote processes.
        exclusive (V0038JobPropertiesExclusive | Unset): The job allocation can share nodes just other users with the
            "user" option or with the "mcs" option).
        get_user_environment (bool | Unset): Load new login environment for user on job node.
        gres (str | Unset): Specifies a comma delimited list of generic consumable resources.
        gres_flags (V0038JobPropertiesGresFlags | Unset): Specify generic resource task binding options.
        gpu_binding (str | Unset): Requested binding of tasks to GPU.
        gpu_frequency (str | Unset): Requested GPU frequency.
        gpus (str | Unset): GPUs per job.
        gpus_per_node (str | Unset): GPUs per node.
        gpus_per_socket (str | Unset): GPUs per socket.
        gpus_per_task (str | Unset): GPUs per task.
        hold (bool | Unset): Specify the job is to be submitted in a held state (priority of zero).
        kill_on_invalid_dependency (bool | Unset): If a job has an invalid dependency, then Slurm is to terminate it.
        licenses (str | Unset): Specification of licenses (or other resources available on all nodes of the cluster)
            which must be allocated to this job.
        mail_type (str | Unset): Notify user by email when certain event types occur.
        mail_user (str | Unset): User to receive email notification of state changes as defined by mail_type.
        mcs_label (str | Unset): This parameter is a group among the groups of the user.
        memory_binding (str | Unset): Bind tasks to memory.
        memory_per_cpu (int | Unset): Minimum real memory per cpu (MB).
        memory_per_gpu (int | Unset): Minimum memory required per allocated GPU.
        memory_per_node (int | Unset): Minimum real memory per node (MB).
        minimum_cpus_per_node (int | Unset): Minimum number of CPUs per node.
        minimum_nodes (bool | Unset): If a range of node counts is given, prefer the smaller count.
        name (str | Unset): Specify a name for the job allocation.
        nice (int | Unset): Run the job with an adjusted scheduling priority within Slurm.
        no_kill (bool | Unset): Do not automatically terminate a job if one of the nodes it has been allocated fails.
        nodes (list[int] | Unset): Request that a minimum of minnodes nodes and a maximum node count.
        open_mode (V0038JobPropertiesOpenMode | Unset): Open the output and error files using append or truncate mode as
            specified. Default: V0038JobPropertiesOpenMode.APPEND.
        oversubscribe (bool | Unset): The job allocation can over-subscribe resources with other running jobs. Default:
            False.
        partition (str | Unset): Request a specific partition for the resource allocation.
        prefer (str | Unset): Comma delimited list of features for scheduler to prefer but not a strict requirement like
            a constraint. Value can be used for job submission but is only displayed for PENDING jobs.
        priority (str | Unset): Request a specific job priority.
        qos (str | Unset): Request a quality of service for the job.
        requeue (bool | Unset): Specifies that the batch job should eligible to being requeue.
        reservation (str | Unset): Allocate resources for the job from the named reservation.
        signal (str | Unset): When a job is within sig_time seconds of its end time, send it the signal sig_num.
        sockets_per_node (int | Unset): Restrict node selection to nodes with at least the specified number of sockets.
        spread_job (bool | Unset): Spread the job allocation over as many nodes as possible and attempt to evenly
            distribute tasks across the allocated nodes.
        standard_error (str | Unset): Instruct Slurm to connect the batch script's standard error directly to the file
            name.
        standard_input (str | Unset): Instruct Slurm to connect the batch script's standard input directly to the file
            name specified.
        standard_output (str | Unset): Instruct Slurm to connect the batch script's standard output directly to the file
            name.
        tasks (int | Unset): Advises the Slurm controller that job steps run within the allocation will launch a maximum
            of number tasks and to provide for sufficient resources.
        tasks_per_core (int | Unset): Request the maximum ntasks be invoked on each core.
        tasks_per_node (int | Unset): Request the maximum ntasks be invoked on each node.
        tasks_per_socket (int | Unset): Request the maximum ntasks be invoked on each socket.
        thread_specification (int | Unset): Count of specialized threads per node reserved by the job for system
            operations and not used by the application.
        threads_per_core (int | Unset): Restrict node selection to nodes with at least the specified number of threads
            per core.
        time_limit (int | Unset): Step time limit in minutes.
        time_minimum (int | Unset): Minimum run time in minutes.
        wait_all_nodes (bool | Unset): Do not begin execution until all nodes are ready for use.
        wckey (str | Unset): Specify wckey to be used with job.
    """

    environment: V0038JobPropertiesEnvironment
    account: str | Unset = UNSET
    account_gather_frequency: str | Unset = UNSET
    argv: list[str] | Unset = UNSET
    array: str | Unset = UNSET
    batch_features: str | Unset = UNSET
    begin_time: int | Unset = UNSET
    burst_buffer: str | Unset = UNSET
    cluster_constraint: str | Unset = UNSET
    comment: str | Unset = UNSET
    constraints: str | Unset = UNSET
    container: str | Unset = UNSET
    core_specification: int | Unset = UNSET
    cores_per_socket: int | Unset = UNSET
    cpu_binding: str | Unset = UNSET
    cpu_binding_hint: str | Unset = UNSET
    cpu_frequency: str | Unset = UNSET
    cpus_per_gpu: str | Unset = UNSET
    cpus_per_task: int | Unset = UNSET
    current_working_directory: str | Unset = UNSET
    deadline: str | Unset = UNSET
    delay_boot: int | Unset = UNSET
    dependency: str | Unset = UNSET
    distribution: str | Unset = UNSET
    exclusive: V0038JobPropertiesExclusive | Unset = UNSET
    get_user_environment: bool | Unset = UNSET
    gres: str | Unset = UNSET
    gres_flags: V0038JobPropertiesGresFlags | Unset = UNSET
    gpu_binding: str | Unset = UNSET
    gpu_frequency: str | Unset = UNSET
    gpus: str | Unset = UNSET
    gpus_per_node: str | Unset = UNSET
    gpus_per_socket: str | Unset = UNSET
    gpus_per_task: str | Unset = UNSET
    hold: bool | Unset = UNSET
    kill_on_invalid_dependency: bool | Unset = UNSET
    licenses: str | Unset = UNSET
    mail_type: str | Unset = UNSET
    mail_user: str | Unset = UNSET
    mcs_label: str | Unset = UNSET
    memory_binding: str | Unset = UNSET
    memory_per_cpu: int | Unset = UNSET
    memory_per_gpu: int | Unset = UNSET
    memory_per_node: int | Unset = UNSET
    minimum_cpus_per_node: int | Unset = UNSET
    minimum_nodes: bool | Unset = UNSET
    name: str | Unset = UNSET
    nice: int | Unset = UNSET
    no_kill: bool | Unset = UNSET
    nodes: list[int] | Unset = UNSET
    open_mode: V0038JobPropertiesOpenMode | Unset = V0038JobPropertiesOpenMode.APPEND
    oversubscribe: bool | Unset = False
    partition: str | Unset = UNSET
    prefer: str | Unset = UNSET
    priority: str | Unset = UNSET
    qos: str | Unset = UNSET
    requeue: bool | Unset = UNSET
    reservation: str | Unset = UNSET
    signal: str | Unset = UNSET
    sockets_per_node: int | Unset = UNSET
    spread_job: bool | Unset = UNSET
    standard_error: str | Unset = UNSET
    standard_input: str | Unset = UNSET
    standard_output: str | Unset = UNSET
    tasks: int | Unset = UNSET
    tasks_per_core: int | Unset = UNSET
    tasks_per_node: int | Unset = UNSET
    tasks_per_socket: int | Unset = UNSET
    thread_specification: int | Unset = UNSET
    threads_per_core: int | Unset = UNSET
    time_limit: int | Unset = UNSET
    time_minimum: int | Unset = UNSET
    wait_all_nodes: bool | Unset = UNSET
    wckey: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        environment = self.environment.to_dict()

        account = self.account

        account_gather_frequency = self.account_gather_frequency

        argv: list[str] | Unset = UNSET
        if not isinstance(self.argv, Unset):
            argv = self.argv

        array = self.array

        batch_features = self.batch_features

        begin_time = self.begin_time

        burst_buffer = self.burst_buffer

        cluster_constraint = self.cluster_constraint

        comment = self.comment

        constraints = self.constraints

        container = self.container

        core_specification = self.core_specification

        cores_per_socket = self.cores_per_socket

        cpu_binding = self.cpu_binding

        cpu_binding_hint = self.cpu_binding_hint

        cpu_frequency = self.cpu_frequency

        cpus_per_gpu = self.cpus_per_gpu

        cpus_per_task = self.cpus_per_task

        current_working_directory = self.current_working_directory

        deadline = self.deadline

        delay_boot = self.delay_boot

        dependency = self.dependency

        distribution = self.distribution

        exclusive: str | Unset = UNSET
        if not isinstance(self.exclusive, Unset):
            exclusive = self.exclusive.value

        get_user_environment = self.get_user_environment

        gres = self.gres

        gres_flags: str | Unset = UNSET
        if not isinstance(self.gres_flags, Unset):
            gres_flags = self.gres_flags.value

        gpu_binding = self.gpu_binding

        gpu_frequency = self.gpu_frequency

        gpus = self.gpus

        gpus_per_node = self.gpus_per_node

        gpus_per_socket = self.gpus_per_socket

        gpus_per_task = self.gpus_per_task

        hold = self.hold

        kill_on_invalid_dependency = self.kill_on_invalid_dependency

        licenses = self.licenses

        mail_type = self.mail_type

        mail_user = self.mail_user

        mcs_label = self.mcs_label

        memory_binding = self.memory_binding

        memory_per_cpu = self.memory_per_cpu

        memory_per_gpu = self.memory_per_gpu

        memory_per_node = self.memory_per_node

        minimum_cpus_per_node = self.minimum_cpus_per_node

        minimum_nodes = self.minimum_nodes

        name = self.name

        nice = self.nice

        no_kill = self.no_kill

        nodes: list[int] | Unset = UNSET
        if not isinstance(self.nodes, Unset):
            nodes = self.nodes

        open_mode: str | Unset = UNSET
        if not isinstance(self.open_mode, Unset):
            open_mode = self.open_mode.value

        oversubscribe = self.oversubscribe

        partition = self.partition

        prefer = self.prefer

        priority = self.priority

        qos = self.qos

        requeue = self.requeue

        reservation = self.reservation

        signal = self.signal

        sockets_per_node = self.sockets_per_node

        spread_job = self.spread_job

        standard_error = self.standard_error

        standard_input = self.standard_input

        standard_output = self.standard_output

        tasks = self.tasks

        tasks_per_core = self.tasks_per_core

        tasks_per_node = self.tasks_per_node

        tasks_per_socket = self.tasks_per_socket

        thread_specification = self.thread_specification

        threads_per_core = self.threads_per_core

        time_limit = self.time_limit

        time_minimum = self.time_minimum

        wait_all_nodes = self.wait_all_nodes

        wckey = self.wckey

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "environment": environment,
            }
        )
        if account is not UNSET:
            field_dict["account"] = account
        if account_gather_frequency is not UNSET:
            field_dict["account_gather_frequency"] = account_gather_frequency
        if argv is not UNSET:
            field_dict["argv"] = argv
        if array is not UNSET:
            field_dict["array"] = array
        if batch_features is not UNSET:
            field_dict["batch_features"] = batch_features
        if begin_time is not UNSET:
            field_dict["begin_time"] = begin_time
        if burst_buffer is not UNSET:
            field_dict["burst_buffer"] = burst_buffer
        if cluster_constraint is not UNSET:
            field_dict["cluster_constraint"] = cluster_constraint
        if comment is not UNSET:
            field_dict["comment"] = comment
        if constraints is not UNSET:
            field_dict["constraints"] = constraints
        if container is not UNSET:
            field_dict["container"] = container
        if core_specification is not UNSET:
            field_dict["core_specification"] = core_specification
        if cores_per_socket is not UNSET:
            field_dict["cores_per_socket"] = cores_per_socket
        if cpu_binding is not UNSET:
            field_dict["cpu_binding"] = cpu_binding
        if cpu_binding_hint is not UNSET:
            field_dict["cpu_binding_hint"] = cpu_binding_hint
        if cpu_frequency is not UNSET:
            field_dict["cpu_frequency"] = cpu_frequency
        if cpus_per_gpu is not UNSET:
            field_dict["cpus_per_gpu"] = cpus_per_gpu
        if cpus_per_task is not UNSET:
            field_dict["cpus_per_task"] = cpus_per_task
        if current_working_directory is not UNSET:
            field_dict["current_working_directory"] = current_working_directory
        if deadline is not UNSET:
            field_dict["deadline"] = deadline
        if delay_boot is not UNSET:
            field_dict["delay_boot"] = delay_boot
        if dependency is not UNSET:
            field_dict["dependency"] = dependency
        if distribution is not UNSET:
            field_dict["distribution"] = distribution
        if exclusive is not UNSET:
            field_dict["exclusive"] = exclusive
        if get_user_environment is not UNSET:
            field_dict["get_user_environment"] = get_user_environment
        if gres is not UNSET:
            field_dict["gres"] = gres
        if gres_flags is not UNSET:
            field_dict["gres_flags"] = gres_flags
        if gpu_binding is not UNSET:
            field_dict["gpu_binding"] = gpu_binding
        if gpu_frequency is not UNSET:
            field_dict["gpu_frequency"] = gpu_frequency
        if gpus is not UNSET:
            field_dict["gpus"] = gpus
        if gpus_per_node is not UNSET:
            field_dict["gpus_per_node"] = gpus_per_node
        if gpus_per_socket is not UNSET:
            field_dict["gpus_per_socket"] = gpus_per_socket
        if gpus_per_task is not UNSET:
            field_dict["gpus_per_task"] = gpus_per_task
        if hold is not UNSET:
            field_dict["hold"] = hold
        if kill_on_invalid_dependency is not UNSET:
            field_dict["kill_on_invalid_dependency"] = kill_on_invalid_dependency
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
        if memory_per_cpu is not UNSET:
            field_dict["memory_per_cpu"] = memory_per_cpu
        if memory_per_gpu is not UNSET:
            field_dict["memory_per_gpu"] = memory_per_gpu
        if memory_per_node is not UNSET:
            field_dict["memory_per_node"] = memory_per_node
        if minimum_cpus_per_node is not UNSET:
            field_dict["minimum_cpus_per_node"] = minimum_cpus_per_node
        if minimum_nodes is not UNSET:
            field_dict["minimum_nodes"] = minimum_nodes
        if name is not UNSET:
            field_dict["name"] = name
        if nice is not UNSET:
            field_dict["nice"] = nice
        if no_kill is not UNSET:
            field_dict["no_kill"] = no_kill
        if nodes is not UNSET:
            field_dict["nodes"] = nodes
        if open_mode is not UNSET:
            field_dict["open_mode"] = open_mode
        if oversubscribe is not UNSET:
            field_dict["oversubscribe"] = oversubscribe
        if partition is not UNSET:
            field_dict["partition"] = partition
        if prefer is not UNSET:
            field_dict["prefer"] = prefer
        if priority is not UNSET:
            field_dict["priority"] = priority
        if qos is not UNSET:
            field_dict["qos"] = qos
        if requeue is not UNSET:
            field_dict["requeue"] = requeue
        if reservation is not UNSET:
            field_dict["reservation"] = reservation
        if signal is not UNSET:
            field_dict["signal"] = signal
        if sockets_per_node is not UNSET:
            field_dict["sockets_per_node"] = sockets_per_node
        if spread_job is not UNSET:
            field_dict["spread_job"] = spread_job
        if standard_error is not UNSET:
            field_dict["standard_error"] = standard_error
        if standard_input is not UNSET:
            field_dict["standard_input"] = standard_input
        if standard_output is not UNSET:
            field_dict["standard_output"] = standard_output
        if tasks is not UNSET:
            field_dict["tasks"] = tasks
        if tasks_per_core is not UNSET:
            field_dict["tasks_per_core"] = tasks_per_core
        if tasks_per_node is not UNSET:
            field_dict["tasks_per_node"] = tasks_per_node
        if tasks_per_socket is not UNSET:
            field_dict["tasks_per_socket"] = tasks_per_socket
        if thread_specification is not UNSET:
            field_dict["thread_specification"] = thread_specification
        if threads_per_core is not UNSET:
            field_dict["threads_per_core"] = threads_per_core
        if time_limit is not UNSET:
            field_dict["time_limit"] = time_limit
        if time_minimum is not UNSET:
            field_dict["time_minimum"] = time_minimum
        if wait_all_nodes is not UNSET:
            field_dict["wait_all_nodes"] = wait_all_nodes
        if wckey is not UNSET:
            field_dict["wckey"] = wckey

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v0038_job_properties_environment import V0038JobPropertiesEnvironment

        d = dict(src_dict)
        environment = V0038JobPropertiesEnvironment.from_dict(d.pop("environment"))

        account = d.pop("account", UNSET)

        account_gather_frequency = d.pop("account_gather_frequency", UNSET)

        argv = cast(list[str], d.pop("argv", UNSET))

        array = d.pop("array", UNSET)

        batch_features = d.pop("batch_features", UNSET)

        begin_time = d.pop("begin_time", UNSET)

        burst_buffer = d.pop("burst_buffer", UNSET)

        cluster_constraint = d.pop("cluster_constraint", UNSET)

        comment = d.pop("comment", UNSET)

        constraints = d.pop("constraints", UNSET)

        container = d.pop("container", UNSET)

        core_specification = d.pop("core_specification", UNSET)

        cores_per_socket = d.pop("cores_per_socket", UNSET)

        cpu_binding = d.pop("cpu_binding", UNSET)

        cpu_binding_hint = d.pop("cpu_binding_hint", UNSET)

        cpu_frequency = d.pop("cpu_frequency", UNSET)

        cpus_per_gpu = d.pop("cpus_per_gpu", UNSET)

        cpus_per_task = d.pop("cpus_per_task", UNSET)

        current_working_directory = d.pop("current_working_directory", UNSET)

        deadline = d.pop("deadline", UNSET)

        delay_boot = d.pop("delay_boot", UNSET)

        dependency = d.pop("dependency", UNSET)

        distribution = d.pop("distribution", UNSET)

        _exclusive = d.pop("exclusive", UNSET)
        exclusive: V0038JobPropertiesExclusive | Unset
        if isinstance(_exclusive, Unset):
            exclusive = UNSET
        else:
            exclusive = V0038JobPropertiesExclusive(_exclusive)

        get_user_environment = d.pop("get_user_environment", UNSET)

        gres = d.pop("gres", UNSET)

        _gres_flags = d.pop("gres_flags", UNSET)
        gres_flags: V0038JobPropertiesGresFlags | Unset
        if isinstance(_gres_flags, Unset):
            gres_flags = UNSET
        else:
            gres_flags = V0038JobPropertiesGresFlags(_gres_flags)

        gpu_binding = d.pop("gpu_binding", UNSET)

        gpu_frequency = d.pop("gpu_frequency", UNSET)

        gpus = d.pop("gpus", UNSET)

        gpus_per_node = d.pop("gpus_per_node", UNSET)

        gpus_per_socket = d.pop("gpus_per_socket", UNSET)

        gpus_per_task = d.pop("gpus_per_task", UNSET)

        hold = d.pop("hold", UNSET)

        kill_on_invalid_dependency = d.pop("kill_on_invalid_dependency", UNSET)

        licenses = d.pop("licenses", UNSET)

        mail_type = d.pop("mail_type", UNSET)

        mail_user = d.pop("mail_user", UNSET)

        mcs_label = d.pop("mcs_label", UNSET)

        memory_binding = d.pop("memory_binding", UNSET)

        memory_per_cpu = d.pop("memory_per_cpu", UNSET)

        memory_per_gpu = d.pop("memory_per_gpu", UNSET)

        memory_per_node = d.pop("memory_per_node", UNSET)

        minimum_cpus_per_node = d.pop("minimum_cpus_per_node", UNSET)

        minimum_nodes = d.pop("minimum_nodes", UNSET)

        name = d.pop("name", UNSET)

        nice = d.pop("nice", UNSET)

        no_kill = d.pop("no_kill", UNSET)

        nodes = cast(list[int], d.pop("nodes", UNSET))

        _open_mode = d.pop("open_mode", UNSET)
        open_mode: V0038JobPropertiesOpenMode | Unset
        if isinstance(_open_mode, Unset):
            open_mode = UNSET
        else:
            open_mode = V0038JobPropertiesOpenMode(_open_mode)

        oversubscribe = d.pop("oversubscribe", UNSET)

        partition = d.pop("partition", UNSET)

        prefer = d.pop("prefer", UNSET)

        priority = d.pop("priority", UNSET)

        qos = d.pop("qos", UNSET)

        requeue = d.pop("requeue", UNSET)

        reservation = d.pop("reservation", UNSET)

        signal = d.pop("signal", UNSET)

        sockets_per_node = d.pop("sockets_per_node", UNSET)

        spread_job = d.pop("spread_job", UNSET)

        standard_error = d.pop("standard_error", UNSET)

        standard_input = d.pop("standard_input", UNSET)

        standard_output = d.pop("standard_output", UNSET)

        tasks = d.pop("tasks", UNSET)

        tasks_per_core = d.pop("tasks_per_core", UNSET)

        tasks_per_node = d.pop("tasks_per_node", UNSET)

        tasks_per_socket = d.pop("tasks_per_socket", UNSET)

        thread_specification = d.pop("thread_specification", UNSET)

        threads_per_core = d.pop("threads_per_core", UNSET)

        time_limit = d.pop("time_limit", UNSET)

        time_minimum = d.pop("time_minimum", UNSET)

        wait_all_nodes = d.pop("wait_all_nodes", UNSET)

        wckey = d.pop("wckey", UNSET)

        v0038_job_properties = cls(
            environment=environment,
            account=account,
            account_gather_frequency=account_gather_frequency,
            argv=argv,
            array=array,
            batch_features=batch_features,
            begin_time=begin_time,
            burst_buffer=burst_buffer,
            cluster_constraint=cluster_constraint,
            comment=comment,
            constraints=constraints,
            container=container,
            core_specification=core_specification,
            cores_per_socket=cores_per_socket,
            cpu_binding=cpu_binding,
            cpu_binding_hint=cpu_binding_hint,
            cpu_frequency=cpu_frequency,
            cpus_per_gpu=cpus_per_gpu,
            cpus_per_task=cpus_per_task,
            current_working_directory=current_working_directory,
            deadline=deadline,
            delay_boot=delay_boot,
            dependency=dependency,
            distribution=distribution,
            exclusive=exclusive,
            get_user_environment=get_user_environment,
            gres=gres,
            gres_flags=gres_flags,
            gpu_binding=gpu_binding,
            gpu_frequency=gpu_frequency,
            gpus=gpus,
            gpus_per_node=gpus_per_node,
            gpus_per_socket=gpus_per_socket,
            gpus_per_task=gpus_per_task,
            hold=hold,
            kill_on_invalid_dependency=kill_on_invalid_dependency,
            licenses=licenses,
            mail_type=mail_type,
            mail_user=mail_user,
            mcs_label=mcs_label,
            memory_binding=memory_binding,
            memory_per_cpu=memory_per_cpu,
            memory_per_gpu=memory_per_gpu,
            memory_per_node=memory_per_node,
            minimum_cpus_per_node=minimum_cpus_per_node,
            minimum_nodes=minimum_nodes,
            name=name,
            nice=nice,
            no_kill=no_kill,
            nodes=nodes,
            open_mode=open_mode,
            oversubscribe=oversubscribe,
            partition=partition,
            prefer=prefer,
            priority=priority,
            qos=qos,
            requeue=requeue,
            reservation=reservation,
            signal=signal,
            sockets_per_node=sockets_per_node,
            spread_job=spread_job,
            standard_error=standard_error,
            standard_input=standard_input,
            standard_output=standard_output,
            tasks=tasks,
            tasks_per_core=tasks_per_core,
            tasks_per_node=tasks_per_node,
            tasks_per_socket=tasks_per_socket,
            thread_specification=thread_specification,
            threads_per_core=threads_per_core,
            time_limit=time_limit,
            time_minimum=time_minimum,
            wait_all_nodes=wait_all_nodes,
            wckey=wckey,
        )

        v0038_job_properties.additional_properties = d
        return v0038_job_properties

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
