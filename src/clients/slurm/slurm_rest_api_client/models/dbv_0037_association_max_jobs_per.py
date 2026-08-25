from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Dbv0037AssociationMaxJobsPer")


@_attrs_define
class Dbv0037AssociationMaxJobsPer:
    """Max jobs per settings

    Attributes:
        wall_clock (int | Unset): Max wallclock per job
    """

    wall_clock: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        wall_clock = self.wall_clock

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if wall_clock is not UNSET:
            field_dict["wall_clock"] = wall_clock

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        wall_clock = d.pop("wall_clock", UNSET)

        dbv_0037_association_max_jobs_per = cls(
            wall_clock=wall_clock,
        )

        dbv_0037_association_max_jobs_per.additional_properties = d
        return dbv_0037_association_max_jobs_per

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
