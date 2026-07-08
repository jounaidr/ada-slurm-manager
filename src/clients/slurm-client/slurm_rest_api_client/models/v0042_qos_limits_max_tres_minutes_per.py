from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v0042_tres import V0042Tres


T = TypeVar("T", bound="V0042QosLimitsMaxTresMinutesPer")


@_attrs_define
class V0042QosLimitsMaxTresMinutesPer:
    """
    Attributes:
        qos (list[V0042Tres] | Unset):
        job (list[V0042Tres] | Unset):
        account (list[V0042Tres] | Unset):
        user (list[V0042Tres] | Unset):
    """

    qos: list[V0042Tres] | Unset = UNSET
    job: list[V0042Tres] | Unset = UNSET
    account: list[V0042Tres] | Unset = UNSET
    user: list[V0042Tres] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        qos: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.qos, Unset):
            qos = []
            for componentsschemasv0_0_42_tres_list_item_data in self.qos:
                componentsschemasv0_0_42_tres_list_item = componentsschemasv0_0_42_tres_list_item_data.to_dict()
                qos.append(componentsschemasv0_0_42_tres_list_item)

        job: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.job, Unset):
            job = []
            for componentsschemasv0_0_42_tres_list_item_data in self.job:
                componentsschemasv0_0_42_tres_list_item = componentsschemasv0_0_42_tres_list_item_data.to_dict()
                job.append(componentsschemasv0_0_42_tres_list_item)

        account: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.account, Unset):
            account = []
            for componentsschemasv0_0_42_tres_list_item_data in self.account:
                componentsschemasv0_0_42_tres_list_item = componentsschemasv0_0_42_tres_list_item_data.to_dict()
                account.append(componentsschemasv0_0_42_tres_list_item)

        user: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = []
            for componentsschemasv0_0_42_tres_list_item_data in self.user:
                componentsschemasv0_0_42_tres_list_item = componentsschemasv0_0_42_tres_list_item_data.to_dict()
                user.append(componentsschemasv0_0_42_tres_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if qos is not UNSET:
            field_dict["qos"] = qos
        if job is not UNSET:
            field_dict["job"] = job
        if account is not UNSET:
            field_dict["account"] = account
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v0042_tres import V0042Tres

        d = dict(src_dict)
        _qos = d.pop("qos", UNSET)
        qos: list[V0042Tres] | Unset = UNSET
        if _qos is not UNSET:
            qos = []
            for componentsschemasv0_0_42_tres_list_item_data in _qos:
                componentsschemasv0_0_42_tres_list_item = V0042Tres.from_dict(
                    componentsschemasv0_0_42_tres_list_item_data
                )

                qos.append(componentsschemasv0_0_42_tres_list_item)

        _job = d.pop("job", UNSET)
        job: list[V0042Tres] | Unset = UNSET
        if _job is not UNSET:
            job = []
            for componentsschemasv0_0_42_tres_list_item_data in _job:
                componentsschemasv0_0_42_tres_list_item = V0042Tres.from_dict(
                    componentsschemasv0_0_42_tres_list_item_data
                )

                job.append(componentsschemasv0_0_42_tres_list_item)

        _account = d.pop("account", UNSET)
        account: list[V0042Tres] | Unset = UNSET
        if _account is not UNSET:
            account = []
            for componentsschemasv0_0_42_tres_list_item_data in _account:
                componentsschemasv0_0_42_tres_list_item = V0042Tres.from_dict(
                    componentsschemasv0_0_42_tres_list_item_data
                )

                account.append(componentsschemasv0_0_42_tres_list_item)

        _user = d.pop("user", UNSET)
        user: list[V0042Tres] | Unset = UNSET
        if _user is not UNSET:
            user = []
            for componentsschemasv0_0_42_tres_list_item_data in _user:
                componentsschemasv0_0_42_tres_list_item = V0042Tres.from_dict(
                    componentsschemasv0_0_42_tres_list_item_data
                )

                user.append(componentsschemasv0_0_42_tres_list_item)

        v0042_qos_limits_max_tres_minutes_per = cls(
            qos=qos,
            job=job,
            account=account,
            user=user,
        )

        v0042_qos_limits_max_tres_minutes_per.additional_properties = d
        return v0042_qos_limits_max_tres_minutes_per

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
