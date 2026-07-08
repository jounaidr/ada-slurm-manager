from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v0044_account import V0044Account
    from ..models.v0044_assoc import V0044Assoc
    from ..models.v0044_cluster_rec import V0044ClusterRec
    from ..models.v0044_instance import V0044Instance
    from ..models.v0044_openapi_error import V0044OpenapiError
    from ..models.v0044_openapi_meta import V0044OpenapiMeta
    from ..models.v0044_openapi_warning import V0044OpenapiWarning
    from ..models.v0044_qos import V0044Qos
    from ..models.v0044_tres import V0044Tres
    from ..models.v0044_user import V0044User
    from ..models.v0044_wckey import V0044Wckey


T = TypeVar("T", bound="V0044OpenapiSlurmdbdConfigResp")


@_attrs_define
class V0044OpenapiSlurmdbdConfigResp:
    """
    Attributes:
        clusters (list[V0044ClusterRec] | Unset):
        tres (list[V0044Tres] | Unset):
        accounts (list[V0044Account] | Unset):
        users (list[V0044User] | Unset):
        qos (list[V0044Qos] | Unset):
        wckeys (list[V0044Wckey] | Unset):
        associations (list[V0044Assoc] | Unset):
        instances (list[V0044Instance] | Unset):
        meta (V0044OpenapiMeta | Unset):
        errors (list[V0044OpenapiError] | Unset):
        warnings (list[V0044OpenapiWarning] | Unset):
    """

    clusters: list[V0044ClusterRec] | Unset = UNSET
    tres: list[V0044Tres] | Unset = UNSET
    accounts: list[V0044Account] | Unset = UNSET
    users: list[V0044User] | Unset = UNSET
    qos: list[V0044Qos] | Unset = UNSET
    wckeys: list[V0044Wckey] | Unset = UNSET
    associations: list[V0044Assoc] | Unset = UNSET
    instances: list[V0044Instance] | Unset = UNSET
    meta: V0044OpenapiMeta | Unset = UNSET
    errors: list[V0044OpenapiError] | Unset = UNSET
    warnings: list[V0044OpenapiWarning] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        clusters: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.clusters, Unset):
            clusters = []
            for componentsschemasv0_0_44_cluster_rec_list_item_data in self.clusters:
                componentsschemasv0_0_44_cluster_rec_list_item = (
                    componentsschemasv0_0_44_cluster_rec_list_item_data.to_dict()
                )
                clusters.append(componentsschemasv0_0_44_cluster_rec_list_item)

        tres: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tres, Unset):
            tres = []
            for componentsschemasv0_0_44_tres_list_item_data in self.tres:
                componentsschemasv0_0_44_tres_list_item = componentsschemasv0_0_44_tres_list_item_data.to_dict()
                tres.append(componentsschemasv0_0_44_tres_list_item)

        accounts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.accounts, Unset):
            accounts = []
            for componentsschemasv0_0_44_account_list_item_data in self.accounts:
                componentsschemasv0_0_44_account_list_item = componentsschemasv0_0_44_account_list_item_data.to_dict()
                accounts.append(componentsschemasv0_0_44_account_list_item)

        users: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.users, Unset):
            users = []
            for componentsschemasv0_0_44_user_list_item_data in self.users:
                componentsschemasv0_0_44_user_list_item = componentsschemasv0_0_44_user_list_item_data.to_dict()
                users.append(componentsschemasv0_0_44_user_list_item)

        qos: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.qos, Unset):
            qos = []
            for componentsschemasv0_0_44_qos_list_item_data in self.qos:
                componentsschemasv0_0_44_qos_list_item = componentsschemasv0_0_44_qos_list_item_data.to_dict()
                qos.append(componentsschemasv0_0_44_qos_list_item)

        wckeys: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.wckeys, Unset):
            wckeys = []
            for componentsschemasv0_0_44_wckey_list_item_data in self.wckeys:
                componentsschemasv0_0_44_wckey_list_item = componentsschemasv0_0_44_wckey_list_item_data.to_dict()
                wckeys.append(componentsschemasv0_0_44_wckey_list_item)

        associations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.associations, Unset):
            associations = []
            for componentsschemasv0_0_44_assoc_list_item_data in self.associations:
                componentsschemasv0_0_44_assoc_list_item = componentsschemasv0_0_44_assoc_list_item_data.to_dict()
                associations.append(componentsschemasv0_0_44_assoc_list_item)

        instances: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.instances, Unset):
            instances = []
            for componentsschemasv0_0_44_instance_list_item_data in self.instances:
                componentsschemasv0_0_44_instance_list_item = componentsschemasv0_0_44_instance_list_item_data.to_dict()
                instances.append(componentsschemasv0_0_44_instance_list_item)

        meta: dict[str, Any] | Unset = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        errors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for componentsschemasv0_0_44_openapi_errors_item_data in self.errors:
                componentsschemasv0_0_44_openapi_errors_item = (
                    componentsschemasv0_0_44_openapi_errors_item_data.to_dict()
                )
                errors.append(componentsschemasv0_0_44_openapi_errors_item)

        warnings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = []
            for componentsschemasv0_0_44_openapi_warnings_item_data in self.warnings:
                componentsschemasv0_0_44_openapi_warnings_item = (
                    componentsschemasv0_0_44_openapi_warnings_item_data.to_dict()
                )
                warnings.append(componentsschemasv0_0_44_openapi_warnings_item)

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
        from ..models.v0044_account import V0044Account
        from ..models.v0044_assoc import V0044Assoc
        from ..models.v0044_cluster_rec import V0044ClusterRec
        from ..models.v0044_instance import V0044Instance
        from ..models.v0044_openapi_error import V0044OpenapiError
        from ..models.v0044_openapi_meta import V0044OpenapiMeta
        from ..models.v0044_openapi_warning import V0044OpenapiWarning
        from ..models.v0044_qos import V0044Qos
        from ..models.v0044_tres import V0044Tres
        from ..models.v0044_user import V0044User
        from ..models.v0044_wckey import V0044Wckey

        d = dict(src_dict)
        _clusters = d.pop("clusters", UNSET)
        clusters: list[V0044ClusterRec] | Unset = UNSET
        if _clusters is not UNSET:
            clusters = []
            for componentsschemasv0_0_44_cluster_rec_list_item_data in _clusters:
                componentsschemasv0_0_44_cluster_rec_list_item = V0044ClusterRec.from_dict(
                    componentsschemasv0_0_44_cluster_rec_list_item_data
                )

                clusters.append(componentsschemasv0_0_44_cluster_rec_list_item)

        _tres = d.pop("tres", UNSET)
        tres: list[V0044Tres] | Unset = UNSET
        if _tres is not UNSET:
            tres = []
            for componentsschemasv0_0_44_tres_list_item_data in _tres:
                componentsschemasv0_0_44_tres_list_item = V0044Tres.from_dict(
                    componentsschemasv0_0_44_tres_list_item_data
                )

                tres.append(componentsschemasv0_0_44_tres_list_item)

        _accounts = d.pop("accounts", UNSET)
        accounts: list[V0044Account] | Unset = UNSET
        if _accounts is not UNSET:
            accounts = []
            for componentsschemasv0_0_44_account_list_item_data in _accounts:
                componentsschemasv0_0_44_account_list_item = V0044Account.from_dict(
                    componentsschemasv0_0_44_account_list_item_data
                )

                accounts.append(componentsschemasv0_0_44_account_list_item)

        _users = d.pop("users", UNSET)
        users: list[V0044User] | Unset = UNSET
        if _users is not UNSET:
            users = []
            for componentsschemasv0_0_44_user_list_item_data in _users:
                componentsschemasv0_0_44_user_list_item = V0044User.from_dict(
                    componentsschemasv0_0_44_user_list_item_data
                )

                users.append(componentsschemasv0_0_44_user_list_item)

        _qos = d.pop("qos", UNSET)
        qos: list[V0044Qos] | Unset = UNSET
        if _qos is not UNSET:
            qos = []
            for componentsschemasv0_0_44_qos_list_item_data in _qos:
                componentsschemasv0_0_44_qos_list_item = V0044Qos.from_dict(componentsschemasv0_0_44_qos_list_item_data)

                qos.append(componentsschemasv0_0_44_qos_list_item)

        _wckeys = d.pop("wckeys", UNSET)
        wckeys: list[V0044Wckey] | Unset = UNSET
        if _wckeys is not UNSET:
            wckeys = []
            for componentsschemasv0_0_44_wckey_list_item_data in _wckeys:
                componentsschemasv0_0_44_wckey_list_item = V0044Wckey.from_dict(
                    componentsschemasv0_0_44_wckey_list_item_data
                )

                wckeys.append(componentsschemasv0_0_44_wckey_list_item)

        _associations = d.pop("associations", UNSET)
        associations: list[V0044Assoc] | Unset = UNSET
        if _associations is not UNSET:
            associations = []
            for componentsschemasv0_0_44_assoc_list_item_data in _associations:
                componentsschemasv0_0_44_assoc_list_item = V0044Assoc.from_dict(
                    componentsschemasv0_0_44_assoc_list_item_data
                )

                associations.append(componentsschemasv0_0_44_assoc_list_item)

        _instances = d.pop("instances", UNSET)
        instances: list[V0044Instance] | Unset = UNSET
        if _instances is not UNSET:
            instances = []
            for componentsschemasv0_0_44_instance_list_item_data in _instances:
                componentsschemasv0_0_44_instance_list_item = V0044Instance.from_dict(
                    componentsschemasv0_0_44_instance_list_item_data
                )

                instances.append(componentsschemasv0_0_44_instance_list_item)

        _meta = d.pop("meta", UNSET)
        meta: V0044OpenapiMeta | Unset
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = V0044OpenapiMeta.from_dict(_meta)

        _errors = d.pop("errors", UNSET)
        errors: list[V0044OpenapiError] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for componentsschemasv0_0_44_openapi_errors_item_data in _errors:
                componentsschemasv0_0_44_openapi_errors_item = V0044OpenapiError.from_dict(
                    componentsschemasv0_0_44_openapi_errors_item_data
                )

                errors.append(componentsschemasv0_0_44_openapi_errors_item)

        _warnings = d.pop("warnings", UNSET)
        warnings: list[V0044OpenapiWarning] | Unset = UNSET
        if _warnings is not UNSET:
            warnings = []
            for componentsschemasv0_0_44_openapi_warnings_item_data in _warnings:
                componentsschemasv0_0_44_openapi_warnings_item = V0044OpenapiWarning.from_dict(
                    componentsschemasv0_0_44_openapi_warnings_item_data
                )

                warnings.append(componentsschemasv0_0_44_openapi_warnings_item)

        v0044_openapi_slurmdbd_config_resp = cls(
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

        v0044_openapi_slurmdbd_config_resp.additional_properties = d
        return v0044_openapi_slurmdbd_config_resp

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
