from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.v0041_openapi_slurmdbd_jobs_resp_jobs_item_wckey_flags_item import (
    V0041OpenapiSlurmdbdJobsRespJobsItemWckeyFlagsItem,
)

T = TypeVar("T", bound="V0041OpenapiSlurmdbdJobsRespJobsItemWckey")


@_attrs_define
class V0041OpenapiSlurmdbdJobsRespJobsItemWckey:
    """Workload characterization key

    Attributes:
        wckey (str): WCKey name
        flags (list[V0041OpenapiSlurmdbdJobsRespJobsItemWckeyFlagsItem]): Active flags
    """

    wckey: str
    flags: list[V0041OpenapiSlurmdbdJobsRespJobsItemWckeyFlagsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        wckey = self.wckey

        flags = []
        for flags_item_data in self.flags:
            flags_item = flags_item_data.value
            flags.append(flags_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "wckey": wckey,
                "flags": flags,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        wckey = d.pop("wckey")

        flags = []
        _flags = d.pop("flags")
        for flags_item_data in _flags:
            flags_item = V0041OpenapiSlurmdbdJobsRespJobsItemWckeyFlagsItem(flags_item_data)

            flags.append(flags_item)

        v0041_openapi_slurmdbd_jobs_resp_jobs_item_wckey = cls(
            wckey=wckey,
            flags=flags,
        )

        v0041_openapi_slurmdbd_jobs_resp_jobs_item_wckey.additional_properties = d
        return v0041_openapi_slurmdbd_jobs_resp_jobs_item_wckey

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
