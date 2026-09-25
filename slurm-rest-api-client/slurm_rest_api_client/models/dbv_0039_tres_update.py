from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v0039_tres import V0039Tres


T = TypeVar("T", bound="Dbv0039TresUpdate")


@_attrs_define
class Dbv0039TresUpdate:
    """
    Attributes:
        tres (list[V0039Tres] | Unset):
    """

    tres: list[V0039Tres] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tres: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tres, Unset):
            tres = []
            for componentsschemasv0_0_39_tres_list_item_data in self.tres:
                componentsschemasv0_0_39_tres_list_item = componentsschemasv0_0_39_tres_list_item_data.to_dict()
                tres.append(componentsschemasv0_0_39_tres_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tres is not UNSET:
            field_dict["tres"] = tres

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v0039_tres import V0039Tres

        d = dict(src_dict)
        _tres = d.pop("tres", UNSET)
        tres: list[V0039Tres] | Unset = UNSET
        if _tres is not UNSET:
            tres = []
            for componentsschemasv0_0_39_tres_list_item_data in _tres:
                componentsschemasv0_0_39_tres_list_item = V0039Tres.from_dict(
                    componentsschemasv0_0_39_tres_list_item_data
                )

                tres.append(componentsschemasv0_0_39_tres_list_item)

        dbv_0039_tres_update = cls(
            tres=tres,
        )

        dbv_0039_tres_update.additional_properties = d
        return dbv_0039_tres_update

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
