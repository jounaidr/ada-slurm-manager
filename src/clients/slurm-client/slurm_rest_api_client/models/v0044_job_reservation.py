from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="V0044JobReservation")


@_attrs_define
class V0044JobReservation:
    """
    Attributes:
        id (int | Unset): Unique identifier of requested reservation
        name (str | Unset): Name of reservation to use
        requested (str | Unset): Comma-separated list of requested reservation names
    """

    id: int | Unset = UNSET
    name: str | Unset = UNSET
    requested: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        requested = self.requested

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if requested is not UNSET:
            field_dict["requested"] = requested

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        requested = d.pop("requested", UNSET)

        v0044_job_reservation = cls(
            id=id,
            name=name,
            requested=requested,
        )

        v0044_job_reservation.additional_properties = d
        return v0044_job_reservation

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
