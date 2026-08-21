from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SlurmV0041GetDiagResponseDefaultStatisticsPendingRpcsItem")


@_attrs_define
class SlurmV0041GetDiagResponseDefaultStatisticsPendingRpcsItem:
    """Pending RPCs

    Attributes:
        type_id (int): Message type as integer
        message_type (str): Message type as string
        count (int): Number of pending RPCs queued
    """

    type_id: int
    message_type: str
    count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_id = self.type_id

        message_type = self.message_type

        count = self.count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type_id": type_id,
                "message_type": message_type,
                "count": count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_id = d.pop("type_id")

        message_type = d.pop("message_type")

        count = d.pop("count")

        slurm_v0041_get_diag_response_default_statistics_pending_rpcs_item = cls(
            type_id=type_id,
            message_type=message_type,
            count=count,
        )

        slurm_v0041_get_diag_response_default_statistics_pending_rpcs_item.additional_properties = d
        return slurm_v0041_get_diag_response_default_statistics_pending_rpcs_item

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
