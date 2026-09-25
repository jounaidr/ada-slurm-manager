from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dbv_0037_job_step_time_system import Dbv0037JobStepTimeSystem
    from ..models.dbv_0037_job_step_time_total import Dbv0037JobStepTimeTotal
    from ..models.dbv_0037_job_step_time_user import Dbv0037JobStepTimeUser


T = TypeVar("T", bound="Dbv0037JobStepTime")


@_attrs_define
class Dbv0037JobStepTime:
    """Time properties

    Attributes:
        elapsed (int | Unset): Total time elapsed
        end (int | Unset): Timestamp of when job ended
        start (int | Unset): Timestamp of when job started
        suspended (int | Unset): Timestamp of when job last suspended
        system (Dbv0037JobStepTimeSystem | Unset): System time values
        total (Dbv0037JobStepTimeTotal | Unset): System time values
        user (Dbv0037JobStepTimeUser | Unset): User land time values
    """

    elapsed: int | Unset = UNSET
    end: int | Unset = UNSET
    start: int | Unset = UNSET
    suspended: int | Unset = UNSET
    system: Dbv0037JobStepTimeSystem | Unset = UNSET
    total: Dbv0037JobStepTimeTotal | Unset = UNSET
    user: Dbv0037JobStepTimeUser | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        elapsed = self.elapsed

        end = self.end

        start = self.start

        suspended = self.suspended

        system: dict[str, Any] | Unset = UNSET
        if not isinstance(self.system, Unset):
            system = self.system.to_dict()

        total: dict[str, Any] | Unset = UNSET
        if not isinstance(self.total, Unset):
            total = self.total.to_dict()

        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if elapsed is not UNSET:
            field_dict["elapsed"] = elapsed
        if end is not UNSET:
            field_dict["end"] = end
        if start is not UNSET:
            field_dict["start"] = start
        if suspended is not UNSET:
            field_dict["suspended"] = suspended
        if system is not UNSET:
            field_dict["system"] = system
        if total is not UNSET:
            field_dict["total"] = total
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dbv_0037_job_step_time_system import Dbv0037JobStepTimeSystem
        from ..models.dbv_0037_job_step_time_total import Dbv0037JobStepTimeTotal
        from ..models.dbv_0037_job_step_time_user import Dbv0037JobStepTimeUser

        d = dict(src_dict)
        elapsed = d.pop("elapsed", UNSET)

        end = d.pop("end", UNSET)

        start = d.pop("start", UNSET)

        suspended = d.pop("suspended", UNSET)

        _system = d.pop("system", UNSET)
        system: Dbv0037JobStepTimeSystem | Unset
        if isinstance(_system, Unset):
            system = UNSET
        else:
            system = Dbv0037JobStepTimeSystem.from_dict(_system)

        _total = d.pop("total", UNSET)
        total: Dbv0037JobStepTimeTotal | Unset
        if isinstance(_total, Unset):
            total = UNSET
        else:
            total = Dbv0037JobStepTimeTotal.from_dict(_total)

        _user = d.pop("user", UNSET)
        user: Dbv0037JobStepTimeUser | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = Dbv0037JobStepTimeUser.from_dict(_user)

        dbv_0037_job_step_time = cls(
            elapsed=elapsed,
            end=end,
            start=start,
            suspended=suspended,
            system=system,
            total=total,
            user=user,
        )

        dbv_0037_job_step_time.additional_properties = d
        return dbv_0037_job_step_time

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
