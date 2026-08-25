from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.v0039_account_flags_item import V0039AccountFlagsItem
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v0039_assoc_short import V0039AssocShort
    from ..models.v0039_coord import V0039Coord


T = TypeVar("T", bound="V0039Account")


@_attrs_define
class V0039Account:
    """
    Attributes:
        description (str):
        name (str):
        organization (str):
        associations (list[V0039AssocShort] | Unset):
        coordinators (list[V0039Coord] | Unset):
        flags (list[V0039AccountFlagsItem] | Unset):
    """

    description: str
    name: str
    organization: str
    associations: list[V0039AssocShort] | Unset = UNSET
    coordinators: list[V0039Coord] | Unset = UNSET
    flags: list[V0039AccountFlagsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        name = self.name

        organization = self.organization

        associations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.associations, Unset):
            associations = []
            for componentsschemasv0_0_39_assoc_short_list_item_data in self.associations:
                componentsschemasv0_0_39_assoc_short_list_item = (
                    componentsschemasv0_0_39_assoc_short_list_item_data.to_dict()
                )
                associations.append(componentsschemasv0_0_39_assoc_short_list_item)

        coordinators: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.coordinators, Unset):
            coordinators = []
            for componentsschemasv0_0_39_coord_list_item_data in self.coordinators:
                componentsschemasv0_0_39_coord_list_item = componentsschemasv0_0_39_coord_list_item_data.to_dict()
                coordinators.append(componentsschemasv0_0_39_coord_list_item)

        flags: list[str] | Unset = UNSET
        if not isinstance(self.flags, Unset):
            flags = []
            for flags_item_data in self.flags:
                flags_item = flags_item_data.value
                flags.append(flags_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
                "name": name,
                "organization": organization,
            }
        )
        if associations is not UNSET:
            field_dict["associations"] = associations
        if coordinators is not UNSET:
            field_dict["coordinators"] = coordinators
        if flags is not UNSET:
            field_dict["flags"] = flags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v0039_assoc_short import V0039AssocShort
        from ..models.v0039_coord import V0039Coord

        d = dict(src_dict)
        description = d.pop("description")

        name = d.pop("name")

        organization = d.pop("organization")

        _associations = d.pop("associations", UNSET)
        associations: list[V0039AssocShort] | Unset = UNSET
        if _associations is not UNSET:
            associations = []
            for componentsschemasv0_0_39_assoc_short_list_item_data in _associations:
                componentsschemasv0_0_39_assoc_short_list_item = V0039AssocShort.from_dict(
                    componentsschemasv0_0_39_assoc_short_list_item_data
                )

                associations.append(componentsschemasv0_0_39_assoc_short_list_item)

        _coordinators = d.pop("coordinators", UNSET)
        coordinators: list[V0039Coord] | Unset = UNSET
        if _coordinators is not UNSET:
            coordinators = []
            for componentsschemasv0_0_39_coord_list_item_data in _coordinators:
                componentsschemasv0_0_39_coord_list_item = V0039Coord.from_dict(
                    componentsschemasv0_0_39_coord_list_item_data
                )

                coordinators.append(componentsschemasv0_0_39_coord_list_item)

        _flags = d.pop("flags", UNSET)
        flags: list[V0039AccountFlagsItem] | Unset = UNSET
        if _flags is not UNSET:
            flags = []
            for flags_item_data in _flags:
                flags_item = V0039AccountFlagsItem(flags_item_data)

                flags.append(flags_item)

        v0039_account = cls(
            description=description,
            name=name,
            organization=organization,
            associations=associations,
            coordinators=coordinators,
            flags=flags,
        )

        v0039_account.additional_properties = d
        return v0039_account

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
