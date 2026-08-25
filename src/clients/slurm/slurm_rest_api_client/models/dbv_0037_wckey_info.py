from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dbv_0037_error import Dbv0037Error
    from ..models.dbv_0037_wckey import Dbv0037Wckey


T = TypeVar("T", bound="Dbv0037WckeyInfo")


@_attrs_define
class Dbv0037WckeyInfo:
    """
    Attributes:
        errors (list[Dbv0037Error] | Unset): Slurm errors
        wckeys (list[Dbv0037Wckey] | Unset): List of wckeys
    """

    errors: list[Dbv0037Error] | Unset = UNSET
    wckeys: list[Dbv0037Wckey] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        errors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()
                errors.append(errors_item)

        wckeys: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.wckeys, Unset):
            wckeys = []
            for wckeys_item_data in self.wckeys:
                wckeys_item = wckeys_item_data.to_dict()
                wckeys.append(wckeys_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if errors is not UNSET:
            field_dict["errors"] = errors
        if wckeys is not UNSET:
            field_dict["wckeys"] = wckeys

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dbv_0037_error import Dbv0037Error
        from ..models.dbv_0037_wckey import Dbv0037Wckey

        d = dict(src_dict)
        _errors = d.pop("errors", UNSET)
        errors: list[Dbv0037Error] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = Dbv0037Error.from_dict(errors_item_data)

                errors.append(errors_item)

        _wckeys = d.pop("wckeys", UNSET)
        wckeys: list[Dbv0037Wckey] | Unset = UNSET
        if _wckeys is not UNSET:
            wckeys = []
            for wckeys_item_data in _wckeys:
                wckeys_item = Dbv0037Wckey.from_dict(wckeys_item_data)

                wckeys.append(wckeys_item)

        dbv_0037_wckey_info = cls(
            errors=errors,
            wckeys=wckeys,
        )

        dbv_0037_wckey_info.additional_properties = d
        return dbv_0037_wckey_info

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
