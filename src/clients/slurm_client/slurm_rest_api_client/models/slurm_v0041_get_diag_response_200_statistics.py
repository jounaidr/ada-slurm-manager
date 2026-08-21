from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.slurm_v0041_get_diag_response_200_statistics_bf_exit import (
        SlurmV0041GetDiagResponse200StatisticsBfExit,
    )
    from ..models.slurm_v0041_get_diag_response_200_statistics_bf_when_last_cycle import (
        SlurmV0041GetDiagResponse200StatisticsBfWhenLastCycle,
    )
    from ..models.slurm_v0041_get_diag_response_200_statistics_job_states_ts import (
        SlurmV0041GetDiagResponse200StatisticsJobStatesTs,
    )
    from ..models.slurm_v0041_get_diag_response_200_statistics_pending_rpcs_by_hostlist_item import (
        SlurmV0041GetDiagResponse200StatisticsPendingRpcsByHostlistItem,
    )
    from ..models.slurm_v0041_get_diag_response_200_statistics_pending_rpcs_item import (
        SlurmV0041GetDiagResponse200StatisticsPendingRpcsItem,
    )
    from ..models.slurm_v0041_get_diag_response_200_statistics_req_time import (
        SlurmV0041GetDiagResponse200StatisticsReqTime,
    )
    from ..models.slurm_v0041_get_diag_response_200_statistics_req_time_start import (
        SlurmV0041GetDiagResponse200StatisticsReqTimeStart,
    )
    from ..models.slurm_v0041_get_diag_response_200_statistics_rpcs_by_message_type_item import (
        SlurmV0041GetDiagResponse200StatisticsRpcsByMessageTypeItem,
    )
    from ..models.slurm_v0041_get_diag_response_200_statistics_rpcs_by_user_item import (
        SlurmV0041GetDiagResponse200StatisticsRpcsByUserItem,
    )
    from ..models.slurm_v0041_get_diag_response_200_statistics_schedule_exit import (
        SlurmV0041GetDiagResponse200StatisticsScheduleExit,
    )


T = TypeVar("T", bound="SlurmV0041GetDiagResponse200Statistics")


@_attrs_define
class SlurmV0041GetDiagResponse200Statistics:
    """statistics

    Attributes:
        parts_packed (int | Unset): Zero if only RPC statistic included
        req_time (SlurmV0041GetDiagResponse200StatisticsReqTime | Unset): When the request was made (UNIX timestamp)
        req_time_start (SlurmV0041GetDiagResponse200StatisticsReqTimeStart | Unset): When the data in the report started
            (UNIX timestamp)
        server_thread_count (int | Unset): Number of current active slurmctld threads
        agent_queue_size (int | Unset): Number of enqueued outgoing RPC requests in an internal retry list
        agent_count (int | Unset): Number of agent threads
        agent_thread_count (int | Unset): Total number of active threads created by all agent threads
        dbd_agent_queue_size (int | Unset): Number of messages for SlurmDBD that are queued
        gettimeofday_latency (int | Unset): Latency of 1000 calls to the gettimeofday() syscall in microseconds, as
            measured at controller startup
        schedule_cycle_max (int | Unset): Max time of any scheduling cycle in microseconds since last reset
        schedule_cycle_last (int | Unset): Time in microseconds for last scheduling cycle
        schedule_cycle_sum (int | Unset): Total run time in microseconds for all scheduling cycles since last reset
        schedule_cycle_total (int | Unset): Number of scheduling cycles since last reset
        schedule_cycle_mean (int | Unset): Mean time in microseconds for all scheduling cycles since last reset
        schedule_cycle_mean_depth (int | Unset): Mean of the number of jobs processed in a scheduling cycle
        schedule_cycle_per_minute (int | Unset): Number of scheduling executions per minute
        schedule_cycle_depth (int | Unset): Total number of jobs processed in scheduling cycles
        schedule_exit (SlurmV0041GetDiagResponse200StatisticsScheduleExit | Unset): Reasons for which the scheduling
            cycle exited since last reset
        schedule_queue_length (int | Unset): Number of jobs pending in queue
        jobs_submitted (int | Unset): Number of jobs submitted since last reset
        jobs_started (int | Unset): Number of jobs started since last reset
        jobs_completed (int | Unset): Number of jobs completed since last reset
        jobs_canceled (int | Unset): Number of jobs canceled since the last reset
        jobs_failed (int | Unset): Number of jobs failed due to slurmd or other internal issues since last reset
        jobs_pending (int | Unset): Number of jobs pending at the time of listed in job_state_ts
        jobs_running (int | Unset): Number of jobs running at the time of listed in job_state_ts
        job_states_ts (SlurmV0041GetDiagResponse200StatisticsJobStatesTs | Unset): When the job state counts were
            gathered (UNIX timestamp)
        bf_backfilled_jobs (int | Unset): Number of jobs started through backfilling since last slurm start
        bf_last_backfilled_jobs (int | Unset): Number of jobs started through backfilling since last reset
        bf_backfilled_het_jobs (int | Unset): Number of heterogeneous job components started through backfilling since
            last Slurm start
        bf_cycle_counter (int | Unset): Number of backfill scheduling cycles since last reset
        bf_cycle_mean (int | Unset): Mean time in microseconds of backfilling scheduling cycles since last reset
        bf_depth_mean (int | Unset): Mean number of eligible to run jobs processed during all backfilling scheduling
            cycles since last reset
        bf_depth_mean_try (int | Unset): The subset of Depth Mean that the backfill scheduler attempted to schedule
        bf_cycle_sum (int | Unset): Total time in microseconds of backfilling scheduling cycles since last reset
        bf_cycle_last (int | Unset): Execution time in microseconds of last backfill scheduling cycle
        bf_cycle_max (int | Unset): Execution time in microseconds of longest backfill scheduling cycle
        bf_exit (SlurmV0041GetDiagResponse200StatisticsBfExit | Unset): Reasons for which the backfill scheduling cycle
            exited since last reset
        bf_last_depth (int | Unset): Number of processed jobs during last backfilling scheduling cycle
        bf_last_depth_try (int | Unset): Number of processed jobs during last backfilling scheduling cycle that had a
            chance to start using available resources
        bf_depth_sum (int | Unset): Total number of jobs processed during all backfilling scheduling cycles since last
            reset
        bf_depth_try_sum (int | Unset): Subset of bf_depth_sum that the backfill scheduler attempted to schedule
        bf_queue_len (int | Unset): Number of jobs pending to be processed by backfilling algorithm
        bf_queue_len_mean (int | Unset): Mean number of jobs pending to be processed by backfilling algorithm
        bf_queue_len_sum (int | Unset): Total number of jobs pending to be processed by backfilling algorithm since last
            reset
        bf_table_size (int | Unset): Number of different time slots tested by the backfill scheduler in its last
            iteration
        bf_table_size_sum (int | Unset): Total number of different time slots tested by the backfill scheduler
        bf_table_size_mean (int | Unset): Mean number of different time slots tested by the backfill scheduler
        bf_when_last_cycle (SlurmV0041GetDiagResponse200StatisticsBfWhenLastCycle | Unset): When the last backfill
            scheduling cycle happened (UNIX timestamp)
        bf_active (bool | Unset): Backfill scheduler currently running
        rpcs_by_message_type (list[SlurmV0041GetDiagResponse200StatisticsRpcsByMessageTypeItem] | Unset): Most
            frequently issued remote procedure calls (RPCs)
        rpcs_by_user (list[SlurmV0041GetDiagResponse200StatisticsRpcsByUserItem] | Unset): RPCs issued by user ID
        pending_rpcs (list[SlurmV0041GetDiagResponse200StatisticsPendingRpcsItem] | Unset): Pending RPC statistics
        pending_rpcs_by_hostlist (list[SlurmV0041GetDiagResponse200StatisticsPendingRpcsByHostlistItem] | Unset):
            Pending RPCs hostlists
    """

    parts_packed: int | Unset = UNSET
    req_time: SlurmV0041GetDiagResponse200StatisticsReqTime | Unset = UNSET
    req_time_start: SlurmV0041GetDiagResponse200StatisticsReqTimeStart | Unset = UNSET
    server_thread_count: int | Unset = UNSET
    agent_queue_size: int | Unset = UNSET
    agent_count: int | Unset = UNSET
    agent_thread_count: int | Unset = UNSET
    dbd_agent_queue_size: int | Unset = UNSET
    gettimeofday_latency: int | Unset = UNSET
    schedule_cycle_max: int | Unset = UNSET
    schedule_cycle_last: int | Unset = UNSET
    schedule_cycle_sum: int | Unset = UNSET
    schedule_cycle_total: int | Unset = UNSET
    schedule_cycle_mean: int | Unset = UNSET
    schedule_cycle_mean_depth: int | Unset = UNSET
    schedule_cycle_per_minute: int | Unset = UNSET
    schedule_cycle_depth: int | Unset = UNSET
    schedule_exit: SlurmV0041GetDiagResponse200StatisticsScheduleExit | Unset = UNSET
    schedule_queue_length: int | Unset = UNSET
    jobs_submitted: int | Unset = UNSET
    jobs_started: int | Unset = UNSET
    jobs_completed: int | Unset = UNSET
    jobs_canceled: int | Unset = UNSET
    jobs_failed: int | Unset = UNSET
    jobs_pending: int | Unset = UNSET
    jobs_running: int | Unset = UNSET
    job_states_ts: SlurmV0041GetDiagResponse200StatisticsJobStatesTs | Unset = UNSET
    bf_backfilled_jobs: int | Unset = UNSET
    bf_last_backfilled_jobs: int | Unset = UNSET
    bf_backfilled_het_jobs: int | Unset = UNSET
    bf_cycle_counter: int | Unset = UNSET
    bf_cycle_mean: int | Unset = UNSET
    bf_depth_mean: int | Unset = UNSET
    bf_depth_mean_try: int | Unset = UNSET
    bf_cycle_sum: int | Unset = UNSET
    bf_cycle_last: int | Unset = UNSET
    bf_cycle_max: int | Unset = UNSET
    bf_exit: SlurmV0041GetDiagResponse200StatisticsBfExit | Unset = UNSET
    bf_last_depth: int | Unset = UNSET
    bf_last_depth_try: int | Unset = UNSET
    bf_depth_sum: int | Unset = UNSET
    bf_depth_try_sum: int | Unset = UNSET
    bf_queue_len: int | Unset = UNSET
    bf_queue_len_mean: int | Unset = UNSET
    bf_queue_len_sum: int | Unset = UNSET
    bf_table_size: int | Unset = UNSET
    bf_table_size_sum: int | Unset = UNSET
    bf_table_size_mean: int | Unset = UNSET
    bf_when_last_cycle: SlurmV0041GetDiagResponse200StatisticsBfWhenLastCycle | Unset = UNSET
    bf_active: bool | Unset = UNSET
    rpcs_by_message_type: list[SlurmV0041GetDiagResponse200StatisticsRpcsByMessageTypeItem] | Unset = UNSET
    rpcs_by_user: list[SlurmV0041GetDiagResponse200StatisticsRpcsByUserItem] | Unset = UNSET
    pending_rpcs: list[SlurmV0041GetDiagResponse200StatisticsPendingRpcsItem] | Unset = UNSET
    pending_rpcs_by_hostlist: list[SlurmV0041GetDiagResponse200StatisticsPendingRpcsByHostlistItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        parts_packed = self.parts_packed

        req_time: dict[str, Any] | Unset = UNSET
        if not isinstance(self.req_time, Unset):
            req_time = self.req_time.to_dict()

        req_time_start: dict[str, Any] | Unset = UNSET
        if not isinstance(self.req_time_start, Unset):
            req_time_start = self.req_time_start.to_dict()

        server_thread_count = self.server_thread_count

        agent_queue_size = self.agent_queue_size

        agent_count = self.agent_count

        agent_thread_count = self.agent_thread_count

        dbd_agent_queue_size = self.dbd_agent_queue_size

        gettimeofday_latency = self.gettimeofday_latency

        schedule_cycle_max = self.schedule_cycle_max

        schedule_cycle_last = self.schedule_cycle_last

        schedule_cycle_sum = self.schedule_cycle_sum

        schedule_cycle_total = self.schedule_cycle_total

        schedule_cycle_mean = self.schedule_cycle_mean

        schedule_cycle_mean_depth = self.schedule_cycle_mean_depth

        schedule_cycle_per_minute = self.schedule_cycle_per_minute

        schedule_cycle_depth = self.schedule_cycle_depth

        schedule_exit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.schedule_exit, Unset):
            schedule_exit = self.schedule_exit.to_dict()

        schedule_queue_length = self.schedule_queue_length

        jobs_submitted = self.jobs_submitted

        jobs_started = self.jobs_started

        jobs_completed = self.jobs_completed

        jobs_canceled = self.jobs_canceled

        jobs_failed = self.jobs_failed

        jobs_pending = self.jobs_pending

        jobs_running = self.jobs_running

        job_states_ts: dict[str, Any] | Unset = UNSET
        if not isinstance(self.job_states_ts, Unset):
            job_states_ts = self.job_states_ts.to_dict()

        bf_backfilled_jobs = self.bf_backfilled_jobs

        bf_last_backfilled_jobs = self.bf_last_backfilled_jobs

        bf_backfilled_het_jobs = self.bf_backfilled_het_jobs

        bf_cycle_counter = self.bf_cycle_counter

        bf_cycle_mean = self.bf_cycle_mean

        bf_depth_mean = self.bf_depth_mean

        bf_depth_mean_try = self.bf_depth_mean_try

        bf_cycle_sum = self.bf_cycle_sum

        bf_cycle_last = self.bf_cycle_last

        bf_cycle_max = self.bf_cycle_max

        bf_exit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.bf_exit, Unset):
            bf_exit = self.bf_exit.to_dict()

        bf_last_depth = self.bf_last_depth

        bf_last_depth_try = self.bf_last_depth_try

        bf_depth_sum = self.bf_depth_sum

        bf_depth_try_sum = self.bf_depth_try_sum

        bf_queue_len = self.bf_queue_len

        bf_queue_len_mean = self.bf_queue_len_mean

        bf_queue_len_sum = self.bf_queue_len_sum

        bf_table_size = self.bf_table_size

        bf_table_size_sum = self.bf_table_size_sum

        bf_table_size_mean = self.bf_table_size_mean

        bf_when_last_cycle: dict[str, Any] | Unset = UNSET
        if not isinstance(self.bf_when_last_cycle, Unset):
            bf_when_last_cycle = self.bf_when_last_cycle.to_dict()

        bf_active = self.bf_active

        rpcs_by_message_type: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.rpcs_by_message_type, Unset):
            rpcs_by_message_type = []
            for rpcs_by_message_type_item_data in self.rpcs_by_message_type:
                rpcs_by_message_type_item = rpcs_by_message_type_item_data.to_dict()
                rpcs_by_message_type.append(rpcs_by_message_type_item)

        rpcs_by_user: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.rpcs_by_user, Unset):
            rpcs_by_user = []
            for rpcs_by_user_item_data in self.rpcs_by_user:
                rpcs_by_user_item = rpcs_by_user_item_data.to_dict()
                rpcs_by_user.append(rpcs_by_user_item)

        pending_rpcs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.pending_rpcs, Unset):
            pending_rpcs = []
            for pending_rpcs_item_data in self.pending_rpcs:
                pending_rpcs_item = pending_rpcs_item_data.to_dict()
                pending_rpcs.append(pending_rpcs_item)

        pending_rpcs_by_hostlist: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.pending_rpcs_by_hostlist, Unset):
            pending_rpcs_by_hostlist = []
            for pending_rpcs_by_hostlist_item_data in self.pending_rpcs_by_hostlist:
                pending_rpcs_by_hostlist_item = pending_rpcs_by_hostlist_item_data.to_dict()
                pending_rpcs_by_hostlist.append(pending_rpcs_by_hostlist_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if parts_packed is not UNSET:
            field_dict["parts_packed"] = parts_packed
        if req_time is not UNSET:
            field_dict["req_time"] = req_time
        if req_time_start is not UNSET:
            field_dict["req_time_start"] = req_time_start
        if server_thread_count is not UNSET:
            field_dict["server_thread_count"] = server_thread_count
        if agent_queue_size is not UNSET:
            field_dict["agent_queue_size"] = agent_queue_size
        if agent_count is not UNSET:
            field_dict["agent_count"] = agent_count
        if agent_thread_count is not UNSET:
            field_dict["agent_thread_count"] = agent_thread_count
        if dbd_agent_queue_size is not UNSET:
            field_dict["dbd_agent_queue_size"] = dbd_agent_queue_size
        if gettimeofday_latency is not UNSET:
            field_dict["gettimeofday_latency"] = gettimeofday_latency
        if schedule_cycle_max is not UNSET:
            field_dict["schedule_cycle_max"] = schedule_cycle_max
        if schedule_cycle_last is not UNSET:
            field_dict["schedule_cycle_last"] = schedule_cycle_last
        if schedule_cycle_sum is not UNSET:
            field_dict["schedule_cycle_sum"] = schedule_cycle_sum
        if schedule_cycle_total is not UNSET:
            field_dict["schedule_cycle_total"] = schedule_cycle_total
        if schedule_cycle_mean is not UNSET:
            field_dict["schedule_cycle_mean"] = schedule_cycle_mean
        if schedule_cycle_mean_depth is not UNSET:
            field_dict["schedule_cycle_mean_depth"] = schedule_cycle_mean_depth
        if schedule_cycle_per_minute is not UNSET:
            field_dict["schedule_cycle_per_minute"] = schedule_cycle_per_minute
        if schedule_cycle_depth is not UNSET:
            field_dict["schedule_cycle_depth"] = schedule_cycle_depth
        if schedule_exit is not UNSET:
            field_dict["schedule_exit"] = schedule_exit
        if schedule_queue_length is not UNSET:
            field_dict["schedule_queue_length"] = schedule_queue_length
        if jobs_submitted is not UNSET:
            field_dict["jobs_submitted"] = jobs_submitted
        if jobs_started is not UNSET:
            field_dict["jobs_started"] = jobs_started
        if jobs_completed is not UNSET:
            field_dict["jobs_completed"] = jobs_completed
        if jobs_canceled is not UNSET:
            field_dict["jobs_canceled"] = jobs_canceled
        if jobs_failed is not UNSET:
            field_dict["jobs_failed"] = jobs_failed
        if jobs_pending is not UNSET:
            field_dict["jobs_pending"] = jobs_pending
        if jobs_running is not UNSET:
            field_dict["jobs_running"] = jobs_running
        if job_states_ts is not UNSET:
            field_dict["job_states_ts"] = job_states_ts
        if bf_backfilled_jobs is not UNSET:
            field_dict["bf_backfilled_jobs"] = bf_backfilled_jobs
        if bf_last_backfilled_jobs is not UNSET:
            field_dict["bf_last_backfilled_jobs"] = bf_last_backfilled_jobs
        if bf_backfilled_het_jobs is not UNSET:
            field_dict["bf_backfilled_het_jobs"] = bf_backfilled_het_jobs
        if bf_cycle_counter is not UNSET:
            field_dict["bf_cycle_counter"] = bf_cycle_counter
        if bf_cycle_mean is not UNSET:
            field_dict["bf_cycle_mean"] = bf_cycle_mean
        if bf_depth_mean is not UNSET:
            field_dict["bf_depth_mean"] = bf_depth_mean
        if bf_depth_mean_try is not UNSET:
            field_dict["bf_depth_mean_try"] = bf_depth_mean_try
        if bf_cycle_sum is not UNSET:
            field_dict["bf_cycle_sum"] = bf_cycle_sum
        if bf_cycle_last is not UNSET:
            field_dict["bf_cycle_last"] = bf_cycle_last
        if bf_cycle_max is not UNSET:
            field_dict["bf_cycle_max"] = bf_cycle_max
        if bf_exit is not UNSET:
            field_dict["bf_exit"] = bf_exit
        if bf_last_depth is not UNSET:
            field_dict["bf_last_depth"] = bf_last_depth
        if bf_last_depth_try is not UNSET:
            field_dict["bf_last_depth_try"] = bf_last_depth_try
        if bf_depth_sum is not UNSET:
            field_dict["bf_depth_sum"] = bf_depth_sum
        if bf_depth_try_sum is not UNSET:
            field_dict["bf_depth_try_sum"] = bf_depth_try_sum
        if bf_queue_len is not UNSET:
            field_dict["bf_queue_len"] = bf_queue_len
        if bf_queue_len_mean is not UNSET:
            field_dict["bf_queue_len_mean"] = bf_queue_len_mean
        if bf_queue_len_sum is not UNSET:
            field_dict["bf_queue_len_sum"] = bf_queue_len_sum
        if bf_table_size is not UNSET:
            field_dict["bf_table_size"] = bf_table_size
        if bf_table_size_sum is not UNSET:
            field_dict["bf_table_size_sum"] = bf_table_size_sum
        if bf_table_size_mean is not UNSET:
            field_dict["bf_table_size_mean"] = bf_table_size_mean
        if bf_when_last_cycle is not UNSET:
            field_dict["bf_when_last_cycle"] = bf_when_last_cycle
        if bf_active is not UNSET:
            field_dict["bf_active"] = bf_active
        if rpcs_by_message_type is not UNSET:
            field_dict["rpcs_by_message_type"] = rpcs_by_message_type
        if rpcs_by_user is not UNSET:
            field_dict["rpcs_by_user"] = rpcs_by_user
        if pending_rpcs is not UNSET:
            field_dict["pending_rpcs"] = pending_rpcs
        if pending_rpcs_by_hostlist is not UNSET:
            field_dict["pending_rpcs_by_hostlist"] = pending_rpcs_by_hostlist

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.slurm_v0041_get_diag_response_200_statistics_bf_exit import (
            SlurmV0041GetDiagResponse200StatisticsBfExit,
        )
        from ..models.slurm_v0041_get_diag_response_200_statistics_bf_when_last_cycle import (
            SlurmV0041GetDiagResponse200StatisticsBfWhenLastCycle,
        )
        from ..models.slurm_v0041_get_diag_response_200_statistics_job_states_ts import (
            SlurmV0041GetDiagResponse200StatisticsJobStatesTs,
        )
        from ..models.slurm_v0041_get_diag_response_200_statistics_pending_rpcs_by_hostlist_item import (
            SlurmV0041GetDiagResponse200StatisticsPendingRpcsByHostlistItem,
        )
        from ..models.slurm_v0041_get_diag_response_200_statistics_pending_rpcs_item import (
            SlurmV0041GetDiagResponse200StatisticsPendingRpcsItem,
        )
        from ..models.slurm_v0041_get_diag_response_200_statistics_req_time import (
            SlurmV0041GetDiagResponse200StatisticsReqTime,
        )
        from ..models.slurm_v0041_get_diag_response_200_statistics_req_time_start import (
            SlurmV0041GetDiagResponse200StatisticsReqTimeStart,
        )
        from ..models.slurm_v0041_get_diag_response_200_statistics_rpcs_by_message_type_item import (
            SlurmV0041GetDiagResponse200StatisticsRpcsByMessageTypeItem,
        )
        from ..models.slurm_v0041_get_diag_response_200_statistics_rpcs_by_user_item import (
            SlurmV0041GetDiagResponse200StatisticsRpcsByUserItem,
        )
        from ..models.slurm_v0041_get_diag_response_200_statistics_schedule_exit import (
            SlurmV0041GetDiagResponse200StatisticsScheduleExit,
        )

        d = dict(src_dict)
        parts_packed = d.pop("parts_packed", UNSET)

        _req_time = d.pop("req_time", UNSET)
        req_time: SlurmV0041GetDiagResponse200StatisticsReqTime | Unset
        if isinstance(_req_time, Unset):
            req_time = UNSET
        else:
            req_time = SlurmV0041GetDiagResponse200StatisticsReqTime.from_dict(_req_time)

        _req_time_start = d.pop("req_time_start", UNSET)
        req_time_start: SlurmV0041GetDiagResponse200StatisticsReqTimeStart | Unset
        if isinstance(_req_time_start, Unset):
            req_time_start = UNSET
        else:
            req_time_start = SlurmV0041GetDiagResponse200StatisticsReqTimeStart.from_dict(_req_time_start)

        server_thread_count = d.pop("server_thread_count", UNSET)

        agent_queue_size = d.pop("agent_queue_size", UNSET)

        agent_count = d.pop("agent_count", UNSET)

        agent_thread_count = d.pop("agent_thread_count", UNSET)

        dbd_agent_queue_size = d.pop("dbd_agent_queue_size", UNSET)

        gettimeofday_latency = d.pop("gettimeofday_latency", UNSET)

        schedule_cycle_max = d.pop("schedule_cycle_max", UNSET)

        schedule_cycle_last = d.pop("schedule_cycle_last", UNSET)

        schedule_cycle_sum = d.pop("schedule_cycle_sum", UNSET)

        schedule_cycle_total = d.pop("schedule_cycle_total", UNSET)

        schedule_cycle_mean = d.pop("schedule_cycle_mean", UNSET)

        schedule_cycle_mean_depth = d.pop("schedule_cycle_mean_depth", UNSET)

        schedule_cycle_per_minute = d.pop("schedule_cycle_per_minute", UNSET)

        schedule_cycle_depth = d.pop("schedule_cycle_depth", UNSET)

        _schedule_exit = d.pop("schedule_exit", UNSET)
        schedule_exit: SlurmV0041GetDiagResponse200StatisticsScheduleExit | Unset
        if isinstance(_schedule_exit, Unset):
            schedule_exit = UNSET
        else:
            schedule_exit = SlurmV0041GetDiagResponse200StatisticsScheduleExit.from_dict(_schedule_exit)

        schedule_queue_length = d.pop("schedule_queue_length", UNSET)

        jobs_submitted = d.pop("jobs_submitted", UNSET)

        jobs_started = d.pop("jobs_started", UNSET)

        jobs_completed = d.pop("jobs_completed", UNSET)

        jobs_canceled = d.pop("jobs_canceled", UNSET)

        jobs_failed = d.pop("jobs_failed", UNSET)

        jobs_pending = d.pop("jobs_pending", UNSET)

        jobs_running = d.pop("jobs_running", UNSET)

        _job_states_ts = d.pop("job_states_ts", UNSET)
        job_states_ts: SlurmV0041GetDiagResponse200StatisticsJobStatesTs | Unset
        if isinstance(_job_states_ts, Unset):
            job_states_ts = UNSET
        else:
            job_states_ts = SlurmV0041GetDiagResponse200StatisticsJobStatesTs.from_dict(_job_states_ts)

        bf_backfilled_jobs = d.pop("bf_backfilled_jobs", UNSET)

        bf_last_backfilled_jobs = d.pop("bf_last_backfilled_jobs", UNSET)

        bf_backfilled_het_jobs = d.pop("bf_backfilled_het_jobs", UNSET)

        bf_cycle_counter = d.pop("bf_cycle_counter", UNSET)

        bf_cycle_mean = d.pop("bf_cycle_mean", UNSET)

        bf_depth_mean = d.pop("bf_depth_mean", UNSET)

        bf_depth_mean_try = d.pop("bf_depth_mean_try", UNSET)

        bf_cycle_sum = d.pop("bf_cycle_sum", UNSET)

        bf_cycle_last = d.pop("bf_cycle_last", UNSET)

        bf_cycle_max = d.pop("bf_cycle_max", UNSET)

        _bf_exit = d.pop("bf_exit", UNSET)
        bf_exit: SlurmV0041GetDiagResponse200StatisticsBfExit | Unset
        if isinstance(_bf_exit, Unset):
            bf_exit = UNSET
        else:
            bf_exit = SlurmV0041GetDiagResponse200StatisticsBfExit.from_dict(_bf_exit)

        bf_last_depth = d.pop("bf_last_depth", UNSET)

        bf_last_depth_try = d.pop("bf_last_depth_try", UNSET)

        bf_depth_sum = d.pop("bf_depth_sum", UNSET)

        bf_depth_try_sum = d.pop("bf_depth_try_sum", UNSET)

        bf_queue_len = d.pop("bf_queue_len", UNSET)

        bf_queue_len_mean = d.pop("bf_queue_len_mean", UNSET)

        bf_queue_len_sum = d.pop("bf_queue_len_sum", UNSET)

        bf_table_size = d.pop("bf_table_size", UNSET)

        bf_table_size_sum = d.pop("bf_table_size_sum", UNSET)

        bf_table_size_mean = d.pop("bf_table_size_mean", UNSET)

        _bf_when_last_cycle = d.pop("bf_when_last_cycle", UNSET)
        bf_when_last_cycle: SlurmV0041GetDiagResponse200StatisticsBfWhenLastCycle | Unset
        if isinstance(_bf_when_last_cycle, Unset):
            bf_when_last_cycle = UNSET
        else:
            bf_when_last_cycle = SlurmV0041GetDiagResponse200StatisticsBfWhenLastCycle.from_dict(_bf_when_last_cycle)

        bf_active = d.pop("bf_active", UNSET)

        _rpcs_by_message_type = d.pop("rpcs_by_message_type", UNSET)
        rpcs_by_message_type: list[SlurmV0041GetDiagResponse200StatisticsRpcsByMessageTypeItem] | Unset = UNSET
        if _rpcs_by_message_type is not UNSET:
            rpcs_by_message_type = []
            for rpcs_by_message_type_item_data in _rpcs_by_message_type:
                rpcs_by_message_type_item = SlurmV0041GetDiagResponse200StatisticsRpcsByMessageTypeItem.from_dict(
                    rpcs_by_message_type_item_data
                )

                rpcs_by_message_type.append(rpcs_by_message_type_item)

        _rpcs_by_user = d.pop("rpcs_by_user", UNSET)
        rpcs_by_user: list[SlurmV0041GetDiagResponse200StatisticsRpcsByUserItem] | Unset = UNSET
        if _rpcs_by_user is not UNSET:
            rpcs_by_user = []
            for rpcs_by_user_item_data in _rpcs_by_user:
                rpcs_by_user_item = SlurmV0041GetDiagResponse200StatisticsRpcsByUserItem.from_dict(
                    rpcs_by_user_item_data
                )

                rpcs_by_user.append(rpcs_by_user_item)

        _pending_rpcs = d.pop("pending_rpcs", UNSET)
        pending_rpcs: list[SlurmV0041GetDiagResponse200StatisticsPendingRpcsItem] | Unset = UNSET
        if _pending_rpcs is not UNSET:
            pending_rpcs = []
            for pending_rpcs_item_data in _pending_rpcs:
                pending_rpcs_item = SlurmV0041GetDiagResponse200StatisticsPendingRpcsItem.from_dict(
                    pending_rpcs_item_data
                )

                pending_rpcs.append(pending_rpcs_item)

        _pending_rpcs_by_hostlist = d.pop("pending_rpcs_by_hostlist", UNSET)
        pending_rpcs_by_hostlist: list[SlurmV0041GetDiagResponse200StatisticsPendingRpcsByHostlistItem] | Unset = UNSET
        if _pending_rpcs_by_hostlist is not UNSET:
            pending_rpcs_by_hostlist = []
            for pending_rpcs_by_hostlist_item_data in _pending_rpcs_by_hostlist:
                pending_rpcs_by_hostlist_item = (
                    SlurmV0041GetDiagResponse200StatisticsPendingRpcsByHostlistItem.from_dict(
                        pending_rpcs_by_hostlist_item_data
                    )
                )

                pending_rpcs_by_hostlist.append(pending_rpcs_by_hostlist_item)

        slurm_v0041_get_diag_response_200_statistics = cls(
            parts_packed=parts_packed,
            req_time=req_time,
            req_time_start=req_time_start,
            server_thread_count=server_thread_count,
            agent_queue_size=agent_queue_size,
            agent_count=agent_count,
            agent_thread_count=agent_thread_count,
            dbd_agent_queue_size=dbd_agent_queue_size,
            gettimeofday_latency=gettimeofday_latency,
            schedule_cycle_max=schedule_cycle_max,
            schedule_cycle_last=schedule_cycle_last,
            schedule_cycle_sum=schedule_cycle_sum,
            schedule_cycle_total=schedule_cycle_total,
            schedule_cycle_mean=schedule_cycle_mean,
            schedule_cycle_mean_depth=schedule_cycle_mean_depth,
            schedule_cycle_per_minute=schedule_cycle_per_minute,
            schedule_cycle_depth=schedule_cycle_depth,
            schedule_exit=schedule_exit,
            schedule_queue_length=schedule_queue_length,
            jobs_submitted=jobs_submitted,
            jobs_started=jobs_started,
            jobs_completed=jobs_completed,
            jobs_canceled=jobs_canceled,
            jobs_failed=jobs_failed,
            jobs_pending=jobs_pending,
            jobs_running=jobs_running,
            job_states_ts=job_states_ts,
            bf_backfilled_jobs=bf_backfilled_jobs,
            bf_last_backfilled_jobs=bf_last_backfilled_jobs,
            bf_backfilled_het_jobs=bf_backfilled_het_jobs,
            bf_cycle_counter=bf_cycle_counter,
            bf_cycle_mean=bf_cycle_mean,
            bf_depth_mean=bf_depth_mean,
            bf_depth_mean_try=bf_depth_mean_try,
            bf_cycle_sum=bf_cycle_sum,
            bf_cycle_last=bf_cycle_last,
            bf_cycle_max=bf_cycle_max,
            bf_exit=bf_exit,
            bf_last_depth=bf_last_depth,
            bf_last_depth_try=bf_last_depth_try,
            bf_depth_sum=bf_depth_sum,
            bf_depth_try_sum=bf_depth_try_sum,
            bf_queue_len=bf_queue_len,
            bf_queue_len_mean=bf_queue_len_mean,
            bf_queue_len_sum=bf_queue_len_sum,
            bf_table_size=bf_table_size,
            bf_table_size_sum=bf_table_size_sum,
            bf_table_size_mean=bf_table_size_mean,
            bf_when_last_cycle=bf_when_last_cycle,
            bf_active=bf_active,
            rpcs_by_message_type=rpcs_by_message_type,
            rpcs_by_user=rpcs_by_user,
            pending_rpcs=pending_rpcs,
            pending_rpcs_by_hostlist=pending_rpcs_by_hostlist,
        )

        slurm_v0041_get_diag_response_200_statistics.additional_properties = d
        return slurm_v0041_get_diag_response_200_statistics

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
