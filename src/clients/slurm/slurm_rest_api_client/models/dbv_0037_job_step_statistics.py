from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dbv_0037_job_step_statistics_cpu import Dbv0037JobStepStatisticsCPU
    from ..models.dbv_0037_job_step_statistics_energy import Dbv0037JobStepStatisticsEnergy


T = TypeVar("T", bound="Dbv0037JobStepStatistics")


@_attrs_define
class Dbv0037JobStepStatistics:
    """Statistics of job step

    Attributes:
        cpu (Dbv0037JobStepStatisticsCPU | Unset): Statistics of CPU
        energy (Dbv0037JobStepStatisticsEnergy | Unset): Statistics of energy
    """

    cpu: Dbv0037JobStepStatisticsCPU | Unset = UNSET
    energy: Dbv0037JobStepStatisticsEnergy | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cpu: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cpu, Unset):
            cpu = self.cpu.to_dict()

        energy: dict[str, Any] | Unset = UNSET
        if not isinstance(self.energy, Unset):
            energy = self.energy.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cpu is not UNSET:
            field_dict["CPU"] = cpu
        if energy is not UNSET:
            field_dict["energy"] = energy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dbv_0037_job_step_statistics_cpu import Dbv0037JobStepStatisticsCPU
        from ..models.dbv_0037_job_step_statistics_energy import Dbv0037JobStepStatisticsEnergy

        d = dict(src_dict)
        _cpu = d.pop("CPU", UNSET)
        cpu: Dbv0037JobStepStatisticsCPU | Unset
        if isinstance(_cpu, Unset):
            cpu = UNSET
        else:
            cpu = Dbv0037JobStepStatisticsCPU.from_dict(_cpu)

        _energy = d.pop("energy", UNSET)
        energy: Dbv0037JobStepStatisticsEnergy | Unset
        if isinstance(_energy, Unset):
            energy = UNSET
        else:
            energy = Dbv0037JobStepStatisticsEnergy.from_dict(_energy)

        dbv_0037_job_step_statistics = cls(
            cpu=cpu,
            energy=energy,
        )

        dbv_0037_job_step_statistics.additional_properties = d
        return dbv_0037_job_step_statistics

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
