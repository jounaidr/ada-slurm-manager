from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v0038_error import V0038Error
    from ..models.v0038_license import V0038License


T = TypeVar("T", bound="V0038Licenses")


@_attrs_define
class V0038Licenses:
    """
    Attributes:
        errors (list[V0038Error] | Unset): slurm errors
        licenses (list[V0038License] | Unset): licenses info
    """

    errors: list[V0038Error] | Unset = UNSET
    licenses: list[V0038License] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        errors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()
                errors.append(errors_item)

        licenses: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.licenses, Unset):
            licenses = []
            for licenses_item_data in self.licenses:
                licenses_item = licenses_item_data.to_dict()
                licenses.append(licenses_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if errors is not UNSET:
            field_dict["errors"] = errors
        if licenses is not UNSET:
            field_dict["licenses"] = licenses

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v0038_error import V0038Error
        from ..models.v0038_license import V0038License

        d = dict(src_dict)
        _errors = d.pop("errors", UNSET)
        errors: list[V0038Error] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = V0038Error.from_dict(errors_item_data)

                errors.append(errors_item)

        _licenses = d.pop("licenses", UNSET)
        licenses: list[V0038License] | Unset = UNSET
        if _licenses is not UNSET:
            licenses = []
            for licenses_item_data in _licenses:
                licenses_item = V0038License.from_dict(licenses_item_data)

                licenses.append(licenses_item)

        v0038_licenses = cls(
            errors=errors,
            licenses=licenses,
        )

        v0038_licenses.additional_properties = d
        return v0038_licenses

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
