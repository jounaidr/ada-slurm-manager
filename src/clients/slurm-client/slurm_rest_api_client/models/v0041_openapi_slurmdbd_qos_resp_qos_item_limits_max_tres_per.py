from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v0041_openapi_slurmdbd_qos_resp_qos_item_limits_max_tres_per_account_item import (
        V0041OpenapiSlurmdbdQosRespQosItemLimitsMaxTresPerAccountItem,
    )
    from ..models.v0041_openapi_slurmdbd_qos_resp_qos_item_limits_max_tres_per_job_item import (
        V0041OpenapiSlurmdbdQosRespQosItemLimitsMaxTresPerJobItem,
    )
    from ..models.v0041_openapi_slurmdbd_qos_resp_qos_item_limits_max_tres_per_node_item import (
        V0041OpenapiSlurmdbdQosRespQosItemLimitsMaxTresPerNodeItem,
    )
    from ..models.v0041_openapi_slurmdbd_qos_resp_qos_item_limits_max_tres_per_user_item import (
        V0041OpenapiSlurmdbdQosRespQosItemLimitsMaxTresPerUserItem,
    )


T = TypeVar("T", bound="V0041OpenapiSlurmdbdQosRespQosItemLimitsMaxTresPer")


@_attrs_define
class V0041OpenapiSlurmdbdQosRespQosItemLimitsMaxTresPer:
    """
    Attributes:
        account (list[V0041OpenapiSlurmdbdQosRespQosItemLimitsMaxTresPerAccountItem] | Unset): MaxTRESPerAccount
        job (list[V0041OpenapiSlurmdbdQosRespQosItemLimitsMaxTresPerJobItem] | Unset): MaxTRESPerJob
        node (list[V0041OpenapiSlurmdbdQosRespQosItemLimitsMaxTresPerNodeItem] | Unset): MaxTRESPerNode
        user (list[V0041OpenapiSlurmdbdQosRespQosItemLimitsMaxTresPerUserItem] | Unset): MaxTRESPerUser
    """

    account: list[V0041OpenapiSlurmdbdQosRespQosItemLimitsMaxTresPerAccountItem] | Unset = UNSET
    job: list[V0041OpenapiSlurmdbdQosRespQosItemLimitsMaxTresPerJobItem] | Unset = UNSET
    node: list[V0041OpenapiSlurmdbdQosRespQosItemLimitsMaxTresPerNodeItem] | Unset = UNSET
    user: list[V0041OpenapiSlurmdbdQosRespQosItemLimitsMaxTresPerUserItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.account, Unset):
            account = []
            for account_item_data in self.account:
                account_item = account_item_data.to_dict()
                account.append(account_item)

        job: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.job, Unset):
            job = []
            for job_item_data in self.job:
                job_item = job_item_data.to_dict()
                job.append(job_item)

        node: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.node, Unset):
            node = []
            for node_item_data in self.node:
                node_item = node_item_data.to_dict()
                node.append(node_item)

        user: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = []
            for user_item_data in self.user:
                user_item = user_item_data.to_dict()
                user.append(user_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account is not UNSET:
            field_dict["account"] = account
        if job is not UNSET:
            field_dict["job"] = job
        if node is not UNSET:
            field_dict["node"] = node
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v0041_openapi_slurmdbd_qos_resp_qos_item_limits_max_tres_per_account_item import (
            V0041OpenapiSlurmdbdQosRespQosItemLimitsMaxTresPerAccountItem,
        )
        from ..models.v0041_openapi_slurmdbd_qos_resp_qos_item_limits_max_tres_per_job_item import (
            V0041OpenapiSlurmdbdQosRespQosItemLimitsMaxTresPerJobItem,
        )
        from ..models.v0041_openapi_slurmdbd_qos_resp_qos_item_limits_max_tres_per_node_item import (
            V0041OpenapiSlurmdbdQosRespQosItemLimitsMaxTresPerNodeItem,
        )
        from ..models.v0041_openapi_slurmdbd_qos_resp_qos_item_limits_max_tres_per_user_item import (
            V0041OpenapiSlurmdbdQosRespQosItemLimitsMaxTresPerUserItem,
        )

        d = dict(src_dict)
        _account = d.pop("account", UNSET)
        account: list[V0041OpenapiSlurmdbdQosRespQosItemLimitsMaxTresPerAccountItem] | Unset = UNSET
        if _account is not UNSET:
            account = []
            for account_item_data in _account:
                account_item = V0041OpenapiSlurmdbdQosRespQosItemLimitsMaxTresPerAccountItem.from_dict(
                    account_item_data
                )

                account.append(account_item)

        _job = d.pop("job", UNSET)
        job: list[V0041OpenapiSlurmdbdQosRespQosItemLimitsMaxTresPerJobItem] | Unset = UNSET
        if _job is not UNSET:
            job = []
            for job_item_data in _job:
                job_item = V0041OpenapiSlurmdbdQosRespQosItemLimitsMaxTresPerJobItem.from_dict(job_item_data)

                job.append(job_item)

        _node = d.pop("node", UNSET)
        node: list[V0041OpenapiSlurmdbdQosRespQosItemLimitsMaxTresPerNodeItem] | Unset = UNSET
        if _node is not UNSET:
            node = []
            for node_item_data in _node:
                node_item = V0041OpenapiSlurmdbdQosRespQosItemLimitsMaxTresPerNodeItem.from_dict(node_item_data)

                node.append(node_item)

        _user = d.pop("user", UNSET)
        user: list[V0041OpenapiSlurmdbdQosRespQosItemLimitsMaxTresPerUserItem] | Unset = UNSET
        if _user is not UNSET:
            user = []
            for user_item_data in _user:
                user_item = V0041OpenapiSlurmdbdQosRespQosItemLimitsMaxTresPerUserItem.from_dict(user_item_data)

                user.append(user_item)

        v0041_openapi_slurmdbd_qos_resp_qos_item_limits_max_tres_per = cls(
            account=account,
            job=job,
            node=node,
            user=user,
        )

        v0041_openapi_slurmdbd_qos_resp_qos_item_limits_max_tres_per.additional_properties = d
        return v0041_openapi_slurmdbd_qos_resp_qos_item_limits_max_tres_per

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
