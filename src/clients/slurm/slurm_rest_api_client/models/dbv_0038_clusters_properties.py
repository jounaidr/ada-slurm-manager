from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dbv_0038_cluster_info import Dbv0038ClusterInfo


T = TypeVar("T", bound="Dbv0038ClustersProperties")


@_attrs_define
class Dbv0038ClustersProperties:
    """
    Attributes:
        clusters (Dbv0038ClusterInfo | Unset):
    """

    clusters: Dbv0038ClusterInfo | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        clusters: dict[str, Any] | Unset = UNSET
        if not isinstance(self.clusters, Unset):
            clusters = self.clusters.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if clusters is not UNSET:
            field_dict["clusters"] = clusters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dbv_0038_cluster_info import Dbv0038ClusterInfo

        d = dict(src_dict)
        _clusters = d.pop("clusters", UNSET)
        clusters: Dbv0038ClusterInfo | Unset
        if isinstance(_clusters, Unset):
            clusters = UNSET
        else:
            clusters = Dbv0038ClusterInfo.from_dict(_clusters)

        dbv_0038_clusters_properties = cls(
            clusters=clusters,
        )

        dbv_0038_clusters_properties.additional_properties = d
        return dbv_0038_clusters_properties

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
