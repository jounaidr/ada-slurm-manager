from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dbv_0037_association_max_jobs_per import Dbv0037AssociationMaxJobsPer


T = TypeVar("T", bound="Dbv0037AssociationMaxJobs")


@_attrs_define
class Dbv0037AssociationMaxJobs:
    """Max jobs settings

    Attributes:
        active (int | Unset): Max TRES for active total jobs
        accruing (int | Unset): Max TRES for job accruing priority
        total (int | Unset): Max TRES for job total submitted
        per (Dbv0037AssociationMaxJobsPer | Unset): Max jobs per settings
    """

    active: int | Unset = UNSET
    accruing: int | Unset = UNSET
    total: int | Unset = UNSET
    per: Dbv0037AssociationMaxJobsPer | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        active = self.active

        accruing = self.accruing

        total = self.total

        per: dict[str, Any] | Unset = UNSET
        if not isinstance(self.per, Unset):
            per = self.per.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if active is not UNSET:
            field_dict["active"] = active
        if accruing is not UNSET:
            field_dict["accruing"] = accruing
        if total is not UNSET:
            field_dict["total"] = total
        if per is not UNSET:
            field_dict["per"] = per

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dbv_0037_association_max_jobs_per import Dbv0037AssociationMaxJobsPer

        d = dict(src_dict)
        active = d.pop("active", UNSET)

        accruing = d.pop("accruing", UNSET)

        total = d.pop("total", UNSET)

        _per = d.pop("per", UNSET)
        per: Dbv0037AssociationMaxJobsPer | Unset
        if isinstance(_per, Unset):
            per = UNSET
        else:
            per = Dbv0037AssociationMaxJobsPer.from_dict(_per)

        dbv_0037_association_max_jobs = cls(
            active=active,
            accruing=accruing,
            total=total,
            per=per,
        )

        dbv_0037_association_max_jobs.additional_properties = d
        return dbv_0037_association_max_jobs

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
