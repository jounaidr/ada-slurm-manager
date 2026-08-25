from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dbv_0038_association import Dbv0038Association
    from ..models.dbv_0038_clusters_properties import Dbv0038ClustersProperties
    from ..models.dbv_0038_qos import Dbv0038Qos
    from ..models.dbv_0038_tres_list_item import Dbv0038TresListItem
    from ..models.dbv_0038_update_account import Dbv0038UpdateAccount
    from ..models.dbv_0038_user import Dbv0038User
    from ..models.dbv_0038_wckey import Dbv0038Wckey


T = TypeVar("T", bound="Dbv0038SetConfig")


@_attrs_define
class Dbv0038SetConfig:
    """
    Attributes:
        clusters (list[Dbv0038ClustersProperties] | Unset):
        tres (list[list[Dbv0038TresListItem]] | Unset):
        accounts (list[Dbv0038UpdateAccount] | Unset):
        users (list[Dbv0038User] | Unset):
        qos (list[Dbv0038Qos] | Unset):
        wckeys (list[Dbv0038Wckey] | Unset):
        associations (list[Dbv0038Association] | Unset):
    """

    clusters: list[Dbv0038ClustersProperties] | Unset = UNSET
    tres: list[list[Dbv0038TresListItem]] | Unset = UNSET
    accounts: list[Dbv0038UpdateAccount] | Unset = UNSET
    users: list[Dbv0038User] | Unset = UNSET
    qos: list[Dbv0038Qos] | Unset = UNSET
    wckeys: list[Dbv0038Wckey] | Unset = UNSET
    associations: list[Dbv0038Association] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        clusters: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.clusters, Unset):
            clusters = []
            for clusters_item_data in self.clusters:
                clusters_item = clusters_item_data.to_dict()
                clusters.append(clusters_item)

        tres: list[list[dict[str, Any]]] | Unset = UNSET
        if not isinstance(self.tres, Unset):
            tres = []
            for tres_item_data in self.tres:
                tres_item = []
                for componentsschemasdbv0_0_38_tres_list_item_data in tres_item_data:
                    componentsschemasdbv0_0_38_tres_list_item = componentsschemasdbv0_0_38_tres_list_item_data.to_dict()
                    tres_item.append(componentsschemasdbv0_0_38_tres_list_item)

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if clusters is not UNSET:
            field_dict["clusters"] = clusters
        if tres is not UNSET:
            field_dict["TRES"] = tres
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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dbv_0038_association import Dbv0038Association
        from ..models.dbv_0038_clusters_properties import Dbv0038ClustersProperties
        from ..models.dbv_0038_qos import Dbv0038Qos
        from ..models.dbv_0038_tres_list_item import Dbv0038TresListItem
        from ..models.dbv_0038_update_account import Dbv0038UpdateAccount
        from ..models.dbv_0038_user import Dbv0038User
        from ..models.dbv_0038_wckey import Dbv0038Wckey

        d = dict(src_dict)
        _clusters = d.pop("clusters", UNSET)
        clusters: list[Dbv0038ClustersProperties] | Unset = UNSET
        if _clusters is not UNSET:
            clusters = []
            for clusters_item_data in _clusters:
                clusters_item = Dbv0038ClustersProperties.from_dict(clusters_item_data)

                clusters.append(clusters_item)

        _tres = d.pop("TRES", UNSET)
        tres: list[list[Dbv0038TresListItem]] | Unset = UNSET
        if _tres is not UNSET:
            tres = []
            for tres_item_data in _tres:
                tres_item = []
                _tres_item = tres_item_data
                for componentsschemasdbv0_0_38_tres_list_item_data in _tres_item:
                    componentsschemasdbv0_0_38_tres_list_item = Dbv0038TresListItem.from_dict(
                        componentsschemasdbv0_0_38_tres_list_item_data
                    )

                    tres_item.append(componentsschemasdbv0_0_38_tres_list_item)

                tres.append(tres_item)

        _accounts = d.pop("accounts", UNSET)
        accounts: list[Dbv0038UpdateAccount] | Unset = UNSET
        if _accounts is not UNSET:
            accounts = []
            for accounts_item_data in _accounts:
                accounts_item = Dbv0038UpdateAccount.from_dict(accounts_item_data)

                accounts.append(accounts_item)

        _users = d.pop("users", UNSET)
        users: list[Dbv0038User] | Unset = UNSET
        if _users is not UNSET:
            users = []
            for users_item_data in _users:
                users_item = Dbv0038User.from_dict(users_item_data)

                users.append(users_item)

        _qos = d.pop("qos", UNSET)
        qos: list[Dbv0038Qos] | Unset = UNSET
        if _qos is not UNSET:
            qos = []
            for qos_item_data in _qos:
                qos_item = Dbv0038Qos.from_dict(qos_item_data)

                qos.append(qos_item)

        _wckeys = d.pop("wckeys", UNSET)
        wckeys: list[Dbv0038Wckey] | Unset = UNSET
        if _wckeys is not UNSET:
            wckeys = []
            for wckeys_item_data in _wckeys:
                wckeys_item = Dbv0038Wckey.from_dict(wckeys_item_data)

                wckeys.append(wckeys_item)

        _associations = d.pop("associations", UNSET)
        associations: list[Dbv0038Association] | Unset = UNSET
        if _associations is not UNSET:
            associations = []
            for associations_item_data in _associations:
                associations_item = Dbv0038Association.from_dict(associations_item_data)

                associations.append(associations_item)

        dbv_0038_set_config = cls(
            clusters=clusters,
            tres=tres,
            accounts=accounts,
            users=users,
            qos=qos,
            wckeys=wckeys,
            associations=associations,
        )

        dbv_0038_set_config.additional_properties = d
        return dbv_0038_set_config

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
