from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dbv_0039_error import Dbv0039Error
    from ..models.dbv_0039_meta import Dbv0039Meta
    from ..models.dbv_0039_warning import Dbv0039Warning
    from ..models.v0039_cluster_rec import V0039ClusterRec


T = TypeVar("T", bound="Dbv0039ClustersInfo")


@_attrs_define
class Dbv0039ClustersInfo:
    """
    Attributes:
        meta (Dbv0039Meta | Unset):
        errors (list[Dbv0039Error] | Unset): Slurm errors
        warnings (list[Dbv0039Warning] | Unset): Slurm warnings
        clusters (list[V0039ClusterRec] | Unset):
    """

    meta: Dbv0039Meta | Unset = UNSET
    errors: list[Dbv0039Error] | Unset = UNSET
    warnings: list[Dbv0039Warning] | Unset = UNSET
    clusters: list[V0039ClusterRec] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        meta: dict[str, Any] | Unset = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        errors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for componentsschemasdbv0_0_39_errors_item_data in self.errors:
                componentsschemasdbv0_0_39_errors_item = componentsschemasdbv0_0_39_errors_item_data.to_dict()
                errors.append(componentsschemasdbv0_0_39_errors_item)

        warnings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = []
            for componentsschemasdbv0_0_39_warnings_item_data in self.warnings:
                componentsschemasdbv0_0_39_warnings_item = componentsschemasdbv0_0_39_warnings_item_data.to_dict()
                warnings.append(componentsschemasdbv0_0_39_warnings_item)

        clusters: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.clusters, Unset):
            clusters = []
            for componentsschemasv0_0_39_cluster_rec_list_item_data in self.clusters:
                componentsschemasv0_0_39_cluster_rec_list_item = (
                    componentsschemasv0_0_39_cluster_rec_list_item_data.to_dict()
                )
                clusters.append(componentsschemasv0_0_39_cluster_rec_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if meta is not UNSET:
            field_dict["meta"] = meta
        if errors is not UNSET:
            field_dict["errors"] = errors
        if warnings is not UNSET:
            field_dict["warnings"] = warnings
        if clusters is not UNSET:
            field_dict["clusters"] = clusters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dbv_0039_error import Dbv0039Error
        from ..models.dbv_0039_meta import Dbv0039Meta
        from ..models.dbv_0039_warning import Dbv0039Warning
        from ..models.v0039_cluster_rec import V0039ClusterRec

        d = dict(src_dict)
        _meta = d.pop("meta", UNSET)
        meta: Dbv0039Meta | Unset
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = Dbv0039Meta.from_dict(_meta)

        _errors = d.pop("errors", UNSET)
        errors: list[Dbv0039Error] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for componentsschemasdbv0_0_39_errors_item_data in _errors:
                componentsschemasdbv0_0_39_errors_item = Dbv0039Error.from_dict(
                    componentsschemasdbv0_0_39_errors_item_data
                )

                errors.append(componentsschemasdbv0_0_39_errors_item)

        _warnings = d.pop("warnings", UNSET)
        warnings: list[Dbv0039Warning] | Unset = UNSET
        if _warnings is not UNSET:
            warnings = []
            for componentsschemasdbv0_0_39_warnings_item_data in _warnings:
                componentsschemasdbv0_0_39_warnings_item = Dbv0039Warning.from_dict(
                    componentsschemasdbv0_0_39_warnings_item_data
                )

                warnings.append(componentsschemasdbv0_0_39_warnings_item)

        _clusters = d.pop("clusters", UNSET)
        clusters: list[V0039ClusterRec] | Unset = UNSET
        if _clusters is not UNSET:
            clusters = []
            for componentsschemasv0_0_39_cluster_rec_list_item_data in _clusters:
                componentsschemasv0_0_39_cluster_rec_list_item = V0039ClusterRec.from_dict(
                    componentsschemasv0_0_39_cluster_rec_list_item_data
                )

                clusters.append(componentsschemasv0_0_39_cluster_rec_list_item)

        dbv_0039_clusters_info = cls(
            meta=meta,
            errors=errors,
            warnings=warnings,
            clusters=clusters,
        )

        dbv_0039_clusters_info.additional_properties = d
        return dbv_0039_clusters_info

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
