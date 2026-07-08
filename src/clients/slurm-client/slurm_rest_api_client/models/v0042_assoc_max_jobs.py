from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v0042_assoc_max_jobs_per import V0042AssocMaxJobsPer
    from ..models.v0042_uint_32_no_val_struct import V0042Uint32NoValStruct


T = TypeVar("T", bound="V0042AssocMaxJobs")


@_attrs_define
class V0042AssocMaxJobs:
    """
    Attributes:
        per (V0042AssocMaxJobsPer | Unset):
        active (V0042Uint32NoValStruct | Unset):
        accruing (V0042Uint32NoValStruct | Unset):
        total (V0042Uint32NoValStruct | Unset):
    """

    per: V0042AssocMaxJobsPer | Unset = UNSET
    active: V0042Uint32NoValStruct | Unset = UNSET
    accruing: V0042Uint32NoValStruct | Unset = UNSET
    total: V0042Uint32NoValStruct | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        per: dict[str, Any] | Unset = UNSET
        if not isinstance(self.per, Unset):
            per = self.per.to_dict()

        active: dict[str, Any] | Unset = UNSET
        if not isinstance(self.active, Unset):
            active = self.active.to_dict()

        accruing: dict[str, Any] | Unset = UNSET
        if not isinstance(self.accruing, Unset):
            accruing = self.accruing.to_dict()

        total: dict[str, Any] | Unset = UNSET
        if not isinstance(self.total, Unset):
            total = self.total.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if per is not UNSET:
            field_dict["per"] = per
        if active is not UNSET:
            field_dict["active"] = active
        if accruing is not UNSET:
            field_dict["accruing"] = accruing
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v0042_assoc_max_jobs_per import V0042AssocMaxJobsPer
        from ..models.v0042_uint_32_no_val_struct import V0042Uint32NoValStruct

        d = dict(src_dict)
        _per = d.pop("per", UNSET)
        per: V0042AssocMaxJobsPer | Unset
        if isinstance(_per, Unset):
            per = UNSET
        else:
            per = V0042AssocMaxJobsPer.from_dict(_per)

        _active = d.pop("active", UNSET)
        active: V0042Uint32NoValStruct | Unset
        if isinstance(_active, Unset):
            active = UNSET
        else:
            active = V0042Uint32NoValStruct.from_dict(_active)

        _accruing = d.pop("accruing", UNSET)
        accruing: V0042Uint32NoValStruct | Unset
        if isinstance(_accruing, Unset):
            accruing = UNSET
        else:
            accruing = V0042Uint32NoValStruct.from_dict(_accruing)

        _total = d.pop("total", UNSET)
        total: V0042Uint32NoValStruct | Unset
        if isinstance(_total, Unset):
            total = UNSET
        else:
            total = V0042Uint32NoValStruct.from_dict(_total)

        v0042_assoc_max_jobs = cls(
            per=per,
            active=active,
            accruing=accruing,
            total=total,
        )

        v0042_assoc_max_jobs.additional_properties = d
        return v0042_assoc_max_jobs

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
