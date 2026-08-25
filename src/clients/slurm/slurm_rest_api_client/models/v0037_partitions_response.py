from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v0037_error import V0037Error
    from ..models.v0037_partition import V0037Partition


T = TypeVar("T", bound="V0037PartitionsResponse")


@_attrs_define
class V0037PartitionsResponse:
    """
    Attributes:
        errors (list[V0037Error] | Unset): slurm errors
        partitions (list[V0037Partition] | Unset): partition info
    """

    errors: list[V0037Error] | Unset = UNSET
    partitions: list[V0037Partition] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        errors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()
                errors.append(errors_item)

        partitions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.partitions, Unset):
            partitions = []
            for partitions_item_data in self.partitions:
                partitions_item = partitions_item_data.to_dict()
                partitions.append(partitions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if errors is not UNSET:
            field_dict["errors"] = errors
        if partitions is not UNSET:
            field_dict["partitions"] = partitions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v0037_error import V0037Error
        from ..models.v0037_partition import V0037Partition

        d = dict(src_dict)
        _errors = d.pop("errors", UNSET)
        errors: list[V0037Error] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = V0037Error.from_dict(errors_item_data)

                errors.append(errors_item)

        _partitions = d.pop("partitions", UNSET)
        partitions: list[V0037Partition] | Unset = UNSET
        if _partitions is not UNSET:
            partitions = []
            for partitions_item_data in _partitions:
                partitions_item = V0037Partition.from_dict(partitions_item_data)

                partitions.append(partitions_item)

        v0037_partitions_response = cls(
            errors=errors,
            partitions=partitions,
        )

        v0037_partitions_response.additional_properties = d
        return v0037_partitions_response

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
