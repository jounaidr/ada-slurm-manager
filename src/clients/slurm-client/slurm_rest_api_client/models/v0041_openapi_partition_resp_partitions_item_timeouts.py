from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v0041_openapi_partition_resp_partitions_item_timeouts_resume import (
        V0041OpenapiPartitionRespPartitionsItemTimeoutsResume,
    )
    from ..models.v0041_openapi_partition_resp_partitions_item_timeouts_suspend import (
        V0041OpenapiPartitionRespPartitionsItemTimeoutsSuspend,
    )


T = TypeVar("T", bound="V0041OpenapiPartitionRespPartitionsItemTimeouts")


@_attrs_define
class V0041OpenapiPartitionRespPartitionsItemTimeouts:
    """
    Attributes:
        resume (V0041OpenapiPartitionRespPartitionsItemTimeoutsResume | Unset): ResumeTimeout (GLOBAL if both set and
            infinite are false)
        suspend (V0041OpenapiPartitionRespPartitionsItemTimeoutsSuspend | Unset): SuspendTimeout (GLOBAL if both set and
            infinite are false)
    """

    resume: V0041OpenapiPartitionRespPartitionsItemTimeoutsResume | Unset = UNSET
    suspend: V0041OpenapiPartitionRespPartitionsItemTimeoutsSuspend | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resume: dict[str, Any] | Unset = UNSET
        if not isinstance(self.resume, Unset):
            resume = self.resume.to_dict()

        suspend: dict[str, Any] | Unset = UNSET
        if not isinstance(self.suspend, Unset):
            suspend = self.suspend.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if resume is not UNSET:
            field_dict["resume"] = resume
        if suspend is not UNSET:
            field_dict["suspend"] = suspend

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v0041_openapi_partition_resp_partitions_item_timeouts_resume import (
            V0041OpenapiPartitionRespPartitionsItemTimeoutsResume,
        )
        from ..models.v0041_openapi_partition_resp_partitions_item_timeouts_suspend import (
            V0041OpenapiPartitionRespPartitionsItemTimeoutsSuspend,
        )

        d = dict(src_dict)
        _resume = d.pop("resume", UNSET)
        resume: V0041OpenapiPartitionRespPartitionsItemTimeoutsResume | Unset
        if isinstance(_resume, Unset):
            resume = UNSET
        else:
            resume = V0041OpenapiPartitionRespPartitionsItemTimeoutsResume.from_dict(_resume)

        _suspend = d.pop("suspend", UNSET)
        suspend: V0041OpenapiPartitionRespPartitionsItemTimeoutsSuspend | Unset
        if isinstance(_suspend, Unset):
            suspend = UNSET
        else:
            suspend = V0041OpenapiPartitionRespPartitionsItemTimeoutsSuspend.from_dict(_suspend)

        v0041_openapi_partition_resp_partitions_item_timeouts = cls(
            resume=resume,
            suspend=suspend,
        )

        v0041_openapi_partition_resp_partitions_item_timeouts.additional_properties = d
        return v0041_openapi_partition_resp_partitions_item_timeouts

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
