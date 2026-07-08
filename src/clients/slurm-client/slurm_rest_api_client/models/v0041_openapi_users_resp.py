from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v0041_openapi_users_resp_errors_item import V0041OpenapiUsersRespErrorsItem
    from ..models.v0041_openapi_users_resp_meta import V0041OpenapiUsersRespMeta
    from ..models.v0041_openapi_users_resp_users_item import V0041OpenapiUsersRespUsersItem
    from ..models.v0041_openapi_users_resp_warnings_item import V0041OpenapiUsersRespWarningsItem


T = TypeVar("T", bound="V0041OpenapiUsersResp")


@_attrs_define
class V0041OpenapiUsersResp:
    """
    Attributes:
        users (list[V0041OpenapiUsersRespUsersItem]): users
        meta (V0041OpenapiUsersRespMeta | Unset): Slurm meta values
        errors (list[V0041OpenapiUsersRespErrorsItem] | Unset): Query errors
        warnings (list[V0041OpenapiUsersRespWarningsItem] | Unset): Query warnings
    """

    users: list[V0041OpenapiUsersRespUsersItem]
    meta: V0041OpenapiUsersRespMeta | Unset = UNSET
    errors: list[V0041OpenapiUsersRespErrorsItem] | Unset = UNSET
    warnings: list[V0041OpenapiUsersRespWarningsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        users = []
        for users_item_data in self.users:
            users_item = users_item_data.to_dict()
            users.append(users_item)

        meta: dict[str, Any] | Unset = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        errors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()
                errors.append(errors_item)

        warnings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = []
            for warnings_item_data in self.warnings:
                warnings_item = warnings_item_data.to_dict()
                warnings.append(warnings_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "users": users,
            }
        )
        if meta is not UNSET:
            field_dict["meta"] = meta
        if errors is not UNSET:
            field_dict["errors"] = errors
        if warnings is not UNSET:
            field_dict["warnings"] = warnings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v0041_openapi_users_resp_errors_item import V0041OpenapiUsersRespErrorsItem
        from ..models.v0041_openapi_users_resp_meta import V0041OpenapiUsersRespMeta
        from ..models.v0041_openapi_users_resp_users_item import V0041OpenapiUsersRespUsersItem
        from ..models.v0041_openapi_users_resp_warnings_item import V0041OpenapiUsersRespWarningsItem

        d = dict(src_dict)
        users = []
        _users = d.pop("users")
        for users_item_data in _users:
            users_item = V0041OpenapiUsersRespUsersItem.from_dict(users_item_data)

            users.append(users_item)

        _meta = d.pop("meta", UNSET)
        meta: V0041OpenapiUsersRespMeta | Unset
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = V0041OpenapiUsersRespMeta.from_dict(_meta)

        _errors = d.pop("errors", UNSET)
        errors: list[V0041OpenapiUsersRespErrorsItem] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = V0041OpenapiUsersRespErrorsItem.from_dict(errors_item_data)

                errors.append(errors_item)

        _warnings = d.pop("warnings", UNSET)
        warnings: list[V0041OpenapiUsersRespWarningsItem] | Unset = UNSET
        if _warnings is not UNSET:
            warnings = []
            for warnings_item_data in _warnings:
                warnings_item = V0041OpenapiUsersRespWarningsItem.from_dict(warnings_item_data)

                warnings.append(warnings_item)

        v0041_openapi_users_resp = cls(
            users=users,
            meta=meta,
            errors=errors,
            warnings=warnings,
        )

        v0041_openapi_users_resp.additional_properties = d
        return v0041_openapi_users_resp

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
