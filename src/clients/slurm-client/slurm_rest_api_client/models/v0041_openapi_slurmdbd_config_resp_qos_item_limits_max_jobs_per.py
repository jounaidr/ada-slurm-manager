from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v0041_openapi_slurmdbd_config_resp_qos_item_limits_max_jobs_per_account import (
        V0041OpenapiSlurmdbdConfigRespQosItemLimitsMaxJobsPerAccount,
    )
    from ..models.v0041_openapi_slurmdbd_config_resp_qos_item_limits_max_jobs_per_user import (
        V0041OpenapiSlurmdbdConfigRespQosItemLimitsMaxJobsPerUser,
    )


T = TypeVar("T", bound="V0041OpenapiSlurmdbdConfigRespQosItemLimitsMaxJobsPer")


@_attrs_define
class V0041OpenapiSlurmdbdConfigRespQosItemLimitsMaxJobsPer:
    """
    Attributes:
        account (V0041OpenapiSlurmdbdConfigRespQosItemLimitsMaxJobsPerAccount | Unset): MaxSubmitJobsPerAccount
        user (V0041OpenapiSlurmdbdConfigRespQosItemLimitsMaxJobsPerUser | Unset): MaxSubmitJobsPerUser
    """

    account: V0041OpenapiSlurmdbdConfigRespQosItemLimitsMaxJobsPerAccount | Unset = UNSET
    user: V0041OpenapiSlurmdbdConfigRespQosItemLimitsMaxJobsPerUser | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account: dict[str, Any] | Unset = UNSET
        if not isinstance(self.account, Unset):
            account = self.account.to_dict()

        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account is not UNSET:
            field_dict["account"] = account
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v0041_openapi_slurmdbd_config_resp_qos_item_limits_max_jobs_per_account import (
            V0041OpenapiSlurmdbdConfigRespQosItemLimitsMaxJobsPerAccount,
        )
        from ..models.v0041_openapi_slurmdbd_config_resp_qos_item_limits_max_jobs_per_user import (
            V0041OpenapiSlurmdbdConfigRespQosItemLimitsMaxJobsPerUser,
        )

        d = dict(src_dict)
        _account = d.pop("account", UNSET)
        account: V0041OpenapiSlurmdbdConfigRespQosItemLimitsMaxJobsPerAccount | Unset
        if isinstance(_account, Unset):
            account = UNSET
        else:
            account = V0041OpenapiSlurmdbdConfigRespQosItemLimitsMaxJobsPerAccount.from_dict(_account)

        _user = d.pop("user", UNSET)
        user: V0041OpenapiSlurmdbdConfigRespQosItemLimitsMaxJobsPerUser | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = V0041OpenapiSlurmdbdConfigRespQosItemLimitsMaxJobsPerUser.from_dict(_user)

        v0041_openapi_slurmdbd_config_resp_qos_item_limits_max_jobs_per = cls(
            account=account,
            user=user,
        )

        v0041_openapi_slurmdbd_config_resp_qos_item_limits_max_jobs_per.additional_properties = d
        return v0041_openapi_slurmdbd_config_resp_qos_item_limits_max_jobs_per

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
