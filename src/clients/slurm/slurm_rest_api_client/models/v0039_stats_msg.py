from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v0039_stats_msg_rpcs_by_type_item import V0039StatsMsgRpcsByTypeItem
    from ..models.v0039_stats_msg_rpcs_by_user_item import V0039StatsMsgRpcsByUserItem


T = TypeVar("T", bound="V0039StatsMsg")


@_attrs_define
class V0039StatsMsg:
    """
    Attributes:
        parts_packed (int | Unset):
        req_time (int | Unset):
        req_time_start (int | Unset):
        server_thread_count (int | Unset):
        agent_queue_size (int | Unset):
        agent_count (int | Unset):
        agent_thread_count (int | Unset):
        dbd_agent_queue_size (int | Unset):
        gettimeofday_latency (int | Unset):
        schedule_cycle_max (int | Unset):
        schedule_cycle_last (int | Unset):
        schedule_cycle_total (int | Unset):
        schedule_cycle_mean (int | Unset):
        schedule_cycle_mean_depth (int | Unset):
        schedule_cycle_per_minute (int | Unset):
        schedule_queue_length (int | Unset):
        jobs_submitted (int | Unset):
        jobs_started (int | Unset):
        jobs_completed (int | Unset):
        jobs_canceled (int | Unset):
        jobs_failed (int | Unset):
        jobs_pending (int | Unset):
        jobs_running (int | Unset):
        job_states_ts (int | Unset):
        bf_backfilled_jobs (int | Unset):
        bf_last_backfilled_jobs (int | Unset):
        bf_backfilled_het_jobs (int | Unset):
        bf_cycle_counter (int | Unset):
        bf_cycle_mean (int | Unset):
        bf_depth_mean (int | Unset):
        bf_depth_mean_try (int | Unset):
        bf_cycle_sum (int | Unset):
        bf_cycle_last (int | Unset):
        bf_last_depth (int | Unset):
        bf_last_depth_try (int | Unset):
        bf_depth_sum (int | Unset):
        bf_depth_try_sum (int | Unset):
        bf_queue_len (int | Unset):
        bf_queue_len_mean (int | Unset):
        bf_queue_len_sum (int | Unset):
        bf_table_size (int | Unset):
        bf_table_size_mean (int | Unset):
        bf_when_last_cycle (int | Unset):
        bf_active (bool | Unset):
        rpcs_by_message_type (list[V0039StatsMsgRpcsByTypeItem] | Unset): RPCs by message type
        rpcs_by_user (list[V0039StatsMsgRpcsByUserItem] | Unset): RPCs by user
    """

    parts_packed: int | Unset = UNSET
    req_time: int | Unset = UNSET
    req_time_start: int | Unset = UNSET
    server_thread_count: int | Unset = UNSET
    agent_queue_size: int | Unset = UNSET
    agent_count: int | Unset = UNSET
    agent_thread_count: int | Unset = UNSET
    dbd_agent_queue_size: int | Unset = UNSET
    gettimeofday_latency: int | Unset = UNSET
    schedule_cycle_max: int | Unset = UNSET
    schedule_cycle_last: int | Unset = UNSET
    schedule_cycle_total: int | Unset = UNSET
    schedule_cycle_mean: int | Unset = UNSET
    schedule_cycle_mean_depth: int | Unset = UNSET
    schedule_cycle_per_minute: int | Unset = UNSET
    schedule_queue_length: int | Unset = UNSET
    jobs_submitted: int | Unset = UNSET
    jobs_started: int | Unset = UNSET
    jobs_completed: int | Unset = UNSET
    jobs_canceled: int | Unset = UNSET
    jobs_failed: int | Unset = UNSET
    jobs_pending: int | Unset = UNSET
    jobs_running: int | Unset = UNSET
    job_states_ts: int | Unset = UNSET
    bf_backfilled_jobs: int | Unset = UNSET
    bf_last_backfilled_jobs: int | Unset = UNSET
    bf_backfilled_het_jobs: int | Unset = UNSET
    bf_cycle_counter: int | Unset = UNSET
    bf_cycle_mean: int | Unset = UNSET
    bf_depth_mean: int | Unset = UNSET
    bf_depth_mean_try: int | Unset = UNSET
    bf_cycle_sum: int | Unset = UNSET
    bf_cycle_last: int | Unset = UNSET
    bf_last_depth: int | Unset = UNSET
    bf_last_depth_try: int | Unset = UNSET
    bf_depth_sum: int | Unset = UNSET
    bf_depth_try_sum: int | Unset = UNSET
    bf_queue_len: int | Unset = UNSET
    bf_queue_len_mean: int | Unset = UNSET
    bf_queue_len_sum: int | Unset = UNSET
    bf_table_size: int | Unset = UNSET
    bf_table_size_mean: int | Unset = UNSET
    bf_when_last_cycle: int | Unset = UNSET
    bf_active: bool | Unset = UNSET
    rpcs_by_message_type: list[V0039StatsMsgRpcsByTypeItem] | Unset = UNSET
    rpcs_by_user: list[V0039StatsMsgRpcsByUserItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        parts_packed = self.parts_packed

        req_time = self.req_time

        req_time_start = self.req_time_start

        server_thread_count = self.server_thread_count

        agent_queue_size = self.agent_queue_size

        agent_count = self.agent_count

        agent_thread_count = self.agent_thread_count

        dbd_agent_queue_size = self.dbd_agent_queue_size

        gettimeofday_latency = self.gettimeofday_latency

        schedule_cycle_max = self.schedule_cycle_max

        schedule_cycle_last = self.schedule_cycle_last

        schedule_cycle_total = self.schedule_cycle_total

        schedule_cycle_mean = self.schedule_cycle_mean

        schedule_cycle_mean_depth = self.schedule_cycle_mean_depth

        schedule_cycle_per_minute = self.schedule_cycle_per_minute

        schedule_queue_length = self.schedule_queue_length

        jobs_submitted = self.jobs_submitted

        jobs_started = self.jobs_started

        jobs_completed = self.jobs_completed

        jobs_canceled = self.jobs_canceled

        jobs_failed = self.jobs_failed

        jobs_pending = self.jobs_pending

        jobs_running = self.jobs_running

        job_states_ts = self.job_states_ts

        bf_backfilled_jobs = self.bf_backfilled_jobs

        bf_last_backfilled_jobs = self.bf_last_backfilled_jobs

        bf_backfilled_het_jobs = self.bf_backfilled_het_jobs

        bf_cycle_counter = self.bf_cycle_counter

        bf_cycle_mean = self.bf_cycle_mean

        bf_depth_mean = self.bf_depth_mean

        bf_depth_mean_try = self.bf_depth_mean_try

        bf_cycle_sum = self.bf_cycle_sum

        bf_cycle_last = self.bf_cycle_last

        bf_last_depth = self.bf_last_depth

        bf_last_depth_try = self.bf_last_depth_try

        bf_depth_sum = self.bf_depth_sum

        bf_depth_try_sum = self.bf_depth_try_sum

        bf_queue_len = self.bf_queue_len

        bf_queue_len_mean = self.bf_queue_len_mean

        bf_queue_len_sum = self.bf_queue_len_sum

        bf_table_size = self.bf_table_size

        bf_table_size_mean = self.bf_table_size_mean

        bf_when_last_cycle = self.bf_when_last_cycle

        bf_active = self.bf_active

        rpcs_by_message_type: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.rpcs_by_message_type, Unset):
            rpcs_by_message_type = []
            for componentsschemasv0_0_39_stats_msg_rpcs_by_type_item_data in self.rpcs_by_message_type:
                componentsschemasv0_0_39_stats_msg_rpcs_by_type_item = (
                    componentsschemasv0_0_39_stats_msg_rpcs_by_type_item_data.to_dict()
                )
                rpcs_by_message_type.append(componentsschemasv0_0_39_stats_msg_rpcs_by_type_item)

        rpcs_by_user: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.rpcs_by_user, Unset):
            rpcs_by_user = []
            for componentsschemasv0_0_39_stats_msg_rpcs_by_user_item_data in self.rpcs_by_user:
                componentsschemasv0_0_39_stats_msg_rpcs_by_user_item = (
                    componentsschemasv0_0_39_stats_msg_rpcs_by_user_item_data.to_dict()
                )
                rpcs_by_user.append(componentsschemasv0_0_39_stats_msg_rpcs_by_user_item)

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
        if schedule_cycle_total is not UNSET:
            field_dict["schedule_cycle_total"] = schedule_cycle_total
        if schedule_cycle_mean is not UNSET:
            field_dict["schedule_cycle_mean"] = schedule_cycle_mean
        if schedule_cycle_mean_depth is not UNSET:
            field_dict["schedule_cycle_mean_depth"] = schedule_cycle_mean_depth
        if schedule_cycle_per_minute is not UNSET:
            field_dict["schedule_cycle_per_minute"] = schedule_cycle_per_minute
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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v0039_stats_msg_rpcs_by_type_item import V0039StatsMsgRpcsByTypeItem
        from ..models.v0039_stats_msg_rpcs_by_user_item import V0039StatsMsgRpcsByUserItem

        d = dict(src_dict)
        parts_packed = d.pop("parts_packed", UNSET)

        req_time = d.pop("req_time", UNSET)

        req_time_start = d.pop("req_time_start", UNSET)

        server_thread_count = d.pop("server_thread_count", UNSET)

        agent_queue_size = d.pop("agent_queue_size", UNSET)

        agent_count = d.pop("agent_count", UNSET)

        agent_thread_count = d.pop("agent_thread_count", UNSET)

        dbd_agent_queue_size = d.pop("dbd_agent_queue_size", UNSET)

        gettimeofday_latency = d.pop("gettimeofday_latency", UNSET)

        schedule_cycle_max = d.pop("schedule_cycle_max", UNSET)

        schedule_cycle_last = d.pop("schedule_cycle_last", UNSET)

        schedule_cycle_total = d.pop("schedule_cycle_total", UNSET)

        schedule_cycle_mean = d.pop("schedule_cycle_mean", UNSET)

        schedule_cycle_mean_depth = d.pop("schedule_cycle_mean_depth", UNSET)

        schedule_cycle_per_minute = d.pop("schedule_cycle_per_minute", UNSET)

        schedule_queue_length = d.pop("schedule_queue_length", UNSET)

        jobs_submitted = d.pop("jobs_submitted", UNSET)

        jobs_started = d.pop("jobs_started", UNSET)

        jobs_completed = d.pop("jobs_completed", UNSET)

        jobs_canceled = d.pop("jobs_canceled", UNSET)

        jobs_failed = d.pop("jobs_failed", UNSET)

        jobs_pending = d.pop("jobs_pending", UNSET)

        jobs_running = d.pop("jobs_running", UNSET)

        job_states_ts = d.pop("job_states_ts", UNSET)

        bf_backfilled_jobs = d.pop("bf_backfilled_jobs", UNSET)

        bf_last_backfilled_jobs = d.pop("bf_last_backfilled_jobs", UNSET)

        bf_backfilled_het_jobs = d.pop("bf_backfilled_het_jobs", UNSET)

        bf_cycle_counter = d.pop("bf_cycle_counter", UNSET)

        bf_cycle_mean = d.pop("bf_cycle_mean", UNSET)

        bf_depth_mean = d.pop("bf_depth_mean", UNSET)

        bf_depth_mean_try = d.pop("bf_depth_mean_try", UNSET)

        bf_cycle_sum = d.pop("bf_cycle_sum", UNSET)

        bf_cycle_last = d.pop("bf_cycle_last", UNSET)

        bf_last_depth = d.pop("bf_last_depth", UNSET)

        bf_last_depth_try = d.pop("bf_last_depth_try", UNSET)

        bf_depth_sum = d.pop("bf_depth_sum", UNSET)

        bf_depth_try_sum = d.pop("bf_depth_try_sum", UNSET)

        bf_queue_len = d.pop("bf_queue_len", UNSET)

        bf_queue_len_mean = d.pop("bf_queue_len_mean", UNSET)

        bf_queue_len_sum = d.pop("bf_queue_len_sum", UNSET)

        bf_table_size = d.pop("bf_table_size", UNSET)

        bf_table_size_mean = d.pop("bf_table_size_mean", UNSET)

        bf_when_last_cycle = d.pop("bf_when_last_cycle", UNSET)

        bf_active = d.pop("bf_active", UNSET)

        _rpcs_by_message_type = d.pop("rpcs_by_message_type", UNSET)
        rpcs_by_message_type: list[V0039StatsMsgRpcsByTypeItem] | Unset = UNSET
        if _rpcs_by_message_type is not UNSET:
            rpcs_by_message_type = []
            for componentsschemasv0_0_39_stats_msg_rpcs_by_type_item_data in _rpcs_by_message_type:
                componentsschemasv0_0_39_stats_msg_rpcs_by_type_item = V0039StatsMsgRpcsByTypeItem.from_dict(
                    componentsschemasv0_0_39_stats_msg_rpcs_by_type_item_data
                )

                rpcs_by_message_type.append(componentsschemasv0_0_39_stats_msg_rpcs_by_type_item)

        _rpcs_by_user = d.pop("rpcs_by_user", UNSET)
        rpcs_by_user: list[V0039StatsMsgRpcsByUserItem] | Unset = UNSET
        if _rpcs_by_user is not UNSET:
            rpcs_by_user = []
            for componentsschemasv0_0_39_stats_msg_rpcs_by_user_item_data in _rpcs_by_user:
                componentsschemasv0_0_39_stats_msg_rpcs_by_user_item = V0039StatsMsgRpcsByUserItem.from_dict(
                    componentsschemasv0_0_39_stats_msg_rpcs_by_user_item_data
                )

                rpcs_by_user.append(componentsschemasv0_0_39_stats_msg_rpcs_by_user_item)

        v0039_stats_msg = cls(
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
            schedule_cycle_total=schedule_cycle_total,
            schedule_cycle_mean=schedule_cycle_mean,
            schedule_cycle_mean_depth=schedule_cycle_mean_depth,
            schedule_cycle_per_minute=schedule_cycle_per_minute,
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
            bf_last_depth=bf_last_depth,
            bf_last_depth_try=bf_last_depth_try,
            bf_depth_sum=bf_depth_sum,
            bf_depth_try_sum=bf_depth_try_sum,
            bf_queue_len=bf_queue_len,
            bf_queue_len_mean=bf_queue_len_mean,
            bf_queue_len_sum=bf_queue_len_sum,
            bf_table_size=bf_table_size,
            bf_table_size_mean=bf_table_size_mean,
            bf_when_last_cycle=bf_when_last_cycle,
            bf_active=bf_active,
            rpcs_by_message_type=rpcs_by_message_type,
            rpcs_by_user=rpcs_by_user,
        )

        v0039_stats_msg.additional_properties = d
        return v0039_stats_msg

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
