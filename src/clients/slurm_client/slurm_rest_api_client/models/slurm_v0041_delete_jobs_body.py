from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.slurm_v0041_delete_jobs_body_flags_item import SlurmV0041DeleteJobsBodyFlagsItem
from ..models.slurm_v0041_delete_jobs_body_job_state_item import SlurmV0041DeleteJobsBodyJobStateItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="SlurmV0041DeleteJobsBody")


@_attrs_define
class SlurmV0041DeleteJobsBody:
    """
    Attributes:
        account (str | Unset): Filter jobs to a specific account
        flags (list[SlurmV0041DeleteJobsBodyFlagsItem] | Unset): Filter jobs according to flags
        job_name (str | Unset): Filter jobs to a specific name
        jobs (list[str] | Unset): List of jobs to signal
        partition (str | Unset): Filter jobs to a specific partition
        qos (str | Unset): Filter jobs to a specific QOS
        reservation (str | Unset): Filter jobs to a specific reservation
        signal (str | Unset): Signal to send to jobs
        job_state (list[SlurmV0041DeleteJobsBodyJobStateItem] | Unset): Filter jobs to a specific state
        user_id (str | Unset): Filter jobs to a specific numeric user id
        user_name (str | Unset): Filter jobs to a specific user name
        wckey (str | Unset): Filter jobs to a specific wckey
        nodes (list[str] | Unset): Filter jobs to a set of nodes
    """

    account: str | Unset = UNSET
    flags: list[SlurmV0041DeleteJobsBodyFlagsItem] | Unset = UNSET
    job_name: str | Unset = UNSET
    jobs: list[str] | Unset = UNSET
    partition: str | Unset = UNSET
    qos: str | Unset = UNSET
    reservation: str | Unset = UNSET
    signal: str | Unset = UNSET
    job_state: list[SlurmV0041DeleteJobsBodyJobStateItem] | Unset = UNSET
    user_id: str | Unset = UNSET
    user_name: str | Unset = UNSET
    wckey: str | Unset = UNSET
    nodes: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account = self.account

        flags: list[str] | Unset = UNSET
        if not isinstance(self.flags, Unset):
            flags = []
            for flags_item_data in self.flags:
                flags_item = flags_item_data.value
                flags.append(flags_item)

        job_name = self.job_name

        jobs: list[str] | Unset = UNSET
        if not isinstance(self.jobs, Unset):
            jobs = self.jobs

        partition = self.partition

        qos = self.qos

        reservation = self.reservation

        signal = self.signal

        job_state: list[str] | Unset = UNSET
        if not isinstance(self.job_state, Unset):
            job_state = []
            for job_state_item_data in self.job_state:
                job_state_item = job_state_item_data.value
                job_state.append(job_state_item)

        user_id = self.user_id

        user_name = self.user_name

        wckey = self.wckey

        nodes: list[str] | Unset = UNSET
        if not isinstance(self.nodes, Unset):
            nodes = self.nodes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account is not UNSET:
            field_dict["account"] = account
        if flags is not UNSET:
            field_dict["flags"] = flags
        if job_name is not UNSET:
            field_dict["job_name"] = job_name
        if jobs is not UNSET:
            field_dict["jobs"] = jobs
        if partition is not UNSET:
            field_dict["partition"] = partition
        if qos is not UNSET:
            field_dict["qos"] = qos
        if reservation is not UNSET:
            field_dict["reservation"] = reservation
        if signal is not UNSET:
            field_dict["signal"] = signal
        if job_state is not UNSET:
            field_dict["job_state"] = job_state
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if user_name is not UNSET:
            field_dict["user_name"] = user_name
        if wckey is not UNSET:
            field_dict["wckey"] = wckey
        if nodes is not UNSET:
            field_dict["nodes"] = nodes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account = d.pop("account", UNSET)

        _flags = d.pop("flags", UNSET)
        flags: list[SlurmV0041DeleteJobsBodyFlagsItem] | Unset = UNSET
        if _flags is not UNSET:
            flags = []
            for flags_item_data in _flags:
                flags_item = SlurmV0041DeleteJobsBodyFlagsItem(flags_item_data)

                flags.append(flags_item)

        job_name = d.pop("job_name", UNSET)

        jobs = cast(list[str], d.pop("jobs", UNSET))

        partition = d.pop("partition", UNSET)

        qos = d.pop("qos", UNSET)

        reservation = d.pop("reservation", UNSET)

        signal = d.pop("signal", UNSET)

        _job_state = d.pop("job_state", UNSET)
        job_state: list[SlurmV0041DeleteJobsBodyJobStateItem] | Unset = UNSET
        if _job_state is not UNSET:
            job_state = []
            for job_state_item_data in _job_state:
                job_state_item = SlurmV0041DeleteJobsBodyJobStateItem(job_state_item_data)

                job_state.append(job_state_item)

        user_id = d.pop("user_id", UNSET)

        user_name = d.pop("user_name", UNSET)

        wckey = d.pop("wckey", UNSET)

        nodes = cast(list[str], d.pop("nodes", UNSET))

        slurm_v0041_delete_jobs_body = cls(
            account=account,
            flags=flags,
            job_name=job_name,
            jobs=jobs,
            partition=partition,
            qos=qos,
            reservation=reservation,
            signal=signal,
            job_state=job_state,
            user_id=user_id,
            user_name=user_name,
            wckey=wckey,
            nodes=nodes,
        )

        slurm_v0041_delete_jobs_body.additional_properties = d
        return slurm_v0041_delete_jobs_body

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
