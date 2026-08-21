from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v0041_openapi_clusters_resp_clusters_item_associations_root import (
        V0041OpenapiClustersRespClustersItemAssociationsRoot,
    )


T = TypeVar("T", bound="V0041OpenapiClustersRespClustersItemAssociations")


@_attrs_define
class V0041OpenapiClustersRespClustersItemAssociations:
    """
    Attributes:
        root (V0041OpenapiClustersRespClustersItemAssociationsRoot | Unset): Root association information
    """

    root: V0041OpenapiClustersRespClustersItemAssociationsRoot | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        root: dict[str, Any] | Unset = UNSET
        if not isinstance(self.root, Unset):
            root = self.root.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if root is not UNSET:
            field_dict["root"] = root

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v0041_openapi_clusters_resp_clusters_item_associations_root import (
            V0041OpenapiClustersRespClustersItemAssociationsRoot,
        )

        d = dict(src_dict)
        _root = d.pop("root", UNSET)
        root: V0041OpenapiClustersRespClustersItemAssociationsRoot | Unset
        if isinstance(_root, Unset):
            root = UNSET
        else:
            root = V0041OpenapiClustersRespClustersItemAssociationsRoot.from_dict(_root)

        v0041_openapi_clusters_resp_clusters_item_associations = cls(
            root=root,
        )

        v0041_openapi_clusters_resp_clusters_item_associations.additional_properties = d
        return v0041_openapi_clusters_resp_clusters_item_associations

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
