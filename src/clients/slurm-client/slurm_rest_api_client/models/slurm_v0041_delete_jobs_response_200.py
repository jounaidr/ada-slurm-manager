from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.slurm_v0041_delete_jobs_response_200_errors_item import SlurmV0041DeleteJobsResponse200ErrorsItem
    from ..models.slurm_v0041_delete_jobs_response_200_meta import SlurmV0041DeleteJobsResponse200Meta
    from ..models.slurm_v0041_delete_jobs_response_200_status_item import SlurmV0041DeleteJobsResponse200StatusItem
    from ..models.slurm_v0041_delete_jobs_response_200_warnings_item import SlurmV0041DeleteJobsResponse200WarningsItem


T = TypeVar("T", bound="SlurmV0041DeleteJobsResponse200")


@_attrs_define
class SlurmV0041DeleteJobsResponse200:
    """
    Attributes:
        status (list[SlurmV0041DeleteJobsResponse200StatusItem]): resultant status of signal request
        meta (SlurmV0041DeleteJobsResponse200Meta | Unset): Slurm meta values
        errors (list[SlurmV0041DeleteJobsResponse200ErrorsItem] | Unset): Query errors
        warnings (list[SlurmV0041DeleteJobsResponse200WarningsItem] | Unset): Query warnings
    """

    status: list[SlurmV0041DeleteJobsResponse200StatusItem]
    meta: SlurmV0041DeleteJobsResponse200Meta | Unset = UNSET
    errors: list[SlurmV0041DeleteJobsResponse200ErrorsItem] | Unset = UNSET
    warnings: list[SlurmV0041DeleteJobsResponse200WarningsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = []
        for status_item_data in self.status:
            status_item = status_item_data.to_dict()
            status.append(status_item)

        meta: dict[str, Any] | Unset = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        errors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()
                errors.append(errors_item)

        warnings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = []
            for warnings_item_data in self.warnings:
                warnings_item = warnings_item_data.to_dict()
                warnings.append(warnings_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
            }
        )
        if meta is not UNSET:
            field_dict["meta"] = meta
        if errors is not UNSET:
            field_dict["errors"] = errors
        if warnings is not UNSET:
            field_dict["warnings"] = warnings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.slurm_v0041_delete_jobs_response_200_errors_item import SlurmV0041DeleteJobsResponse200ErrorsItem
        from ..models.slurm_v0041_delete_jobs_response_200_meta import SlurmV0041DeleteJobsResponse200Meta
        from ..models.slurm_v0041_delete_jobs_response_200_status_item import SlurmV0041DeleteJobsResponse200StatusItem
        from ..models.slurm_v0041_delete_jobs_response_200_warnings_item import (
            SlurmV0041DeleteJobsResponse200WarningsItem,
        )

        d = dict(src_dict)
        status = []
        _status = d.pop("status")
        for status_item_data in _status:
            status_item = SlurmV0041DeleteJobsResponse200StatusItem.from_dict(status_item_data)

            status.append(status_item)

        _meta = d.pop("meta", UNSET)
        meta: SlurmV0041DeleteJobsResponse200Meta | Unset
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = SlurmV0041DeleteJobsResponse200Meta.from_dict(_meta)

        _errors = d.pop("errors", UNSET)
        errors: list[SlurmV0041DeleteJobsResponse200ErrorsItem] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = SlurmV0041DeleteJobsResponse200ErrorsItem.from_dict(errors_item_data)

                errors.append(errors_item)

        _warnings = d.pop("warnings", UNSET)
        warnings: list[SlurmV0041DeleteJobsResponse200WarningsItem] | Unset = UNSET
        if _warnings is not UNSET:
            warnings = []
            for warnings_item_data in _warnings:
                warnings_item = SlurmV0041DeleteJobsResponse200WarningsItem.from_dict(warnings_item_data)

                warnings.append(warnings_item)

        slurm_v0041_delete_jobs_response_200 = cls(
            status=status,
            meta=meta,
            errors=errors,
            warnings=warnings,
        )

        slurm_v0041_delete_jobs_response_200.additional_properties = d
        return slurm_v0041_delete_jobs_response_200

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
