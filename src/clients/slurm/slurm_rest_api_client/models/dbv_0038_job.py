from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dbv_0038_association_short_info import Dbv0038AssociationShortInfo
    from ..models.dbv_0038_job_array import Dbv0038JobArray
    from ..models.dbv_0038_job_comment import Dbv0038JobComment
    from ..models.dbv_0038_job_exit_code import Dbv0038JobExitCode
    from ..models.dbv_0038_job_het import Dbv0038JobHet
    from ..models.dbv_0038_job_mcs import Dbv0038JobMcs
    from ..models.dbv_0038_job_required import Dbv0038JobRequired
    from ..models.dbv_0038_job_reservation import Dbv0038JobReservation
    from ..models.dbv_0038_job_state import Dbv0038JobState
    from ..models.dbv_0038_job_step import Dbv0038JobStep
    from ..models.dbv_0038_job_time import Dbv0038JobTime
    from ..models.dbv_0038_job_tres import Dbv0038JobTres
    from ..models.dbv_0038_job_wckey import Dbv0038JobWckey


T = TypeVar("T", bound="Dbv0038Job")


@_attrs_define
class Dbv0038Job:
    """Single job description

    Attributes:
        account (str | Unset): Account charged by job
        comment (Dbv0038JobComment | Unset): Job comments by type
        allocation_nodes (str | Unset): Nodes allocated to job
        array (Dbv0038JobArray | Unset): Array properties (optional)
        time (Dbv0038JobTime | Unset): Time properties
        association (Dbv0038AssociationShortInfo | Unset):
        cluster (str | Unset): Assigned cluster
        constraints (str | Unset): Constraints on job
        derived_exit_code (Dbv0038JobExitCode | Unset):
        exit_code (Dbv0038JobExitCode | Unset):
        flags (list[str] | Unset): List of properties of job
        group (str | Unset): User's group to run job
        het (Dbv0038JobHet | Unset): Heterogeneous Job details (optional)
        job_id (int | Unset): Job id
        name (str | Unset): Assigned job name
        mcs (Dbv0038JobMcs | Unset): Multi-Category Security
        nodes (str | Unset): List of nodes allocated for job
        partition (str | Unset): Assigned job's partition
        priority (int | Unset): Priority
        qos (str | Unset): Assigned qos name
        required (Dbv0038JobRequired | Unset): Job run requirements
        kill_request_user (str | Unset): User who requested job killed
        reservation (Dbv0038JobReservation | Unset): Reservation usage details
        state (Dbv0038JobState | Unset): State properties of job
        steps (list[Dbv0038JobStep] | Unset): Job step description
        tres (Dbv0038JobTres | Unset): TRES settings
        user (str | Unset): Job user
        wckey (Dbv0038JobWckey | Unset): Job assigned wckey details
        working_directory (str | Unset): Directory where job was initially started
        container (str | Unset): absolute path to OCI container bundle
    """

    account: str | Unset = UNSET
    comment: Dbv0038JobComment | Unset = UNSET
    allocation_nodes: str | Unset = UNSET
    array: Dbv0038JobArray | Unset = UNSET
    time: Dbv0038JobTime | Unset = UNSET
    association: Dbv0038AssociationShortInfo | Unset = UNSET
    cluster: str | Unset = UNSET
    constraints: str | Unset = UNSET
    derived_exit_code: Dbv0038JobExitCode | Unset = UNSET
    exit_code: Dbv0038JobExitCode | Unset = UNSET
    flags: list[str] | Unset = UNSET
    group: str | Unset = UNSET
    het: Dbv0038JobHet | Unset = UNSET
    job_id: int | Unset = UNSET
    name: str | Unset = UNSET
    mcs: Dbv0038JobMcs | Unset = UNSET
    nodes: str | Unset = UNSET
    partition: str | Unset = UNSET
    priority: int | Unset = UNSET
    qos: str | Unset = UNSET
    required: Dbv0038JobRequired | Unset = UNSET
    kill_request_user: str | Unset = UNSET
    reservation: Dbv0038JobReservation | Unset = UNSET
    state: Dbv0038JobState | Unset = UNSET
    steps: list[Dbv0038JobStep] | Unset = UNSET
    tres: Dbv0038JobTres | Unset = UNSET
    user: str | Unset = UNSET
    wckey: Dbv0038JobWckey | Unset = UNSET
    working_directory: str | Unset = UNSET
    container: str | Unset = UNSET
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

        time: dict[str, Any] | Unset = UNSET
        if not isinstance(self.time, Unset):
            time = self.time.to_dict()

        association: dict[str, Any] | Unset = UNSET
        if not isinstance(self.association, Unset):
            association = self.association.to_dict()

        cluster = self.cluster

        constraints = self.constraints

        derived_exit_code: dict[str, Any] | Unset = UNSET
        if not isinstance(self.derived_exit_code, Unset):
            derived_exit_code = self.derived_exit_code.to_dict()

        exit_code: dict[str, Any] | Unset = UNSET
        if not isinstance(self.exit_code, Unset):
            exit_code = self.exit_code.to_dict()

        flags: list[str] | Unset = UNSET
        if not isinstance(self.flags, Unset):
            flags = self.flags

        group = self.group

        het: dict[str, Any] | Unset = UNSET
        if not isinstance(self.het, Unset):
            het = self.het.to_dict()

        job_id = self.job_id

        name = self.name

        mcs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mcs, Unset):
            mcs = self.mcs.to_dict()

        nodes = self.nodes

        partition = self.partition

        priority = self.priority

        qos = self.qos

        required: dict[str, Any] | Unset = UNSET
        if not isinstance(self.required, Unset):
            required = self.required.to_dict()

        kill_request_user = self.kill_request_user

        reservation: dict[str, Any] | Unset = UNSET
        if not isinstance(self.reservation, Unset):
            reservation = self.reservation.to_dict()

        state: dict[str, Any] | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.to_dict()

        steps: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.steps, Unset):
            steps = []
            for steps_item_data in self.steps:
                steps_item = steps_item_data.to_dict()
                steps.append(steps_item)

        tres: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tres, Unset):
            tres = self.tres.to_dict()

        user = self.user

        wckey: dict[str, Any] | Unset = UNSET
        if not isinstance(self.wckey, Unset):
            wckey = self.wckey.to_dict()

        working_directory = self.working_directory

        container = self.container

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
        if time is not UNSET:
            field_dict["time"] = time
        if association is not UNSET:
            field_dict["association"] = association
        if cluster is not UNSET:
            field_dict["cluster"] = cluster
        if constraints is not UNSET:
            field_dict["constraints"] = constraints
        if derived_exit_code is not UNSET:
            field_dict["derived_exit_code"] = derived_exit_code
        if exit_code is not UNSET:
            field_dict["exit_code"] = exit_code
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
        if mcs is not UNSET:
            field_dict["mcs"] = mcs
        if nodes is not UNSET:
            field_dict["nodes"] = nodes
        if partition is not UNSET:
            field_dict["partition"] = partition
        if priority is not UNSET:
            field_dict["priority"] = priority
        if qos is not UNSET:
            field_dict["qos"] = qos
        if required is not UNSET:
            field_dict["required"] = required
        if kill_request_user is not UNSET:
            field_dict["kill_request_user"] = kill_request_user
        if reservation is not UNSET:
            field_dict["reservation"] = reservation
        if state is not UNSET:
            field_dict["state"] = state
        if steps is not UNSET:
            field_dict["steps"] = steps
        if tres is not UNSET:
            field_dict["tres"] = tres
        if user is not UNSET:
            field_dict["user"] = user
        if wckey is not UNSET:
            field_dict["wckey"] = wckey
        if working_directory is not UNSET:
            field_dict["working_directory"] = working_directory
        if container is not UNSET:
            field_dict["container"] = container

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dbv_0038_association_short_info import Dbv0038AssociationShortInfo
        from ..models.dbv_0038_job_array import Dbv0038JobArray
        from ..models.dbv_0038_job_comment import Dbv0038JobComment
        from ..models.dbv_0038_job_exit_code import Dbv0038JobExitCode
        from ..models.dbv_0038_job_het import Dbv0038JobHet
        from ..models.dbv_0038_job_mcs import Dbv0038JobMcs
        from ..models.dbv_0038_job_required import Dbv0038JobRequired
        from ..models.dbv_0038_job_reservation import Dbv0038JobReservation
        from ..models.dbv_0038_job_state import Dbv0038JobState
        from ..models.dbv_0038_job_step import Dbv0038JobStep
        from ..models.dbv_0038_job_time import Dbv0038JobTime
        from ..models.dbv_0038_job_tres import Dbv0038JobTres
        from ..models.dbv_0038_job_wckey import Dbv0038JobWckey

        d = dict(src_dict)
        account = d.pop("account", UNSET)

        _comment = d.pop("comment", UNSET)
        comment: Dbv0038JobComment | Unset
        if isinstance(_comment, Unset):
            comment = UNSET
        else:
            comment = Dbv0038JobComment.from_dict(_comment)

        allocation_nodes = d.pop("allocation_nodes", UNSET)

        _array = d.pop("array", UNSET)
        array: Dbv0038JobArray | Unset
        if isinstance(_array, Unset):
            array = UNSET
        else:
            array = Dbv0038JobArray.from_dict(_array)

        _time = d.pop("time", UNSET)
        time: Dbv0038JobTime | Unset
        if isinstance(_time, Unset):
            time = UNSET
        else:
            time = Dbv0038JobTime.from_dict(_time)

        _association = d.pop("association", UNSET)
        association: Dbv0038AssociationShortInfo | Unset
        if isinstance(_association, Unset):
            association = UNSET
        else:
            association = Dbv0038AssociationShortInfo.from_dict(_association)

        cluster = d.pop("cluster", UNSET)

        constraints = d.pop("constraints", UNSET)

        _derived_exit_code = d.pop("derived_exit_code", UNSET)
        derived_exit_code: Dbv0038JobExitCode | Unset
        if isinstance(_derived_exit_code, Unset):
            derived_exit_code = UNSET
        else:
            derived_exit_code = Dbv0038JobExitCode.from_dict(_derived_exit_code)

        _exit_code = d.pop("exit_code", UNSET)
        exit_code: Dbv0038JobExitCode | Unset
        if isinstance(_exit_code, Unset):
            exit_code = UNSET
        else:
            exit_code = Dbv0038JobExitCode.from_dict(_exit_code)

        flags = cast(list[str], d.pop("flags", UNSET))

        group = d.pop("group", UNSET)

        _het = d.pop("het", UNSET)
        het: Dbv0038JobHet | Unset
        if isinstance(_het, Unset):
            het = UNSET
        else:
            het = Dbv0038JobHet.from_dict(_het)

        job_id = d.pop("job_id", UNSET)

        name = d.pop("name", UNSET)

        _mcs = d.pop("mcs", UNSET)
        mcs: Dbv0038JobMcs | Unset
        if isinstance(_mcs, Unset):
            mcs = UNSET
        else:
            mcs = Dbv0038JobMcs.from_dict(_mcs)

        nodes = d.pop("nodes", UNSET)

        partition = d.pop("partition", UNSET)

        priority = d.pop("priority", UNSET)

        qos = d.pop("qos", UNSET)

        _required = d.pop("required", UNSET)
        required: Dbv0038JobRequired | Unset
        if isinstance(_required, Unset):
            required = UNSET
        else:
            required = Dbv0038JobRequired.from_dict(_required)

        kill_request_user = d.pop("kill_request_user", UNSET)

        _reservation = d.pop("reservation", UNSET)
        reservation: Dbv0038JobReservation | Unset
        if isinstance(_reservation, Unset):
            reservation = UNSET
        else:
            reservation = Dbv0038JobReservation.from_dict(_reservation)

        _state = d.pop("state", UNSET)
        state: Dbv0038JobState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = Dbv0038JobState.from_dict(_state)

        _steps = d.pop("steps", UNSET)
        steps: list[Dbv0038JobStep] | Unset = UNSET
        if _steps is not UNSET:
            steps = []
            for steps_item_data in _steps:
                steps_item = Dbv0038JobStep.from_dict(steps_item_data)

                steps.append(steps_item)

        _tres = d.pop("tres", UNSET)
        tres: Dbv0038JobTres | Unset
        if isinstance(_tres, Unset):
            tres = UNSET
        else:
            tres = Dbv0038JobTres.from_dict(_tres)

        user = d.pop("user", UNSET)

        _wckey = d.pop("wckey", UNSET)
        wckey: Dbv0038JobWckey | Unset
        if isinstance(_wckey, Unset):
            wckey = UNSET
        else:
            wckey = Dbv0038JobWckey.from_dict(_wckey)

        working_directory = d.pop("working_directory", UNSET)

        container = d.pop("container", UNSET)

        dbv_0038_job = cls(
            account=account,
            comment=comment,
            allocation_nodes=allocation_nodes,
            array=array,
            time=time,
            association=association,
            cluster=cluster,
            constraints=constraints,
            derived_exit_code=derived_exit_code,
            exit_code=exit_code,
            flags=flags,
            group=group,
            het=het,
            job_id=job_id,
            name=name,
            mcs=mcs,
            nodes=nodes,
            partition=partition,
            priority=priority,
            qos=qos,
            required=required,
            kill_request_user=kill_request_user,
            reservation=reservation,
            state=state,
            steps=steps,
            tres=tres,
            user=user,
            wckey=wckey,
            working_directory=working_directory,
            container=container,
        )

        dbv_0038_job.additional_properties = d
        return dbv_0038_job

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
