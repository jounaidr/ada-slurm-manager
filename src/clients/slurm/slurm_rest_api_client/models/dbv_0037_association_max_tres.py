from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dbv_0037_association_max_tres_group import Dbv0037AssociationMaxTresGroup
    from ..models.dbv_0037_association_max_tres_minutes import Dbv0037AssociationMaxTresMinutes
    from ..models.dbv_0037_association_max_tres_per import Dbv0037AssociationMaxTresPer
    from ..models.dbv_0037_tres_list_item import Dbv0037TresListItem


T = TypeVar("T", bound="Dbv0037AssociationMaxTres")


@_attrs_define
class Dbv0037AssociationMaxTres:
    """Max TRES settings

    Attributes:
        group (Dbv0037AssociationMaxTresGroup | Unset): Max TRES per group
        per (Dbv0037AssociationMaxTresPer | Unset): Max TRES per settings
        total (list[Dbv0037TresListItem] | Unset): TRES list of attributes
        minutes (Dbv0037AssociationMaxTresMinutes | Unset): Max TRES minutes settings
    """

    group: Dbv0037AssociationMaxTresGroup | Unset = UNSET
    per: Dbv0037AssociationMaxTresPer | Unset = UNSET
    total: list[Dbv0037TresListItem] | Unset = UNSET
    minutes: Dbv0037AssociationMaxTresMinutes | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        group: dict[str, Any] | Unset = UNSET
        if not isinstance(self.group, Unset):
            group = self.group.to_dict()

        per: dict[str, Any] | Unset = UNSET
        if not isinstance(self.per, Unset):
            per = self.per.to_dict()

        total: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.total, Unset):
            total = []
            for componentsschemasdbv0_0_37_tres_list_item_data in self.total:
                componentsschemasdbv0_0_37_tres_list_item = componentsschemasdbv0_0_37_tres_list_item_data.to_dict()
                total.append(componentsschemasdbv0_0_37_tres_list_item)

        minutes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.minutes, Unset):
            minutes = self.minutes.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if group is not UNSET:
            field_dict["group"] = group
        if per is not UNSET:
            field_dict["per"] = per
        if total is not UNSET:
            field_dict["total"] = total
        if minutes is not UNSET:
            field_dict["minutes"] = minutes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dbv_0037_association_max_tres_group import Dbv0037AssociationMaxTresGroup
        from ..models.dbv_0037_association_max_tres_minutes import Dbv0037AssociationMaxTresMinutes
        from ..models.dbv_0037_association_max_tres_per import Dbv0037AssociationMaxTresPer
        from ..models.dbv_0037_tres_list_item import Dbv0037TresListItem

        d = dict(src_dict)
        _group = d.pop("group", UNSET)
        group: Dbv0037AssociationMaxTresGroup | Unset
        if isinstance(_group, Unset):
            group = UNSET
        else:
            group = Dbv0037AssociationMaxTresGroup.from_dict(_group)

        _per = d.pop("per", UNSET)
        per: Dbv0037AssociationMaxTresPer | Unset
        if isinstance(_per, Unset):
            per = UNSET
        else:
            per = Dbv0037AssociationMaxTresPer.from_dict(_per)

        _total = d.pop("total", UNSET)
        total: list[Dbv0037TresListItem] | Unset = UNSET
        if _total is not UNSET:
            total = []
            for componentsschemasdbv0_0_37_tres_list_item_data in _total:
                componentsschemasdbv0_0_37_tres_list_item = Dbv0037TresListItem.from_dict(
                    componentsschemasdbv0_0_37_tres_list_item_data
                )

                total.append(componentsschemasdbv0_0_37_tres_list_item)

        _minutes = d.pop("minutes", UNSET)
        minutes: Dbv0037AssociationMaxTresMinutes | Unset
        if isinstance(_minutes, Unset):
            minutes = UNSET
        else:
            minutes = Dbv0037AssociationMaxTresMinutes.from_dict(_minutes)

        dbv_0037_association_max_tres = cls(
            group=group,
            per=per,
            total=total,
            minutes=minutes,
        )

        dbv_0037_association_max_tres.additional_properties = d
        return dbv_0037_association_max_tres

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
