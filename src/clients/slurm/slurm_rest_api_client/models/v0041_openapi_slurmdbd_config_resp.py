from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v0041_openapi_slurmdbd_config_resp_accounts_item import V0041OpenapiSlurmdbdConfigRespAccountsItem
    from ..models.v0041_openapi_slurmdbd_config_resp_associations_item import (
        V0041OpenapiSlurmdbdConfigRespAssociationsItem,
    )
    from ..models.v0041_openapi_slurmdbd_config_resp_clusters_item import V0041OpenapiSlurmdbdConfigRespClustersItem
    from ..models.v0041_openapi_slurmdbd_config_resp_errors_item import V0041OpenapiSlurmdbdConfigRespErrorsItem
    from ..models.v0041_openapi_slurmdbd_config_resp_instances_item import V0041OpenapiSlurmdbdConfigRespInstancesItem
    from ..models.v0041_openapi_slurmdbd_config_resp_meta import V0041OpenapiSlurmdbdConfigRespMeta
    from ..models.v0041_openapi_slurmdbd_config_resp_qos_item import V0041OpenapiSlurmdbdConfigRespQosItem
    from ..models.v0041_openapi_slurmdbd_config_resp_tres_item import V0041OpenapiSlurmdbdConfigRespTresItem
    from ..models.v0041_openapi_slurmdbd_config_resp_users_item import V0041OpenapiSlurmdbdConfigRespUsersItem
    from ..models.v0041_openapi_slurmdbd_config_resp_warnings_item import V0041OpenapiSlurmdbdConfigRespWarningsItem
    from ..models.v0041_openapi_slurmdbd_config_resp_wckeys_item import V0041OpenapiSlurmdbdConfigRespWckeysItem


T = TypeVar("T", bound="V0041OpenapiSlurmdbdConfigResp")


@_attrs_define
class V0041OpenapiSlurmdbdConfigResp:
    """
    Attributes:
        clusters (list[V0041OpenapiSlurmdbdConfigRespClustersItem] | Unset): Clusters
        tres (list[V0041OpenapiSlurmdbdConfigRespTresItem] | Unset): TRES
        accounts (list[V0041OpenapiSlurmdbdConfigRespAccountsItem] | Unset): Accounts
        users (list[V0041OpenapiSlurmdbdConfigRespUsersItem] | Unset): Users
        qos (list[V0041OpenapiSlurmdbdConfigRespQosItem] | Unset): QOS
        wckeys (list[V0041OpenapiSlurmdbdConfigRespWckeysItem] | Unset): WCKeys
        associations (list[V0041OpenapiSlurmdbdConfigRespAssociationsItem] | Unset): Associations
        instances (list[V0041OpenapiSlurmdbdConfigRespInstancesItem] | Unset): Instances
        meta (V0041OpenapiSlurmdbdConfigRespMeta | Unset): Slurm meta values
        errors (list[V0041OpenapiSlurmdbdConfigRespErrorsItem] | Unset): Query errors
        warnings (list[V0041OpenapiSlurmdbdConfigRespWarningsItem] | Unset): Query warnings
    """

    clusters: list[V0041OpenapiSlurmdbdConfigRespClustersItem] | Unset = UNSET
    tres: list[V0041OpenapiSlurmdbdConfigRespTresItem] | Unset = UNSET
    accounts: list[V0041OpenapiSlurmdbdConfigRespAccountsItem] | Unset = UNSET
    users: list[V0041OpenapiSlurmdbdConfigRespUsersItem] | Unset = UNSET
    qos: list[V0041OpenapiSlurmdbdConfigRespQosItem] | Unset = UNSET
    wckeys: list[V0041OpenapiSlurmdbdConfigRespWckeysItem] | Unset = UNSET
    associations: list[V0041OpenapiSlurmdbdConfigRespAssociationsItem] | Unset = UNSET
    instances: list[V0041OpenapiSlurmdbdConfigRespInstancesItem] | Unset = UNSET
    meta: V0041OpenapiSlurmdbdConfigRespMeta | Unset = UNSET
    errors: list[V0041OpenapiSlurmdbdConfigRespErrorsItem] | Unset = UNSET
    warnings: list[V0041OpenapiSlurmdbdConfigRespWarningsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        clusters: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.clusters, Unset):
            clusters = []
            for clusters_item_data in self.clusters:
                clusters_item = clusters_item_data.to_dict()
                clusters.append(clusters_item)

        tres: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tres, Unset):
            tres = []
            for tres_item_data in self.tres:
                tres_item = tres_item_data.to_dict()
                tres.append(tres_item)

        accounts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.accounts, Unset):
            accounts = []
            for accounts_item_data in self.accounts:
                accounts_item = accounts_item_data.to_dict()
                accounts.append(accounts_item)

        users: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.users, Unset):
            users = []
            for users_item_data in self.users:
                users_item = users_item_data.to_dict()
                users.append(users_item)

        qos: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.qos, Unset):
            qos = []
            for qos_item_data in self.qos:
                qos_item = qos_item_data.to_dict()
                qos.append(qos_item)

        wckeys: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.wckeys, Unset):
            wckeys = []
            for wckeys_item_data in self.wckeys:
                wckeys_item = wckeys_item_data.to_dict()
                wckeys.append(wckeys_item)

        associations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.associations, Unset):
            associations = []
            for associations_item_data in self.associations:
                associations_item = associations_item_data.to_dict()
                associations.append(associations_item)

        instances: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.instances, Unset):
            instances = []
            for instances_item_data in self.instances:
                instances_item = instances_item_data.to_dict()
                instances.append(instances_item)

        meta: dict[str, Any] | Unset = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        errors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()
                errors.append(errors_item)

        warnings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = []
            for warnings_item_data in self.warnings:
                warnings_item = warnings_item_data.to_dict()
                warnings.append(warnings_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if clusters is not UNSET:
            field_dict["clusters"] = clusters
        if tres is not UNSET:
            field_dict["tres"] = tres
        if accounts is not UNSET:
            field_dict["accounts"] = accounts
        if users is not UNSET:
            field_dict["users"] = users
        if qos is not UNSET:
            field_dict["qos"] = qos
        if wckeys is not UNSET:
            field_dict["wckeys"] = wckeys
        if associations is not UNSET:
            field_dict["associations"] = associations
        if instances is not UNSET:
            field_dict["instances"] = instances
        if meta is not UNSET:
            field_dict["meta"] = meta
        if errors is not UNSET:
            field_dict["errors"] = errors
        if warnings is not UNSET:
            field_dict["warnings"] = warnings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v0041_openapi_slurmdbd_config_resp_accounts_item import V0041OpenapiSlurmdbdConfigRespAccountsItem
        from ..models.v0041_openapi_slurmdbd_config_resp_associations_item import (
            V0041OpenapiSlurmdbdConfigRespAssociationsItem,
        )
        from ..models.v0041_openapi_slurmdbd_config_resp_clusters_item import V0041OpenapiSlurmdbdConfigRespClustersItem
        from ..models.v0041_openapi_slurmdbd_config_resp_errors_item import V0041OpenapiSlurmdbdConfigRespErrorsItem
        from ..models.v0041_openapi_slurmdbd_config_resp_instances_item import (
            V0041OpenapiSlurmdbdConfigRespInstancesItem,
        )
        from ..models.v0041_openapi_slurmdbd_config_resp_meta import V0041OpenapiSlurmdbdConfigRespMeta
        from ..models.v0041_openapi_slurmdbd_config_resp_qos_item import V0041OpenapiSlurmdbdConfigRespQosItem
        from ..models.v0041_openapi_slurmdbd_config_resp_tres_item import V0041OpenapiSlurmdbdConfigRespTresItem
        from ..models.v0041_openapi_slurmdbd_config_resp_users_item import V0041OpenapiSlurmdbdConfigRespUsersItem
        from ..models.v0041_openapi_slurmdbd_config_resp_warnings_item import V0041OpenapiSlurmdbdConfigRespWarningsItem
        from ..models.v0041_openapi_slurmdbd_config_resp_wckeys_item import V0041OpenapiSlurmdbdConfigRespWckeysItem

        d = dict(src_dict)
        _clusters = d.pop("clusters", UNSET)
        clusters: list[V0041OpenapiSlurmdbdConfigRespClustersItem] | Unset = UNSET
        if _clusters is not UNSET:
            clusters = []
            for clusters_item_data in _clusters:
                clusters_item = V0041OpenapiSlurmdbdConfigRespClustersItem.from_dict(clusters_item_data)

                clusters.append(clusters_item)

        _tres = d.pop("tres", UNSET)
        tres: list[V0041OpenapiSlurmdbdConfigRespTresItem] | Unset = UNSET
        if _tres is not UNSET:
            tres = []
            for tres_item_data in _tres:
                tres_item = V0041OpenapiSlurmdbdConfigRespTresItem.from_dict(tres_item_data)

                tres.append(tres_item)

        _accounts = d.pop("accounts", UNSET)
        accounts: list[V0041OpenapiSlurmdbdConfigRespAccountsItem] | Unset = UNSET
        if _accounts is not UNSET:
            accounts = []
            for accounts_item_data in _accounts:
                accounts_item = V0041OpenapiSlurmdbdConfigRespAccountsItem.from_dict(accounts_item_data)

                accounts.append(accounts_item)

        _users = d.pop("users", UNSET)
        users: list[V0041OpenapiSlurmdbdConfigRespUsersItem] | Unset = UNSET
        if _users is not UNSET:
            users = []
            for users_item_data in _users:
                users_item = V0041OpenapiSlurmdbdConfigRespUsersItem.from_dict(users_item_data)

                users.append(users_item)

        _qos = d.pop("qos", UNSET)
        qos: list[V0041OpenapiSlurmdbdConfigRespQosItem] | Unset = UNSET
        if _qos is not UNSET:
            qos = []
            for qos_item_data in _qos:
                qos_item = V0041OpenapiSlurmdbdConfigRespQosItem.from_dict(qos_item_data)

                qos.append(qos_item)

        _wckeys = d.pop("wckeys", UNSET)
        wckeys: list[V0041OpenapiSlurmdbdConfigRespWckeysItem] | Unset = UNSET
        if _wckeys is not UNSET:
            wckeys = []
            for wckeys_item_data in _wckeys:
                wckeys_item = V0041OpenapiSlurmdbdConfigRespWckeysItem.from_dict(wckeys_item_data)

                wckeys.append(wckeys_item)

        _associations = d.pop("associations", UNSET)
        associations: list[V0041OpenapiSlurmdbdConfigRespAssociationsItem] | Unset = UNSET
        if _associations is not UNSET:
            associations = []
            for associations_item_data in _associations:
                associations_item = V0041OpenapiSlurmdbdConfigRespAssociationsItem.from_dict(associations_item_data)

                associations.append(associations_item)

        _instances = d.pop("instances", UNSET)
        instances: list[V0041OpenapiSlurmdbdConfigRespInstancesItem] | Unset = UNSET
        if _instances is not UNSET:
            instances = []
            for instances_item_data in _instances:
                instances_item = V0041OpenapiSlurmdbdConfigRespInstancesItem.from_dict(instances_item_data)

                instances.append(instances_item)

        _meta = d.pop("meta", UNSET)
        meta: V0041OpenapiSlurmdbdConfigRespMeta | Unset
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = V0041OpenapiSlurmdbdConfigRespMeta.from_dict(_meta)

        _errors = d.pop("errors", UNSET)
        errors: list[V0041OpenapiSlurmdbdConfigRespErrorsItem] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = V0041OpenapiSlurmdbdConfigRespErrorsItem.from_dict(errors_item_data)

                errors.append(errors_item)

        _warnings = d.pop("warnings", UNSET)
        warnings: list[V0041OpenapiSlurmdbdConfigRespWarningsItem] | Unset = UNSET
        if _warnings is not UNSET:
            warnings = []
            for warnings_item_data in _warnings:
                warnings_item = V0041OpenapiSlurmdbdConfigRespWarningsItem.from_dict(warnings_item_data)

                warnings.append(warnings_item)

        v0041_openapi_slurmdbd_config_resp = cls(
            clusters=clusters,
            tres=tres,
            accounts=accounts,
            users=users,
            qos=qos,
            wckeys=wckeys,
            associations=associations,
            instances=instances,
            meta=meta,
            errors=errors,
            warnings=warnings,
        )

        v0041_openapi_slurmdbd_config_resp.additional_properties = d
        return v0041_openapi_slurmdbd_config_resp

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
