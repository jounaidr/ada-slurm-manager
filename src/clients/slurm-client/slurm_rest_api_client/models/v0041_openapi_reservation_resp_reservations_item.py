from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.v0041_openapi_reservation_resp_reservations_item_flags_item import (
    V0041OpenapiReservationRespReservationsItemFlagsItem,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v0041_openapi_reservation_resp_reservations_item_core_specializations_item import (
        V0041OpenapiReservationRespReservationsItemCoreSpecializationsItem,
    )
    from ..models.v0041_openapi_reservation_resp_reservations_item_end_time import (
        V0041OpenapiReservationRespReservationsItemEndTime,
    )
    from ..models.v0041_openapi_reservation_resp_reservations_item_purge_completed import (
        V0041OpenapiReservationRespReservationsItemPurgeCompleted,
    )
    from ..models.v0041_openapi_reservation_resp_reservations_item_start_time import (
        V0041OpenapiReservationRespReservationsItemStartTime,
    )
    from ..models.v0041_openapi_reservation_resp_reservations_item_watts import (
        V0041OpenapiReservationRespReservationsItemWatts,
    )


T = TypeVar("T", bound="V0041OpenapiReservationRespReservationsItem")


@_attrs_define
class V0041OpenapiReservationRespReservationsItem:
    """
    Attributes:
        accounts (str | Unset): Comma separated list of permitted accounts
        burst_buffer (str | Unset): BurstBuffer
        core_count (int | Unset): CoreCnt
        core_specializations (list[V0041OpenapiReservationRespReservationsItemCoreSpecializationsItem] | Unset):
            Reserved cores specification
        end_time (V0041OpenapiReservationRespReservationsItemEndTime | Unset): EndTime (UNIX timestamp)
        features (str | Unset): Features
        flags (list[V0041OpenapiReservationRespReservationsItemFlagsItem] | Unset): Flags associated with the
            reservation
        groups (str | Unset): Groups
        licenses (str | Unset): Licenses
        max_start_delay (int | Unset): MaxStartDelay in seconds
        name (str | Unset): ReservationName
        node_count (int | Unset): NodeCnt
        node_list (str | Unset): Nodes
        partition (str | Unset): PartitionName
        purge_completed (V0041OpenapiReservationRespReservationsItemPurgeCompleted | Unset):
        start_time (V0041OpenapiReservationRespReservationsItemStartTime | Unset): StartTime (UNIX timestamp)
        watts (V0041OpenapiReservationRespReservationsItemWatts | Unset): 32 bit integer number with flags
        tres (str | Unset): Comma separated list of required TRES
        users (str | Unset): Comma separated list of permitted users
    """

    accounts: str | Unset = UNSET
    burst_buffer: str | Unset = UNSET
    core_count: int | Unset = UNSET
    core_specializations: list[V0041OpenapiReservationRespReservationsItemCoreSpecializationsItem] | Unset = UNSET
    end_time: V0041OpenapiReservationRespReservationsItemEndTime | Unset = UNSET
    features: str | Unset = UNSET
    flags: list[V0041OpenapiReservationRespReservationsItemFlagsItem] | Unset = UNSET
    groups: str | Unset = UNSET
    licenses: str | Unset = UNSET
    max_start_delay: int | Unset = UNSET
    name: str | Unset = UNSET
    node_count: int | Unset = UNSET
    node_list: str | Unset = UNSET
    partition: str | Unset = UNSET
    purge_completed: V0041OpenapiReservationRespReservationsItemPurgeCompleted | Unset = UNSET
    start_time: V0041OpenapiReservationRespReservationsItemStartTime | Unset = UNSET
    watts: V0041OpenapiReservationRespReservationsItemWatts | Unset = UNSET
    tres: str | Unset = UNSET
    users: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        accounts = self.accounts

        burst_buffer = self.burst_buffer

        core_count = self.core_count

        core_specializations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.core_specializations, Unset):
            core_specializations = []
            for core_specializations_item_data in self.core_specializations:
                core_specializations_item = core_specializations_item_data.to_dict()
                core_specializations.append(core_specializations_item)

        end_time: dict[str, Any] | Unset = UNSET
        if not isinstance(self.end_time, Unset):
            end_time = self.end_time.to_dict()

        features = self.features

        flags: list[str] | Unset = UNSET
        if not isinstance(self.flags, Unset):
            flags = []
            for flags_item_data in self.flags:
                flags_item = flags_item_data.value
                flags.append(flags_item)

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

        start_time: dict[str, Any] | Unset = UNSET
        if not isinstance(self.start_time, Unset):
            start_time = self.start_time.to_dict()

        watts: dict[str, Any] | Unset = UNSET
        if not isinstance(self.watts, Unset):
            watts = self.watts.to_dict()

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
        if core_specializations is not UNSET:
            field_dict["core_specializations"] = core_specializations
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
        from ..models.v0041_openapi_reservation_resp_reservations_item_core_specializations_item import (
            V0041OpenapiReservationRespReservationsItemCoreSpecializationsItem,
        )
        from ..models.v0041_openapi_reservation_resp_reservations_item_end_time import (
            V0041OpenapiReservationRespReservationsItemEndTime,
        )
        from ..models.v0041_openapi_reservation_resp_reservations_item_purge_completed import (
            V0041OpenapiReservationRespReservationsItemPurgeCompleted,
        )
        from ..models.v0041_openapi_reservation_resp_reservations_item_start_time import (
            V0041OpenapiReservationRespReservationsItemStartTime,
        )
        from ..models.v0041_openapi_reservation_resp_reservations_item_watts import (
            V0041OpenapiReservationRespReservationsItemWatts,
        )

        d = dict(src_dict)
        accounts = d.pop("accounts", UNSET)

        burst_buffer = d.pop("burst_buffer", UNSET)

        core_count = d.pop("core_count", UNSET)

        _core_specializations = d.pop("core_specializations", UNSET)
        core_specializations: list[V0041OpenapiReservationRespReservationsItemCoreSpecializationsItem] | Unset = UNSET
        if _core_specializations is not UNSET:
            core_specializations = []
            for core_specializations_item_data in _core_specializations:
                core_specializations_item = (
                    V0041OpenapiReservationRespReservationsItemCoreSpecializationsItem.from_dict(
                        core_specializations_item_data
                    )
                )

                core_specializations.append(core_specializations_item)

        _end_time = d.pop("end_time", UNSET)
        end_time: V0041OpenapiReservationRespReservationsItemEndTime | Unset
        if isinstance(_end_time, Unset):
            end_time = UNSET
        else:
            end_time = V0041OpenapiReservationRespReservationsItemEndTime.from_dict(_end_time)

        features = d.pop("features", UNSET)

        _flags = d.pop("flags", UNSET)
        flags: list[V0041OpenapiReservationRespReservationsItemFlagsItem] | Unset = UNSET
        if _flags is not UNSET:
            flags = []
            for flags_item_data in _flags:
                flags_item = V0041OpenapiReservationRespReservationsItemFlagsItem(flags_item_data)

                flags.append(flags_item)

        groups = d.pop("groups", UNSET)

        licenses = d.pop("licenses", UNSET)

        max_start_delay = d.pop("max_start_delay", UNSET)

        name = d.pop("name", UNSET)

        node_count = d.pop("node_count", UNSET)

        node_list = d.pop("node_list", UNSET)

        partition = d.pop("partition", UNSET)

        _purge_completed = d.pop("purge_completed", UNSET)
        purge_completed: V0041OpenapiReservationRespReservationsItemPurgeCompleted | Unset
        if isinstance(_purge_completed, Unset):
            purge_completed = UNSET
        else:
            purge_completed = V0041OpenapiReservationRespReservationsItemPurgeCompleted.from_dict(_purge_completed)

        _start_time = d.pop("start_time", UNSET)
        start_time: V0041OpenapiReservationRespReservationsItemStartTime | Unset
        if isinstance(_start_time, Unset):
            start_time = UNSET
        else:
            start_time = V0041OpenapiReservationRespReservationsItemStartTime.from_dict(_start_time)

        _watts = d.pop("watts", UNSET)
        watts: V0041OpenapiReservationRespReservationsItemWatts | Unset
        if isinstance(_watts, Unset):
            watts = UNSET
        else:
            watts = V0041OpenapiReservationRespReservationsItemWatts.from_dict(_watts)

        tres = d.pop("tres", UNSET)

        users = d.pop("users", UNSET)

        v0041_openapi_reservation_resp_reservations_item = cls(
            accounts=accounts,
            burst_buffer=burst_buffer,
            core_count=core_count,
            core_specializations=core_specializations,
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

        v0041_openapi_reservation_resp_reservations_item.additional_properties = d
        return v0041_openapi_reservation_resp_reservations_item

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
