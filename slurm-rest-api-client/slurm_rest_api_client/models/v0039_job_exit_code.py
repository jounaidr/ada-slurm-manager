from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v0039_job_exit_code_signal import V0039JobExitCodeSignal


T = TypeVar("T", bound="V0039JobExitCode")


@_attrs_define
class V0039JobExitCode:
    """job exit details

    Attributes:
        status (str | Unset): exit status
        return_code (int | Unset): return code (numeric)
        signal (V0039JobExitCodeSignal | Unset): Job exited due to signal
    """

    status: str | Unset = UNSET
    return_code: int | Unset = UNSET
    signal: V0039JobExitCodeSignal | Unset = UNSET
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
        from ..models.v0039_job_exit_code_signal import V0039JobExitCodeSignal

        d = dict(src_dict)
        status = d.pop("status", UNSET)

        return_code = d.pop("return_code", UNSET)

        _signal = d.pop("signal", UNSET)
        signal: V0039JobExitCodeSignal | Unset
        if isinstance(_signal, Unset):
            signal = UNSET
        else:
            signal = V0039JobExitCodeSignal.from_dict(_signal)

        v0039_job_exit_code = cls(
            status=status,
            return_code=return_code,
            signal=signal,
        )

        v0039_job_exit_code.additional_properties = d
        return v0039_job_exit_code

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
