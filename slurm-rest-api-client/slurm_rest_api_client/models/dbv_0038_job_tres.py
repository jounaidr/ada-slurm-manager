from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dbv_0038_tres_list_item import Dbv0038TresListItem


T = TypeVar("T", bound="Dbv0038JobTres")


@_attrs_define
class Dbv0038JobTres:
    """TRES settings

    Attributes:
        allocated (list[Dbv0038TresListItem] | Unset): TRES list of attributes
        requested (list[Dbv0038TresListItem] | Unset): TRES list of attributes
    """

    allocated: list[Dbv0038TresListItem] | Unset = UNSET
    requested: list[Dbv0038TresListItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allocated: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.allocated, Unset):
            allocated = []
            for componentsschemasdbv0_0_38_tres_list_item_data in self.allocated:
                componentsschemasdbv0_0_38_tres_list_item = componentsschemasdbv0_0_38_tres_list_item_data.to_dict()
                allocated.append(componentsschemasdbv0_0_38_tres_list_item)

        requested: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.requested, Unset):
            requested = []
            for componentsschemasdbv0_0_38_tres_list_item_data in self.requested:
                componentsschemasdbv0_0_38_tres_list_item = componentsschemasdbv0_0_38_tres_list_item_data.to_dict()
                requested.append(componentsschemasdbv0_0_38_tres_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if allocated is not UNSET:
            field_dict["allocated"] = allocated
        if requested is not UNSET:
            field_dict["requested"] = requested

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dbv_0038_tres_list_item import Dbv0038TresListItem

        d = dict(src_dict)
        _allocated = d.pop("allocated", UNSET)
        allocated: list[Dbv0038TresListItem] | Unset = UNSET
        if _allocated is not UNSET:
            allocated = []
            for componentsschemasdbv0_0_38_tres_list_item_data in _allocated:
                componentsschemasdbv0_0_38_tres_list_item = Dbv0038TresListItem.from_dict(
                    componentsschemasdbv0_0_38_tres_list_item_data
                )

                allocated.append(componentsschemasdbv0_0_38_tres_list_item)

        _requested = d.pop("requested", UNSET)
        requested: list[Dbv0038TresListItem] | Unset = UNSET
        if _requested is not UNSET:
            requested = []
            for componentsschemasdbv0_0_38_tres_list_item_data in _requested:
                componentsschemasdbv0_0_38_tres_list_item = Dbv0038TresListItem.from_dict(
                    componentsschemasdbv0_0_38_tres_list_item_data
                )

                requested.append(componentsschemasdbv0_0_38_tres_list_item)

        dbv_0038_job_tres = cls(
            allocated=allocated,
            requested=requested,
        )

        dbv_0038_job_tres.additional_properties = d
        return dbv_0038_job_tres

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
