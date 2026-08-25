from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dbv_0037_error import Dbv0037Error
    from ..models.dbv_0037_tres_list_item import Dbv0037TresListItem


T = TypeVar("T", bound="Dbv0037TresInfo")


@_attrs_define
class Dbv0037TresInfo:
    """
    Attributes:
        errors (list[Dbv0037Error] | Unset): Slurm errors
        tres (list[list[Dbv0037TresListItem]] | Unset): Array of tres
    """

    errors: list[Dbv0037Error] | Unset = UNSET
    tres: list[list[Dbv0037TresListItem]] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        errors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()
                errors.append(errors_item)

        tres: list[list[dict[str, Any]]] | Unset = UNSET
        if not isinstance(self.tres, Unset):
            tres = []
            for tres_item_data in self.tres:
                tres_item = []
                for componentsschemasdbv0_0_37_tres_list_item_data in tres_item_data:
                    componentsschemasdbv0_0_37_tres_list_item = componentsschemasdbv0_0_37_tres_list_item_data.to_dict()
                    tres_item.append(componentsschemasdbv0_0_37_tres_list_item)

                tres.append(tres_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if errors is not UNSET:
            field_dict["errors"] = errors
        if tres is not UNSET:
            field_dict["tres"] = tres

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dbv_0037_error import Dbv0037Error
        from ..models.dbv_0037_tres_list_item import Dbv0037TresListItem

        d = dict(src_dict)
        _errors = d.pop("errors", UNSET)
        errors: list[Dbv0037Error] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = Dbv0037Error.from_dict(errors_item_data)

                errors.append(errors_item)

        _tres = d.pop("tres", UNSET)
        tres: list[list[Dbv0037TresListItem]] | Unset = UNSET
        if _tres is not UNSET:
            tres = []
            for tres_item_data in _tres:
                tres_item = []
                _tres_item = tres_item_data
                for componentsschemasdbv0_0_37_tres_list_item_data in _tres_item:
                    componentsschemasdbv0_0_37_tres_list_item = Dbv0037TresListItem.from_dict(
                        componentsschemasdbv0_0_37_tres_list_item_data
                    )

                    tres_item.append(componentsschemasdbv0_0_37_tres_list_item)

                tres.append(tres_item)

        dbv_0037_tres_info = cls(
            errors=errors,
            tres=tres,
        )

        dbv_0037_tres_info.additional_properties = d
        return dbv_0037_tres_info

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
