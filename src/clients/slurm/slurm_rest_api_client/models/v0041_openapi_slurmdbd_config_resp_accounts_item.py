from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.v0041_openapi_slurmdbd_config_resp_accounts_item_flags_item import (
    V0041OpenapiSlurmdbdConfigRespAccountsItemFlagsItem,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v0041_openapi_slurmdbd_config_resp_accounts_item_associations_item import (
        V0041OpenapiSlurmdbdConfigRespAccountsItemAssociationsItem,
    )
    from ..models.v0041_openapi_slurmdbd_config_resp_accounts_item_coordinators_item import (
        V0041OpenapiSlurmdbdConfigRespAccountsItemCoordinatorsItem,
    )


T = TypeVar("T", bound="V0041OpenapiSlurmdbdConfigRespAccountsItem")


@_attrs_define
class V0041OpenapiSlurmdbdConfigRespAccountsItem:
    """
    Attributes:
        description (str): Arbitrary string describing the account
        name (str): Account name
        organization (str): Organization to which the account belongs
        associations (list[V0041OpenapiSlurmdbdConfigRespAccountsItemAssociationsItem] | Unset): Associations involving
            this account (only populated if requested)
        coordinators (list[V0041OpenapiSlurmdbdConfigRespAccountsItemCoordinatorsItem] | Unset): List of users that are
            a coordinator of this account (only populated if requested)
        flags (list[V0041OpenapiSlurmdbdConfigRespAccountsItemFlagsItem] | Unset): Flags associated with the account
    """

    description: str
    name: str
    organization: str
    associations: list[V0041OpenapiSlurmdbdConfigRespAccountsItemAssociationsItem] | Unset = UNSET
    coordinators: list[V0041OpenapiSlurmdbdConfigRespAccountsItemCoordinatorsItem] | Unset = UNSET
    flags: list[V0041OpenapiSlurmdbdConfigRespAccountsItemFlagsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        name = self.name

        organization = self.organization

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
        from ..models.v0041_openapi_slurmdbd_config_resp_accounts_item_associations_item import (
            V0041OpenapiSlurmdbdConfigRespAccountsItemAssociationsItem,
        )
        from ..models.v0041_openapi_slurmdbd_config_resp_accounts_item_coordinators_item import (
            V0041OpenapiSlurmdbdConfigRespAccountsItemCoordinatorsItem,
        )

        d = dict(src_dict)
        description = d.pop("description")

        name = d.pop("name")

        organization = d.pop("organization")

        _associations = d.pop("associations", UNSET)
        associations: list[V0041OpenapiSlurmdbdConfigRespAccountsItemAssociationsItem] | Unset = UNSET
        if _associations is not UNSET:
            associations = []
            for associations_item_data in _associations:
                associations_item = V0041OpenapiSlurmdbdConfigRespAccountsItemAssociationsItem.from_dict(
                    associations_item_data
                )

                associations.append(associations_item)

        _coordinators = d.pop("coordinators", UNSET)
        coordinators: list[V0041OpenapiSlurmdbdConfigRespAccountsItemCoordinatorsItem] | Unset = UNSET
        if _coordinators is not UNSET:
            coordinators = []
            for coordinators_item_data in _coordinators:
                coordinators_item = V0041OpenapiSlurmdbdConfigRespAccountsItemCoordinatorsItem.from_dict(
                    coordinators_item_data
                )

                coordinators.append(coordinators_item)

        _flags = d.pop("flags", UNSET)
        flags: list[V0041OpenapiSlurmdbdConfigRespAccountsItemFlagsItem] | Unset = UNSET
        if _flags is not UNSET:
            flags = []
            for flags_item_data in _flags:
                flags_item = V0041OpenapiSlurmdbdConfigRespAccountsItemFlagsItem(flags_item_data)

                flags.append(flags_item)

        v0041_openapi_slurmdbd_config_resp_accounts_item = cls(
            description=description,
            name=name,
            organization=organization,
            associations=associations,
            coordinators=coordinators,
            flags=flags,
        )

        v0041_openapi_slurmdbd_config_resp_accounts_item.additional_properties = d
        return v0041_openapi_slurmdbd_config_resp_accounts_item

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
