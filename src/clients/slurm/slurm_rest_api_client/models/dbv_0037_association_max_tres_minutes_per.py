from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dbv_0037_tres_list_item import Dbv0037TresListItem


T = TypeVar("T", bound="Dbv0037AssociationMaxTresMinutesPer")


@_attrs_define
class Dbv0037AssociationMaxTresMinutesPer:
    """Max TRES minutes per settings

    Attributes:
        job (list[Dbv0037TresListItem] | Unset): TRES list of attributes
    """

    job: list[Dbv0037TresListItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        job: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.job, Unset):
            job = []
            for componentsschemasdbv0_0_37_tres_list_item_data in self.job:
                componentsschemasdbv0_0_37_tres_list_item = componentsschemasdbv0_0_37_tres_list_item_data.to_dict()
                job.append(componentsschemasdbv0_0_37_tres_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if job is not UNSET:
            field_dict["job"] = job

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dbv_0037_tres_list_item import Dbv0037TresListItem

        d = dict(src_dict)
        _job = d.pop("job", UNSET)
        job: list[Dbv0037TresListItem] | Unset = UNSET
        if _job is not UNSET:
            job = []
            for componentsschemasdbv0_0_37_tres_list_item_data in _job:
                componentsschemasdbv0_0_37_tres_list_item = Dbv0037TresListItem.from_dict(
                    componentsschemasdbv0_0_37_tres_list_item_data
                )

                job.append(componentsschemasdbv0_0_37_tres_list_item)

        dbv_0037_association_max_tres_minutes_per = cls(
            job=job,
        )

        dbv_0037_association_max_tres_minutes_per.additional_properties = d
        return dbv_0037_association_max_tres_minutes_per

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
