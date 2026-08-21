from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v0041_openapi_slurmdbd_jobs_resp_jobs_item_steps_item_time_end import (
        V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemTimeEnd,
    )
    from ..models.v0041_openapi_slurmdbd_jobs_resp_jobs_item_steps_item_time_start import (
        V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemTimeStart,
    )
    from ..models.v0041_openapi_slurmdbd_jobs_resp_jobs_item_steps_item_time_system import (
        V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemTimeSystem,
    )
    from ..models.v0041_openapi_slurmdbd_jobs_resp_jobs_item_steps_item_time_total import (
        V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemTimeTotal,
    )
    from ..models.v0041_openapi_slurmdbd_jobs_resp_jobs_item_steps_item_time_user import (
        V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemTimeUser,
    )


T = TypeVar("T", bound="V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemTime")


@_attrs_define
class V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemTime:
    """
    Attributes:
        elapsed (int | Unset): Elapsed time in seconds
        end (V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemTimeEnd | Unset): End time (UNIX timestamp)
        start (V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemTimeStart | Unset): Time execution began (UNIX timestamp)
        suspended (int | Unset): Time in suspended state in seconds
        system (V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemTimeSystem | Unset):
        total (V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemTimeTotal | Unset):
        user (V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemTimeUser | Unset):
    """

    elapsed: int | Unset = UNSET
    end: V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemTimeEnd | Unset = UNSET
    start: V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemTimeStart | Unset = UNSET
    suspended: int | Unset = UNSET
    system: V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemTimeSystem | Unset = UNSET
    total: V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemTimeTotal | Unset = UNSET
    user: V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemTimeUser | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        elapsed = self.elapsed

        end: dict[str, Any] | Unset = UNSET
        if not isinstance(self.end, Unset):
            end = self.end.to_dict()

        start: dict[str, Any] | Unset = UNSET
        if not isinstance(self.start, Unset):
            start = self.start.to_dict()

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
        from ..models.v0041_openapi_slurmdbd_jobs_resp_jobs_item_steps_item_time_end import (
            V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemTimeEnd,
        )
        from ..models.v0041_openapi_slurmdbd_jobs_resp_jobs_item_steps_item_time_start import (
            V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemTimeStart,
        )
        from ..models.v0041_openapi_slurmdbd_jobs_resp_jobs_item_steps_item_time_system import (
            V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemTimeSystem,
        )
        from ..models.v0041_openapi_slurmdbd_jobs_resp_jobs_item_steps_item_time_total import (
            V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemTimeTotal,
        )
        from ..models.v0041_openapi_slurmdbd_jobs_resp_jobs_item_steps_item_time_user import (
            V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemTimeUser,
        )

        d = dict(src_dict)
        elapsed = d.pop("elapsed", UNSET)

        _end = d.pop("end", UNSET)
        end: V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemTimeEnd | Unset
        if isinstance(_end, Unset):
            end = UNSET
        else:
            end = V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemTimeEnd.from_dict(_end)

        _start = d.pop("start", UNSET)
        start: V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemTimeStart | Unset
        if isinstance(_start, Unset):
            start = UNSET
        else:
            start = V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemTimeStart.from_dict(_start)

        suspended = d.pop("suspended", UNSET)

        _system = d.pop("system", UNSET)
        system: V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemTimeSystem | Unset
        if isinstance(_system, Unset):
            system = UNSET
        else:
            system = V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemTimeSystem.from_dict(_system)

        _total = d.pop("total", UNSET)
        total: V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemTimeTotal | Unset
        if isinstance(_total, Unset):
            total = UNSET
        else:
            total = V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemTimeTotal.from_dict(_total)

        _user = d.pop("user", UNSET)
        user: V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemTimeUser | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemTimeUser.from_dict(_user)

        v0041_openapi_slurmdbd_jobs_resp_jobs_item_steps_item_time = cls(
            elapsed=elapsed,
            end=end,
            start=start,
            suspended=suspended,
            system=system,
            total=total,
            user=user,
        )

        v0041_openapi_slurmdbd_jobs_resp_jobs_item_steps_item_time.additional_properties = d
        return v0041_openapi_slurmdbd_jobs_resp_jobs_item_steps_item_time

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
