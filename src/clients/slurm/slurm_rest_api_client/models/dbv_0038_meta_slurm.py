from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dbv_0038_meta_slurm_version import Dbv0038MetaSlurmVersion


T = TypeVar("T", bound="Dbv0038MetaSlurm")


@_attrs_define
class Dbv0038MetaSlurm:
    """Slurm information

    Attributes:
        version (Dbv0038MetaSlurmVersion | Unset):
        release (str | Unset): version specifier
    """

    version: Dbv0038MetaSlurmVersion | Unset = UNSET
    release: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        version: dict[str, Any] | Unset = UNSET
        if not isinstance(self.version, Unset):
            version = self.version.to_dict()

        release = self.release

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if version is not UNSET:
            field_dict["version"] = version
        if release is not UNSET:
            field_dict["release"] = release

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dbv_0038_meta_slurm_version import Dbv0038MetaSlurmVersion

        d = dict(src_dict)
        _version = d.pop("version", UNSET)
        version: Dbv0038MetaSlurmVersion | Unset
        if isinstance(_version, Unset):
            version = UNSET
        else:
            version = Dbv0038MetaSlurmVersion.from_dict(_version)

        release = d.pop("release", UNSET)

        dbv_0038_meta_slurm = cls(
            version=version,
            release=release,
        )

        dbv_0038_meta_slurm.additional_properties = d
        return dbv_0038_meta_slurm

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
