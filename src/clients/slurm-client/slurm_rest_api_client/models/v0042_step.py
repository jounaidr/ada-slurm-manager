from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.v0042_job_state_item import V0042JobStateItem
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v0042_process_exit_code_verbose import V0042ProcessExitCodeVerbose
    from ..models.v0042_step_cpu import V0042StepCPU
    from ..models.v0042_step_nodes import V0042StepNodes
    from ..models.v0042_step_statistics import V0042StepStatistics
    from ..models.v0042_step_step import V0042StepStep
    from ..models.v0042_step_task import V0042StepTask
    from ..models.v0042_step_tasks import V0042StepTasks
    from ..models.v0042_step_time import V0042StepTime
    from ..models.v0042_step_tres import V0042StepTres


T = TypeVar("T", bound="V0042Step")


@_attrs_define
class V0042Step:
    """
    Attributes:
        time (V0042StepTime | Unset):
        exit_code (V0042ProcessExitCodeVerbose | Unset):
        nodes (V0042StepNodes | Unset):
        tasks (V0042StepTasks | Unset):
        pid (str | Unset): Deprecated; Process ID
        cpu (V0042StepCPU | Unset):
        kill_request_user (str | Unset): User ID that requested termination of the step
        state (list[V0042JobStateItem] | Unset):
        statistics (V0042StepStatistics | Unset):
        step (V0042StepStep | Unset):
        task (V0042StepTask | Unset):
        tres (V0042StepTres | Unset):
    """

    time: V0042StepTime | Unset = UNSET
    exit_code: V0042ProcessExitCodeVerbose | Unset = UNSET
    nodes: V0042StepNodes | Unset = UNSET
    tasks: V0042StepTasks | Unset = UNSET
    pid: str | Unset = UNSET
    cpu: V0042StepCPU | Unset = UNSET
    kill_request_user: str | Unset = UNSET
    state: list[V0042JobStateItem] | Unset = UNSET
    statistics: V0042StepStatistics | Unset = UNSET
    step: V0042StepStep | Unset = UNSET
    task: V0042StepTask | Unset = UNSET
    tres: V0042StepTres | Unset = UNSET
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

        state: list[str] | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = []
            for componentsschemasv0_0_42_job_state_item_data in self.state:
                componentsschemasv0_0_42_job_state_item = componentsschemasv0_0_42_job_state_item_data.value
                state.append(componentsschemasv0_0_42_job_state_item)

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
        from ..models.v0042_process_exit_code_verbose import V0042ProcessExitCodeVerbose
        from ..models.v0042_step_cpu import V0042StepCPU
        from ..models.v0042_step_nodes import V0042StepNodes
        from ..models.v0042_step_statistics import V0042StepStatistics
        from ..models.v0042_step_step import V0042StepStep
        from ..models.v0042_step_task import V0042StepTask
        from ..models.v0042_step_tasks import V0042StepTasks
        from ..models.v0042_step_time import V0042StepTime
        from ..models.v0042_step_tres import V0042StepTres

        d = dict(src_dict)
        _time = d.pop("time", UNSET)
        time: V0042StepTime | Unset
        if isinstance(_time, Unset):
            time = UNSET
        else:
            time = V0042StepTime.from_dict(_time)

        _exit_code = d.pop("exit_code", UNSET)
        exit_code: V0042ProcessExitCodeVerbose | Unset
        if isinstance(_exit_code, Unset):
            exit_code = UNSET
        else:
            exit_code = V0042ProcessExitCodeVerbose.from_dict(_exit_code)

        _nodes = d.pop("nodes", UNSET)
        nodes: V0042StepNodes | Unset
        if isinstance(_nodes, Unset):
            nodes = UNSET
        else:
            nodes = V0042StepNodes.from_dict(_nodes)

        _tasks = d.pop("tasks", UNSET)
        tasks: V0042StepTasks | Unset
        if isinstance(_tasks, Unset):
            tasks = UNSET
        else:
            tasks = V0042StepTasks.from_dict(_tasks)

        pid = d.pop("pid", UNSET)

        _cpu = d.pop("CPU", UNSET)
        cpu: V0042StepCPU | Unset
        if isinstance(_cpu, Unset):
            cpu = UNSET
        else:
            cpu = V0042StepCPU.from_dict(_cpu)

        kill_request_user = d.pop("kill_request_user", UNSET)

        _state = d.pop("state", UNSET)
        state: list[V0042JobStateItem] | Unset = UNSET
        if _state is not UNSET:
            state = []
            for componentsschemasv0_0_42_job_state_item_data in _state:
                componentsschemasv0_0_42_job_state_item = V0042JobStateItem(
                    componentsschemasv0_0_42_job_state_item_data
                )

                state.append(componentsschemasv0_0_42_job_state_item)

        _statistics = d.pop("statistics", UNSET)
        statistics: V0042StepStatistics | Unset
        if isinstance(_statistics, Unset):
            statistics = UNSET
        else:
            statistics = V0042StepStatistics.from_dict(_statistics)

        _step = d.pop("step", UNSET)
        step: V0042StepStep | Unset
        if isinstance(_step, Unset):
            step = UNSET
        else:
            step = V0042StepStep.from_dict(_step)

        _task = d.pop("task", UNSET)
        task: V0042StepTask | Unset
        if isinstance(_task, Unset):
            task = UNSET
        else:
            task = V0042StepTask.from_dict(_task)

        _tres = d.pop("tres", UNSET)
        tres: V0042StepTres | Unset
        if isinstance(_tres, Unset):
            tres = UNSET
        else:
            tres = V0042StepTres.from_dict(_tres)

        v0042_step = cls(
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

        v0042_step.additional_properties = d
        return v0042_step

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
