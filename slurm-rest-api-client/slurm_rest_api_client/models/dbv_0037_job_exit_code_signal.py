from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Dbv0037JobExitCodeSignal")


@_attrs_define
class Dbv0037JobExitCodeSignal:
    """Signal details (if signaled)

    Attributes:
        signal_id (int | Unset): Signal number process received
        name (str | Unset): Name of signal received
    """

    signal_id: int | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        signal_id = self.signal_id

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if signal_id is not UNSET:
            field_dict["signal_id"] = signal_id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        signal_id = d.pop("signal_id", UNSET)

        name = d.pop("name", UNSET)

        dbv_0037_job_exit_code_signal = cls(
            signal_id=signal_id,
            name=name,
        )

        dbv_0037_job_exit_code_signal.additional_properties = d
        return dbv_0037_job_exit_code_signal

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
