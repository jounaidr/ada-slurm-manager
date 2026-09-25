from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="V0039Warning")


@_attrs_define
class V0039Warning:
    """
    Attributes:
        warning (str | Unset): Earning message
        source (str | Unset): Where error occurred in the source
        description (str | Unset): Explanation of cause of error
    """

    warning: str | Unset = UNSET
    source: str | Unset = UNSET
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        warning = self.warning

        source = self.source

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if warning is not UNSET:
            field_dict["warning"] = warning
        if source is not UNSET:
            field_dict["source"] = source
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        warning = d.pop("warning", UNSET)

        source = d.pop("source", UNSET)

        description = d.pop("description", UNSET)

        v0039_warning = cls(
            warning=warning,
            source=source,
            description=description,
        )

        v0039_warning.additional_properties = d
        return v0039_warning

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
