from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="V0039JobArrayResponseMsgItem")


@_attrs_define
class V0039JobArrayResponseMsgItem:
    """ArrayJob

    Attributes:
        job_id (int | Unset): JobId
        error_code (int | Unset): numeric error code
        error (str | Unset): error code description
        why (str | Unset): error message
    """

    job_id: int | Unset = UNSET
    error_code: int | Unset = UNSET
    error: str | Unset = UNSET
    why: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        job_id = self.job_id

        error_code = self.error_code

        error = self.error

        why = self.why

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if job_id is not UNSET:
            field_dict["job_id"] = job_id
        if error_code is not UNSET:
            field_dict["error_code"] = error_code
        if error is not UNSET:
            field_dict["error"] = error
        if why is not UNSET:
            field_dict["why"] = why

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        job_id = d.pop("job_id", UNSET)

        error_code = d.pop("error_code", UNSET)

        error = d.pop("error", UNSET)

        why = d.pop("why", UNSET)

        v0039_job_array_response_msg_item = cls(
            job_id=job_id,
            error_code=error_code,
            error=error,
            why=why,
        )

        v0039_job_array_response_msg_item.additional_properties = d
        return v0039_job_array_response_msg_item

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
