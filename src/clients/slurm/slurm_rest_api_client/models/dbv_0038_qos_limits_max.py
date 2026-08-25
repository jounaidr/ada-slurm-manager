from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dbv_0038_qos_limits_max_accruing import Dbv0038QosLimitsMaxAccruing
    from ..models.dbv_0038_qos_limits_max_jobs import Dbv0038QosLimitsMaxJobs
    from ..models.dbv_0038_qos_limits_max_tres import Dbv0038QosLimitsMaxTres
    from ..models.dbv_0038_qos_limits_max_wall_clock import Dbv0038QosLimitsMaxWallClock


T = TypeVar("T", bound="Dbv0038QosLimitsMax")


@_attrs_define
class Dbv0038QosLimitsMax:
    """Limits on max settings

    Attributes:
        wall_clock (Dbv0038QosLimitsMaxWallClock | Unset): Limit on wallclock settings
        jobs (Dbv0038QosLimitsMaxJobs | Unset): Limits on jobs settings
        accruing (Dbv0038QosLimitsMaxAccruing | Unset): Limits on accruing priority
        tres (Dbv0038QosLimitsMaxTres | Unset): Limits on TRES
    """

    wall_clock: Dbv0038QosLimitsMaxWallClock | Unset = UNSET
    jobs: Dbv0038QosLimitsMaxJobs | Unset = UNSET
    accruing: Dbv0038QosLimitsMaxAccruing | Unset = UNSET
    tres: Dbv0038QosLimitsMaxTres | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        wall_clock: dict[str, Any] | Unset = UNSET
        if not isinstance(self.wall_clock, Unset):
            wall_clock = self.wall_clock.to_dict()

        jobs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.jobs, Unset):
            jobs = self.jobs.to_dict()

        accruing: dict[str, Any] | Unset = UNSET
        if not isinstance(self.accruing, Unset):
            accruing = self.accruing.to_dict()

        tres: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tres, Unset):
            tres = self.tres.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if wall_clock is not UNSET:
            field_dict["wall_clock"] = wall_clock
        if jobs is not UNSET:
            field_dict["jobs"] = jobs
        if accruing is not UNSET:
            field_dict["accruing"] = accruing
        if tres is not UNSET:
            field_dict["tres"] = tres

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dbv_0038_qos_limits_max_accruing import Dbv0038QosLimitsMaxAccruing
        from ..models.dbv_0038_qos_limits_max_jobs import Dbv0038QosLimitsMaxJobs
        from ..models.dbv_0038_qos_limits_max_tres import Dbv0038QosLimitsMaxTres
        from ..models.dbv_0038_qos_limits_max_wall_clock import Dbv0038QosLimitsMaxWallClock

        d = dict(src_dict)
        _wall_clock = d.pop("wall_clock", UNSET)
        wall_clock: Dbv0038QosLimitsMaxWallClock | Unset
        if isinstance(_wall_clock, Unset):
            wall_clock = UNSET
        else:
            wall_clock = Dbv0038QosLimitsMaxWallClock.from_dict(_wall_clock)

        _jobs = d.pop("jobs", UNSET)
        jobs: Dbv0038QosLimitsMaxJobs | Unset
        if isinstance(_jobs, Unset):
            jobs = UNSET
        else:
            jobs = Dbv0038QosLimitsMaxJobs.from_dict(_jobs)

        _accruing = d.pop("accruing", UNSET)
        accruing: Dbv0038QosLimitsMaxAccruing | Unset
        if isinstance(_accruing, Unset):
            accruing = UNSET
        else:
            accruing = Dbv0038QosLimitsMaxAccruing.from_dict(_accruing)

        _tres = d.pop("tres", UNSET)
        tres: Dbv0038QosLimitsMaxTres | Unset
        if isinstance(_tres, Unset):
            tres = UNSET
        else:
            tres = Dbv0038QosLimitsMaxTres.from_dict(_tres)

        dbv_0038_qos_limits_max = cls(
            wall_clock=wall_clock,
            jobs=jobs,
            accruing=accruing,
            tres=tres,
        )

        dbv_0038_qos_limits_max.additional_properties = d
        return dbv_0038_qos_limits_max

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
