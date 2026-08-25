from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dbv_0038_job_exit_code_signal import Dbv0038JobExitCodeSignal


T = TypeVar("T", bound="Dbv0038JobExitCode")


@_attrs_define
class Dbv0038JobExitCode:
    """
    Attributes:
        status (str | Unset): Job exit status
        return_code (int | Unset): Return code from parent process
        signal (Dbv0038JobExitCodeSignal | Unset): Signal details (if signaled)
    """

    status: str | Unset = UNSET
    return_code: int | Unset = UNSET
    signal: Dbv0038JobExitCodeSignal | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        return_code = self.return_code

        signal: dict[str, Any] | Unset = UNSET
        if not isinstance(self.signal, Unset):
            signal = self.signal.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if return_code is not UNSET:
            field_dict["return_code"] = return_code
        if signal is not UNSET:
            field_dict["signal"] = signal

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dbv_0038_job_exit_code_signal import Dbv0038JobExitCodeSignal

        d = dict(src_dict)
        status = d.pop("status", UNSET)

        return_code = d.pop("return_code", UNSET)

        _signal = d.pop("signal", UNSET)
        signal: Dbv0038JobExitCodeSignal | Unset
        if isinstance(_signal, Unset):
            signal = UNSET
        else:
            signal = Dbv0038JobExitCodeSignal.from_dict(_signal)

        dbv_0038_job_exit_code = cls(
            status=status,
            return_code=return_code,
            signal=signal,
        )

        dbv_0038_job_exit_code.additional_properties = d
        return dbv_0038_job_exit_code

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
