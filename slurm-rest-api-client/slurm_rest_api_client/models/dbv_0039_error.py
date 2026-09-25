from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Dbv0039Error")


@_attrs_define
class Dbv0039Error:
    """
    Attributes:
        error_number (int | Unset): Slurm internal error number
        error (str | Unset): Error message
        source (str | Unset): Where error occurred in the source
        description (str | Unset): Explanation of cause of error
    """

    error_number: int | Unset = UNSET
    error: str | Unset = UNSET
    source: str | Unset = UNSET
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error_number = self.error_number

        error = self.error

        source = self.source

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error_number is not UNSET:
            field_dict["error_number"] = error_number
        if error is not UNSET:
            field_dict["error"] = error
        if source is not UNSET:
            field_dict["source"] = source
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        error_number = d.pop("error_number", UNSET)

        error = d.pop("error", UNSET)

        source = d.pop("source", UNSET)

        description = d.pop("description", UNSET)

        dbv_0039_error = cls(
            error_number=error_number,
            error=error,
            source=source,
            description=description,
        )

        dbv_0039_error.additional_properties = d
        return dbv_0039_error

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
