from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v0041_openapi_slurmdbd_jobs_resp_jobs_item_steps_item_tres_consumed_average_item import (
        V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemTresConsumedAverageItem,
    )
    from ..models.v0041_openapi_slurmdbd_jobs_resp_jobs_item_steps_item_tres_consumed_max_item import (
        V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemTresConsumedMaxItem,
    )
    from ..models.v0041_openapi_slurmdbd_jobs_resp_jobs_item_steps_item_tres_consumed_min_item import (
        V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemTresConsumedMinItem,
    )
    from ..models.v0041_openapi_slurmdbd_jobs_resp_jobs_item_steps_item_tres_consumed_total_item import (
        V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemTresConsumedTotalItem,
    )


T = TypeVar("T", bound="V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemTresConsumed")


@_attrs_define
class V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemTresConsumed:
    """
    Attributes:
        max_ (list[V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemTresConsumedMaxItem] | Unset): Maximum TRES usage
            consumed among all tasks
        min_ (list[V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemTresConsumedMinItem] | Unset): Minimum TRES usage
            consumed among all tasks
        average (list[V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemTresConsumedAverageItem] | Unset): Average TRES usage
            consumed among all tasks
        total (list[V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemTresConsumedTotalItem] | Unset): Total TRES usage
            consumed among all tasks
    """

    max_: list[V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemTresConsumedMaxItem] | Unset = UNSET
    min_: list[V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemTresConsumedMinItem] | Unset = UNSET
    average: list[V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemTresConsumedAverageItem] | Unset = UNSET
    total: list[V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemTresConsumedTotalItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        max_: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.max_, Unset):
            max_ = []
            for max_item_data in self.max_:
                max_item = max_item_data.to_dict()
                max_.append(max_item)

        min_: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.min_, Unset):
            min_ = []
            for min_item_data in self.min_:
                min_item = min_item_data.to_dict()
                min_.append(min_item)

        average: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.average, Unset):
            average = []
            for average_item_data in self.average:
                average_item = average_item_data.to_dict()
                average.append(average_item)

        total: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.total, Unset):
            total = []
            for total_item_data in self.total:
                total_item = total_item_data.to_dict()
                total.append(total_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if max_ is not UNSET:
            field_dict["max"] = max_
        if min_ is not UNSET:
            field_dict["min"] = min_
        if average is not UNSET:
            field_dict["average"] = average
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v0041_openapi_slurmdbd_jobs_resp_jobs_item_steps_item_tres_consumed_average_item import (
            V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemTresConsumedAverageItem,
        )
        from ..models.v0041_openapi_slurmdbd_jobs_resp_jobs_item_steps_item_tres_consumed_max_item import (
            V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemTresConsumedMaxItem,
        )
        from ..models.v0041_openapi_slurmdbd_jobs_resp_jobs_item_steps_item_tres_consumed_min_item import (
            V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemTresConsumedMinItem,
        )
        from ..models.v0041_openapi_slurmdbd_jobs_resp_jobs_item_steps_item_tres_consumed_total_item import (
            V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemTresConsumedTotalItem,
        )

        d = dict(src_dict)
        _max_ = d.pop("max", UNSET)
        max_: list[V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemTresConsumedMaxItem] | Unset = UNSET
        if _max_ is not UNSET:
            max_ = []
            for max_item_data in _max_:
                max_item = V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemTresConsumedMaxItem.from_dict(max_item_data)

                max_.append(max_item)

        _min_ = d.pop("min", UNSET)
        min_: list[V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemTresConsumedMinItem] | Unset = UNSET
        if _min_ is not UNSET:
            min_ = []
            for min_item_data in _min_:
                min_item = V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemTresConsumedMinItem.from_dict(min_item_data)

                min_.append(min_item)

        _average = d.pop("average", UNSET)
        average: list[V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemTresConsumedAverageItem] | Unset = UNSET
        if _average is not UNSET:
            average = []
            for average_item_data in _average:
                average_item = V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemTresConsumedAverageItem.from_dict(
                    average_item_data
                )

                average.append(average_item)

        _total = d.pop("total", UNSET)
        total: list[V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemTresConsumedTotalItem] | Unset = UNSET
        if _total is not UNSET:
            total = []
            for total_item_data in _total:
                total_item = V0041OpenapiSlurmdbdJobsRespJobsItemStepsItemTresConsumedTotalItem.from_dict(
                    total_item_data
                )

                total.append(total_item)

        v0041_openapi_slurmdbd_jobs_resp_jobs_item_steps_item_tres_consumed = cls(
            max_=max_,
            min_=min_,
            average=average,
            total=total,
        )

        v0041_openapi_slurmdbd_jobs_resp_jobs_item_steps_item_tres_consumed.additional_properties = d
        return v0041_openapi_slurmdbd_jobs_resp_jobs_item_steps_item_tres_consumed

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
