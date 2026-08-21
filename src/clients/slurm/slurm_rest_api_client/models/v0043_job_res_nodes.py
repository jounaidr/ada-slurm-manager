from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.v0043_job_res_nodes_select_type_item import V0043JobResNodesSelectTypeItem
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v0043_job_res_node import V0043JobResNode


T = TypeVar("T", bound="V0043JobResNodes")


@_attrs_define
class V0043JobResNodes:
    """
    Attributes:
        count (int | Unset): Number of allocated nodes
        select_type (list[V0043JobResNodesSelectTypeItem] | Unset): Node scheduling selection method
        list_ (str | Unset): Node(s) allocated to the job
        whole (bool | Unset): Whether whole nodes were allocated
        allocation (list[V0043JobResNode] | Unset): Job resources for a node
    """

    count: int | Unset = UNSET
    select_type: list[V0043JobResNodesSelectTypeItem] | Unset = UNSET
    list_: str | Unset = UNSET
    whole: bool | Unset = UNSET
    allocation: list[V0043JobResNode] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        select_type: list[str] | Unset = UNSET
        if not isinstance(self.select_type, Unset):
            select_type = []
            for select_type_item_data in self.select_type:
                select_type_item = select_type_item_data.value
                select_type.append(select_type_item)

        list_ = self.list_

        whole = self.whole

        allocation: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.allocation, Unset):
            allocation = []
            for componentsschemasv0_0_43_job_res_nodes_item_data in self.allocation:
                componentsschemasv0_0_43_job_res_nodes_item = componentsschemasv0_0_43_job_res_nodes_item_data.to_dict()
                allocation.append(componentsschemasv0_0_43_job_res_nodes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if count is not UNSET:
            field_dict["count"] = count
        if select_type is not UNSET:
            field_dict["select_type"] = select_type
        if list_ is not UNSET:
            field_dict["list"] = list_
        if whole is not UNSET:
            field_dict["whole"] = whole
        if allocation is not UNSET:
            field_dict["allocation"] = allocation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v0043_job_res_node import V0043JobResNode

        d = dict(src_dict)
        count = d.pop("count", UNSET)

        _select_type = d.pop("select_type", UNSET)
        select_type: list[V0043JobResNodesSelectTypeItem] | Unset = UNSET
        if _select_type is not UNSET:
            select_type = []
            for select_type_item_data in _select_type:
                select_type_item = V0043JobResNodesSelectTypeItem(select_type_item_data)

                select_type.append(select_type_item)

        list_ = d.pop("list", UNSET)

        whole = d.pop("whole", UNSET)

        _allocation = d.pop("allocation", UNSET)
        allocation: list[V0043JobResNode] | Unset = UNSET
        if _allocation is not UNSET:
            allocation = []
            for componentsschemasv0_0_43_job_res_nodes_item_data in _allocation:
                componentsschemasv0_0_43_job_res_nodes_item = V0043JobResNode.from_dict(
                    componentsschemasv0_0_43_job_res_nodes_item_data
                )

                allocation.append(componentsschemasv0_0_43_job_res_nodes_item)

        v0043_job_res_nodes = cls(
            count=count,
            select_type=select_type,
            list_=list_,
            whole=whole,
            allocation=allocation,
        )

        v0043_job_res_nodes.additional_properties = d
        return v0043_job_res_nodes

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
