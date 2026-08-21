from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.slurm_v0041_get_diag_response_200_statistics_rpcs_by_user_item_average_time import (
        SlurmV0041GetDiagResponse200StatisticsRpcsByUserItemAverageTime,
    )


T = TypeVar("T", bound="SlurmV0041GetDiagResponse200StatisticsRpcsByUserItem")


@_attrs_define
class SlurmV0041GetDiagResponse200StatisticsRpcsByUserItem:
    """RPCs by user

    Attributes:
        user_id (int): User ID (numeric)
        user (str): User name
        count (int): Number of RPCs received
        total_time (int): Total time spent processing RPC in seconds
        average_time (SlurmV0041GetDiagResponse200StatisticsRpcsByUserItemAverageTime): Average time spent processing
            RPC in seconds
    """

    user_id: int
    user: str
    count: int
    total_time: int
    average_time: SlurmV0041GetDiagResponse200StatisticsRpcsByUserItemAverageTime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_id = self.user_id

        user = self.user

        count = self.count

        total_time = self.total_time

        average_time = self.average_time.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user_id": user_id,
                "user": user,
                "count": count,
                "total_time": total_time,
                "average_time": average_time,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.slurm_v0041_get_diag_response_200_statistics_rpcs_by_user_item_average_time import (
            SlurmV0041GetDiagResponse200StatisticsRpcsByUserItemAverageTime,
        )

        d = dict(src_dict)
        user_id = d.pop("user_id")

        user = d.pop("user")

        count = d.pop("count")

        total_time = d.pop("total_time")

        average_time = SlurmV0041GetDiagResponse200StatisticsRpcsByUserItemAverageTime.from_dict(d.pop("average_time"))

        slurm_v0041_get_diag_response_200_statistics_rpcs_by_user_item = cls(
            user_id=user_id,
            user=user,
            count=count,
            total_time=total_time,
            average_time=average_time,
        )

        slurm_v0041_get_diag_response_200_statistics_rpcs_by_user_item.additional_properties = d
        return slurm_v0041_get_diag_response_200_statistics_rpcs_by_user_item

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
