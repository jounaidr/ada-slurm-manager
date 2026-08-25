from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dbv_0037_error import Dbv0037Error
    from ..models.dbv_0037_qos import Dbv0037Qos


T = TypeVar("T", bound="Dbv0037QosInfo")


@_attrs_define
class Dbv0037QosInfo:
    """
    Attributes:
        errors (list[Dbv0037Error] | Unset): Slurm errors
        qos (list[Dbv0037Qos] | Unset): Array of QOS
    """

    errors: list[Dbv0037Error] | Unset = UNSET
    qos: list[Dbv0037Qos] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        errors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()
                errors.append(errors_item)

        qos: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.qos, Unset):
            qos = []
            for qos_item_data in self.qos:
                qos_item = qos_item_data.to_dict()
                qos.append(qos_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if errors is not UNSET:
            field_dict["errors"] = errors
        if qos is not UNSET:
            field_dict["qos"] = qos

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dbv_0037_error import Dbv0037Error
        from ..models.dbv_0037_qos import Dbv0037Qos

        d = dict(src_dict)
        _errors = d.pop("errors", UNSET)
        errors: list[Dbv0037Error] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = Dbv0037Error.from_dict(errors_item_data)

                errors.append(errors_item)

        _qos = d.pop("qos", UNSET)
        qos: list[Dbv0037Qos] | Unset = UNSET
        if _qos is not UNSET:
            qos = []
            for qos_item_data in _qos:
                qos_item = Dbv0037Qos.from_dict(qos_item_data)

                qos.append(qos_item)

        dbv_0037_qos_info = cls(
            errors=errors,
            qos=qos,
        )

        dbv_0037_qos_info.additional_properties = d
        return dbv_0037_qos_info

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
