from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dbv_0038_association_max_tres_minutes import Dbv0038AssociationMaxTresMinutes
    from ..models.dbv_0038_association_max_tres_per import Dbv0038AssociationMaxTresPer
    from ..models.dbv_0038_tres_list_item import Dbv0038TresListItem


T = TypeVar("T", bound="Dbv0038AssociationMaxTres")


@_attrs_define
class Dbv0038AssociationMaxTres:
    """Max TRES settings

    Attributes:
        per (Dbv0038AssociationMaxTresPer | Unset): Max TRES per settings
        total (list[Dbv0038TresListItem] | Unset): TRES list of attributes
        minutes (Dbv0038AssociationMaxTresMinutes | Unset): Max TRES minutes settings
    """

    per: Dbv0038AssociationMaxTresPer | Unset = UNSET
    total: list[Dbv0038TresListItem] | Unset = UNSET
    minutes: Dbv0038AssociationMaxTresMinutes | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        per: dict[str, Any] | Unset = UNSET
        if not isinstance(self.per, Unset):
            per = self.per.to_dict()

        total: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.total, Unset):
            total = []
            for componentsschemasdbv0_0_38_tres_list_item_data in self.total:
                componentsschemasdbv0_0_38_tres_list_item = componentsschemasdbv0_0_38_tres_list_item_data.to_dict()
                total.append(componentsschemasdbv0_0_38_tres_list_item)

        minutes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.minutes, Unset):
            minutes = self.minutes.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if per is not UNSET:
            field_dict["per"] = per
        if total is not UNSET:
            field_dict["total"] = total
        if minutes is not UNSET:
            field_dict["minutes"] = minutes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dbv_0038_association_max_tres_minutes import Dbv0038AssociationMaxTresMinutes
        from ..models.dbv_0038_association_max_tres_per import Dbv0038AssociationMaxTresPer
        from ..models.dbv_0038_tres_list_item import Dbv0038TresListItem

        d = dict(src_dict)
        _per = d.pop("per", UNSET)
        per: Dbv0038AssociationMaxTresPer | Unset
        if isinstance(_per, Unset):
            per = UNSET
        else:
            per = Dbv0038AssociationMaxTresPer.from_dict(_per)

        _total = d.pop("total", UNSET)
        total: list[Dbv0038TresListItem] | Unset = UNSET
        if _total is not UNSET:
            total = []
            for componentsschemasdbv0_0_38_tres_list_item_data in _total:
                componentsschemasdbv0_0_38_tres_list_item = Dbv0038TresListItem.from_dict(
                    componentsschemasdbv0_0_38_tres_list_item_data
                )

                total.append(componentsschemasdbv0_0_38_tres_list_item)

        _minutes = d.pop("minutes", UNSET)
        minutes: Dbv0038AssociationMaxTresMinutes | Unset
        if isinstance(_minutes, Unset):
            minutes = UNSET
        else:
            minutes = Dbv0038AssociationMaxTresMinutes.from_dict(_minutes)

        dbv_0038_association_max_tres = cls(
            per=per,
            total=total,
            minutes=minutes,
        )

        dbv_0038_association_max_tres.additional_properties = d
        return dbv_0038_association_max_tres

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
