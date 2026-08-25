from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v0039_user import V0039User


T = TypeVar("T", bound="Dbv0039UpdateUsers")


@_attrs_define
class Dbv0039UpdateUsers:
    """
    Attributes:
        users (list[V0039User] | Unset):
    """

    users: list[V0039User] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        users: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.users, Unset):
            users = []
            for componentsschemasv0_0_39_user_list_item_data in self.users:
                componentsschemasv0_0_39_user_list_item = componentsschemasv0_0_39_user_list_item_data.to_dict()
                users.append(componentsschemasv0_0_39_user_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if users is not UNSET:
            field_dict["users"] = users

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v0039_user import V0039User

        d = dict(src_dict)
        _users = d.pop("users", UNSET)
        users: list[V0039User] | Unset = UNSET
        if _users is not UNSET:
            users = []
            for componentsschemasv0_0_39_user_list_item_data in _users:
                componentsschemasv0_0_39_user_list_item = V0039User.from_dict(
                    componentsschemasv0_0_39_user_list_item_data
                )

                users.append(componentsschemasv0_0_39_user_list_item)

        dbv_0039_update_users = cls(
            users=users,
        )

        dbv_0039_update_users.additional_properties = d
        return dbv_0039_update_users

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
