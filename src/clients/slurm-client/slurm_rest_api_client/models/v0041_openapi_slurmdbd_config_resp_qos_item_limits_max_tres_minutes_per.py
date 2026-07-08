from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v0041_openapi_slurmdbd_config_resp_qos_item_limits_max_tres_minutes_per_account_item import (
        V0041OpenapiSlurmdbdConfigRespQosItemLimitsMaxTresMinutesPerAccountItem,
    )
    from ..models.v0041_openapi_slurmdbd_config_resp_qos_item_limits_max_tres_minutes_per_job_item import (
        V0041OpenapiSlurmdbdConfigRespQosItemLimitsMaxTresMinutesPerJobItem,
    )
    from ..models.v0041_openapi_slurmdbd_config_resp_qos_item_limits_max_tres_minutes_per_qos_item import (
        V0041OpenapiSlurmdbdConfigRespQosItemLimitsMaxTresMinutesPerQosItem,
    )
    from ..models.v0041_openapi_slurmdbd_config_resp_qos_item_limits_max_tres_minutes_per_user_item import (
        V0041OpenapiSlurmdbdConfigRespQosItemLimitsMaxTresMinutesPerUserItem,
    )


T = TypeVar("T", bound="V0041OpenapiSlurmdbdConfigRespQosItemLimitsMaxTresMinutesPer")


@_attrs_define
class V0041OpenapiSlurmdbdConfigRespQosItemLimitsMaxTresMinutesPer:
    """
    Attributes:
        qos (list[V0041OpenapiSlurmdbdConfigRespQosItemLimitsMaxTresMinutesPerQosItem] | Unset): GrpTRESRunMins
        job (list[V0041OpenapiSlurmdbdConfigRespQosItemLimitsMaxTresMinutesPerJobItem] | Unset): MaxTRESMinsPerJob
        account (list[V0041OpenapiSlurmdbdConfigRespQosItemLimitsMaxTresMinutesPerAccountItem] | Unset):
            MaxTRESRunMinsPerAccount
        user (list[V0041OpenapiSlurmdbdConfigRespQosItemLimitsMaxTresMinutesPerUserItem] | Unset): MaxTRESRunMinsPerUser
    """

    qos: list[V0041OpenapiSlurmdbdConfigRespQosItemLimitsMaxTresMinutesPerQosItem] | Unset = UNSET
    job: list[V0041OpenapiSlurmdbdConfigRespQosItemLimitsMaxTresMinutesPerJobItem] | Unset = UNSET
    account: list[V0041OpenapiSlurmdbdConfigRespQosItemLimitsMaxTresMinutesPerAccountItem] | Unset = UNSET
    user: list[V0041OpenapiSlurmdbdConfigRespQosItemLimitsMaxTresMinutesPerUserItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        qos: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.qos, Unset):
            qos = []
            for qos_item_data in self.qos:
                qos_item = qos_item_data.to_dict()
                qos.append(qos_item)

        job: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.job, Unset):
            job = []
            for job_item_data in self.job:
                job_item = job_item_data.to_dict()
                job.append(job_item)

        account: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.account, Unset):
            account = []
            for account_item_data in self.account:
                account_item = account_item_data.to_dict()
                account.append(account_item)

        user: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = []
            for user_item_data in self.user:
                user_item = user_item_data.to_dict()
                user.append(user_item)

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
        from ..models.v0041_openapi_slurmdbd_config_resp_qos_item_limits_max_tres_minutes_per_account_item import (
            V0041OpenapiSlurmdbdConfigRespQosItemLimitsMaxTresMinutesPerAccountItem,
        )
        from ..models.v0041_openapi_slurmdbd_config_resp_qos_item_limits_max_tres_minutes_per_job_item import (
            V0041OpenapiSlurmdbdConfigRespQosItemLimitsMaxTresMinutesPerJobItem,
        )
        from ..models.v0041_openapi_slurmdbd_config_resp_qos_item_limits_max_tres_minutes_per_qos_item import (
            V0041OpenapiSlurmdbdConfigRespQosItemLimitsMaxTresMinutesPerQosItem,
        )
        from ..models.v0041_openapi_slurmdbd_config_resp_qos_item_limits_max_tres_minutes_per_user_item import (
            V0041OpenapiSlurmdbdConfigRespQosItemLimitsMaxTresMinutesPerUserItem,
        )

        d = dict(src_dict)
        _qos = d.pop("qos", UNSET)
        qos: list[V0041OpenapiSlurmdbdConfigRespQosItemLimitsMaxTresMinutesPerQosItem] | Unset = UNSET
        if _qos is not UNSET:
            qos = []
            for qos_item_data in _qos:
                qos_item = V0041OpenapiSlurmdbdConfigRespQosItemLimitsMaxTresMinutesPerQosItem.from_dict(qos_item_data)

                qos.append(qos_item)

        _job = d.pop("job", UNSET)
        job: list[V0041OpenapiSlurmdbdConfigRespQosItemLimitsMaxTresMinutesPerJobItem] | Unset = UNSET
        if _job is not UNSET:
            job = []
            for job_item_data in _job:
                job_item = V0041OpenapiSlurmdbdConfigRespQosItemLimitsMaxTresMinutesPerJobItem.from_dict(job_item_data)

                job.append(job_item)

        _account = d.pop("account", UNSET)
        account: list[V0041OpenapiSlurmdbdConfigRespQosItemLimitsMaxTresMinutesPerAccountItem] | Unset = UNSET
        if _account is not UNSET:
            account = []
            for account_item_data in _account:
                account_item = V0041OpenapiSlurmdbdConfigRespQosItemLimitsMaxTresMinutesPerAccountItem.from_dict(
                    account_item_data
                )

                account.append(account_item)

        _user = d.pop("user", UNSET)
        user: list[V0041OpenapiSlurmdbdConfigRespQosItemLimitsMaxTresMinutesPerUserItem] | Unset = UNSET
        if _user is not UNSET:
            user = []
            for user_item_data in _user:
                user_item = V0041OpenapiSlurmdbdConfigRespQosItemLimitsMaxTresMinutesPerUserItem.from_dict(
                    user_item_data
                )

                user.append(user_item)

        v0041_openapi_slurmdbd_config_resp_qos_item_limits_max_tres_minutes_per = cls(
            qos=qos,
            job=job,
            account=account,
            user=user,
        )

        v0041_openapi_slurmdbd_config_resp_qos_item_limits_max_tres_minutes_per.additional_properties = d
        return v0041_openapi_slurmdbd_config_resp_qos_item_limits_max_tres_minutes_per

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
