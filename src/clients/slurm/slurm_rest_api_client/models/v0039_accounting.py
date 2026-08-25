from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v0039_accounting_allocated import V0039AccountingAllocated
    from ..models.v0039_tres import V0039Tres


T = TypeVar("T", bound="V0039Accounting")


@_attrs_define
class V0039Accounting:
    """
    Attributes:
        allocated (V0039AccountingAllocated | Unset):
        id (int | Unset):
        start (int | Unset):
        tres (V0039Tres | Unset):
    """

    allocated: V0039AccountingAllocated | Unset = UNSET
    id: int | Unset = UNSET
    start: int | Unset = UNSET
    tres: V0039Tres | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allocated: dict[str, Any] | Unset = UNSET
        if not isinstance(self.allocated, Unset):
            allocated = self.allocated.to_dict()

        id = self.id

        start = self.start

        tres: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tres, Unset):
            tres = self.tres.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if allocated is not UNSET:
            field_dict["allocated"] = allocated
        if id is not UNSET:
            field_dict["id"] = id
        if start is not UNSET:
            field_dict["start"] = start
        if tres is not UNSET:
            field_dict["TRES"] = tres

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v0039_accounting_allocated import V0039AccountingAllocated
        from ..models.v0039_tres import V0039Tres

        d = dict(src_dict)
        _allocated = d.pop("allocated", UNSET)
        allocated: V0039AccountingAllocated | Unset
        if isinstance(_allocated, Unset):
            allocated = UNSET
        else:
            allocated = V0039AccountingAllocated.from_dict(_allocated)

        id = d.pop("id", UNSET)

        start = d.pop("start", UNSET)

        _tres = d.pop("TRES", UNSET)
        tres: V0039Tres | Unset
        if isinstance(_tres, Unset):
            tres = UNSET
        else:
            tres = V0039Tres.from_dict(_tres)

        v0039_accounting = cls(
            allocated=allocated,
            id=id,
            start=start,
            tres=tres,
        )

        v0039_accounting.additional_properties = d
        return v0039_accounting

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
