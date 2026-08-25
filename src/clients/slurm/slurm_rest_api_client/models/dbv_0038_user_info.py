from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dbv_0038_error import Dbv0038Error
    from ..models.dbv_0038_meta import Dbv0038Meta
    from ..models.dbv_0038_user import Dbv0038User


T = TypeVar("T", bound="Dbv0038UserInfo")


@_attrs_define
class Dbv0038UserInfo:
    """
    Attributes:
        meta (Dbv0038Meta | Unset):
        errors (list[Dbv0038Error] | Unset): Slurm errors
        users (list[Dbv0038User] | Unset): Array of users
    """

    meta: Dbv0038Meta | Unset = UNSET
    errors: list[Dbv0038Error] | Unset = UNSET
    users: list[Dbv0038User] | Unset = UNSET
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

        users: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.users, Unset):
            users = []
            for users_item_data in self.users:
                users_item = users_item_data.to_dict()
                users.append(users_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if meta is not UNSET:
            field_dict["meta"] = meta
        if errors is not UNSET:
            field_dict["errors"] = errors
        if users is not UNSET:
            field_dict["users"] = users

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dbv_0038_error import Dbv0038Error
        from ..models.dbv_0038_meta import Dbv0038Meta
        from ..models.dbv_0038_user import Dbv0038User

        d = dict(src_dict)
        _meta = d.pop("meta", UNSET)
        meta: Dbv0038Meta | Unset
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = Dbv0038Meta.from_dict(_meta)

        _errors = d.pop("errors", UNSET)
        errors: list[Dbv0038Error] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = Dbv0038Error.from_dict(errors_item_data)

                errors.append(errors_item)

        _users = d.pop("users", UNSET)
        users: list[Dbv0038User] | Unset = UNSET
        if _users is not UNSET:
            users = []
            for users_item_data in _users:
                users_item = Dbv0038User.from_dict(users_item_data)

                users.append(users_item)

        dbv_0038_user_info = cls(
            meta=meta,
            errors=errors,
            users=users,
        )

        dbv_0038_user_info.additional_properties = d
        return dbv_0038_user_info

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
