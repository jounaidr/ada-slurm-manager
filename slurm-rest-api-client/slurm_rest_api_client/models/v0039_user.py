from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.v0039_user_administrator_level_item import V0039UserAdministratorLevelItem
from ..models.v0039_user_flags_item import V0039UserFlagsItem
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v0039_assoc_short import V0039AssocShort
    from ..models.v0039_coord import V0039Coord
    from ..models.v0039_user_default import V0039UserDefault
    from ..models.v0039_wckey import V0039Wckey


T = TypeVar("T", bound="V0039User")


@_attrs_define
class V0039User:
    """
    Attributes:
        name (str):
        administrator_level (list[V0039UserAdministratorLevelItem] | Unset):
        associations (list[V0039AssocShort] | Unset):
        coordinators (list[V0039Coord] | Unset):
        default (V0039UserDefault | Unset):
        flags (list[V0039UserFlagsItem] | Unset):
        old_name (str | Unset):
        wckeys (list[V0039Wckey] | Unset):
    """

    name: str
    administrator_level: list[V0039UserAdministratorLevelItem] | Unset = UNSET
    associations: list[V0039AssocShort] | Unset = UNSET
    coordinators: list[V0039Coord] | Unset = UNSET
    default: V0039UserDefault | Unset = UNSET
    flags: list[V0039UserFlagsItem] | Unset = UNSET
    old_name: str | Unset = UNSET
    wckeys: list[V0039Wckey] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        administrator_level: list[str] | Unset = UNSET
        if not isinstance(self.administrator_level, Unset):
            administrator_level = []
            for administrator_level_item_data in self.administrator_level:
                administrator_level_item = administrator_level_item_data.value
                administrator_level.append(administrator_level_item)

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

        default: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default, Unset):
            default = self.default.to_dict()

        flags: list[str] | Unset = UNSET
        if not isinstance(self.flags, Unset):
            flags = []
            for flags_item_data in self.flags:
                flags_item = flags_item_data.value
                flags.append(flags_item)

        old_name = self.old_name

        wckeys: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.wckeys, Unset):
            wckeys = []
            for componentsschemasv0_0_39_wckey_list_item_data in self.wckeys:
                componentsschemasv0_0_39_wckey_list_item = componentsschemasv0_0_39_wckey_list_item_data.to_dict()
                wckeys.append(componentsschemasv0_0_39_wckey_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if administrator_level is not UNSET:
            field_dict["administrator_level"] = administrator_level
        if associations is not UNSET:
            field_dict["associations"] = associations
        if coordinators is not UNSET:
            field_dict["coordinators"] = coordinators
        if default is not UNSET:
            field_dict["default"] = default
        if flags is not UNSET:
            field_dict["flags"] = flags
        if old_name is not UNSET:
            field_dict["old_name"] = old_name
        if wckeys is not UNSET:
            field_dict["wckeys"] = wckeys

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v0039_assoc_short import V0039AssocShort
        from ..models.v0039_coord import V0039Coord
        from ..models.v0039_user_default import V0039UserDefault
        from ..models.v0039_wckey import V0039Wckey

        d = dict(src_dict)
        name = d.pop("name")

        _administrator_level = d.pop("administrator_level", UNSET)
        administrator_level: list[V0039UserAdministratorLevelItem] | Unset = UNSET
        if _administrator_level is not UNSET:
            administrator_level = []
            for administrator_level_item_data in _administrator_level:
                administrator_level_item = V0039UserAdministratorLevelItem(administrator_level_item_data)

                administrator_level.append(administrator_level_item)

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

        _default = d.pop("default", UNSET)
        default: V0039UserDefault | Unset
        if isinstance(_default, Unset):
            default = UNSET
        else:
            default = V0039UserDefault.from_dict(_default)

        _flags = d.pop("flags", UNSET)
        flags: list[V0039UserFlagsItem] | Unset = UNSET
        if _flags is not UNSET:
            flags = []
            for flags_item_data in _flags:
                flags_item = V0039UserFlagsItem(flags_item_data)

                flags.append(flags_item)

        old_name = d.pop("old_name", UNSET)

        _wckeys = d.pop("wckeys", UNSET)
        wckeys: list[V0039Wckey] | Unset = UNSET
        if _wckeys is not UNSET:
            wckeys = []
            for componentsschemasv0_0_39_wckey_list_item_data in _wckeys:
                componentsschemasv0_0_39_wckey_list_item = V0039Wckey.from_dict(
                    componentsschemasv0_0_39_wckey_list_item_data
                )

                wckeys.append(componentsschemasv0_0_39_wckey_list_item)

        v0039_user = cls(
            name=name,
            administrator_level=administrator_level,
            associations=associations,
            coordinators=coordinators,
            default=default,
            flags=flags,
            old_name=old_name,
            wckeys=wckeys,
        )

        v0039_user.additional_properties = d
        return v0039_user

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
