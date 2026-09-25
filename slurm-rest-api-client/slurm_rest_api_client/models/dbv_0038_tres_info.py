from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dbv_0038_error import Dbv0038Error
    from ..models.dbv_0038_meta import Dbv0038Meta
    from ..models.dbv_0038_tres_list_item import Dbv0038TresListItem


T = TypeVar("T", bound="Dbv0038TresInfo")


@_attrs_define
class Dbv0038TresInfo:
    """
    Attributes:
        meta (Dbv0038Meta | Unset):
        errors (list[Dbv0038Error] | Unset): Slurm errors
        tres (list[Dbv0038TresListItem] | Unset): TRES list of attributes
    """

    meta: Dbv0038Meta | Unset = UNSET
    errors: list[Dbv0038Error] | Unset = UNSET
    tres: list[Dbv0038TresListItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        meta: dict[str, Any] | Unset = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        errors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()
                errors.append(errors_item)

        tres: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tres, Unset):
            tres = []
            for componentsschemasdbv0_0_38_tres_list_item_data in self.tres:
                componentsschemasdbv0_0_38_tres_list_item = componentsschemasdbv0_0_38_tres_list_item_data.to_dict()
                tres.append(componentsschemasdbv0_0_38_tres_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if meta is not UNSET:
            field_dict["meta"] = meta
        if errors is not UNSET:
            field_dict["errors"] = errors
        if tres is not UNSET:
            field_dict["tres"] = tres

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dbv_0038_error import Dbv0038Error
        from ..models.dbv_0038_meta import Dbv0038Meta
        from ..models.dbv_0038_tres_list_item import Dbv0038TresListItem

        d = dict(src_dict)
        _meta = d.pop("meta", UNSET)
        meta: Dbv0038Meta | Unset
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = Dbv0038Meta.from_dict(_meta)

        _errors = d.pop("errors", UNSET)
        errors: list[Dbv0038Error] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = Dbv0038Error.from_dict(errors_item_data)

                errors.append(errors_item)

        _tres = d.pop("tres", UNSET)
        tres: list[Dbv0038TresListItem] | Unset = UNSET
        if _tres is not UNSET:
            tres = []
            for componentsschemasdbv0_0_38_tres_list_item_data in _tres:
                componentsschemasdbv0_0_38_tres_list_item = Dbv0038TresListItem.from_dict(
                    componentsschemasdbv0_0_38_tres_list_item_data
                )

                tres.append(componentsschemasdbv0_0_38_tres_list_item)

        dbv_0038_tres_info = cls(
            meta=meta,
            errors=errors,
            tres=tres,
        )

        dbv_0038_tres_info.additional_properties = d
        return dbv_0038_tres_info

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
