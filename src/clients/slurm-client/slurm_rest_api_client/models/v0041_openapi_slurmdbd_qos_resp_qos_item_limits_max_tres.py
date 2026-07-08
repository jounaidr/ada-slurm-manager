from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v0041_openapi_slurmdbd_qos_resp_qos_item_limits_max_tres_minutes import (
        V0041OpenapiSlurmdbdQosRespQosItemLimitsMaxTresMinutes,
    )
    from ..models.v0041_openapi_slurmdbd_qos_resp_qos_item_limits_max_tres_per import (
        V0041OpenapiSlurmdbdQosRespQosItemLimitsMaxTresPer,
    )
    from ..models.v0041_openapi_slurmdbd_qos_resp_qos_item_limits_max_tres_total_item import (
        V0041OpenapiSlurmdbdQosRespQosItemLimitsMaxTresTotalItem,
    )


T = TypeVar("T", bound="V0041OpenapiSlurmdbdQosRespQosItemLimitsMaxTres")


@_attrs_define
class V0041OpenapiSlurmdbdQosRespQosItemLimitsMaxTres:
    """
    Attributes:
        total (list[V0041OpenapiSlurmdbdQosRespQosItemLimitsMaxTresTotalItem] | Unset): GrpTRES
        minutes (V0041OpenapiSlurmdbdQosRespQosItemLimitsMaxTresMinutes | Unset):
        per (V0041OpenapiSlurmdbdQosRespQosItemLimitsMaxTresPer | Unset):
    """

    total: list[V0041OpenapiSlurmdbdQosRespQosItemLimitsMaxTresTotalItem] | Unset = UNSET
    minutes: V0041OpenapiSlurmdbdQosRespQosItemLimitsMaxTresMinutes | Unset = UNSET
    per: V0041OpenapiSlurmdbdQosRespQosItemLimitsMaxTresPer | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.total, Unset):
            total = []
            for total_item_data in self.total:
                total_item = total_item_data.to_dict()
                total.append(total_item)

        minutes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.minutes, Unset):
            minutes = self.minutes.to_dict()

        per: dict[str, Any] | Unset = UNSET
        if not isinstance(self.per, Unset):
            per = self.per.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total is not UNSET:
            field_dict["total"] = total
        if minutes is not UNSET:
            field_dict["minutes"] = minutes
        if per is not UNSET:
            field_dict["per"] = per

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v0041_openapi_slurmdbd_qos_resp_qos_item_limits_max_tres_minutes import (
            V0041OpenapiSlurmdbdQosRespQosItemLimitsMaxTresMinutes,
        )
        from ..models.v0041_openapi_slurmdbd_qos_resp_qos_item_limits_max_tres_per import (
            V0041OpenapiSlurmdbdQosRespQosItemLimitsMaxTresPer,
        )
        from ..models.v0041_openapi_slurmdbd_qos_resp_qos_item_limits_max_tres_total_item import (
            V0041OpenapiSlurmdbdQosRespQosItemLimitsMaxTresTotalItem,
        )

        d = dict(src_dict)
        _total = d.pop("total", UNSET)
        total: list[V0041OpenapiSlurmdbdQosRespQosItemLimitsMaxTresTotalItem] | Unset = UNSET
        if _total is not UNSET:
            total = []
            for total_item_data in _total:
                total_item = V0041OpenapiSlurmdbdQosRespQosItemLimitsMaxTresTotalItem.from_dict(total_item_data)

                total.append(total_item)

        _minutes = d.pop("minutes", UNSET)
        minutes: V0041OpenapiSlurmdbdQosRespQosItemLimitsMaxTresMinutes | Unset
        if isinstance(_minutes, Unset):
            minutes = UNSET
        else:
            minutes = V0041OpenapiSlurmdbdQosRespQosItemLimitsMaxTresMinutes.from_dict(_minutes)

        _per = d.pop("per", UNSET)
        per: V0041OpenapiSlurmdbdQosRespQosItemLimitsMaxTresPer | Unset
        if isinstance(_per, Unset):
            per = UNSET
        else:
            per = V0041OpenapiSlurmdbdQosRespQosItemLimitsMaxTresPer.from_dict(_per)

        v0041_openapi_slurmdbd_qos_resp_qos_item_limits_max_tres = cls(
            total=total,
            minutes=minutes,
            per=per,
        )

        v0041_openapi_slurmdbd_qos_resp_qos_item_limits_max_tres.additional_properties = d
        return v0041_openapi_slurmdbd_qos_resp_qos_item_limits_max_tres

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
