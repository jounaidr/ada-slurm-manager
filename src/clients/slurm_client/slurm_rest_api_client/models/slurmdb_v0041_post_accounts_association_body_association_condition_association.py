from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.slurmdb_v0041_post_accounts_association_body_association_condition_association_grpjobs import (
        SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationGrpjobs,
    )
    from ..models.slurmdb_v0041_post_accounts_association_body_association_condition_association_grpjobsaccrue import (
        SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationGrpjobsaccrue,
    )
    from ..models.slurmdb_v0041_post_accounts_association_body_association_condition_association_grpsubmitjobs import (
        SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationGrpsubmitjobs,
    )
    from ..models.slurmdb_v0041_post_accounts_association_body_association_condition_association_grptres_item import (
        SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationGrptresItem,
    )
    from ..models.slurmdb_v0041_post_accounts_association_body_association_condition_association_grptresmins_item import (
        SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationGrptresminsItem,
    )
    from ..models.slurmdb_v0041_post_accounts_association_body_association_condition_association_grptresrunmins_item import (
        SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationGrptresrunminsItem,
    )
    from ..models.slurmdb_v0041_post_accounts_association_body_association_condition_association_grpwall import (
        SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationGrpwall,
    )
    from ..models.slurmdb_v0041_post_accounts_association_body_association_condition_association_maxjobs import (
        SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationMaxjobs,
    )
    from ..models.slurmdb_v0041_post_accounts_association_body_association_condition_association_maxjobsaccrue import (
        SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationMaxjobsaccrue,
    )
    from ..models.slurmdb_v0041_post_accounts_association_body_association_condition_association_maxsubmitjobs import (
        SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationMaxsubmitjobs,
    )
    from ..models.slurmdb_v0041_post_accounts_association_body_association_condition_association_maxtresminsperjob_item import (
        SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationMaxtresminsperjobItem,
    )
    from ..models.slurmdb_v0041_post_accounts_association_body_association_condition_association_maxtresperjob_item import (
        SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationMaxtresperjobItem,
    )
    from ..models.slurmdb_v0041_post_accounts_association_body_association_condition_association_maxtrespernode_item import (
        SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationMaxtrespernodeItem,
    )
    from ..models.slurmdb_v0041_post_accounts_association_body_association_condition_association_maxtresrunmins_item import (
        SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationMaxtresrunminsItem,
    )
    from ..models.slurmdb_v0041_post_accounts_association_body_association_condition_association_maxwalldurationperjob import (
        SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationMaxwalldurationperjob,
    )
    from ..models.slurmdb_v0041_post_accounts_association_body_association_condition_association_minpriothresh import (
        SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationMinpriothresh,
    )
    from ..models.slurmdb_v0041_post_accounts_association_body_association_condition_association_priority import (
        SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationPriority,
    )


T = TypeVar("T", bound="SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociation")


@_attrs_define
class SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociation:
    """Association limits and options

    Attributes:
        comment (str | Unset): Arbitrary comment
        defaultqos (str | Unset): Default QOS
        grpjobs (SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationGrpjobs | Unset): Maximum number
            of running jobs in this association and its children
        grpjobsaccrue (SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationGrpjobsaccrue | Unset):
            Maximum number of pending jobs able to accrue age priority in this association and its children
        grpsubmitjobs (SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationGrpsubmitjobs | Unset):
            Maximum number of jobs which can be in a pending or running state at any time in this association and its
            children
        grptres (list[SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationGrptresItem] | Unset):
            Maximum number of TRES able to be allocated by running jobs in this association and its children
        grptresmins (list[SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationGrptresminsItem] |
            Unset): Total number of TRES minutes that can possibly be used by past, present and future jobs in this
            association and its children
        grptresrunmins (list[SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationGrptresrunminsItem] |
            Unset): Maximum number of TRES minutes able to be allocated by running jobs in this association and its children
        grpwall (SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationGrpwall | Unset): Maximum wall
            clock time in minutes able to be allocated by running jobs in this association and its children
        maxjobs (SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationMaxjobs | Unset): Maximum number
            of running jobs per user in this association
        maxjobsaccrue (SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationMaxjobsaccrue | Unset):
            Maximum number of pending jobs able to accrue age priority at any given time in this association
        maxsubmitjobs (SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationMaxsubmitjobs | Unset):
            Maximum number of jobs which can be in a pending or running state at any time in this association
        maxtresminsperjob
            (list[SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationMaxtresminsperjobItem] | Unset):
            Maximum number of TRES minutes each job is able to use in this association
        maxtresrunmins (list[SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationMaxtresrunminsItem] |
            Unset): Maximum number of TRES minutes able to be allocated by running jobs in this association
        maxtresperjob (list[SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationMaxtresperjobItem] |
            Unset): Maximum number of TRES each job is able to use in this association
        maxtrespernode (list[SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationMaxtrespernodeItem] |
            Unset): Maximum number of TRES each node is able to use
        maxwalldurationperjob
            (SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationMaxwalldurationperjob | Unset): Maximum
            wall clock time each job is able to use in this association
        minpriothresh (SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationMinpriothresh | Unset):
            Minimum priority required to reserve resources when scheduling
        parent (str | Unset): Name of parent account
        priority (SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationPriority | Unset): Association
            priority factor
        qoslevel (list[str] | Unset): List of available QOS names
        fairshare (int | Unset): Allocated shares used for fairshare calculation
    """

    comment: str | Unset = UNSET
    defaultqos: str | Unset = UNSET
    grpjobs: SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationGrpjobs | Unset = UNSET
    grpjobsaccrue: SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationGrpjobsaccrue | Unset = UNSET
    grpsubmitjobs: SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationGrpsubmitjobs | Unset = UNSET
    grptres: list[SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationGrptresItem] | Unset = UNSET
    grptresmins: list[SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationGrptresminsItem] | Unset = (
        UNSET
    )
    grptresrunmins: (
        list[SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationGrptresrunminsItem] | Unset
    ) = UNSET
    grpwall: SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationGrpwall | Unset = UNSET
    maxjobs: SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationMaxjobs | Unset = UNSET
    maxjobsaccrue: SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationMaxjobsaccrue | Unset = UNSET
    maxsubmitjobs: SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationMaxsubmitjobs | Unset = UNSET
    maxtresminsperjob: (
        list[SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationMaxtresminsperjobItem] | Unset
    ) = UNSET
    maxtresrunmins: (
        list[SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationMaxtresrunminsItem] | Unset
    ) = UNSET
    maxtresperjob: (
        list[SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationMaxtresperjobItem] | Unset
    ) = UNSET
    maxtrespernode: (
        list[SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationMaxtrespernodeItem] | Unset
    ) = UNSET
    maxwalldurationperjob: (
        SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationMaxwalldurationperjob | Unset
    ) = UNSET
    minpriothresh: SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationMinpriothresh | Unset = UNSET
    parent: str | Unset = UNSET
    priority: SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationPriority | Unset = UNSET
    qoslevel: list[str] | Unset = UNSET
    fairshare: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        comment = self.comment

        defaultqos = self.defaultqos

        grpjobs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.grpjobs, Unset):
            grpjobs = self.grpjobs.to_dict()

        grpjobsaccrue: dict[str, Any] | Unset = UNSET
        if not isinstance(self.grpjobsaccrue, Unset):
            grpjobsaccrue = self.grpjobsaccrue.to_dict()

        grpsubmitjobs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.grpsubmitjobs, Unset):
            grpsubmitjobs = self.grpsubmitjobs.to_dict()

        grptres: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.grptres, Unset):
            grptres = []
            for grptres_item_data in self.grptres:
                grptres_item = grptres_item_data.to_dict()
                grptres.append(grptres_item)

        grptresmins: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.grptresmins, Unset):
            grptresmins = []
            for grptresmins_item_data in self.grptresmins:
                grptresmins_item = grptresmins_item_data.to_dict()
                grptresmins.append(grptresmins_item)

        grptresrunmins: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.grptresrunmins, Unset):
            grptresrunmins = []
            for grptresrunmins_item_data in self.grptresrunmins:
                grptresrunmins_item = grptresrunmins_item_data.to_dict()
                grptresrunmins.append(grptresrunmins_item)

        grpwall: dict[str, Any] | Unset = UNSET
        if not isinstance(self.grpwall, Unset):
            grpwall = self.grpwall.to_dict()

        maxjobs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.maxjobs, Unset):
            maxjobs = self.maxjobs.to_dict()

        maxjobsaccrue: dict[str, Any] | Unset = UNSET
        if not isinstance(self.maxjobsaccrue, Unset):
            maxjobsaccrue = self.maxjobsaccrue.to_dict()

        maxsubmitjobs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.maxsubmitjobs, Unset):
            maxsubmitjobs = self.maxsubmitjobs.to_dict()

        maxtresminsperjob: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.maxtresminsperjob, Unset):
            maxtresminsperjob = []
            for maxtresminsperjob_item_data in self.maxtresminsperjob:
                maxtresminsperjob_item = maxtresminsperjob_item_data.to_dict()
                maxtresminsperjob.append(maxtresminsperjob_item)

        maxtresrunmins: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.maxtresrunmins, Unset):
            maxtresrunmins = []
            for maxtresrunmins_item_data in self.maxtresrunmins:
                maxtresrunmins_item = maxtresrunmins_item_data.to_dict()
                maxtresrunmins.append(maxtresrunmins_item)

        maxtresperjob: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.maxtresperjob, Unset):
            maxtresperjob = []
            for maxtresperjob_item_data in self.maxtresperjob:
                maxtresperjob_item = maxtresperjob_item_data.to_dict()
                maxtresperjob.append(maxtresperjob_item)

        maxtrespernode: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.maxtrespernode, Unset):
            maxtrespernode = []
            for maxtrespernode_item_data in self.maxtrespernode:
                maxtrespernode_item = maxtrespernode_item_data.to_dict()
                maxtrespernode.append(maxtrespernode_item)

        maxwalldurationperjob: dict[str, Any] | Unset = UNSET
        if not isinstance(self.maxwalldurationperjob, Unset):
            maxwalldurationperjob = self.maxwalldurationperjob.to_dict()

        minpriothresh: dict[str, Any] | Unset = UNSET
        if not isinstance(self.minpriothresh, Unset):
            minpriothresh = self.minpriothresh.to_dict()

        parent = self.parent

        priority: dict[str, Any] | Unset = UNSET
        if not isinstance(self.priority, Unset):
            priority = self.priority.to_dict()

        qoslevel: list[str] | Unset = UNSET
        if not isinstance(self.qoslevel, Unset):
            qoslevel = self.qoslevel

        fairshare = self.fairshare

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if comment is not UNSET:
            field_dict["comment"] = comment
        if defaultqos is not UNSET:
            field_dict["defaultqos"] = defaultqos
        if grpjobs is not UNSET:
            field_dict["grpjobs"] = grpjobs
        if grpjobsaccrue is not UNSET:
            field_dict["grpjobsaccrue"] = grpjobsaccrue
        if grpsubmitjobs is not UNSET:
            field_dict["grpsubmitjobs"] = grpsubmitjobs
        if grptres is not UNSET:
            field_dict["grptres"] = grptres
        if grptresmins is not UNSET:
            field_dict["grptresmins"] = grptresmins
        if grptresrunmins is not UNSET:
            field_dict["grptresrunmins"] = grptresrunmins
        if grpwall is not UNSET:
            field_dict["grpwall"] = grpwall
        if maxjobs is not UNSET:
            field_dict["maxjobs"] = maxjobs
        if maxjobsaccrue is not UNSET:
            field_dict["maxjobsaccrue"] = maxjobsaccrue
        if maxsubmitjobs is not UNSET:
            field_dict["maxsubmitjobs"] = maxsubmitjobs
        if maxtresminsperjob is not UNSET:
            field_dict["maxtresminsperjob"] = maxtresminsperjob
        if maxtresrunmins is not UNSET:
            field_dict["maxtresrunmins"] = maxtresrunmins
        if maxtresperjob is not UNSET:
            field_dict["maxtresperjob"] = maxtresperjob
        if maxtrespernode is not UNSET:
            field_dict["maxtrespernode"] = maxtrespernode
        if maxwalldurationperjob is not UNSET:
            field_dict["maxwalldurationperjob"] = maxwalldurationperjob
        if minpriothresh is not UNSET:
            field_dict["minpriothresh"] = minpriothresh
        if parent is not UNSET:
            field_dict["parent"] = parent
        if priority is not UNSET:
            field_dict["priority"] = priority
        if qoslevel is not UNSET:
            field_dict["qoslevel"] = qoslevel
        if fairshare is not UNSET:
            field_dict["fairshare"] = fairshare

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.slurmdb_v0041_post_accounts_association_body_association_condition_association_grpjobs import (
            SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationGrpjobs,
        )
        from ..models.slurmdb_v0041_post_accounts_association_body_association_condition_association_grpjobsaccrue import (
            SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationGrpjobsaccrue,
        )
        from ..models.slurmdb_v0041_post_accounts_association_body_association_condition_association_grpsubmitjobs import (
            SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationGrpsubmitjobs,
        )
        from ..models.slurmdb_v0041_post_accounts_association_body_association_condition_association_grptres_item import (
            SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationGrptresItem,
        )
        from ..models.slurmdb_v0041_post_accounts_association_body_association_condition_association_grptresmins_item import (
            SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationGrptresminsItem,
        )
        from ..models.slurmdb_v0041_post_accounts_association_body_association_condition_association_grptresrunmins_item import (
            SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationGrptresrunminsItem,
        )
        from ..models.slurmdb_v0041_post_accounts_association_body_association_condition_association_grpwall import (
            SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationGrpwall,
        )
        from ..models.slurmdb_v0041_post_accounts_association_body_association_condition_association_maxjobs import (
            SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationMaxjobs,
        )
        from ..models.slurmdb_v0041_post_accounts_association_body_association_condition_association_maxjobsaccrue import (
            SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationMaxjobsaccrue,
        )
        from ..models.slurmdb_v0041_post_accounts_association_body_association_condition_association_maxsubmitjobs import (
            SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationMaxsubmitjobs,
        )
        from ..models.slurmdb_v0041_post_accounts_association_body_association_condition_association_maxtresminsperjob_item import (
            SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationMaxtresminsperjobItem,
        )
        from ..models.slurmdb_v0041_post_accounts_association_body_association_condition_association_maxtresperjob_item import (
            SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationMaxtresperjobItem,
        )
        from ..models.slurmdb_v0041_post_accounts_association_body_association_condition_association_maxtrespernode_item import (
            SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationMaxtrespernodeItem,
        )
        from ..models.slurmdb_v0041_post_accounts_association_body_association_condition_association_maxtresrunmins_item import (
            SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationMaxtresrunminsItem,
        )
        from ..models.slurmdb_v0041_post_accounts_association_body_association_condition_association_maxwalldurationperjob import (
            SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationMaxwalldurationperjob,
        )
        from ..models.slurmdb_v0041_post_accounts_association_body_association_condition_association_minpriothresh import (
            SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationMinpriothresh,
        )
        from ..models.slurmdb_v0041_post_accounts_association_body_association_condition_association_priority import (
            SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationPriority,
        )

        d = dict(src_dict)
        comment = d.pop("comment", UNSET)

        defaultqos = d.pop("defaultqos", UNSET)

        _grpjobs = d.pop("grpjobs", UNSET)
        grpjobs: SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationGrpjobs | Unset
        if isinstance(_grpjobs, Unset):
            grpjobs = UNSET
        else:
            grpjobs = SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationGrpjobs.from_dict(_grpjobs)

        _grpjobsaccrue = d.pop("grpjobsaccrue", UNSET)
        grpjobsaccrue: SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationGrpjobsaccrue | Unset
        if isinstance(_grpjobsaccrue, Unset):
            grpjobsaccrue = UNSET
        else:
            grpjobsaccrue = (
                SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationGrpjobsaccrue.from_dict(
                    _grpjobsaccrue
                )
            )

        _grpsubmitjobs = d.pop("grpsubmitjobs", UNSET)
        grpsubmitjobs: SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationGrpsubmitjobs | Unset
        if isinstance(_grpsubmitjobs, Unset):
            grpsubmitjobs = UNSET
        else:
            grpsubmitjobs = (
                SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationGrpsubmitjobs.from_dict(
                    _grpsubmitjobs
                )
            )

        _grptres = d.pop("grptres", UNSET)
        grptres: list[SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationGrptresItem] | Unset = UNSET
        if _grptres is not UNSET:
            grptres = []
            for grptres_item_data in _grptres:
                grptres_item = (
                    SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationGrptresItem.from_dict(
                        grptres_item_data
                    )
                )

                grptres.append(grptres_item)

        _grptresmins = d.pop("grptresmins", UNSET)
        grptresmins: (
            list[SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationGrptresminsItem] | Unset
        ) = UNSET
        if _grptresmins is not UNSET:
            grptresmins = []
            for grptresmins_item_data in _grptresmins:
                grptresmins_item = (
                    SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationGrptresminsItem.from_dict(
                        grptresmins_item_data
                    )
                )

                grptresmins.append(grptresmins_item)

        _grptresrunmins = d.pop("grptresrunmins", UNSET)
        grptresrunmins: (
            list[SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationGrptresrunminsItem] | Unset
        ) = UNSET
        if _grptresrunmins is not UNSET:
            grptresrunmins = []
            for grptresrunmins_item_data in _grptresrunmins:
                grptresrunmins_item = (
                    SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationGrptresrunminsItem.from_dict(
                        grptresrunmins_item_data
                    )
                )

                grptresrunmins.append(grptresrunmins_item)

        _grpwall = d.pop("grpwall", UNSET)
        grpwall: SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationGrpwall | Unset
        if isinstance(_grpwall, Unset):
            grpwall = UNSET
        else:
            grpwall = SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationGrpwall.from_dict(_grpwall)

        _maxjobs = d.pop("maxjobs", UNSET)
        maxjobs: SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationMaxjobs | Unset
        if isinstance(_maxjobs, Unset):
            maxjobs = UNSET
        else:
            maxjobs = SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationMaxjobs.from_dict(_maxjobs)

        _maxjobsaccrue = d.pop("maxjobsaccrue", UNSET)
        maxjobsaccrue: SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationMaxjobsaccrue | Unset
        if isinstance(_maxjobsaccrue, Unset):
            maxjobsaccrue = UNSET
        else:
            maxjobsaccrue = (
                SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationMaxjobsaccrue.from_dict(
                    _maxjobsaccrue
                )
            )

        _maxsubmitjobs = d.pop("maxsubmitjobs", UNSET)
        maxsubmitjobs: SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationMaxsubmitjobs | Unset
        if isinstance(_maxsubmitjobs, Unset):
            maxsubmitjobs = UNSET
        else:
            maxsubmitjobs = (
                SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationMaxsubmitjobs.from_dict(
                    _maxsubmitjobs
                )
            )

        _maxtresminsperjob = d.pop("maxtresminsperjob", UNSET)
        maxtresminsperjob: (
            list[SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationMaxtresminsperjobItem] | Unset
        ) = UNSET
        if _maxtresminsperjob is not UNSET:
            maxtresminsperjob = []
            for maxtresminsperjob_item_data in _maxtresminsperjob:
                maxtresminsperjob_item = SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationMaxtresminsperjobItem.from_dict(
                    maxtresminsperjob_item_data
                )

                maxtresminsperjob.append(maxtresminsperjob_item)

        _maxtresrunmins = d.pop("maxtresrunmins", UNSET)
        maxtresrunmins: (
            list[SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationMaxtresrunminsItem] | Unset
        ) = UNSET
        if _maxtresrunmins is not UNSET:
            maxtresrunmins = []
            for maxtresrunmins_item_data in _maxtresrunmins:
                maxtresrunmins_item = (
                    SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationMaxtresrunminsItem.from_dict(
                        maxtresrunmins_item_data
                    )
                )

                maxtresrunmins.append(maxtresrunmins_item)

        _maxtresperjob = d.pop("maxtresperjob", UNSET)
        maxtresperjob: (
            list[SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationMaxtresperjobItem] | Unset
        ) = UNSET
        if _maxtresperjob is not UNSET:
            maxtresperjob = []
            for maxtresperjob_item_data in _maxtresperjob:
                maxtresperjob_item = (
                    SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationMaxtresperjobItem.from_dict(
                        maxtresperjob_item_data
                    )
                )

                maxtresperjob.append(maxtresperjob_item)

        _maxtrespernode = d.pop("maxtrespernode", UNSET)
        maxtrespernode: (
            list[SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationMaxtrespernodeItem] | Unset
        ) = UNSET
        if _maxtrespernode is not UNSET:
            maxtrespernode = []
            for maxtrespernode_item_data in _maxtrespernode:
                maxtrespernode_item = (
                    SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationMaxtrespernodeItem.from_dict(
                        maxtrespernode_item_data
                    )
                )

                maxtrespernode.append(maxtrespernode_item)

        _maxwalldurationperjob = d.pop("maxwalldurationperjob", UNSET)
        maxwalldurationperjob: (
            SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationMaxwalldurationperjob | Unset
        )
        if isinstance(_maxwalldurationperjob, Unset):
            maxwalldurationperjob = UNSET
        else:
            maxwalldurationperjob = (
                SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationMaxwalldurationperjob.from_dict(
                    _maxwalldurationperjob
                )
            )

        _minpriothresh = d.pop("minpriothresh", UNSET)
        minpriothresh: SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationMinpriothresh | Unset
        if isinstance(_minpriothresh, Unset):
            minpriothresh = UNSET
        else:
            minpriothresh = (
                SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationMinpriothresh.from_dict(
                    _minpriothresh
                )
            )

        parent = d.pop("parent", UNSET)

        _priority = d.pop("priority", UNSET)
        priority: SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationPriority | Unset
        if isinstance(_priority, Unset):
            priority = UNSET
        else:
            priority = SlurmdbV0041PostAccountsAssociationBodyAssociationConditionAssociationPriority.from_dict(
                _priority
            )

        qoslevel = cast(list[str], d.pop("qoslevel", UNSET))

        fairshare = d.pop("fairshare", UNSET)

        slurmdb_v0041_post_accounts_association_body_association_condition_association = cls(
            comment=comment,
            defaultqos=defaultqos,
            grpjobs=grpjobs,
            grpjobsaccrue=grpjobsaccrue,
            grpsubmitjobs=grpsubmitjobs,
            grptres=grptres,
            grptresmins=grptresmins,
            grptresrunmins=grptresrunmins,
            grpwall=grpwall,
            maxjobs=maxjobs,
            maxjobsaccrue=maxjobsaccrue,
            maxsubmitjobs=maxsubmitjobs,
            maxtresminsperjob=maxtresminsperjob,
            maxtresrunmins=maxtresrunmins,
            maxtresperjob=maxtresperjob,
            maxtrespernode=maxtrespernode,
            maxwalldurationperjob=maxwalldurationperjob,
            minpriothresh=minpriothresh,
            parent=parent,
            priority=priority,
            qoslevel=qoslevel,
            fairshare=fairshare,
        )

        slurmdb_v0041_post_accounts_association_body_association_condition_association.additional_properties = d
        return slurmdb_v0041_post_accounts_association_body_association_condition_association

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
