from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemTimeTotal")


@_attrs_define
class V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemTimeTotal:
    """
    Attributes:
        seconds (int | Unset): Total CPU time used by the step in seconds
        microseconds (int | Unset): Total CPU time used by the step in microseconds
    """

    seconds: int | Unset = UNSET
    microseconds: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        seconds = self.seconds

        microseconds = self.microseconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if seconds is not UNSET:
            field_dict["seconds"] = seconds
        if microseconds is not UNSET:
            field_dict["microseconds"] = microseconds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        seconds = d.pop("seconds", UNSET)

        microseconds = d.pop("microseconds", UNSET)

        v0041_openapi_slurmdbd_jobs_resp_jobs_item_steps_item_time_total = cls(
            seconds=seconds,
            microseconds=microseconds,
        )

        v0041_openapi_slurmdbd_jobs_resp_jobs_item_steps_item_time_total.additional_properties = d
        return v0041_openapi_slurmdbd_jobs_resp_jobs_item_steps_item_time_total

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
