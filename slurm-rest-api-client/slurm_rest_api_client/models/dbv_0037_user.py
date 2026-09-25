from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dbv_0037_coordinator_info import Dbv0037CoordinatorInfo
    from ..models.dbv_0037_user_associations import Dbv0037UserAssociations
    from ..models.dbv_0037_user_default import Dbv0037UserDefault


T = TypeVar("T", bound="Dbv0037User")


@_attrs_define
class Dbv0037User:
    """User description

    Attributes:
        administrator_level (str | Unset): Description of administrator level
        associations (Dbv0037UserAssociations | Unset): Assigned associations
        coordinators (list[Dbv0037CoordinatorInfo] | Unset): List of assigned coordinators
        default (Dbv0037UserDefault | Unset): Default settings
        name (str | Unset): User name
    """

    administrator_level: str | Unset = UNSET
    associations: Dbv0037UserAssociations | Unset = UNSET
    coordinators: list[Dbv0037CoordinatorInfo] | Unset = UNSET
    default: Dbv0037UserDefault | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        administrator_level = self.administrator_level

        associations: dict[str, Any] | Unset = UNSET
        if not isinstance(self.associations, Unset):
            associations = self.associations.to_dict()

        coordinators: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.coordinators, Unset):
            coordinators = []
            for coordinators_item_data in self.coordinators:
                coordinators_item = coordinators_item_data.to_dict()
                coordinators.append(coordinators_item)

        default: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default, Unset):
            default = self.default.to_dict()

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if administrator_level is not UNSET:
            field_dict["administrator_level"] = administrator_level
        if associations is not UNSET:
            field_dict["associations"] = associations
        if coordinators is not UNSET:
            field_dict["coordinators"] = coordinators
        if default is not UNSET:
            field_dict["default"] = default
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dbv_0037_coordinator_info import Dbv0037CoordinatorInfo
        from ..models.dbv_0037_user_associations import Dbv0037UserAssociations
        from ..models.dbv_0037_user_default import Dbv0037UserDefault

        d = dict(src_dict)
        administrator_level = d.pop("administrator_level", UNSET)

        _associations = d.pop("associations", UNSET)
        associations: Dbv0037UserAssociations | Unset
        if isinstance(_associations, Unset):
            associations = UNSET
        else:
            associations = Dbv0037UserAssociations.from_dict(_associations)

        _coordinators = d.pop("coordinators", UNSET)
        coordinators: list[Dbv0037CoordinatorInfo] | Unset = UNSET
        if _coordinators is not UNSET:
            coordinators = []
            for coordinators_item_data in _coordinators:
                coordinators_item = Dbv0037CoordinatorInfo.from_dict(coordinators_item_data)

                coordinators.append(coordinators_item)

        _default = d.pop("default", UNSET)
        default: Dbv0037UserDefault | Unset
        if isinstance(_default, Unset):
            default = UNSET
        else:
            default = Dbv0037UserDefault.from_dict(_default)

        name = d.pop("name", UNSET)

        dbv_0037_user = cls(
            administrator_level=administrator_level,
            associations=associations,
            coordinators=coordinators,
            default=default,
            name=name,
        )

        dbv_0037_user.additional_properties = d
        return dbv_0037_user

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
