from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v0041_openapi_nodes_resp_errors_item import V0041OpenapiNodesRespErrorsItem
    from ..models.v0041_openapi_nodes_resp_last_update import V0041OpenapiNodesRespLastUpdate
    from ..models.v0041_openapi_nodes_resp_meta import V0041OpenapiNodesRespMeta
    from ..models.v0041_openapi_nodes_resp_nodes_item import V0041OpenapiNodesRespNodesItem
    from ..models.v0041_openapi_nodes_resp_warnings_item import V0041OpenapiNodesRespWarningsItem


T = TypeVar("T", bound="V0041OpenapiNodesResp")


@_attrs_define
class V0041OpenapiNodesResp:
    """
    Attributes:
        nodes (list[V0041OpenapiNodesRespNodesItem]): List of nodes
        last_update (V0041OpenapiNodesRespLastUpdate): Time of last node change (UNIX timestamp)
        meta (V0041OpenapiNodesRespMeta | Unset): Slurm meta values
        errors (list[V0041OpenapiNodesRespErrorsItem] | Unset): Query errors
        warnings (list[V0041OpenapiNodesRespWarningsItem] | Unset): Query warnings
    """

    nodes: list[V0041OpenapiNodesRespNodesItem]
    last_update: V0041OpenapiNodesRespLastUpdate
    meta: V0041OpenapiNodesRespMeta | Unset = UNSET
    errors: list[V0041OpenapiNodesRespErrorsItem] | Unset = UNSET
    warnings: list[V0041OpenapiNodesRespWarningsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        nodes = []
        for nodes_item_data in self.nodes:
            nodes_item = nodes_item_data.to_dict()
            nodes.append(nodes_item)

        last_update = self.last_update.to_dict()

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
                "nodes": nodes,
                "last_update": last_update,
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
        from ..models.v0041_openapi_nodes_resp_errors_item import V0041OpenapiNodesRespErrorsItem
        from ..models.v0041_openapi_nodes_resp_last_update import V0041OpenapiNodesRespLastUpdate
        from ..models.v0041_openapi_nodes_resp_meta import V0041OpenapiNodesRespMeta
        from ..models.v0041_openapi_nodes_resp_nodes_item import V0041OpenapiNodesRespNodesItem
        from ..models.v0041_openapi_nodes_resp_warnings_item import V0041OpenapiNodesRespWarningsItem

        d = dict(src_dict)
        nodes = []
        _nodes = d.pop("nodes")
        for nodes_item_data in _nodes:
            nodes_item = V0041OpenapiNodesRespNodesItem.from_dict(nodes_item_data)

            nodes.append(nodes_item)

        last_update = V0041OpenapiNodesRespLastUpdate.from_dict(d.pop("last_update"))

        _meta = d.pop("meta", UNSET)
        meta: V0041OpenapiNodesRespMeta | Unset
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = V0041OpenapiNodesRespMeta.from_dict(_meta)

        _errors = d.pop("errors", UNSET)
        errors: list[V0041OpenapiNodesRespErrorsItem] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = V0041OpenapiNodesRespErrorsItem.from_dict(errors_item_data)

                errors.append(errors_item)

        _warnings = d.pop("warnings", UNSET)
        warnings: list[V0041OpenapiNodesRespWarningsItem] | Unset = UNSET
        if _warnings is not UNSET:
            warnings = []
            for warnings_item_data in _warnings:
                warnings_item = V0041OpenapiNodesRespWarningsItem.from_dict(warnings_item_data)

                warnings.append(warnings_item)

        v0041_openapi_nodes_resp = cls(
            nodes=nodes,
            last_update=last_update,
            meta=meta,
            errors=errors,
            warnings=warnings,
        )

        v0041_openapi_nodes_resp.additional_properties = d
        return v0041_openapi_nodes_resp

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
