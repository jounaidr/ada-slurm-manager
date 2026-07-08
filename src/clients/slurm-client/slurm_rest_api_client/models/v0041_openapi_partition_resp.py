from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v0041_openapi_partition_resp_errors_item import V0041OpenapiPartitionRespErrorsItem
    from ..models.v0041_openapi_partition_resp_last_update import V0041OpenapiPartitionRespLastUpdate
    from ..models.v0041_openapi_partition_resp_meta import V0041OpenapiPartitionRespMeta
    from ..models.v0041_openapi_partition_resp_partitions_item import V0041OpenapiPartitionRespPartitionsItem
    from ..models.v0041_openapi_partition_resp_warnings_item import V0041OpenapiPartitionRespWarningsItem


T = TypeVar("T", bound="V0041OpenapiPartitionResp")


@_attrs_define
class V0041OpenapiPartitionResp:
    """
    Attributes:
        partitions (list[V0041OpenapiPartitionRespPartitionsItem]): List of partitions
        last_update (V0041OpenapiPartitionRespLastUpdate): Time of last partition change (UNIX timestamp)
        meta (V0041OpenapiPartitionRespMeta | Unset): Slurm meta values
        errors (list[V0041OpenapiPartitionRespErrorsItem] | Unset): Query errors
        warnings (list[V0041OpenapiPartitionRespWarningsItem] | Unset): Query warnings
    """

    partitions: list[V0041OpenapiPartitionRespPartitionsItem]
    last_update: V0041OpenapiPartitionRespLastUpdate
    meta: V0041OpenapiPartitionRespMeta | Unset = UNSET
    errors: list[V0041OpenapiPartitionRespErrorsItem] | Unset = UNSET
    warnings: list[V0041OpenapiPartitionRespWarningsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        partitions = []
        for partitions_item_data in self.partitions:
            partitions_item = partitions_item_data.to_dict()
            partitions.append(partitions_item)

        last_update = self.last_update.to_dict()

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
                "partitions": partitions,
                "last_update": last_update,
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
        from ..models.v0041_openapi_partition_resp_errors_item import V0041OpenapiPartitionRespErrorsItem
        from ..models.v0041_openapi_partition_resp_last_update import V0041OpenapiPartitionRespLastUpdate
        from ..models.v0041_openapi_partition_resp_meta import V0041OpenapiPartitionRespMeta
        from ..models.v0041_openapi_partition_resp_partitions_item import V0041OpenapiPartitionRespPartitionsItem
        from ..models.v0041_openapi_partition_resp_warnings_item import V0041OpenapiPartitionRespWarningsItem

        d = dict(src_dict)
        partitions = []
        _partitions = d.pop("partitions")
        for partitions_item_data in _partitions:
            partitions_item = V0041OpenapiPartitionRespPartitionsItem.from_dict(partitions_item_data)

            partitions.append(partitions_item)

        last_update = V0041OpenapiPartitionRespLastUpdate.from_dict(d.pop("last_update"))

        _meta = d.pop("meta", UNSET)
        meta: V0041OpenapiPartitionRespMeta | Unset
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = V0041OpenapiPartitionRespMeta.from_dict(_meta)

        _errors = d.pop("errors", UNSET)
        errors: list[V0041OpenapiPartitionRespErrorsItem] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = V0041OpenapiPartitionRespErrorsItem.from_dict(errors_item_data)

                errors.append(errors_item)

        _warnings = d.pop("warnings", UNSET)
        warnings: list[V0041OpenapiPartitionRespWarningsItem] | Unset = UNSET
        if _warnings is not UNSET:
            warnings = []
            for warnings_item_data in _warnings:
                warnings_item = V0041OpenapiPartitionRespWarningsItem.from_dict(warnings_item_data)

                warnings.append(warnings_item)

        v0041_openapi_partition_resp = cls(
            partitions=partitions,
            last_update=last_update,
            meta=meta,
            errors=errors,
            warnings=warnings,
        )

        v0041_openapi_partition_resp.additional_properties = d
        return v0041_openapi_partition_resp

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
