from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Dbv0038AssociationMin")


@_attrs_define
class Dbv0038AssociationMin:
    """Min settings

    Attributes:
        priority_threshold (int | Unset): Min priority threshold
    """

    priority_threshold: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        priority_threshold = self.priority_threshold

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if priority_threshold is not UNSET:
            field_dict["priority_threshold"] = priority_threshold

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        priority_threshold = d.pop("priority_threshold", UNSET)

        dbv_0038_association_min = cls(
            priority_threshold=priority_threshold,
        )

        dbv_0038_association_min.additional_properties = d
        return dbv_0038_association_min

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
