from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dbv_0038_qos import Dbv0038Qos


T = TypeVar("T", bound="Dbv0038UpdateQos")


@_attrs_define
class Dbv0038UpdateQos:
    """
    Attributes:
        qos (list[Dbv0038Qos] | Unset):
    """

    qos: list[Dbv0038Qos] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        qos: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.qos, Unset):
            qos = []
            for qos_item_data in self.qos:
                qos_item = qos_item_data.to_dict()
                qos.append(qos_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if qos is not UNSET:
            field_dict["qos"] = qos

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dbv_0038_qos import Dbv0038Qos

        d = dict(src_dict)
        _qos = d.pop("qos", UNSET)
        qos: list[Dbv0038Qos] | Unset = UNSET
        if _qos is not UNSET:
            qos = []
            for qos_item_data in _qos:
                qos_item = Dbv0038Qos.from_dict(qos_item_data)

                qos.append(qos_item)

        dbv_0038_update_qos = cls(
            qos=qos,
        )

        dbv_0038_update_qos.additional_properties = d
        return dbv_0038_update_qos

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
