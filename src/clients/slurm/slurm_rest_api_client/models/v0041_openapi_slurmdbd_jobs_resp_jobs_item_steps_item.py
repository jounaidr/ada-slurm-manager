from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.v0041_openapi_slurmdbd_jobs_resp_jobs_item_steps_item_state_item import (
    V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemStateItem,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v0041_openapi_slurmdbd_jobs_resp_jobs_item_steps_item_cpu import (
        V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemCPU,
    )
    from ..models.v0041_openapi_slurmdbd_jobs_resp_jobs_item_steps_item_exit_code import (
        V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemExitCode,
    )
    from ..models.v0041_openapi_slurmdbd_jobs_resp_jobs_item_steps_item_nodes import (
        V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemNodes,
    )
    from ..models.v0041_openapi_slurmdbd_jobs_resp_jobs_item_steps_item_statistics import (
        V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemStatistics,
    )
    from ..models.v0041_openapi_slurmdbd_jobs_resp_jobs_item_steps_item_step import (
        V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemStep,
    )
    from ..models.v0041_openapi_slurmdbd_jobs_resp_jobs_item_steps_item_task import (
        V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemTask,
    )
    from ..models.v0041_openapi_slurmdbd_jobs_resp_jobs_item_steps_item_tasks import (
        V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemTasks,
    )
    from ..models.v0041_openapi_slurmdbd_jobs_resp_jobs_item_steps_item_time import (
        V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemTime,
    )
    from ..models.v0041_openapi_slurmdbd_jobs_resp_jobs_item_steps_item_tres import (
        V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemTres,
    )


T = TypeVar("T", bound="V0041OpenapiSlurmdbdJobsRespJobsItemStepsItem")


@_attrs_define
class V0041OpenapiSlurmdbdJobsRespJobsItemStepsItem:
    """
    Attributes:
        time (V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemTime | Unset):
        exit_code (V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemExitCode | Unset): Exit code
        nodes (V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemNodes | Unset):
        tasks (V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemTasks | Unset):
        pid (str | Unset): Process ID
        cpu (V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemCPU | Unset):
        kill_request_user (str | Unset): User ID that requested termination of the step
        state (list[V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemStateItem] | Unset): Current state
        statistics (V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemStatistics | Unset):
        step (V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemStep | Unset):
        task (V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemTask | Unset):
        tres (V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemTres | Unset):
    """

    time: V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemTime | Unset = UNSET
    exit_code: V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemExitCode | Unset = UNSET
    nodes: V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemNodes | Unset = UNSET
    tasks: V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemTasks | Unset = UNSET
    pid: str | Unset = UNSET
    cpu: V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemCPU | Unset = UNSET
    kill_request_user: str | Unset = UNSET
    state: list[V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemStateItem] | Unset = UNSET
    statistics: V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemStatistics | Unset = UNSET
    step: V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemStep | Unset = UNSET
    task: V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemTask | Unset = UNSET
    tres: V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemTres | Unset = UNSET
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
            for state_item_data in self.state:
                state_item = state_item_data.value
                state.append(state_item)

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
        from ..models.v0041_openapi_slurmdbd_jobs_resp_jobs_item_steps_item_cpu import (
            V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemCPU,
        )
        from ..models.v0041_openapi_slurmdbd_jobs_resp_jobs_item_steps_item_exit_code import (
            V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemExitCode,
        )
        from ..models.v0041_openapi_slurmdbd_jobs_resp_jobs_item_steps_item_nodes import (
            V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemNodes,
        )
        from ..models.v0041_openapi_slurmdbd_jobs_resp_jobs_item_steps_item_statistics import (
            V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemStatistics,
        )
        from ..models.v0041_openapi_slurmdbd_jobs_resp_jobs_item_steps_item_step import (
            V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemStep,
        )
        from ..models.v0041_openapi_slurmdbd_jobs_resp_jobs_item_steps_item_task import (
            V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemTask,
        )
        from ..models.v0041_openapi_slurmdbd_jobs_resp_jobs_item_steps_item_tasks import (
            V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemTasks,
        )
        from ..models.v0041_openapi_slurmdbd_jobs_resp_jobs_item_steps_item_time import (
            V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemTime,
        )
        from ..models.v0041_openapi_slurmdbd_jobs_resp_jobs_item_steps_item_tres import (
            V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemTres,
        )

        d = dict(src_dict)
        _time = d.pop("time", UNSET)
        time: V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemTime | Unset
        if isinstance(_time, Unset):
            time = UNSET
        else:
            time = V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemTime.from_dict(_time)

        _exit_code = d.pop("exit_code", UNSET)
        exit_code: V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemExitCode | Unset
        if isinstance(_exit_code, Unset):
            exit_code = UNSET
        else:
            exit_code = V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemExitCode.from_dict(_exit_code)

        _nodes = d.pop("nodes", UNSET)
        nodes: V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemNodes | Unset
        if isinstance(_nodes, Unset):
            nodes = UNSET
        else:
            nodes = V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemNodes.from_dict(_nodes)

        _tasks = d.pop("tasks", UNSET)
        tasks: V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemTasks | Unset
        if isinstance(_tasks, Unset):
            tasks = UNSET
        else:
            tasks = V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemTasks.from_dict(_tasks)

        pid = d.pop("pid", UNSET)

        _cpu = d.pop("CPU", UNSET)
        cpu: V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemCPU | Unset
        if isinstance(_cpu, Unset):
            cpu = UNSET
        else:
            cpu = V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemCPU.from_dict(_cpu)

        kill_request_user = d.pop("kill_request_user", UNSET)

        _state = d.pop("state", UNSET)
        state: list[V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemStateItem] | Unset = UNSET
        if _state is not UNSET:
            state = []
            for state_item_data in _state:
                state_item = V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemStateItem(state_item_data)

                state.append(state_item)

        _statistics = d.pop("statistics", UNSET)
        statistics: V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemStatistics | Unset
        if isinstance(_statistics, Unset):
            statistics = UNSET
        else:
            statistics = V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemStatistics.from_dict(_statistics)

        _step = d.pop("step", UNSET)
        step: V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemStep | Unset
        if isinstance(_step, Unset):
            step = UNSET
        else:
            step = V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemStep.from_dict(_step)

        _task = d.pop("task", UNSET)
        task: V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemTask | Unset
        if isinstance(_task, Unset):
            task = UNSET
        else:
            task = V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemTask.from_dict(_task)

        _tres = d.pop("tres", UNSET)
        tres: V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemTres | Unset
        if isinstance(_tres, Unset):
            tres = UNSET
        else:
            tres = V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemTres.from_dict(_tres)

        v0041_openapi_slurmdbd_jobs_resp_jobs_item_steps_item = cls(
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

        v0041_openapi_slurmdbd_jobs_resp_jobs_item_steps_item.additional_properties = d
        return v0041_openapi_slurmdbd_jobs_resp_jobs_item_steps_item

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
