from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.slurmdb_v0041_delete_cluster_response_default_errors_item import (
        SlurmdbV0041DeleteClusterResponseDefaultErrorsItem,
    )
    from ..models.slurmdb_v0041_delete_cluster_response_default_meta import SlurmdbV0041DeleteClusterResponseDefaultMeta
    from ..models.slurmdb_v0041_delete_cluster_response_default_warnings_item import (
        SlurmdbV0041DeleteClusterResponseDefaultWarningsItem,
    )


T = TypeVar("T", bound="SlurmdbV0041DeleteClusterResponseDefault")


@_attrs_define
class SlurmdbV0041DeleteClusterResponseDefault:
    """
    Attributes:
        deleted_clusters (list[str]): deleted_clusters
        meta (SlurmdbV0041DeleteClusterResponseDefaultMeta | Unset): Slurm meta values
        errors (list[SlurmdbV0041DeleteClusterResponseDefaultErrorsItem] | Unset): Query errors
        warnings (list[SlurmdbV0041DeleteClusterResponseDefaultWarningsItem] | Unset): Query warnings
    """

    deleted_clusters: list[str]
    meta: SlurmdbV0041DeleteClusterResponseDefaultMeta | Unset = UNSET
    errors: list[SlurmdbV0041DeleteClusterResponseDefaultErrorsItem] | Unset = UNSET
    warnings: list[SlurmdbV0041DeleteClusterResponseDefaultWarningsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        deleted_clusters = self.deleted_clusters

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
                "deleted_clusters": deleted_clusters,
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
        from ..models.slurmdb_v0041_delete_cluster_response_default_errors_item import (
            SlurmdbV0041DeleteClusterResponseDefaultErrorsItem,
        )
        from ..models.slurmdb_v0041_delete_cluster_response_default_meta import (
            SlurmdbV0041DeleteClusterResponseDefaultMeta,
        )
        from ..models.slurmdb_v0041_delete_cluster_response_default_warnings_item import (
            SlurmdbV0041DeleteClusterResponseDefaultWarningsItem,
        )

        d = dict(src_dict)
        deleted_clusters = cast(list[str], d.pop("deleted_clusters"))

        _meta = d.pop("meta", UNSET)
        meta: SlurmdbV0041DeleteClusterResponseDefaultMeta | Unset
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = SlurmdbV0041DeleteClusterResponseDefaultMeta.from_dict(_meta)

        _errors = d.pop("errors", UNSET)
        errors: list[SlurmdbV0041DeleteClusterResponseDefaultErrorsItem] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = SlurmdbV0041DeleteClusterResponseDefaultErrorsItem.from_dict(errors_item_data)

                errors.append(errors_item)

        _warnings = d.pop("warnings", UNSET)
        warnings: list[SlurmdbV0041DeleteClusterResponseDefaultWarningsItem] | Unset = UNSET
        if _warnings is not UNSET:
            warnings = []
            for warnings_item_data in _warnings:
                warnings_item = SlurmdbV0041DeleteClusterResponseDefaultWarningsItem.from_dict(warnings_item_data)

                warnings.append(warnings_item)

        slurmdb_v0041_delete_cluster_response_default = cls(
            deleted_clusters=deleted_clusters,
            meta=meta,
            errors=errors,
            warnings=warnings,
        )

        slurmdb_v0041_delete_cluster_response_default.additional_properties = d
        return slurmdb_v0041_delete_cluster_response_default

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
