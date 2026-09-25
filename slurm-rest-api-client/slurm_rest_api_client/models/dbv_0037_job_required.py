from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Dbv0037JobRequired")


@_attrs_define
class Dbv0037JobRequired:
    """Job run requirements

    Attributes:
        cp_us (int | Unset): Required number of CPUs
        memory (int | Unset): Required amount of memory (MiB)
    """

    cp_us: int | Unset = UNSET
    memory: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cp_us = self.cp_us

        memory = self.memory

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cp_us is not UNSET:
            field_dict["CPUs"] = cp_us
        if memory is not UNSET:
            field_dict["memory"] = memory

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cp_us = d.pop("CPUs", UNSET)

        memory = d.pop("memory", UNSET)

        dbv_0037_job_required = cls(
            cp_us=cp_us,
            memory=memory,
        )

        dbv_0037_job_required.additional_properties = d
        return dbv_0037_job_required

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
