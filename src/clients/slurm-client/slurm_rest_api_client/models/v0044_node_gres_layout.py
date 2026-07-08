from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="V0044NodeGresLayout")


@_attrs_define
class V0044NodeGresLayout:
    """
    Attributes:
        name (str): GRES name
        type_ (str | Unset): GRES type (optional)
        count (int | Unset): Count
        index (str | Unset): Index
    """

    name: str
    type_: str | Unset = UNSET
    count: int | Unset = UNSET
    index: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_ = self.type_

        count = self.count

        index = self.index

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_
        if count is not UNSET:
            field_dict["count"] = count
        if index is not UNSET:
            field_dict["index"] = index

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        type_ = d.pop("type", UNSET)

        count = d.pop("count", UNSET)

        index = d.pop("index", UNSET)

        v0044_node_gres_layout = cls(
            name=name,
            type_=type_,
            count=count,
            index=index,
        )

        v0044_node_gres_layout.additional_properties = d
        return v0044_node_gres_layout

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
