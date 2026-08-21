from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v0041_openapi_slurmdbd_jobs_resp_jobs_item_tres_allocated_item import (
        V0041OpenapiSlurmdbdJobsRespJobsItemTresAllocatedItem,
    )
    from ..models.v0041_openapi_slurmdbd_jobs_resp_jobs_item_tres_requested_item import (
        V0041OpenapiSlurmdbdJobsRespJobsItemTresRequestedItem,
    )


T = TypeVar("T", bound="V0041OpenapiSlurmdbdJobsRespJobsItemTres")


@_attrs_define
class V0041OpenapiSlurmdbdJobsRespJobsItemTres:
    """
    Attributes:
        allocated (list[V0041OpenapiSlurmdbdJobsRespJobsItemTresAllocatedItem] | Unset): Trackable resources allocated
            to the job
        requested (list[V0041OpenapiSlurmdbdJobsRespJobsItemTresRequestedItem] | Unset): Trackable resources requested
            by job
    """

    allocated: list[V0041OpenapiSlurmdbdJobsRespJobsItemTresAllocatedItem] | Unset = UNSET
    requested: list[V0041OpenapiSlurmdbdJobsRespJobsItemTresRequestedItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allocated: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.allocated, Unset):
            allocated = []
            for allocated_item_data in self.allocated:
                allocated_item = allocated_item_data.to_dict()
                allocated.append(allocated_item)

        requested: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.requested, Unset):
            requested = []
            for requested_item_data in self.requested:
                requested_item = requested_item_data.to_dict()
                requested.append(requested_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if allocated is not UNSET:
            field_dict["allocated"] = allocated
        if requested is not UNSET:
            field_dict["requested"] = requested

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v0041_openapi_slurmdbd_jobs_resp_jobs_item_tres_allocated_item import (
            V0041OpenapiSlurmdbdJobsRespJobsItemTresAllocatedItem,
        )
        from ..models.v0041_openapi_slurmdbd_jobs_resp_jobs_item_tres_requested_item import (
            V0041OpenapiSlurmdbdJobsRespJobsItemTresRequestedItem,
        )

        d = dict(src_dict)
        _allocated = d.pop("allocated", UNSET)
        allocated: list[V0041OpenapiSlurmdbdJobsRespJobsItemTresAllocatedItem] | Unset = UNSET
        if _allocated is not UNSET:
            allocated = []
            for allocated_item_data in _allocated:
                allocated_item = V0041OpenapiSlurmdbdJobsRespJobsItemTresAllocatedItem.from_dict(allocated_item_data)

                allocated.append(allocated_item)

        _requested = d.pop("requested", UNSET)
        requested: list[V0041OpenapiSlurmdbdJobsRespJobsItemTresRequestedItem] | Unset = UNSET
        if _requested is not UNSET:
            requested = []
            for requested_item_data in _requested:
                requested_item = V0041OpenapiSlurmdbdJobsRespJobsItemTresRequestedItem.from_dict(requested_item_data)

                requested.append(requested_item)

        v0041_openapi_slurmdbd_jobs_resp_jobs_item_tres = cls(
            allocated=allocated,
            requested=requested,
        )

        v0041_openapi_slurmdbd_jobs_resp_jobs_item_tres.additional_properties = d
        return v0041_openapi_slurmdbd_jobs_resp_jobs_item_tres

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
