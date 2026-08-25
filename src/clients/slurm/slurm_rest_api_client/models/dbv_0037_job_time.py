from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dbv_0037_job_time_system import Dbv0037JobTimeSystem
    from ..models.dbv_0037_job_time_total import Dbv0037JobTimeTotal
    from ..models.dbv_0037_job_time_user import Dbv0037JobTimeUser


T = TypeVar("T", bound="Dbv0037JobTime")


@_attrs_define
class Dbv0037JobTime:
    """Time properties

    Attributes:
        elapsed (int | Unset): Total time elapsed
        eligible (int | Unset): Total time eligible to run
        end (int | Unset): Timestamp of when job ended
        start (int | Unset): Timestamp of when job started
        submission (int | Unset): Timestamp of when job submitted
        suspended (int | Unset): Timestamp of when job last suspended
        system (Dbv0037JobTimeSystem | Unset): System time values
        total (Dbv0037JobTimeTotal | Unset): System time values
        user (Dbv0037JobTimeUser | Unset): User land time values
        limit (int | Unset): Job wall clock time limit
    """

    elapsed: int | Unset = UNSET
    eligible: int | Unset = UNSET
    end: int | Unset = UNSET
    start: int | Unset = UNSET
    submission: int | Unset = UNSET
    suspended: int | Unset = UNSET
    system: Dbv0037JobTimeSystem | Unset = UNSET
    total: Dbv0037JobTimeTotal | Unset = UNSET
    user: Dbv0037JobTimeUser | Unset = UNSET
    limit: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        elapsed = self.elapsed

        eligible = self.eligible

        end = self.end

        start = self.start

        submission = self.submission

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

        limit = self.limit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if elapsed is not UNSET:
            field_dict["elapsed"] = elapsed
        if eligible is not UNSET:
            field_dict["eligible"] = eligible
        if end is not UNSET:
            field_dict["end"] = end
        if start is not UNSET:
            field_dict["start"] = start
        if submission is not UNSET:
            field_dict["submission"] = submission
        if suspended is not UNSET:
            field_dict["suspended"] = suspended
        if system is not UNSET:
            field_dict["system"] = system
        if total is not UNSET:
            field_dict["total"] = total
        if user is not UNSET:
            field_dict["user"] = user
        if limit is not UNSET:
            field_dict["limit"] = limit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dbv_0037_job_time_system import Dbv0037JobTimeSystem
        from ..models.dbv_0037_job_time_total import Dbv0037JobTimeTotal
        from ..models.dbv_0037_job_time_user import Dbv0037JobTimeUser

        d = dict(src_dict)
        elapsed = d.pop("elapsed", UNSET)

        eligible = d.pop("eligible", UNSET)

        end = d.pop("end", UNSET)

        start = d.pop("start", UNSET)

        submission = d.pop("submission", UNSET)

        suspended = d.pop("suspended", UNSET)

        _system = d.pop("system", UNSET)
        system: Dbv0037JobTimeSystem | Unset
        if isinstance(_system, Unset):
            system = UNSET
        else:
            system = Dbv0037JobTimeSystem.from_dict(_system)

        _total = d.pop("total", UNSET)
        total: Dbv0037JobTimeTotal | Unset
        if isinstance(_total, Unset):
            total = UNSET
        else:
            total = Dbv0037JobTimeTotal.from_dict(_total)

        _user = d.pop("user", UNSET)
        user: Dbv0037JobTimeUser | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = Dbv0037JobTimeUser.from_dict(_user)

        limit = d.pop("limit", UNSET)

        dbv_0037_job_time = cls(
            elapsed=elapsed,
            eligible=eligible,
            end=end,
            start=start,
            submission=submission,
            suspended=suspended,
            system=system,
            total=total,
            user=user,
            limit=limit,
        )

        dbv_0037_job_time.additional_properties = d
        return dbv_0037_job_time

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
