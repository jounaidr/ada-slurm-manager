from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v0038_error import V0038Error
    from ..models.v0038_meta import V0038Meta
    from ..models.v0038_reservation import V0038Reservation


T = TypeVar("T", bound="V0038ReservationsResponse")


@_attrs_define
class V0038ReservationsResponse:
    """
    Attributes:
        meta (V0038Meta | Unset):
        errors (list[V0038Error] | Unset): slurm errors
        reservations (list[V0038Reservation] | Unset): reservation info
    """

    meta: V0038Meta | Unset = UNSET
    errors: list[V0038Error] | Unset = UNSET
    reservations: list[V0038Reservation] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        meta: dict[str, Any] | Unset = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        errors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()
                errors.append(errors_item)

        reservations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.reservations, Unset):
            reservations = []
            for reservations_item_data in self.reservations:
                reservations_item = reservations_item_data.to_dict()
                reservations.append(reservations_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if meta is not UNSET:
            field_dict["meta"] = meta
        if errors is not UNSET:
            field_dict["errors"] = errors
        if reservations is not UNSET:
            field_dict["reservations"] = reservations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v0038_error import V0038Error
        from ..models.v0038_meta import V0038Meta
        from ..models.v0038_reservation import V0038Reservation

        d = dict(src_dict)
        _meta = d.pop("meta", UNSET)
        meta: V0038Meta | Unset
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = V0038Meta.from_dict(_meta)

        _errors = d.pop("errors", UNSET)
        errors: list[V0038Error] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = V0038Error.from_dict(errors_item_data)

                errors.append(errors_item)

        _reservations = d.pop("reservations", UNSET)
        reservations: list[V0038Reservation] | Unset = UNSET
        if _reservations is not UNSET:
            reservations = []
            for reservations_item_data in _reservations:
                reservations_item = V0038Reservation.from_dict(reservations_item_data)

                reservations.append(reservations_item)

        v0038_reservations_response = cls(
            meta=meta,
            errors=errors,
            reservations=reservations,
        )

        v0038_reservations_response.additional_properties = d
        return v0038_reservations_response

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
