from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v0041_openapi_slurmdbd_config_resp_associations_item_max_jobs_accruing import (
        V0041OpenapiSlurmdbdConfigRespAssociationsItemMaxJobsAccruing,
    )
    from ..models.v0041_openapi_slurmdbd_config_resp_associations_item_max_jobs_active import (
        V0041OpenapiSlurmdbdConfigRespAssociationsItemMaxJobsActive,
    )
    from ..models.v0041_openapi_slurmdbd_config_resp_associations_item_max_jobs_per import (
        V0041OpenapiSlurmdbdConfigRespAssociationsItemMaxJobsPer,
    )
    from ..models.v0041_openapi_slurmdbd_config_resp_associations_item_max_jobs_total import (
        V0041OpenapiSlurmdbdConfigRespAssociationsItemMaxJobsTotal,
    )


T = TypeVar("T", bound="V0041OpenapiSlurmdbdConfigRespAssociationsItemMaxJobs")


@_attrs_define
class V0041OpenapiSlurmdbdConfigRespAssociationsItemMaxJobs:
    """
    Attributes:
        per (V0041OpenapiSlurmdbdConfigRespAssociationsItemMaxJobsPer | Unset):
        active (V0041OpenapiSlurmdbdConfigRespAssociationsItemMaxJobsActive | Unset): MaxJobs
        accruing (V0041OpenapiSlurmdbdConfigRespAssociationsItemMaxJobsAccruing | Unset): MaxJobsAccrue
        total (V0041OpenapiSlurmdbdConfigRespAssociationsItemMaxJobsTotal | Unset): MaxSubmitJobs
    """

    per: V0041OpenapiSlurmdbdConfigRespAssociationsItemMaxJobsPer | Unset = UNSET
    active: V0041OpenapiSlurmdbdConfigRespAssociationsItemMaxJobsActive | Unset = UNSET
    accruing: V0041OpenapiSlurmdbdConfigRespAssociationsItemMaxJobsAccruing | Unset = UNSET
    total: V0041OpenapiSlurmdbdConfigRespAssociationsItemMaxJobsTotal | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        per: dict[str, Any] | Unset = UNSET
        if not isinstance(self.per, Unset):
            per = self.per.to_dict()

        active: dict[str, Any] | Unset = UNSET
        if not isinstance(self.active, Unset):
            active = self.active.to_dict()

        accruing: dict[str, Any] | Unset = UNSET
        if not isinstance(self.accruing, Unset):
            accruing = self.accruing.to_dict()

        total: dict[str, Any] | Unset = UNSET
        if not isinstance(self.total, Unset):
            total = self.total.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if per is not UNSET:
            field_dict["per"] = per
        if active is not UNSET:
            field_dict["active"] = active
        if accruing is not UNSET:
            field_dict["accruing"] = accruing
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v0041_openapi_slurmdbd_config_resp_associations_item_max_jobs_accruing import (
            V0041OpenapiSlurmdbdConfigRespAssociationsItemMaxJobsAccruing,
        )
        from ..models.v0041_openapi_slurmdbd_config_resp_associations_item_max_jobs_active import (
            V0041OpenapiSlurmdbdConfigRespAssociationsItemMaxJobsActive,
        )
        from ..models.v0041_openapi_slurmdbd_config_resp_associations_item_max_jobs_per import (
            V0041OpenapiSlurmdbdConfigRespAssociationsItemMaxJobsPer,
        )
        from ..models.v0041_openapi_slurmdbd_config_resp_associations_item_max_jobs_total import (
            V0041OpenapiSlurmdbdConfigRespAssociationsItemMaxJobsTotal,
        )

        d = dict(src_dict)
        _per = d.pop("per", UNSET)
        per: V0041OpenapiSlurmdbdConfigRespAssociationsItemMaxJobsPer | Unset
        if isinstance(_per, Unset):
            per = UNSET
        else:
            per = V0041OpenapiSlurmdbdConfigRespAssociationsItemMaxJobsPer.from_dict(_per)

        _active = d.pop("active", UNSET)
        active: V0041OpenapiSlurmdbdConfigRespAssociationsItemMaxJobsActive | Unset
        if isinstance(_active, Unset):
            active = UNSET
        else:
            active = V0041OpenapiSlurmdbdConfigRespAssociationsItemMaxJobsActive.from_dict(_active)

        _accruing = d.pop("accruing", UNSET)
        accruing: V0041OpenapiSlurmdbdConfigRespAssociationsItemMaxJobsAccruing | Unset
        if isinstance(_accruing, Unset):
            accruing = UNSET
        else:
            accruing = V0041OpenapiSlurmdbdConfigRespAssociationsItemMaxJobsAccruing.from_dict(_accruing)

        _total = d.pop("total", UNSET)
        total: V0041OpenapiSlurmdbdConfigRespAssociationsItemMaxJobsTotal | Unset
        if isinstance(_total, Unset):
            total = UNSET
        else:
            total = V0041OpenapiSlurmdbdConfigRespAssociationsItemMaxJobsTotal.from_dict(_total)

        v0041_openapi_slurmdbd_config_resp_associations_item_max_jobs = cls(
            per=per,
            active=active,
            accruing=accruing,
            total=total,
        )

        v0041_openapi_slurmdbd_config_resp_associations_item_max_jobs.additional_properties = d
        return v0041_openapi_slurmdbd_config_resp_associations_item_max_jobs

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
