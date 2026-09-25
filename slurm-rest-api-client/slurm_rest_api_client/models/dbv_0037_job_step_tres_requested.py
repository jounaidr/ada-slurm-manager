from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dbv_0037_tres_list_item import Dbv0037TresListItem


T = TypeVar("T", bound="Dbv0037JobStepTresRequested")


@_attrs_define
class Dbv0037JobStepTresRequested:
    """TRES requested for job

    Attributes:
        average (list[Dbv0037TresListItem] | Unset): TRES list of attributes
        max_ (list[Dbv0037TresListItem] | Unset): TRES list of attributes
        min_ (list[Dbv0037TresListItem] | Unset): TRES list of attributes
        total (list[Dbv0037TresListItem] | Unset): TRES list of attributes
    """

    average: list[Dbv0037TresListItem] | Unset = UNSET
    max_: list[Dbv0037TresListItem] | Unset = UNSET
    min_: list[Dbv0037TresListItem] | Unset = UNSET
    total: list[Dbv0037TresListItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        average: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.average, Unset):
            average = []
            for componentsschemasdbv0_0_37_tres_list_item_data in self.average:
                componentsschemasdbv0_0_37_tres_list_item = componentsschemasdbv0_0_37_tres_list_item_data.to_dict()
                average.append(componentsschemasdbv0_0_37_tres_list_item)

        max_: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.max_, Unset):
            max_ = []
            for componentsschemasdbv0_0_37_tres_list_item_data in self.max_:
                componentsschemasdbv0_0_37_tres_list_item = componentsschemasdbv0_0_37_tres_list_item_data.to_dict()
                max_.append(componentsschemasdbv0_0_37_tres_list_item)

        min_: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.min_, Unset):
            min_ = []
            for componentsschemasdbv0_0_37_tres_list_item_data in self.min_:
                componentsschemasdbv0_0_37_tres_list_item = componentsschemasdbv0_0_37_tres_list_item_data.to_dict()
                min_.append(componentsschemasdbv0_0_37_tres_list_item)

        total: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.total, Unset):
            total = []
            for componentsschemasdbv0_0_37_tres_list_item_data in self.total:
                componentsschemasdbv0_0_37_tres_list_item = componentsschemasdbv0_0_37_tres_list_item_data.to_dict()
                total.append(componentsschemasdbv0_0_37_tres_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if average is not UNSET:
            field_dict["average"] = average
        if max_ is not UNSET:
            field_dict["max"] = max_
        if min_ is not UNSET:
            field_dict["min"] = min_
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dbv_0037_tres_list_item import Dbv0037TresListItem

        d = dict(src_dict)
        _average = d.pop("average", UNSET)
        average: list[Dbv0037TresListItem] | Unset = UNSET
        if _average is not UNSET:
            average = []
            for componentsschemasdbv0_0_37_tres_list_item_data in _average:
                componentsschemasdbv0_0_37_tres_list_item = Dbv0037TresListItem.from_dict(
                    componentsschemasdbv0_0_37_tres_list_item_data
                )

                average.append(componentsschemasdbv0_0_37_tres_list_item)

        _max_ = d.pop("max", UNSET)
        max_: list[Dbv0037TresListItem] | Unset = UNSET
        if _max_ is not UNSET:
            max_ = []
            for componentsschemasdbv0_0_37_tres_list_item_data in _max_:
                componentsschemasdbv0_0_37_tres_list_item = Dbv0037TresListItem.from_dict(
                    componentsschemasdbv0_0_37_tres_list_item_data
                )

                max_.append(componentsschemasdbv0_0_37_tres_list_item)

        _min_ = d.pop("min", UNSET)
        min_: list[Dbv0037TresListItem] | Unset = UNSET
        if _min_ is not UNSET:
            min_ = []
            for componentsschemasdbv0_0_37_tres_list_item_data in _min_:
                componentsschemasdbv0_0_37_tres_list_item = Dbv0037TresListItem.from_dict(
                    componentsschemasdbv0_0_37_tres_list_item_data
                )

                min_.append(componentsschemasdbv0_0_37_tres_list_item)

        _total = d.pop("total", UNSET)
        total: list[Dbv0037TresListItem] | Unset = UNSET
        if _total is not UNSET:
            total = []
            for componentsschemasdbv0_0_37_tres_list_item_data in _total:
                componentsschemasdbv0_0_37_tres_list_item = Dbv0037TresListItem.from_dict(
                    componentsschemasdbv0_0_37_tres_list_item_data
                )

                total.append(componentsschemasdbv0_0_37_tres_list_item)

        dbv_0037_job_step_tres_requested = cls(
            average=average,
            max_=max_,
            min_=min_,
            total=total,
        )

        dbv_0037_job_step_tres_requested.additional_properties = d
        return dbv_0037_job_step_tres_requested

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
