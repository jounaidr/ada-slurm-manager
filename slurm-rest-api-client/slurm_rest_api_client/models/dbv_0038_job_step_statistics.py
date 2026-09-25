from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dbv_0038_job_step_statistics_cpu import Dbv0038JobStepStatisticsCPU
    from ..models.dbv_0038_job_step_statistics_energy import Dbv0038JobStepStatisticsEnergy


T = TypeVar("T", bound="Dbv0038JobStepStatistics")


@_attrs_define
class Dbv0038JobStepStatistics:
    """Statistics of job step

    Attributes:
        cpu (Dbv0038JobStepStatisticsCPU | Unset): Statistics of CPU
        energy (Dbv0038JobStepStatisticsEnergy | Unset): Statistics of energy
    """

    cpu: Dbv0038JobStepStatisticsCPU | Unset = UNSET
    energy: Dbv0038JobStepStatisticsEnergy | Unset = UNSET
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
        from ..models.dbv_0038_job_step_statistics_cpu import Dbv0038JobStepStatisticsCPU
        from ..models.dbv_0038_job_step_statistics_energy import Dbv0038JobStepStatisticsEnergy

        d = dict(src_dict)
        _cpu = d.pop("CPU", UNSET)
        cpu: Dbv0038JobStepStatisticsCPU | Unset
        if isinstance(_cpu, Unset):
            cpu = UNSET
        else:
            cpu = Dbv0038JobStepStatisticsCPU.from_dict(_cpu)

        _energy = d.pop("energy", UNSET)
        energy: Dbv0038JobStepStatisticsEnergy | Unset
        if isinstance(_energy, Unset):
            energy = UNSET
        else:
            energy = Dbv0038JobStepStatisticsEnergy.from_dict(_energy)

        dbv_0038_job_step_statistics = cls(
            cpu=cpu,
            energy=energy,
        )

        dbv_0038_job_step_statistics.additional_properties = d
        return dbv_0038_job_step_statistics

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
