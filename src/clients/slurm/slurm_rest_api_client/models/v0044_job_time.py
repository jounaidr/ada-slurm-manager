from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v0044_job_time_system import V0044JobTimeSystem
    from ..models.v0044_job_time_total import V0044JobTimeTotal
    from ..models.v0044_job_time_user import V0044JobTimeUser
    from ..models.v0044_uint_32_no_val_struct import V0044Uint32NoValStruct
    from ..models.v0044_uint_64_no_val_struct import V0044Uint64NoValStruct


T = TypeVar("T", bound="V0044JobTime")


@_attrs_define
class V0044JobTime:
    """
    Attributes:
        elapsed (int | Unset): Elapsed time in seconds
        eligible (int | Unset): Time when the job became eligible to run (UNIX timestamp) (UNIX timestamp or time string
            recognized by Slurm (e.g., '[MM/DD[/YY]-]HH:MM[:SS]'))
        end (int | Unset): End time (UNIX timestamp) (UNIX timestamp or time string recognized by Slurm (e.g.,
            '[MM/DD[/YY]-]HH:MM[:SS]'))
        planned (V0044Uint64NoValStruct | Unset):
        start (int | Unset): Time execution began (UNIX timestamp) (UNIX timestamp or time string recognized by Slurm
            (e.g., '[MM/DD[/YY]-]HH:MM[:SS]'))
        submission (int | Unset): Time when the job was submitted (UNIX timestamp) (UNIX timestamp or time string
            recognized by Slurm (e.g., '[MM/DD[/YY]-]HH:MM[:SS]'))
        suspended (int | Unset): Total time in suspended state in seconds
        system (V0044JobTimeSystem | Unset):
        limit (V0044Uint32NoValStruct | Unset):
        total (V0044JobTimeTotal | Unset):
        user (V0044JobTimeUser | Unset):
    """

    elapsed: int | Unset = UNSET
    eligible: int | Unset = UNSET
    end: int | Unset = UNSET
    planned: V0044Uint64NoValStruct | Unset = UNSET
    start: int | Unset = UNSET
    submission: int | Unset = UNSET
    suspended: int | Unset = UNSET
    system: V0044JobTimeSystem | Unset = UNSET
    limit: V0044Uint32NoValStruct | Unset = UNSET
    total: V0044JobTimeTotal | Unset = UNSET
    user: V0044JobTimeUser | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        elapsed = self.elapsed

        eligible = self.eligible

        end = self.end

        planned: dict[str, Any] | Unset = UNSET
        if not isinstance(self.planned, Unset):
            planned = self.planned.to_dict()

        start = self.start

        submission = self.submission

        suspended = self.suspended

        system: dict[str, Any] | Unset = UNSET
        if not isinstance(self.system, Unset):
            system = self.system.to_dict()

        limit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.limit, Unset):
            limit = self.limit.to_dict()

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
        if eligible is not UNSET:
            field_dict["eligible"] = eligible
        if end is not UNSET:
            field_dict["end"] = end
        if planned is not UNSET:
            field_dict["planned"] = planned
        if start is not UNSET:
            field_dict["start"] = start
        if submission is not UNSET:
            field_dict["submission"] = submission
        if suspended is not UNSET:
            field_dict["suspended"] = suspended
        if system is not UNSET:
            field_dict["system"] = system
        if limit is not UNSET:
            field_dict["limit"] = limit
        if total is not UNSET:
            field_dict["total"] = total
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v0044_job_time_system import V0044JobTimeSystem
        from ..models.v0044_job_time_total import V0044JobTimeTotal
        from ..models.v0044_job_time_user import V0044JobTimeUser
        from ..models.v0044_uint_32_no_val_struct import V0044Uint32NoValStruct
        from ..models.v0044_uint_64_no_val_struct import V0044Uint64NoValStruct

        d = dict(src_dict)
        elapsed = d.pop("elapsed", UNSET)

        eligible = d.pop("eligible", UNSET)

        end = d.pop("end", UNSET)

        _planned = d.pop("planned", UNSET)
        planned: V0044Uint64NoValStruct | Unset
        if isinstance(_planned, Unset):
            planned = UNSET
        else:
            planned = V0044Uint64NoValStruct.from_dict(_planned)

        start = d.pop("start", UNSET)

        submission = d.pop("submission", UNSET)

        suspended = d.pop("suspended", UNSET)

        _system = d.pop("system", UNSET)
        system: V0044JobTimeSystem | Unset
        if isinstance(_system, Unset):
            system = UNSET
        else:
            system = V0044JobTimeSystem.from_dict(_system)

        _limit = d.pop("limit", UNSET)
        limit: V0044Uint32NoValStruct | Unset
        if isinstance(_limit, Unset):
            limit = UNSET
        else:
            limit = V0044Uint32NoValStruct.from_dict(_limit)

        _total = d.pop("total", UNSET)
        total: V0044JobTimeTotal | Unset
        if isinstance(_total, Unset):
            total = UNSET
        else:
            total = V0044JobTimeTotal.from_dict(_total)

        _user = d.pop("user", UNSET)
        user: V0044JobTimeUser | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = V0044JobTimeUser.from_dict(_user)

        v0044_job_time = cls(
            elapsed=elapsed,
            eligible=eligible,
            end=end,
            planned=planned,
            start=start,
            submission=submission,
            suspended=suspended,
            system=system,
            limit=limit,
            total=total,
            user=user,
        )

        v0044_job_time.additional_properties = d
        return v0044_job_time

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
