from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dbv_0037_error import Dbv0037Error
    from ..models.dbv_0037_user import Dbv0037User


T = TypeVar("T", bound="Dbv0037UserInfo")


@_attrs_define
class Dbv0037UserInfo:
    """
    Attributes:
        errors (list[Dbv0037Error] | Unset): Slurm errors
        users (list[Dbv0037User] | Unset): Array of users
    """

    errors: list[Dbv0037Error] | Unset = UNSET
    users: list[Dbv0037User] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        errors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()
                errors.append(errors_item)

        users: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.users, Unset):
            users = []
            for users_item_data in self.users:
                users_item = users_item_data.to_dict()
                users.append(users_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if errors is not UNSET:
            field_dict["errors"] = errors
        if users is not UNSET:
            field_dict["users"] = users

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dbv_0037_error import Dbv0037Error
        from ..models.dbv_0037_user import Dbv0037User

        d = dict(src_dict)
        _errors = d.pop("errors", UNSET)
        errors: list[Dbv0037Error] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = Dbv0037Error.from_dict(errors_item_data)

                errors.append(errors_item)

        _users = d.pop("users", UNSET)
        users: list[Dbv0037User] | Unset = UNSET
        if _users is not UNSET:
            users = []
            for users_item_data in _users:
                users_item = Dbv0037User.from_dict(users_item_data)

                users.append(users_item)

        dbv_0037_user_info = cls(
            errors=errors,
            users=users,
        )

        dbv_0037_user_info.additional_properties = d
        return dbv_0037_user_info

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
