from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v0043_tres import V0043Tres


T = TypeVar("T", bound="V0043StepTresConsumed")


@_attrs_define
class V0043StepTresConsumed:
    """
    Attributes:
        max_ (list[V0043Tres] | Unset):
        min_ (list[V0043Tres] | Unset):
        average (list[V0043Tres] | Unset):
        total (list[V0043Tres] | Unset):
    """

    max_: list[V0043Tres] | Unset = UNSET
    min_: list[V0043Tres] | Unset = UNSET
    average: list[V0043Tres] | Unset = UNSET
    total: list[V0043Tres] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        max_: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.max_, Unset):
            max_ = []
            for componentsschemasv0_0_43_step_tres_usage_max_item_data in self.max_:
                componentsschemasv0_0_43_step_tres_usage_max_item = (
                    componentsschemasv0_0_43_step_tres_usage_max_item_data.to_dict()
                )
                max_.append(componentsschemasv0_0_43_step_tres_usage_max_item)

        min_: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.min_, Unset):
            min_ = []
            for componentsschemasv0_0_43_step_tres_usage_min_item_data in self.min_:
                componentsschemasv0_0_43_step_tres_usage_min_item = (
                    componentsschemasv0_0_43_step_tres_usage_min_item_data.to_dict()
                )
                min_.append(componentsschemasv0_0_43_step_tres_usage_min_item)

        average: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.average, Unset):
            average = []
            for componentsschemasv0_0_43_tres_list_item_data in self.average:
                componentsschemasv0_0_43_tres_list_item = componentsschemasv0_0_43_tres_list_item_data.to_dict()
                average.append(componentsschemasv0_0_43_tres_list_item)

        total: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.total, Unset):
            total = []
            for componentsschemasv0_0_43_tres_list_item_data in self.total:
                componentsschemasv0_0_43_tres_list_item = componentsschemasv0_0_43_tres_list_item_data.to_dict()
                total.append(componentsschemasv0_0_43_tres_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if max_ is not UNSET:
            field_dict["max"] = max_
        if min_ is not UNSET:
            field_dict["min"] = min_
        if average is not UNSET:
            field_dict["average"] = average
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v0043_tres import V0043Tres

        d = dict(src_dict)
        _max_ = d.pop("max", UNSET)
        max_: list[V0043Tres] | Unset = UNSET
        if _max_ is not UNSET:
            max_ = []
            for componentsschemasv0_0_43_step_tres_usage_max_item_data in _max_:
                componentsschemasv0_0_43_step_tres_usage_max_item = V0043Tres.from_dict(
                    componentsschemasv0_0_43_step_tres_usage_max_item_data
                )

                max_.append(componentsschemasv0_0_43_step_tres_usage_max_item)

        _min_ = d.pop("min", UNSET)
        min_: list[V0043Tres] | Unset = UNSET
        if _min_ is not UNSET:
            min_ = []
            for componentsschemasv0_0_43_step_tres_usage_min_item_data in _min_:
                componentsschemasv0_0_43_step_tres_usage_min_item = V0043Tres.from_dict(
                    componentsschemasv0_0_43_step_tres_usage_min_item_data
                )

                min_.append(componentsschemasv0_0_43_step_tres_usage_min_item)

        _average = d.pop("average", UNSET)
        average: list[V0043Tres] | Unset = UNSET
        if _average is not UNSET:
            average = []
            for componentsschemasv0_0_43_tres_list_item_data in _average:
                componentsschemasv0_0_43_tres_list_item = V0043Tres.from_dict(
                    componentsschemasv0_0_43_tres_list_item_data
                )

                average.append(componentsschemasv0_0_43_tres_list_item)

        _total = d.pop("total", UNSET)
        total: list[V0043Tres] | Unset = UNSET
        if _total is not UNSET:
            total = []
            for componentsschemasv0_0_43_tres_list_item_data in _total:
                componentsschemasv0_0_43_tres_list_item = V0043Tres.from_dict(
                    componentsschemasv0_0_43_tres_list_item_data
                )

                total.append(componentsschemasv0_0_43_tres_list_item)

        v0043_step_tres_consumed = cls(
            max_=max_,
            min_=min_,
            average=average,
            total=total,
        )

        v0043_step_tres_consumed.additional_properties = d
        return v0043_step_tres_consumed

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
