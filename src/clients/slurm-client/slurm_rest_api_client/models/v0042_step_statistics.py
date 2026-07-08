from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v0042_step_statistics_cpu import V0042StepStatisticsCPU
    from ..models.v0042_step_statistics_energy import V0042StepStatisticsEnergy


T = TypeVar("T", bound="V0042StepStatistics")


@_attrs_define
class V0042StepStatistics:
    """
    Attributes:
        cpu (V0042StepStatisticsCPU | Unset):
        energy (V0042StepStatisticsEnergy | Unset):
    """

    cpu: V0042StepStatisticsCPU | Unset = UNSET
    energy: V0042StepStatisticsEnergy | Unset = UNSET
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
        from ..models.v0042_step_statistics_cpu import V0042StepStatisticsCPU
        from ..models.v0042_step_statistics_energy import V0042StepStatisticsEnergy

        d = dict(src_dict)
        _cpu = d.pop("CPU", UNSET)
        cpu: V0042StepStatisticsCPU | Unset
        if isinstance(_cpu, Unset):
            cpu = UNSET
        else:
            cpu = V0042StepStatisticsCPU.from_dict(_cpu)

        _energy = d.pop("energy", UNSET)
        energy: V0042StepStatisticsEnergy | Unset
        if isinstance(_energy, Unset):
            energy = UNSET
        else:
            energy = V0042StepStatisticsEnergy.from_dict(_energy)

        v0042_step_statistics = cls(
            cpu=cpu,
            energy=energy,
        )

        v0042_step_statistics.additional_properties = d
        return v0042_step_statistics

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
