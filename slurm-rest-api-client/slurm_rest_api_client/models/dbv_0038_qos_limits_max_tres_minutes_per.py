from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dbv_0038_tres_list_item import Dbv0038TresListItem


T = TypeVar("T", bound="Dbv0038QosLimitsMaxTresMinutesPer")


@_attrs_define
class Dbv0038QosLimitsMaxTresMinutesPer:
    """Max TRES minutes per settings

    Attributes:
        job (list[Dbv0038TresListItem] | Unset): TRES list of attributes
        account (list[Dbv0038TresListItem] | Unset): TRES list of attributes
        user (list[Dbv0038TresListItem] | Unset): TRES list of attributes
        qos (list[Dbv0038TresListItem] | Unset): TRES list of attributes
    """

    job: list[Dbv0038TresListItem] | Unset = UNSET
    account: list[Dbv0038TresListItem] | Unset = UNSET
    user: list[Dbv0038TresListItem] | Unset = UNSET
    qos: list[Dbv0038TresListItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        job: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.job, Unset):
            job = []
            for componentsschemasdbv0_0_38_tres_list_item_data in self.job:
                componentsschemasdbv0_0_38_tres_list_item = componentsschemasdbv0_0_38_tres_list_item_data.to_dict()
                job.append(componentsschemasdbv0_0_38_tres_list_item)

        account: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.account, Unset):
            account = []
            for componentsschemasdbv0_0_38_tres_list_item_data in self.account:
                componentsschemasdbv0_0_38_tres_list_item = componentsschemasdbv0_0_38_tres_list_item_data.to_dict()
                account.append(componentsschemasdbv0_0_38_tres_list_item)

        user: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = []
            for componentsschemasdbv0_0_38_tres_list_item_data in self.user:
                componentsschemasdbv0_0_38_tres_list_item = componentsschemasdbv0_0_38_tres_list_item_data.to_dict()
                user.append(componentsschemasdbv0_0_38_tres_list_item)

        qos: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.qos, Unset):
            qos = []
            for componentsschemasdbv0_0_38_tres_list_item_data in self.qos:
                componentsschemasdbv0_0_38_tres_list_item = componentsschemasdbv0_0_38_tres_list_item_data.to_dict()
                qos.append(componentsschemasdbv0_0_38_tres_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if job is not UNSET:
            field_dict["job"] = job
        if account is not UNSET:
            field_dict["account"] = account
        if user is not UNSET:
            field_dict["user"] = user
        if qos is not UNSET:
            field_dict["qos"] = qos

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dbv_0038_tres_list_item import Dbv0038TresListItem

        d = dict(src_dict)
        _job = d.pop("job", UNSET)
        job: list[Dbv0038TresListItem] | Unset = UNSET
        if _job is not UNSET:
            job = []
            for componentsschemasdbv0_0_38_tres_list_item_data in _job:
                componentsschemasdbv0_0_38_tres_list_item = Dbv0038TresListItem.from_dict(
                    componentsschemasdbv0_0_38_tres_list_item_data
                )

                job.append(componentsschemasdbv0_0_38_tres_list_item)

        _account = d.pop("account", UNSET)
        account: list[Dbv0038TresListItem] | Unset = UNSET
        if _account is not UNSET:
            account = []
            for componentsschemasdbv0_0_38_tres_list_item_data in _account:
                componentsschemasdbv0_0_38_tres_list_item = Dbv0038TresListItem.from_dict(
                    componentsschemasdbv0_0_38_tres_list_item_data
                )

                account.append(componentsschemasdbv0_0_38_tres_list_item)

        _user = d.pop("user", UNSET)
        user: list[Dbv0038TresListItem] | Unset = UNSET
        if _user is not UNSET:
            user = []
            for componentsschemasdbv0_0_38_tres_list_item_data in _user:
                componentsschemasdbv0_0_38_tres_list_item = Dbv0038TresListItem.from_dict(
                    componentsschemasdbv0_0_38_tres_list_item_data
                )

                user.append(componentsschemasdbv0_0_38_tres_list_item)

        _qos = d.pop("qos", UNSET)
        qos: list[Dbv0038TresListItem] | Unset = UNSET
        if _qos is not UNSET:
            qos = []
            for componentsschemasdbv0_0_38_tres_list_item_data in _qos:
                componentsschemasdbv0_0_38_tres_list_item = Dbv0038TresListItem.from_dict(
                    componentsschemasdbv0_0_38_tres_list_item_data
                )

                qos.append(componentsschemasdbv0_0_38_tres_list_item)

        dbv_0038_qos_limits_max_tres_minutes_per = cls(
            job=job,
            account=account,
            user=user,
            qos=qos,
        )

        dbv_0038_qos_limits_max_tres_minutes_per.additional_properties = d
        return dbv_0038_qos_limits_max_tres_minutes_per

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
