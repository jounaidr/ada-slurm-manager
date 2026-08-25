from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Dbv0037CoordinatorInfo")


@_attrs_define
class Dbv0037CoordinatorInfo:
    """
    Attributes:
        name (str | Unset): Name of user
        direct (int | Unset): If user is coordinator of this account directly or coordinator status was inherited from a
            higher account in the tree
    """

    name: str | Unset = UNSET
    direct: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        direct = self.direct

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if direct is not UNSET:
            field_dict["direct"] = direct

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        direct = d.pop("direct", UNSET)

        dbv_0037_coordinator_info = cls(
            name=name,
            direct=direct,
        )

        dbv_0037_coordinator_info.additional_properties = d
        return dbv_0037_coordinator_info

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
