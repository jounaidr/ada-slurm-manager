from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v0038_reservation_purge_completed import V0038ReservationPurgeCompleted


T = TypeVar("T", bound="V0038Reservation")


@_attrs_define
class V0038Reservation:
    """
    Attributes:
        accounts (str | Unset): Allowed accounts
        burst_buffer (str | Unset): Reserved burst buffer
        core_count (int | Unset): Number of reserved cores
        core_spec_cnt (int | Unset): Number of reserved specialized cores
        end_time (int | Unset): End time of the reservation
        features (str | Unset): List of features
        flags (list[str] | Unset): Reservation options
        groups (str | Unset): List of groups permitted to use the reserved nodes
        licenses (str | Unset): List of licenses
        max_start_delay (int | Unset): Maximum delay in which jobs outside of the reservation will be permitted to
            overlap once any jobs are queued for the reservation
        name (str | Unset): Reservationn name
        node_count (int | Unset): Count of nodes reserved
        node_list (str | Unset): List of reserved nodes
        partition (str | Unset): Partition
        purge_completed (V0038ReservationPurgeCompleted | Unset): If PURGE_COMP flag is set the amount of seconds this
            reservation will sit idle until it is revoked
        start_time (int | Unset): Start time of reservation
        watts (int | Unset): amount of power to reserve in watts
        tres (str | Unset): List of TRES
        users (str | Unset): List of users
    """

    accounts: str | Unset = UNSET
    burst_buffer: str | Unset = UNSET
    core_count: int | Unset = UNSET
    core_spec_cnt: int | Unset = UNSET
    end_time: int | Unset = UNSET
    features: str | Unset = UNSET
    flags: list[str] | Unset = UNSET
    groups: str | Unset = UNSET
    licenses: str | Unset = UNSET
    max_start_delay: int | Unset = UNSET
    name: str | Unset = UNSET
    node_count: int | Unset = UNSET
    node_list: str | Unset = UNSET
    partition: str | Unset = UNSET
    purge_completed: V0038ReservationPurgeCompleted | Unset = UNSET
    start_time: int | Unset = UNSET
    watts: int | Unset = UNSET
    tres: str | Unset = UNSET
    users: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        accounts = self.accounts

        burst_buffer = self.burst_buffer

        core_count = self.core_count

        core_spec_cnt = self.core_spec_cnt

        end_time = self.end_time

        features = self.features

        flags: list[str] | Unset = UNSET
        if not isinstance(self.flags, Unset):
            flags = self.flags

        groups = self.groups

        licenses = self.licenses

        max_start_delay = self.max_start_delay

        name = self.name

        node_count = self.node_count

        node_list = self.node_list

        partition = self.partition

        purge_completed: dict[str, Any] | Unset = UNSET
        if not isinstance(self.purge_completed, Unset):
            purge_completed = self.purge_completed.to_dict()

        start_time = self.start_time

        watts = self.watts

        tres = self.tres

        users = self.users

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if accounts is not UNSET:
            field_dict["accounts"] = accounts
        if burst_buffer is not UNSET:
            field_dict["burst_buffer"] = burst_buffer
        if core_count is not UNSET:
            field_dict["core_count"] = core_count
        if core_spec_cnt is not UNSET:
            field_dict["core_spec_cnt"] = core_spec_cnt
        if end_time is not UNSET:
            field_dict["end_time"] = end_time
        if features is not UNSET:
            field_dict["features"] = features
        if flags is not UNSET:
            field_dict["flags"] = flags
        if groups is not UNSET:
            field_dict["groups"] = groups
        if licenses is not UNSET:
            field_dict["licenses"] = licenses
        if max_start_delay is not UNSET:
            field_dict["max_start_delay"] = max_start_delay
        if name is not UNSET:
            field_dict["name"] = name
        if node_count is not UNSET:
            field_dict["node_count"] = node_count
        if node_list is not UNSET:
            field_dict["node_list"] = node_list
        if partition is not UNSET:
            field_dict["partition"] = partition
        if purge_completed is not UNSET:
            field_dict["purge_completed"] = purge_completed
        if start_time is not UNSET:
            field_dict["start_time"] = start_time
        if watts is not UNSET:
            field_dict["watts"] = watts
        if tres is not UNSET:
            field_dict["tres"] = tres
        if users is not UNSET:
            field_dict["users"] = users

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v0038_reservation_purge_completed import V0038ReservationPurgeCompleted

        d = dict(src_dict)
        accounts = d.pop("accounts", UNSET)

        burst_buffer = d.pop("burst_buffer", UNSET)

        core_count = d.pop("core_count", UNSET)

        core_spec_cnt = d.pop("core_spec_cnt", UNSET)

        end_time = d.pop("end_time", UNSET)

        features = d.pop("features", UNSET)

        flags = cast(list[str], d.pop("flags", UNSET))

        groups = d.pop("groups", UNSET)

        licenses = d.pop("licenses", UNSET)

        max_start_delay = d.pop("max_start_delay", UNSET)

        name = d.pop("name", UNSET)

        node_count = d.pop("node_count", UNSET)

        node_list = d.pop("node_list", UNSET)

        partition = d.pop("partition", UNSET)

        _purge_completed = d.pop("purge_completed", UNSET)
        purge_completed: V0038ReservationPurgeCompleted | Unset
        if isinstance(_purge_completed, Unset):
            purge_completed = UNSET
        else:
            purge_completed = V0038ReservationPurgeCompleted.from_dict(_purge_completed)

        start_time = d.pop("start_time", UNSET)

        watts = d.pop("watts", UNSET)

        tres = d.pop("tres", UNSET)

        users = d.pop("users", UNSET)

        v0038_reservation = cls(
            accounts=accounts,
            burst_buffer=burst_buffer,
            core_count=core_count,
            core_spec_cnt=core_spec_cnt,
            end_time=end_time,
            features=features,
            flags=flags,
            groups=groups,
            licenses=licenses,
            max_start_delay=max_start_delay,
            name=name,
            node_count=node_count,
            node_list=node_list,
            partition=partition,
            purge_completed=purge_completed,
            start_time=start_time,
            watts=watts,
            tres=tres,
            users=users,
        )

        v0038_reservation.additional_properties = d
        return v0038_reservation

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
