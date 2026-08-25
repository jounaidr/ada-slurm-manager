from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dbv_0038_tres_list_item import Dbv0038TresListItem


T = TypeVar("T", bound="Dbv0038Accounting")


@_attrs_define
class Dbv0038Accounting:
    """
    Attributes:
        allocated (int | Unset): total seconds allocated
        id (int | Unset): association/wckey ID
        start (int | Unset): UNIX timestamp when accounting period started
        tres (list[Dbv0038TresListItem] | Unset): TRES list of attributes
    """

    allocated: int | Unset = UNSET
    id: int | Unset = UNSET
    start: int | Unset = UNSET
    tres: list[Dbv0038TresListItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allocated = self.allocated

        id = self.id

        start = self.start

        tres: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tres, Unset):
            tres = []
            for componentsschemasdbv0_0_38_tres_list_item_data in self.tres:
                componentsschemasdbv0_0_38_tres_list_item = componentsschemasdbv0_0_38_tres_list_item_data.to_dict()
                tres.append(componentsschemasdbv0_0_38_tres_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if allocated is not UNSET:
            field_dict["allocated"] = allocated
        if id is not UNSET:
            field_dict["id"] = id
        if start is not UNSET:
            field_dict["start"] = start
        if tres is not UNSET:
            field_dict["TRES"] = tres

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dbv_0038_tres_list_item import Dbv0038TresListItem

        d = dict(src_dict)
        allocated = d.pop("allocated", UNSET)

        id = d.pop("id", UNSET)

        start = d.pop("start", UNSET)

        _tres = d.pop("TRES", UNSET)
        tres: list[Dbv0038TresListItem] | Unset = UNSET
        if _tres is not UNSET:
            tres = []
            for componentsschemasdbv0_0_38_tres_list_item_data in _tres:
                componentsschemasdbv0_0_38_tres_list_item = Dbv0038TresListItem.from_dict(
                    componentsschemasdbv0_0_38_tres_list_item_data
                )

                tres.append(componentsschemasdbv0_0_38_tres_list_item)

        dbv_0038_accounting = cls(
            allocated=allocated,
            id=id,
            start=start,
            tres=tres,
        )

        dbv_0038_accounting.additional_properties = d
        return dbv_0038_accounting

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
