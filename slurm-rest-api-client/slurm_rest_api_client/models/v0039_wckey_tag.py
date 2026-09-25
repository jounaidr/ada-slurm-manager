from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.v0039_wckey_tag_flags_item import V0039WckeyTagFlagsItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="V0039WckeyTag")


@_attrs_define
class V0039WckeyTag:
    """wckey details

    Attributes:
        wckey (str | Unset): wckey
        flags (list[V0039WckeyTagFlagsItem] | Unset): active flags
    """

    wckey: str | Unset = UNSET
    flags: list[V0039WckeyTagFlagsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        wckey = self.wckey

        flags: list[str] | Unset = UNSET
        if not isinstance(self.flags, Unset):
            flags = []
            for flags_item_data in self.flags:
                flags_item = flags_item_data.value
                flags.append(flags_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if wckey is not UNSET:
            field_dict["wckey"] = wckey
        if flags is not UNSET:
            field_dict["flags"] = flags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        wckey = d.pop("wckey", UNSET)

        _flags = d.pop("flags", UNSET)
        flags: list[V0039WckeyTagFlagsItem] | Unset = UNSET
        if _flags is not UNSET:
            flags = []
            for flags_item_data in _flags:
                flags_item = V0039WckeyTagFlagsItem(flags_item_data)

                flags.append(flags_item)

        v0039_wckey_tag = cls(
            wckey=wckey,
            flags=flags,
        )

        v0039_wckey_tag.additional_properties = d
        return v0039_wckey_tag

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
