from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dbv_0037_association_short_info import Dbv0037AssociationShortInfo
    from ..models.dbv_0037_coordinator_info import Dbv0037CoordinatorInfo


T = TypeVar("T", bound="Dbv0037Account")


@_attrs_define
class Dbv0037Account:
    """Account description

    Attributes:
        associations (list[Dbv0037AssociationShortInfo] | Unset): List of assigned associations
        coordinators (list[Dbv0037CoordinatorInfo] | Unset): List of assigned coordinators
        description (str | Unset): Description of account
        name (str | Unset): Name of account
        organization (str | Unset): Assigned organization of account
        flags (list[str] | Unset): List of properties of account
    """

    associations: list[Dbv0037AssociationShortInfo] | Unset = UNSET
    coordinators: list[Dbv0037CoordinatorInfo] | Unset = UNSET
    description: str | Unset = UNSET
    name: str | Unset = UNSET
    organization: str | Unset = UNSET
    flags: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        associations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.associations, Unset):
            associations = []
            for associations_item_data in self.associations:
                associations_item = associations_item_data.to_dict()
                associations.append(associations_item)

        coordinators: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.coordinators, Unset):
            coordinators = []
            for coordinators_item_data in self.coordinators:
                coordinators_item = coordinators_item_data.to_dict()
                coordinators.append(coordinators_item)

        description = self.description

        name = self.name

        organization = self.organization

        flags: list[str] | Unset = UNSET
        if not isinstance(self.flags, Unset):
            flags = self.flags

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if associations is not UNSET:
            field_dict["associations"] = associations
        if coordinators is not UNSET:
            field_dict["coordinators"] = coordinators
        if description is not UNSET:
            field_dict["description"] = description
        if name is not UNSET:
            field_dict["name"] = name
        if organization is not UNSET:
            field_dict["organization"] = organization
        if flags is not UNSET:
            field_dict["flags"] = flags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dbv_0037_association_short_info import Dbv0037AssociationShortInfo
        from ..models.dbv_0037_coordinator_info import Dbv0037CoordinatorInfo

        d = dict(src_dict)
        _associations = d.pop("associations", UNSET)
        associations: list[Dbv0037AssociationShortInfo] | Unset = UNSET
        if _associations is not UNSET:
            associations = []
            for associations_item_data in _associations:
                associations_item = Dbv0037AssociationShortInfo.from_dict(associations_item_data)

                associations.append(associations_item)

        _coordinators = d.pop("coordinators", UNSET)
        coordinators: list[Dbv0037CoordinatorInfo] | Unset = UNSET
        if _coordinators is not UNSET:
            coordinators = []
            for coordinators_item_data in _coordinators:
                coordinators_item = Dbv0037CoordinatorInfo.from_dict(coordinators_item_data)

                coordinators.append(coordinators_item)

        description = d.pop("description", UNSET)

        name = d.pop("name", UNSET)

        organization = d.pop("organization", UNSET)

        flags = cast(list[str], d.pop("flags", UNSET))

        dbv_0037_account = cls(
            associations=associations,
            coordinators=coordinators,
            description=description,
            name=name,
            organization=organization,
            flags=flags,
        )

        dbv_0037_account.additional_properties = d
        return dbv_0037_account

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
