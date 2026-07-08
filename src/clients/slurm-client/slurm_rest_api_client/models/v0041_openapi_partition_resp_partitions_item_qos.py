from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="V0041OpenapiPartitionRespPartitionsItemQos")


@_attrs_define
class V0041OpenapiPartitionRespPartitionsItemQos:
    """
    Attributes:
        allowed (str | Unset): AllowQOS
        deny (str | Unset): DenyQOS
        assigned (str | Unset): QOS
    """

    allowed: str | Unset = UNSET
    deny: str | Unset = UNSET
    assigned: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allowed = self.allowed

        deny = self.deny

        assigned = self.assigned

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if allowed is not UNSET:
            field_dict["allowed"] = allowed
        if deny is not UNSET:
            field_dict["deny"] = deny
        if assigned is not UNSET:
            field_dict["assigned"] = assigned

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        allowed = d.pop("allowed", UNSET)

        deny = d.pop("deny", UNSET)

        assigned = d.pop("assigned", UNSET)

        v0041_openapi_partition_resp_partitions_item_qos = cls(
            allowed=allowed,
            deny=deny,
            assigned=assigned,
        )

        v0041_openapi_partition_resp_partitions_item_qos.additional_properties = d
        return v0041_openapi_partition_resp_partitions_item_qos

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
