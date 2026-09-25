from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dbv_0037_job_step_step_het import Dbv0037JobStepStepHet


T = TypeVar("T", bound="Dbv0037JobStepStep")


@_attrs_define
class Dbv0037JobStepStep:
    """Step details

    Attributes:
        job_id (int | Unset): Parent job id
        het (Dbv0037JobStepStepHet | Unset): Heterogeneous job details
        id (str | Unset): Step id
        name (str | Unset): Step name
    """

    job_id: int | Unset = UNSET
    het: Dbv0037JobStepStepHet | Unset = UNSET
    id: str | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        job_id = self.job_id

        het: dict[str, Any] | Unset = UNSET
        if not isinstance(self.het, Unset):
            het = self.het.to_dict()

        id = self.id

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if job_id is not UNSET:
            field_dict["job_id"] = job_id
        if het is not UNSET:
            field_dict["het"] = het
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dbv_0037_job_step_step_het import Dbv0037JobStepStepHet

        d = dict(src_dict)
        job_id = d.pop("job_id", UNSET)

        _het = d.pop("het", UNSET)
        het: Dbv0037JobStepStepHet | Unset
        if isinstance(_het, Unset):
            het = UNSET
        else:
            het = Dbv0037JobStepStepHet.from_dict(_het)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        dbv_0037_job_step_step = cls(
            job_id=job_id,
            het=het,
            id=id,
            name=name,
        )

        dbv_0037_job_step_step.additional_properties = d
        return dbv_0037_job_step_step

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
