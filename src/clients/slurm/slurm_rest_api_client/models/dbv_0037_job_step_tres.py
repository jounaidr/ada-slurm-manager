from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dbv_0037_job_step_tres_consumed import Dbv0037JobStepTresConsumed
    from ..models.dbv_0037_job_step_tres_requested import Dbv0037JobStepTresRequested
    from ..models.dbv_0037_tres_list_item import Dbv0037TresListItem


T = TypeVar("T", bound="Dbv0037JobStepTres")


@_attrs_define
class Dbv0037JobStepTres:
    """TRES usage

    Attributes:
        requested (Dbv0037JobStepTresRequested | Unset): TRES requested for job
        consumed (Dbv0037JobStepTresConsumed | Unset): TRES requested for job
        allocated (list[Dbv0037TresListItem] | Unset): TRES list of attributes
    """

    requested: Dbv0037JobStepTresRequested | Unset = UNSET
    consumed: Dbv0037JobStepTresConsumed | Unset = UNSET
    allocated: list[Dbv0037TresListItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        requested: dict[str, Any] | Unset = UNSET
        if not isinstance(self.requested, Unset):
            requested = self.requested.to_dict()

        consumed: dict[str, Any] | Unset = UNSET
        if not isinstance(self.consumed, Unset):
            consumed = self.consumed.to_dict()

        allocated: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.allocated, Unset):
            allocated = []
            for componentsschemasdbv0_0_37_tres_list_item_data in self.allocated:
                componentsschemasdbv0_0_37_tres_list_item = componentsschemasdbv0_0_37_tres_list_item_data.to_dict()
                allocated.append(componentsschemasdbv0_0_37_tres_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if requested is not UNSET:
            field_dict["requested"] = requested
        if consumed is not UNSET:
            field_dict["consumed"] = consumed
        if allocated is not UNSET:
            field_dict["allocated"] = allocated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dbv_0037_job_step_tres_consumed import Dbv0037JobStepTresConsumed
        from ..models.dbv_0037_job_step_tres_requested import Dbv0037JobStepTresRequested
        from ..models.dbv_0037_tres_list_item import Dbv0037TresListItem

        d = dict(src_dict)
        _requested = d.pop("requested", UNSET)
        requested: Dbv0037JobStepTresRequested | Unset
        if isinstance(_requested, Unset):
            requested = UNSET
        else:
            requested = Dbv0037JobStepTresRequested.from_dict(_requested)

        _consumed = d.pop("consumed", UNSET)
        consumed: Dbv0037JobStepTresConsumed | Unset
        if isinstance(_consumed, Unset):
            consumed = UNSET
        else:
            consumed = Dbv0037JobStepTresConsumed.from_dict(_consumed)

        _allocated = d.pop("allocated", UNSET)
        allocated: list[Dbv0037TresListItem] | Unset = UNSET
        if _allocated is not UNSET:
            allocated = []
            for componentsschemasdbv0_0_37_tres_list_item_data in _allocated:
                componentsschemasdbv0_0_37_tres_list_item = Dbv0037TresListItem.from_dict(
                    componentsschemasdbv0_0_37_tres_list_item_data
                )

                allocated.append(componentsschemasdbv0_0_37_tres_list_item)

        dbv_0037_job_step_tres = cls(
            requested=requested,
            consumed=consumed,
            allocated=allocated,
        )

        dbv_0037_job_step_tres.additional_properties = d
        return dbv_0037_job_step_tres

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
