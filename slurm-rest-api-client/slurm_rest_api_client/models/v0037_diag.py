from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v0037_diag_statistics import V0037DiagStatistics
    from ..models.v0037_error import V0037Error


T = TypeVar("T", bound="V0037Diag")


@_attrs_define
class V0037Diag:
    """
    Attributes:
        errors (list[V0037Error] | Unset): slurm errors
        statistics (V0037DiagStatistics | Unset): Slurm statistics
    """

    errors: list[V0037Error] | Unset = UNSET
    statistics: V0037DiagStatistics | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        errors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()
                errors.append(errors_item)

        statistics: dict[str, Any] | Unset = UNSET
        if not isinstance(self.statistics, Unset):
            statistics = self.statistics.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if errors is not UNSET:
            field_dict["errors"] = errors
        if statistics is not UNSET:
            field_dict["statistics"] = statistics

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v0037_diag_statistics import V0037DiagStatistics
        from ..models.v0037_error import V0037Error

        d = dict(src_dict)
        _errors = d.pop("errors", UNSET)
        errors: list[V0037Error] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = V0037Error.from_dict(errors_item_data)

                errors.append(errors_item)

        _statistics = d.pop("statistics", UNSET)
        statistics: V0037DiagStatistics | Unset
        if isinstance(_statistics, Unset):
            statistics = UNSET
        else:
            statistics = V0037DiagStatistics.from_dict(_statistics)

        v0037_diag = cls(
            errors=errors,
            statistics=statistics,
        )

        v0037_diag.additional_properties = d
        return v0037_diag

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
