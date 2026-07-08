from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.v0041_openapi_slurmdbd_jobs_resp_jobs_item_derived_exit_code_status_item import (
    V0041OpenapiSlurmdbdJobsRespJobsItemDerivedExitCodeStatusItem,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v0041_openapi_slurmdbd_jobs_resp_jobs_item_derived_exit_code_return_code import (
        V0041OpenapiSlurmdbdJobsRespJobsItemDerivedExitCodeReturnCode,
    )
    from ..models.v0041_openapi_slurmdbd_jobs_resp_jobs_item_derived_exit_code_signal import (
        V0041OpenapiSlurmdbdJobsRespJobsItemDerivedExitCodeSignal,
    )


T = TypeVar("T", bound="V0041OpenapiSlurmdbdJobsRespJobsItemDerivedExitCode")


@_attrs_define
class V0041OpenapiSlurmdbdJobsRespJobsItemDerivedExitCode:
    """Highest exit code of all job steps

    Attributes:
        status (list[V0041OpenapiSlurmdbdJobsRespJobsItemDerivedExitCodeStatusItem] | Unset): Status given by return
            code
        return_code (V0041OpenapiSlurmdbdJobsRespJobsItemDerivedExitCodeReturnCode | Unset): Process return code
            (numeric)
        signal (V0041OpenapiSlurmdbdJobsRespJobsItemDerivedExitCodeSignal | Unset):
    """

    status: list[V0041OpenapiSlurmdbdJobsRespJobsItemDerivedExitCodeStatusItem] | Unset = UNSET
    return_code: V0041OpenapiSlurmdbdJobsRespJobsItemDerivedExitCodeReturnCode | Unset = UNSET
    signal: V0041OpenapiSlurmdbdJobsRespJobsItemDerivedExitCodeSignal | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status: list[str] | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = []
            for status_item_data in self.status:
                status_item = status_item_data.value
                status.append(status_item)

        return_code: dict[str, Any] | Unset = UNSET
        if not isinstance(self.return_code, Unset):
            return_code = self.return_code.to_dict()

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
        from ..models.v0041_openapi_slurmdbd_jobs_resp_jobs_item_derived_exit_code_return_code import (
            V0041OpenapiSlurmdbdJobsRespJobsItemDerivedExitCodeReturnCode,
        )
        from ..models.v0041_openapi_slurmdbd_jobs_resp_jobs_item_derived_exit_code_signal import (
            V0041OpenapiSlurmdbdJobsRespJobsItemDerivedExitCodeSignal,
        )

        d = dict(src_dict)
        _status = d.pop("status", UNSET)
        status: list[V0041OpenapiSlurmdbdJobsRespJobsItemDerivedExitCodeStatusItem] | Unset = UNSET
        if _status is not UNSET:
            status = []
            for status_item_data in _status:
                status_item = V0041OpenapiSlurmdbdJobsRespJobsItemDerivedExitCodeStatusItem(status_item_data)

                status.append(status_item)

        _return_code = d.pop("return_code", UNSET)
        return_code: V0041OpenapiSlurmdbdJobsRespJobsItemDerivedExitCodeReturnCode | Unset
        if isinstance(_return_code, Unset):
            return_code = UNSET
        else:
            return_code = V0041OpenapiSlurmdbdJobsRespJobsItemDerivedExitCodeReturnCode.from_dict(_return_code)

        _signal = d.pop("signal", UNSET)
        signal: V0041OpenapiSlurmdbdJobsRespJobsItemDerivedExitCodeSignal | Unset
        if isinstance(_signal, Unset):
            signal = UNSET
        else:
            signal = V0041OpenapiSlurmdbdJobsRespJobsItemDerivedExitCodeSignal.from_dict(_signal)

        v0041_openapi_slurmdbd_jobs_resp_jobs_item_derived_exit_code = cls(
            status=status,
            return_code=return_code,
            signal=signal,
        )

        v0041_openapi_slurmdbd_jobs_resp_jobs_item_derived_exit_code.additional_properties = d
        return v0041_openapi_slurmdbd_jobs_resp_jobs_item_derived_exit_code

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
