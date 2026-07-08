from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.v0042_slurmdb_job_flags_item import V0042SlurmdbJobFlagsItem
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v0042_assoc_short import V0042AssocShort
    from ..models.v0042_job_array import V0042JobArray
    from ..models.v0042_job_comment import V0042JobComment
    from ..models.v0042_job_het import V0042JobHet
    from ..models.v0042_job_mcs import V0042JobMcs
    from ..models.v0042_job_required import V0042JobRequired
    from ..models.v0042_job_reservation import V0042JobReservation
    from ..models.v0042_job_state import V0042JobState
    from ..models.v0042_job_time import V0042JobTime
    from ..models.v0042_job_tres import V0042JobTres
    from ..models.v0042_process_exit_code_verbose import V0042ProcessExitCodeVerbose
    from ..models.v0042_step import V0042Step
    from ..models.v0042_uint_32_no_val_struct import V0042Uint32NoValStruct
    from ..models.v0042_wckey_tag_struct import V0042WckeyTagStruct


T = TypeVar("T", bound="V0042Job")


@_attrs_define
class V0042Job:
    """
    Attributes:
        account (str | Unset): Account the job ran under
        comment (V0042JobComment | Unset):
        allocation_nodes (int | Unset): List of nodes allocated to the job
        array (V0042JobArray | Unset):
        association (V0042AssocShort | Unset):
        block (str | Unset): The name of the block to be used (used with Blue Gene systems)
        cluster (str | Unset): Cluster name
        constraints (str | Unset): Feature(s) the job requested as a constraint
        container (str | Unset): Absolute path to OCI container bundle
        derived_exit_code (V0042ProcessExitCodeVerbose | Unset):
        time (V0042JobTime | Unset):
        exit_code (V0042ProcessExitCodeVerbose | Unset):
        extra (str | Unset): Arbitrary string used for node filtering if extra constraints are enabled
        failed_node (str | Unset): Name of node that caused job failure
        flags (list[V0042SlurmdbJobFlagsItem] | Unset):
        group (str | Unset): Group ID of the user that owns the job
        het (V0042JobHet | Unset):
        job_id (int | Unset): Job ID
        name (str | Unset): Job name
        licenses (str | Unset): License(s) required by the job
        mcs (V0042JobMcs | Unset):
        nodes (str | Unset): Node(s) allocated to the job
        partition (str | Unset): Partition assigned to the job
        hold (bool | Unset): Hold (true) or release (false) job
        priority (V0042Uint32NoValStruct | Unset):
        qos (str | Unset): Quality of Service assigned to the job
        qosreq (str | Unset): Requested QOS
        required (V0042JobRequired | Unset):
        kill_request_user (str | Unset): User ID that requested termination of the job
        restart_cnt (int | Unset): How many times this job has been requeued/restarted
        reservation (V0042JobReservation | Unset):
        script (str | Unset): Job batch script; only the first component in a HetJob is populated or honored
        stdin_expanded (str | Unset): Job stdin with expanded fields
        stdout_expanded (str | Unset): Job stdout with expanded fields
        stderr_expanded (str | Unset): Job stderr with expanded fields
        stdout (str | Unset): Path to stdout file
        stderr (str | Unset): Path to stderr file
        stdin (str | Unset): Path to stdin file
        state (V0042JobState | Unset):
        steps (list[V0042Step] | Unset):
        submit_line (str | Unset): Command used to submit the job
        tres (V0042JobTres | Unset):
        used_gres (str | Unset): Generic resources used by job
        user (str | Unset): User that owns the job
        wckey (V0042WckeyTagStruct | Unset):
        working_directory (str | Unset): Path to current working directory
    """

    account: str | Unset = UNSET
    comment: V0042JobComment | Unset = UNSET
    allocation_nodes: int | Unset = UNSET
    array: V0042JobArray | Unset = UNSET
    association: V0042AssocShort | Unset = UNSET
    block: str | Unset = UNSET
    cluster: str | Unset = UNSET
    constraints: str | Unset = UNSET
    container: str | Unset = UNSET
    derived_exit_code: V0042ProcessExitCodeVerbose | Unset = UNSET
    time: V0042JobTime | Unset = UNSET
    exit_code: V0042ProcessExitCodeVerbose | Unset = UNSET
    extra: str | Unset = UNSET
    failed_node: str | Unset = UNSET
    flags: list[V0042SlurmdbJobFlagsItem] | Unset = UNSET
    group: str | Unset = UNSET
    het: V0042JobHet | Unset = UNSET
    job_id: int | Unset = UNSET
    name: str | Unset = UNSET
    licenses: str | Unset = UNSET
    mcs: V0042JobMcs | Unset = UNSET
    nodes: str | Unset = UNSET
    partition: str | Unset = UNSET
    hold: bool | Unset = UNSET
    priority: V0042Uint32NoValStruct | Unset = UNSET
    qos: str | Unset = UNSET
    qosreq: str | Unset = UNSET
    required: V0042JobRequired | Unset = UNSET
    kill_request_user: str | Unset = UNSET
    restart_cnt: int | Unset = UNSET
    reservation: V0042JobReservation | Unset = UNSET
    script: str | Unset = UNSET
    stdin_expanded: str | Unset = UNSET
    stdout_expanded: str | Unset = UNSET
    stderr_expanded: str | Unset = UNSET
    stdout: str | Unset = UNSET
    stderr: str | Unset = UNSET
    stdin: str | Unset = UNSET
    state: V0042JobState | Unset = UNSET
    steps: list[V0042Step] | Unset = UNSET
    submit_line: str | Unset = UNSET
    tres: V0042JobTres | Unset = UNSET
    used_gres: str | Unset = UNSET
    user: str | Unset = UNSET
    wckey: V0042WckeyTagStruct | Unset = UNSET
    working_directory: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account = self.account

        comment: dict[str, Any] | Unset = UNSET
        if not isinstance(self.comment, Unset):
            comment = self.comment.to_dict()

        allocation_nodes = self.allocation_nodes

        array: dict[str, Any] | Unset = UNSET
        if not isinstance(self.array, Unset):
            array = self.array.to_dict()

        association: dict[str, Any] | Unset = UNSET
        if not isinstance(self.association, Unset):
            association = self.association.to_dict()

        block = self.block

        cluster = self.cluster

        constraints = self.constraints

        container = self.container

        derived_exit_code: dict[str, Any] | Unset = UNSET
        if not isinstance(self.derived_exit_code, Unset):
            derived_exit_code = self.derived_exit_code.to_dict()

        time: dict[str, Any] | Unset = UNSET
        if not isinstance(self.time, Unset):
            time = self.time.to_dict()

        exit_code: dict[str, Any] | Unset = UNSET
        if not isinstance(self.exit_code, Unset):
            exit_code = self.exit_code.to_dict()

        extra = self.extra

        failed_node = self.failed_node

        flags: list[str] | Unset = UNSET
        if not isinstance(self.flags, Unset):
            flags = []
            for componentsschemasv0_0_42_slurmdb_job_flags_item_data in self.flags:
                componentsschemasv0_0_42_slurmdb_job_flags_item = (
                    componentsschemasv0_0_42_slurmdb_job_flags_item_data.value
                )
                flags.append(componentsschemasv0_0_42_slurmdb_job_flags_item)

        group = self.group

        het: dict[str, Any] | Unset = UNSET
        if not isinstance(self.het, Unset):
            het = self.het.to_dict()

        job_id = self.job_id

        name = self.name

        licenses = self.licenses

        mcs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mcs, Unset):
            mcs = self.mcs.to_dict()

        nodes = self.nodes

        partition = self.partition

        hold = self.hold

        priority: dict[str, Any] | Unset = UNSET
        if not isinstance(self.priority, Unset):
            priority = self.priority.to_dict()

        qos = self.qos

        qosreq = self.qosreq

        required: dict[str, Any] | Unset = UNSET
        if not isinstance(self.required, Unset):
            required = self.required.to_dict()

        kill_request_user = self.kill_request_user

        restart_cnt = self.restart_cnt

        reservation: dict[str, Any] | Unset = UNSET
        if not isinstance(self.reservation, Unset):
            reservation = self.reservation.to_dict()

        script = self.script

        stdin_expanded = self.stdin_expanded

        stdout_expanded = self.stdout_expanded

        stderr_expanded = self.stderr_expanded

        stdout = self.stdout

        stderr = self.stderr

        stdin = self.stdin

        state: dict[str, Any] | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.to_dict()

        steps: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.steps, Unset):
            steps = []
            for componentsschemasv0_0_42_step_list_item_data in self.steps:
                componentsschemasv0_0_42_step_list_item = componentsschemasv0_0_42_step_list_item_data.to_dict()
                steps.append(componentsschemasv0_0_42_step_list_item)

        submit_line = self.submit_line

        tres: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tres, Unset):
            tres = self.tres.to_dict()

        used_gres = self.used_gres

        user = self.user

        wckey: dict[str, Any] | Unset = UNSET
        if not isinstance(self.wckey, Unset):
            wckey = self.wckey.to_dict()

        working_directory = self.working_directory

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account is not UNSET:
            field_dict["account"] = account
        if comment is not UNSET:
            field_dict["comment"] = comment
        if allocation_nodes is not UNSET:
            field_dict["allocation_nodes"] = allocation_nodes
        if array is not UNSET:
            field_dict["array"] = array
        if association is not UNSET:
            field_dict["association"] = association
        if block is not UNSET:
            field_dict["block"] = block
        if cluster is not UNSET:
            field_dict["cluster"] = cluster
        if constraints is not UNSET:
            field_dict["constraints"] = constraints
        if container is not UNSET:
            field_dict["container"] = container
        if derived_exit_code is not UNSET:
            field_dict["derived_exit_code"] = derived_exit_code
        if time is not UNSET:
            field_dict["time"] = time
        if exit_code is not UNSET:
            field_dict["exit_code"] = exit_code
        if extra is not UNSET:
            field_dict["extra"] = extra
        if failed_node is not UNSET:
            field_dict["failed_node"] = failed_node
        if flags is not UNSET:
            field_dict["flags"] = flags
        if group is not UNSET:
            field_dict["group"] = group
        if het is not UNSET:
            field_dict["het"] = het
        if job_id is not UNSET:
            field_dict["job_id"] = job_id
        if name is not UNSET:
            field_dict["name"] = name
        if licenses is not UNSET:
            field_dict["licenses"] = licenses
        if mcs is not UNSET:
            field_dict["mcs"] = mcs
        if nodes is not UNSET:
            field_dict["nodes"] = nodes
        if partition is not UNSET:
            field_dict["partition"] = partition
        if hold is not UNSET:
            field_dict["hold"] = hold
        if priority is not UNSET:
            field_dict["priority"] = priority
        if qos is not UNSET:
            field_dict["qos"] = qos
        if qosreq is not UNSET:
            field_dict["qosreq"] = qosreq
        if required is not UNSET:
            field_dict["required"] = required
        if kill_request_user is not UNSET:
            field_dict["kill_request_user"] = kill_request_user
        if restart_cnt is not UNSET:
            field_dict["restart_cnt"] = restart_cnt
        if reservation is not UNSET:
            field_dict["reservation"] = reservation
        if script is not UNSET:
            field_dict["script"] = script
        if stdin_expanded is not UNSET:
            field_dict["stdin_expanded"] = stdin_expanded
        if stdout_expanded is not UNSET:
            field_dict["stdout_expanded"] = stdout_expanded
        if stderr_expanded is not UNSET:
            field_dict["stderr_expanded"] = stderr_expanded
        if stdout is not UNSET:
            field_dict["stdout"] = stdout
        if stderr is not UNSET:
            field_dict["stderr"] = stderr
        if stdin is not UNSET:
            field_dict["stdin"] = stdin
        if state is not UNSET:
            field_dict["state"] = state
        if steps is not UNSET:
            field_dict["steps"] = steps
        if submit_line is not UNSET:
            field_dict["submit_line"] = submit_line
        if tres is not UNSET:
            field_dict["tres"] = tres
        if used_gres is not UNSET:
            field_dict["used_gres"] = used_gres
        if user is not UNSET:
            field_dict["user"] = user
        if wckey is not UNSET:
            field_dict["wckey"] = wckey
        if working_directory is not UNSET:
            field_dict["working_directory"] = working_directory

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v0042_assoc_short import V0042AssocShort
        from ..models.v0042_job_array import V0042JobArray
        from ..models.v0042_job_comment import V0042JobComment
        from ..models.v0042_job_het import V0042JobHet
        from ..models.v0042_job_mcs import V0042JobMcs
        from ..models.v0042_job_required import V0042JobRequired
        from ..models.v0042_job_reservation import V0042JobReservation
        from ..models.v0042_job_state import V0042JobState
        from ..models.v0042_job_time import V0042JobTime
        from ..models.v0042_job_tres import V0042JobTres
        from ..models.v0042_process_exit_code_verbose import V0042ProcessExitCodeVerbose
        from ..models.v0042_step import V0042Step
        from ..models.v0042_uint_32_no_val_struct import V0042Uint32NoValStruct
        from ..models.v0042_wckey_tag_struct import V0042WckeyTagStruct

        d = dict(src_dict)
        account = d.pop("account", UNSET)

        _comment = d.pop("comment", UNSET)
        comment: V0042JobComment | Unset
        if isinstance(_comment, Unset):
            comment = UNSET
        else:
            comment = V0042JobComment.from_dict(_comment)

        allocation_nodes = d.pop("allocation_nodes", UNSET)

        _array = d.pop("array", UNSET)
        array: V0042JobArray | Unset
        if isinstance(_array, Unset):
            array = UNSET
        else:
            array = V0042JobArray.from_dict(_array)

        _association = d.pop("association", UNSET)
        association: V0042AssocShort | Unset
        if isinstance(_association, Unset):
            association = UNSET
        else:
            association = V0042AssocShort.from_dict(_association)

        block = d.pop("block", UNSET)

        cluster = d.pop("cluster", UNSET)

        constraints = d.pop("constraints", UNSET)

        container = d.pop("container", UNSET)

        _derived_exit_code = d.pop("derived_exit_code", UNSET)
        derived_exit_code: V0042ProcessExitCodeVerbose | Unset
        if isinstance(_derived_exit_code, Unset):
            derived_exit_code = UNSET
        else:
            derived_exit_code = V0042ProcessExitCodeVerbose.from_dict(_derived_exit_code)

        _time = d.pop("time", UNSET)
        time: V0042JobTime | Unset
        if isinstance(_time, Unset):
            time = UNSET
        else:
            time = V0042JobTime.from_dict(_time)

        _exit_code = d.pop("exit_code", UNSET)
        exit_code: V0042ProcessExitCodeVerbose | Unset
        if isinstance(_exit_code, Unset):
            exit_code = UNSET
        else:
            exit_code = V0042ProcessExitCodeVerbose.from_dict(_exit_code)

        extra = d.pop("extra", UNSET)

        failed_node = d.pop("failed_node", UNSET)

        _flags = d.pop("flags", UNSET)
        flags: list[V0042SlurmdbJobFlagsItem] | Unset = UNSET
        if _flags is not UNSET:
            flags = []
            for componentsschemasv0_0_42_slurmdb_job_flags_item_data in _flags:
                componentsschemasv0_0_42_slurmdb_job_flags_item = V0042SlurmdbJobFlagsItem(
                    componentsschemasv0_0_42_slurmdb_job_flags_item_data
                )

                flags.append(componentsschemasv0_0_42_slurmdb_job_flags_item)

        group = d.pop("group", UNSET)

        _het = d.pop("het", UNSET)
        het: V0042JobHet | Unset
        if isinstance(_het, Unset):
            het = UNSET
        else:
            het = V0042JobHet.from_dict(_het)

        job_id = d.pop("job_id", UNSET)

        name = d.pop("name", UNSET)

        licenses = d.pop("licenses", UNSET)

        _mcs = d.pop("mcs", UNSET)
        mcs: V0042JobMcs | Unset
        if isinstance(_mcs, Unset):
            mcs = UNSET
        else:
            mcs = V0042JobMcs.from_dict(_mcs)

        nodes = d.pop("nodes", UNSET)

        partition = d.pop("partition", UNSET)

        hold = d.pop("hold", UNSET)

        _priority = d.pop("priority", UNSET)
        priority: V0042Uint32NoValStruct | Unset
        if isinstance(_priority, Unset):
            priority = UNSET
        else:
            priority = V0042Uint32NoValStruct.from_dict(_priority)

        qos = d.pop("qos", UNSET)

        qosreq = d.pop("qosreq", UNSET)

        _required = d.pop("required", UNSET)
        required: V0042JobRequired | Unset
        if isinstance(_required, Unset):
            required = UNSET
        else:
            required = V0042JobRequired.from_dict(_required)

        kill_request_user = d.pop("kill_request_user", UNSET)

        restart_cnt = d.pop("restart_cnt", UNSET)

        _reservation = d.pop("reservation", UNSET)
        reservation: V0042JobReservation | Unset
        if isinstance(_reservation, Unset):
            reservation = UNSET
        else:
            reservation = V0042JobReservation.from_dict(_reservation)

        script = d.pop("script", UNSET)

        stdin_expanded = d.pop("stdin_expanded", UNSET)

        stdout_expanded = d.pop("stdout_expanded", UNSET)

        stderr_expanded = d.pop("stderr_expanded", UNSET)

        stdout = d.pop("stdout", UNSET)

        stderr = d.pop("stderr", UNSET)

        stdin = d.pop("stdin", UNSET)

        _state = d.pop("state", UNSET)
        state: V0042JobState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = V0042JobState.from_dict(_state)

        _steps = d.pop("steps", UNSET)
        steps: list[V0042Step] | Unset = UNSET
        if _steps is not UNSET:
            steps = []
            for componentsschemasv0_0_42_step_list_item_data in _steps:
                componentsschemasv0_0_42_step_list_item = V0042Step.from_dict(
                    componentsschemasv0_0_42_step_list_item_data
                )

                steps.append(componentsschemasv0_0_42_step_list_item)

        submit_line = d.pop("submit_line", UNSET)

        _tres = d.pop("tres", UNSET)
        tres: V0042JobTres | Unset
        if isinstance(_tres, Unset):
            tres = UNSET
        else:
            tres = V0042JobTres.from_dict(_tres)

        used_gres = d.pop("used_gres", UNSET)

        user = d.pop("user", UNSET)

        _wckey = d.pop("wckey", UNSET)
        wckey: V0042WckeyTagStruct | Unset
        if isinstance(_wckey, Unset):
            wckey = UNSET
        else:
            wckey = V0042WckeyTagStruct.from_dict(_wckey)

        working_directory = d.pop("working_directory", UNSET)

        v0042_job = cls(
            account=account,
            comment=comment,
            allocation_nodes=allocation_nodes,
            array=array,
            association=association,
            block=block,
            cluster=cluster,
            constraints=constraints,
            container=container,
            derived_exit_code=derived_exit_code,
            time=time,
            exit_code=exit_code,
            extra=extra,
            failed_node=failed_node,
            flags=flags,
            group=group,
            het=het,
            job_id=job_id,
            name=name,
            licenses=licenses,
            mcs=mcs,
            nodes=nodes,
            partition=partition,
            hold=hold,
            priority=priority,
            qos=qos,
            qosreq=qosreq,
            required=required,
            kill_request_user=kill_request_user,
            restart_cnt=restart_cnt,
            reservation=reservation,
            script=script,
            stdin_expanded=stdin_expanded,
            stdout_expanded=stdout_expanded,
            stderr_expanded=stderr_expanded,
            stdout=stdout,
            stderr=stderr,
            stdin=stdin,
            state=state,
            steps=steps,
            submit_line=submit_line,
            tres=tres,
            used_gres=used_gres,
            user=user,
            wckey=wckey,
            working_directory=working_directory,
        )

        v0042_job.additional_properties = d
        return v0042_job

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
