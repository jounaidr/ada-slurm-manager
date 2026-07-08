from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v0041_openapi_assocs_resp_associations_item_max_tres_group_active_item import (
        V0041OpenapiAssocsRespAssociationsItemMaxTresGroupActiveItem,
    )
    from ..models.v0041_openapi_assocs_resp_associations_item_max_tres_group_minutes_item import (
        V0041OpenapiAssocsRespAssociationsItemMaxTresGroupMinutesItem,
    )


T = TypeVar("T", bound="V0041OpenapiAssocsRespAssociationsItemMaxTresGroup")


@_attrs_define
class V0041OpenapiAssocsRespAssociationsItemMaxTresGroup:
    """
    Attributes:
        minutes (list[V0041OpenapiAssocsRespAssociationsItemMaxTresGroupMinutesItem] | Unset): GrpTRESMins
        active (list[V0041OpenapiAssocsRespAssociationsItemMaxTresGroupActiveItem] | Unset): GrpTRESRunMins
    """

    minutes: list[V0041OpenapiAssocsRespAssociationsItemMaxTresGroupMinutesItem] | Unset = UNSET
    active: list[V0041OpenapiAssocsRespAssociationsItemMaxTresGroupActiveItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        minutes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.minutes, Unset):
            minutes = []
            for minutes_item_data in self.minutes:
                minutes_item = minutes_item_data.to_dict()
                minutes.append(minutes_item)

        active: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.active, Unset):
            active = []
            for active_item_data in self.active:
                active_item = active_item_data.to_dict()
                active.append(active_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if minutes is not UNSET:
            field_dict["minutes"] = minutes
        if active is not UNSET:
            field_dict["active"] = active

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v0041_openapi_assocs_resp_associations_item_max_tres_group_active_item import (
            V0041OpenapiAssocsRespAssociationsItemMaxTresGroupActiveItem,
        )
        from ..models.v0041_openapi_assocs_resp_associations_item_max_tres_group_minutes_item import (
            V0041OpenapiAssocsRespAssociationsItemMaxTresGroupMinutesItem,
        )

        d = dict(src_dict)
        _minutes = d.pop("minutes", UNSET)
        minutes: list[V0041OpenapiAssocsRespAssociationsItemMaxTresGroupMinutesItem] | Unset = UNSET
        if _minutes is not UNSET:
            minutes = []
            for minutes_item_data in _minutes:
                minutes_item = V0041OpenapiAssocsRespAssociationsItemMaxTresGroupMinutesItem.from_dict(
                    minutes_item_data
                )

                minutes.append(minutes_item)

        _active = d.pop("active", UNSET)
        active: list[V0041OpenapiAssocsRespAssociationsItemMaxTresGroupActiveItem] | Unset = UNSET
        if _active is not UNSET:
            active = []
            for active_item_data in _active:
                active_item = V0041OpenapiAssocsRespAssociationsItemMaxTresGroupActiveItem.from_dict(active_item_data)

                active.append(active_item)

        v0041_openapi_assocs_resp_associations_item_max_tres_group = cls(
            minutes=minutes,
            active=active,
        )

        v0041_openapi_assocs_resp_associations_item_max_tres_group.additional_properties = d
        return v0041_openapi_assocs_resp_associations_item_max_tres_group

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
