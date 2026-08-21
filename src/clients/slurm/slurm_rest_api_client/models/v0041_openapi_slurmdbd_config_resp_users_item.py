from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.v0041_openapi_slurmdbd_config_resp_users_item_administrator_level_item import (
    V0041OpenapiSlurmdbdConfigRespUsersItemAdministratorLevelItem,
)
from ..models.v0041_openapi_slurmdbd_config_resp_users_item_flags_item import (
    V0041OpenapiSlurmdbdConfigRespUsersItemFlagsItem,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v0041_openapi_slurmdbd_config_resp_users_item_associations_item import (
        V0041OpenapiSlurmdbdConfigRespUsersItemAssociationsItem,
    )
    from ..models.v0041_openapi_slurmdbd_config_resp_users_item_coordinators_item import (
        V0041OpenapiSlurmdbdConfigRespUsersItemCoordinatorsItem,
    )
    from ..models.v0041_openapi_slurmdbd_config_resp_users_item_default import (
        V0041OpenapiSlurmdbdConfigRespUsersItemDefault,
    )
    from ..models.v0041_openapi_slurmdbd_config_resp_users_item_wckeys_item import (
        V0041OpenapiSlurmdbdConfigRespUsersItemWckeysItem,
    )


T = TypeVar("T", bound="V0041OpenapiSlurmdbdConfigRespUsersItem")


@_attrs_define
class V0041OpenapiSlurmdbdConfigRespUsersItem:
    """
    Attributes:
        name (str): User name
        administrator_level (list[V0041OpenapiSlurmdbdConfigRespUsersItemAdministratorLevelItem] | Unset): AdminLevel
            granted to the user
        associations (list[V0041OpenapiSlurmdbdConfigRespUsersItemAssociationsItem] | Unset): Associations created for
            this user
        coordinators (list[V0041OpenapiSlurmdbdConfigRespUsersItemCoordinatorsItem] | Unset): Accounts this user is a
            coordinator for
        default (V0041OpenapiSlurmdbdConfigRespUsersItemDefault | Unset):
        flags (list[V0041OpenapiSlurmdbdConfigRespUsersItemFlagsItem] | Unset): Flags associated with user
        old_name (str | Unset): Previous user name
        wckeys (list[V0041OpenapiSlurmdbdConfigRespUsersItemWckeysItem] | Unset): List of available WCKeys
    """

    name: str
    administrator_level: list[V0041OpenapiSlurmdbdConfigRespUsersItemAdministratorLevelItem] | Unset = UNSET
    associations: list[V0041OpenapiSlurmdbdConfigRespUsersItemAssociationsItem] | Unset = UNSET
    coordinators: list[V0041OpenapiSlurmdbdConfigRespUsersItemCoordinatorsItem] | Unset = UNSET
    default: V0041OpenapiSlurmdbdConfigRespUsersItemDefault | Unset = UNSET
    flags: list[V0041OpenapiSlurmdbdConfigRespUsersItemFlagsItem] | Unset = UNSET
    old_name: str | Unset = UNSET
    wckeys: list[V0041OpenapiSlurmdbdConfigRespUsersItemWckeysItem] | Unset = UNSET
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
            for associations_item_data in self.associations:
                associations_item = associations_item_data.to_dict()
                associations.append(associations_item)

        coordinators: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.coordinators, Unset):
            coordinators = []
            for coordinators_item_data in self.coordinators:
                coordinators_item = coordinators_item_data.to_dict()
                coordinators.append(coordinators_item)

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
            for wckeys_item_data in self.wckeys:
                wckeys_item = wckeys_item_data.to_dict()
                wckeys.append(wckeys_item)

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
        from ..models.v0041_openapi_slurmdbd_config_resp_users_item_associations_item import (
            V0041OpenapiSlurmdbdConfigRespUsersItemAssociationsItem,
        )
        from ..models.v0041_openapi_slurmdbd_config_resp_users_item_coordinators_item import (
            V0041OpenapiSlurmdbdConfigRespUsersItemCoordinatorsItem,
        )
        from ..models.v0041_openapi_slurmdbd_config_resp_users_item_default import (
            V0041OpenapiSlurmdbdConfigRespUsersItemDefault,
        )
        from ..models.v0041_openapi_slurmdbd_config_resp_users_item_wckeys_item import (
            V0041OpenapiSlurmdbdConfigRespUsersItemWckeysItem,
        )

        d = dict(src_dict)
        name = d.pop("name")

        _administrator_level = d.pop("administrator_level", UNSET)
        administrator_level: list[V0041OpenapiSlurmdbdConfigRespUsersItemAdministratorLevelItem] | Unset = UNSET
        if _administrator_level is not UNSET:
            administrator_level = []
            for administrator_level_item_data in _administrator_level:
                administrator_level_item = V0041OpenapiSlurmdbdConfigRespUsersItemAdministratorLevelItem(
                    administrator_level_item_data
                )

                administrator_level.append(administrator_level_item)

        _associations = d.pop("associations", UNSET)
        associations: list[V0041OpenapiSlurmdbdConfigRespUsersItemAssociationsItem] | Unset = UNSET
        if _associations is not UNSET:
            associations = []
            for associations_item_data in _associations:
                associations_item = V0041OpenapiSlurmdbdConfigRespUsersItemAssociationsItem.from_dict(
                    associations_item_data
                )

                associations.append(associations_item)

        _coordinators = d.pop("coordinators", UNSET)
        coordinators: list[V0041OpenapiSlurmdbdConfigRespUsersItemCoordinatorsItem] | Unset = UNSET
        if _coordinators is not UNSET:
            coordinators = []
            for coordinators_item_data in _coordinators:
                coordinators_item = V0041OpenapiSlurmdbdConfigRespUsersItemCoordinatorsItem.from_dict(
                    coordinators_item_data
                )

                coordinators.append(coordinators_item)

        _default = d.pop("default", UNSET)
        default: V0041OpenapiSlurmdbdConfigRespUsersItemDefault | Unset
        if isinstance(_default, Unset):
            default = UNSET
        else:
            default = V0041OpenapiSlurmdbdConfigRespUsersItemDefault.from_dict(_default)

        _flags = d.pop("flags", UNSET)
        flags: list[V0041OpenapiSlurmdbdConfigRespUsersItemFlagsItem] | Unset = UNSET
        if _flags is not UNSET:
            flags = []
            for flags_item_data in _flags:
                flags_item = V0041OpenapiSlurmdbdConfigRespUsersItemFlagsItem(flags_item_data)

                flags.append(flags_item)

        old_name = d.pop("old_name", UNSET)

        _wckeys = d.pop("wckeys", UNSET)
        wckeys: list[V0041OpenapiSlurmdbdConfigRespUsersItemWckeysItem] | Unset = UNSET
        if _wckeys is not UNSET:
            wckeys = []
            for wckeys_item_data in _wckeys:
                wckeys_item = V0041OpenapiSlurmdbdConfigRespUsersItemWckeysItem.from_dict(wckeys_item_data)

                wckeys.append(wckeys_item)

        v0041_openapi_slurmdbd_config_resp_users_item = cls(
            name=name,
            administrator_level=administrator_level,
            associations=associations,
            coordinators=coordinators,
            default=default,
            flags=flags,
            old_name=old_name,
            wckeys=wckeys,
        )

        v0041_openapi_slurmdbd_config_resp_users_item.additional_properties = d
        return v0041_openapi_slurmdbd_config_resp_users_item

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
