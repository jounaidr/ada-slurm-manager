from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dbv_0037_job_exit_code import Dbv0037JobExitCode
    from ..models.dbv_0037_job_step_cpu import Dbv0037JobStepCPU
    from ..models.dbv_0037_job_step_nodes import Dbv0037JobStepNodes
    from ..models.dbv_0037_job_step_statistics import Dbv0037JobStepStatistics
    from ..models.dbv_0037_job_step_step import Dbv0037JobStepStep
    from ..models.dbv_0037_job_step_task import Dbv0037JobStepTask
    from ..models.dbv_0037_job_step_tasks import Dbv0037JobStepTasks
    from ..models.dbv_0037_job_step_time import Dbv0037JobStepTime
    from ..models.dbv_0037_job_step_tres import Dbv0037JobStepTres


T = TypeVar("T", bound="Dbv0037JobStep")


@_attrs_define
class Dbv0037JobStep:
    """
    Attributes:
        time (Dbv0037JobStepTime | Unset): Time properties
        exit_code (Dbv0037JobExitCode | Unset):
        nodes (Dbv0037JobStepNodes | Unset): Node details
        tasks (Dbv0037JobStepTasks | Unset): Task properties
        pid (str | Unset): First process PID
        cpu (Dbv0037JobStepCPU | Unset): CPU properties
        kill_request_user (str | Unset): User who requested job killed
        state (str | Unset): State of job step
        statistics (Dbv0037JobStepStatistics | Unset): Statistics of job step
        step (Dbv0037JobStepStep | Unset): Step details
        task (Dbv0037JobStepTask | Unset): Task properties
        tres (Dbv0037JobStepTres | Unset): TRES usage
    """

    time: Dbv0037JobStepTime | Unset = UNSET
    exit_code: Dbv0037JobExitCode | Unset = UNSET
    nodes: Dbv0037JobStepNodes | Unset = UNSET
    tasks: Dbv0037JobStepTasks | Unset = UNSET
    pid: str | Unset = UNSET
    cpu: Dbv0037JobStepCPU | Unset = UNSET
    kill_request_user: str | Unset = UNSET
    state: str | Unset = UNSET
    statistics: Dbv0037JobStepStatistics | Unset = UNSET
    step: Dbv0037JobStepStep | Unset = UNSET
    task: Dbv0037JobStepTask | Unset = UNSET
    tres: Dbv0037JobStepTres | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        time: dict[str, Any] | Unset = UNSET
        if not isinstance(self.time, Unset):
            time = self.time.to_dict()

        exit_code: dict[str, Any] | Unset = UNSET
        if not isinstance(self.exit_code, Unset):
            exit_code = self.exit_code.to_dict()

        nodes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.nodes, Unset):
            nodes = self.nodes.to_dict()

        tasks: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tasks, Unset):
            tasks = self.tasks.to_dict()

        pid = self.pid

        cpu: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cpu, Unset):
            cpu = self.cpu.to_dict()

        kill_request_user = self.kill_request_user

        state = self.state

        statistics: dict[str, Any] | Unset = UNSET
        if not isinstance(self.statistics, Unset):
            statistics = self.statistics.to_dict()

        step: dict[str, Any] | Unset = UNSET
        if not isinstance(self.step, Unset):
            step = self.step.to_dict()

        task: dict[str, Any] | Unset = UNSET
        if not isinstance(self.task, Unset):
            task = self.task.to_dict()

        tres: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tres, Unset):
            tres = self.tres.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if time is not UNSET:
            field_dict["time"] = time
        if exit_code is not UNSET:
            field_dict["exit_code"] = exit_code
        if nodes is not UNSET:
            field_dict["nodes"] = nodes
        if tasks is not UNSET:
            field_dict["tasks"] = tasks
        if pid is not UNSET:
            field_dict["pid"] = pid
        if cpu is not UNSET:
            field_dict["CPU"] = cpu
        if kill_request_user is not UNSET:
            field_dict["kill_request_user"] = kill_request_user
        if state is not UNSET:
            field_dict["state"] = state
        if statistics is not UNSET:
            field_dict["statistics"] = statistics
        if step is not UNSET:
            field_dict["step"] = step
        if task is not UNSET:
            field_dict["task"] = task
        if tres is not UNSET:
            field_dict["tres"] = tres

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dbv_0037_job_exit_code import Dbv0037JobExitCode
        from ..models.dbv_0037_job_step_cpu import Dbv0037JobStepCPU
        from ..models.dbv_0037_job_step_nodes import Dbv0037JobStepNodes
        from ..models.dbv_0037_job_step_statistics import Dbv0037JobStepStatistics
        from ..models.dbv_0037_job_step_step import Dbv0037JobStepStep
        from ..models.dbv_0037_job_step_task import Dbv0037JobStepTask
        from ..models.dbv_0037_job_step_tasks import Dbv0037JobStepTasks
        from ..models.dbv_0037_job_step_time import Dbv0037JobStepTime
        from ..models.dbv_0037_job_step_tres import Dbv0037JobStepTres

        d = dict(src_dict)
        _time = d.pop("time", UNSET)
        time: Dbv0037JobStepTime | Unset
        if isinstance(_time, Unset):
            time = UNSET
        else:
            time = Dbv0037JobStepTime.from_dict(_time)

        _exit_code = d.pop("exit_code", UNSET)
        exit_code: Dbv0037JobExitCode | Unset
        if isinstance(_exit_code, Unset):
            exit_code = UNSET
        else:
            exit_code = Dbv0037JobExitCode.from_dict(_exit_code)

        _nodes = d.pop("nodes", UNSET)
        nodes: Dbv0037JobStepNodes | Unset
        if isinstance(_nodes, Unset):
            nodes = UNSET
        else:
            nodes = Dbv0037JobStepNodes.from_dict(_nodes)

        _tasks = d.pop("tasks", UNSET)
        tasks: Dbv0037JobStepTasks | Unset
        if isinstance(_tasks, Unset):
            tasks = UNSET
        else:
            tasks = Dbv0037JobStepTasks.from_dict(_tasks)

        pid = d.pop("pid", UNSET)

        _cpu = d.pop("CPU", UNSET)
        cpu: Dbv0037JobStepCPU | Unset
        if isinstance(_cpu, Unset):
            cpu = UNSET
        else:
            cpu = Dbv0037JobStepCPU.from_dict(_cpu)

        kill_request_user = d.pop("kill_request_user", UNSET)

        state = d.pop("state", UNSET)

        _statistics = d.pop("statistics", UNSET)
        statistics: Dbv0037JobStepStatistics | Unset
        if isinstance(_statistics, Unset):
            statistics = UNSET
        else:
            statistics = Dbv0037JobStepStatistics.from_dict(_statistics)

        _step = d.pop("step", UNSET)
        step: Dbv0037JobStepStep | Unset
        if isinstance(_step, Unset):
            step = UNSET
        else:
            step = Dbv0037JobStepStep.from_dict(_step)

        _task = d.pop("task", UNSET)
        task: Dbv0037JobStepTask | Unset
        if isinstance(_task, Unset):
            task = UNSET
        else:
            task = Dbv0037JobStepTask.from_dict(_task)

        _tres = d.pop("tres", UNSET)
        tres: Dbv0037JobStepTres | Unset
        if isinstance(_tres, Unset):
            tres = UNSET
        else:
            tres = Dbv0037JobStepTres.from_dict(_tres)

        dbv_0037_job_step = cls(
            time=time,
            exit_code=exit_code,
            nodes=nodes,
            tasks=tasks,
            pid=pid,
            cpu=cpu,
            kill_request_user=kill_request_user,
            state=state,
            statistics=statistics,
            step=step,
            task=task,
            tres=tres,
        )

        dbv_0037_job_step.additional_properties = d
        return dbv_0037_job_step

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
