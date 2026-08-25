from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dbv_0038_association_max_jobs import Dbv0038AssociationMaxJobs
    from ..models.dbv_0038_association_max_per import Dbv0038AssociationMaxPer
    from ..models.dbv_0038_association_max_tres import Dbv0038AssociationMaxTres


T = TypeVar("T", bound="Dbv0038AssociationMax")


@_attrs_define
class Dbv0038AssociationMax:
    """Max settings

    Attributes:
        jobs (Dbv0038AssociationMaxJobs | Unset): Max jobs settings
        per (Dbv0038AssociationMaxPer | Unset): Max per settings
        tres (Dbv0038AssociationMaxTres | Unset): Max TRES settings
    """

    jobs: Dbv0038AssociationMaxJobs | Unset = UNSET
    per: Dbv0038AssociationMaxPer | Unset = UNSET
    tres: Dbv0038AssociationMaxTres | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        jobs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.jobs, Unset):
            jobs = self.jobs.to_dict()

        per: dict[str, Any] | Unset = UNSET
        if not isinstance(self.per, Unset):
            per = self.per.to_dict()

        tres: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tres, Unset):
            tres = self.tres.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if jobs is not UNSET:
            field_dict["jobs"] = jobs
        if per is not UNSET:
            field_dict["per"] = per
        if tres is not UNSET:
            field_dict["tres"] = tres

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dbv_0038_association_max_jobs import Dbv0038AssociationMaxJobs
        from ..models.dbv_0038_association_max_per import Dbv0038AssociationMaxPer
        from ..models.dbv_0038_association_max_tres import Dbv0038AssociationMaxTres

        d = dict(src_dict)
        _jobs = d.pop("jobs", UNSET)
        jobs: Dbv0038AssociationMaxJobs | Unset
        if isinstance(_jobs, Unset):
            jobs = UNSET
        else:
            jobs = Dbv0038AssociationMaxJobs.from_dict(_jobs)

        _per = d.pop("per", UNSET)
        per: Dbv0038AssociationMaxPer | Unset
        if isinstance(_per, Unset):
            per = UNSET
        else:
            per = Dbv0038AssociationMaxPer.from_dict(_per)

        _tres = d.pop("tres", UNSET)
        tres: Dbv0038AssociationMaxTres | Unset
        if isinstance(_tres, Unset):
            tres = UNSET
        else:
            tres = Dbv0038AssociationMaxTres.from_dict(_tres)

        dbv_0038_association_max = cls(
            jobs=jobs,
            per=per,
            tres=tres,
        )

        dbv_0038_association_max.additional_properties = d
        return dbv_0038_association_max

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
