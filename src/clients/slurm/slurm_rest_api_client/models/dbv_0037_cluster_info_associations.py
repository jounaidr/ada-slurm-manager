from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dbv_0037_association_short_info import Dbv0037AssociationShortInfo


T = TypeVar("T", bound="Dbv0037ClusterInfoAssociations")


@_attrs_define
class Dbv0037ClusterInfoAssociations:
    """Information about associations

    Attributes:
        root (Dbv0037AssociationShortInfo | Unset):
    """

    root: Dbv0037AssociationShortInfo | Unset = UNSET
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
        from ..models.dbv_0037_association_short_info import Dbv0037AssociationShortInfo

        d = dict(src_dict)
        _root = d.pop("root", UNSET)
        root: Dbv0037AssociationShortInfo | Unset
        if isinstance(_root, Unset):
            root = UNSET
        else:
            root = Dbv0037AssociationShortInfo.from_dict(_root)

        dbv_0037_cluster_info_associations = cls(
            root=root,
        )

        dbv_0037_cluster_info_associations.additional_properties = d
        return dbv_0037_cluster_info_associations

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
