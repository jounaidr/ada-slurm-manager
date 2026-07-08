from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v0042_tres import V0042Tres
    from ..models.v0042_uint_32_no_val_struct import V0042Uint32NoValStruct


T = TypeVar("T", bound="V0042AssocRecSet")


@_attrs_define
class V0042AssocRecSet:
    """
    Attributes:
        comment (str | Unset): Arbitrary comment
        defaultqos (str | Unset): Default QOS
        grpjobs (V0042Uint32NoValStruct | Unset):
        grpjobsaccrue (V0042Uint32NoValStruct | Unset):
        grpsubmitjobs (V0042Uint32NoValStruct | Unset):
        grptres (list[V0042Tres] | Unset):
        grptresmins (list[V0042Tres] | Unset):
        grptresrunmins (list[V0042Tres] | Unset):
        grpwall (V0042Uint32NoValStruct | Unset):
        maxjobs (V0042Uint32NoValStruct | Unset):
        maxjobsaccrue (V0042Uint32NoValStruct | Unset):
        maxsubmitjobs (V0042Uint32NoValStruct | Unset):
        maxtresminsperjob (list[V0042Tres] | Unset):
        maxtresrunmins (list[V0042Tres] | Unset):
        maxtresperjob (list[V0042Tres] | Unset):
        maxtrespernode (list[V0042Tres] | Unset):
        maxwalldurationperjob (V0042Uint32NoValStruct | Unset):
        minpriothresh (V0042Uint32NoValStruct | Unset):
        parent (str | Unset): Name of parent account
        priority (V0042Uint32NoValStruct | Unset):
        qoslevel (list[str] | Unset): List of QOS names
        fairshare (int | Unset): Allocated shares used for fairshare calculation
    """

    comment: str | Unset = UNSET
    defaultqos: str | Unset = UNSET
    grpjobs: V0042Uint32NoValStruct | Unset = UNSET
    grpjobsaccrue: V0042Uint32NoValStruct | Unset = UNSET
    grpsubmitjobs: V0042Uint32NoValStruct | Unset = UNSET
    grptres: list[V0042Tres] | Unset = UNSET
    grptresmins: list[V0042Tres] | Unset = UNSET
    grptresrunmins: list[V0042Tres] | Unset = UNSET
    grpwall: V0042Uint32NoValStruct | Unset = UNSET
    maxjobs: V0042Uint32NoValStruct | Unset = UNSET
    maxjobsaccrue: V0042Uint32NoValStruct | Unset = UNSET
    maxsubmitjobs: V0042Uint32NoValStruct | Unset = UNSET
    maxtresminsperjob: list[V0042Tres] | Unset = UNSET
    maxtresrunmins: list[V0042Tres] | Unset = UNSET
    maxtresperjob: list[V0042Tres] | Unset = UNSET
    maxtrespernode: list[V0042Tres] | Unset = UNSET
    maxwalldurationperjob: V0042Uint32NoValStruct | Unset = UNSET
    minpriothresh: V0042Uint32NoValStruct | Unset = UNSET
    parent: str | Unset = UNSET
    priority: V0042Uint32NoValStruct | Unset = UNSET
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
            for componentsschemasv0_0_42_tres_list_item_data in self.grptres:
                componentsschemasv0_0_42_tres_list_item = componentsschemasv0_0_42_tres_list_item_data.to_dict()
                grptres.append(componentsschemasv0_0_42_tres_list_item)

        grptresmins: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.grptresmins, Unset):
            grptresmins = []
            for componentsschemasv0_0_42_tres_list_item_data in self.grptresmins:
                componentsschemasv0_0_42_tres_list_item = componentsschemasv0_0_42_tres_list_item_data.to_dict()
                grptresmins.append(componentsschemasv0_0_42_tres_list_item)

        grptresrunmins: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.grptresrunmins, Unset):
            grptresrunmins = []
            for componentsschemasv0_0_42_tres_list_item_data in self.grptresrunmins:
                componentsschemasv0_0_42_tres_list_item = componentsschemasv0_0_42_tres_list_item_data.to_dict()
                grptresrunmins.append(componentsschemasv0_0_42_tres_list_item)

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
            for componentsschemasv0_0_42_tres_list_item_data in self.maxtresminsperjob:
                componentsschemasv0_0_42_tres_list_item = componentsschemasv0_0_42_tres_list_item_data.to_dict()
                maxtresminsperjob.append(componentsschemasv0_0_42_tres_list_item)

        maxtresrunmins: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.maxtresrunmins, Unset):
            maxtresrunmins = []
            for componentsschemasv0_0_42_tres_list_item_data in self.maxtresrunmins:
                componentsschemasv0_0_42_tres_list_item = componentsschemasv0_0_42_tres_list_item_data.to_dict()
                maxtresrunmins.append(componentsschemasv0_0_42_tres_list_item)

        maxtresperjob: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.maxtresperjob, Unset):
            maxtresperjob = []
            for componentsschemasv0_0_42_tres_list_item_data in self.maxtresperjob:
                componentsschemasv0_0_42_tres_list_item = componentsschemasv0_0_42_tres_list_item_data.to_dict()
                maxtresperjob.append(componentsschemasv0_0_42_tres_list_item)

        maxtrespernode: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.maxtrespernode, Unset):
            maxtrespernode = []
            for componentsschemasv0_0_42_tres_list_item_data in self.maxtrespernode:
                componentsschemasv0_0_42_tres_list_item = componentsschemasv0_0_42_tres_list_item_data.to_dict()
                maxtrespernode.append(componentsschemasv0_0_42_tres_list_item)

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
        from ..models.v0042_tres import V0042Tres
        from ..models.v0042_uint_32_no_val_struct import V0042Uint32NoValStruct

        d = dict(src_dict)
        comment = d.pop("comment", UNSET)

        defaultqos = d.pop("defaultqos", UNSET)

        _grpjobs = d.pop("grpjobs", UNSET)
        grpjobs: V0042Uint32NoValStruct | Unset
        if isinstance(_grpjobs, Unset):
            grpjobs = UNSET
        else:
            grpjobs = V0042Uint32NoValStruct.from_dict(_grpjobs)

        _grpjobsaccrue = d.pop("grpjobsaccrue", UNSET)
        grpjobsaccrue: V0042Uint32NoValStruct | Unset
        if isinstance(_grpjobsaccrue, Unset):
            grpjobsaccrue = UNSET
        else:
            grpjobsaccrue = V0042Uint32NoValStruct.from_dict(_grpjobsaccrue)

        _grpsubmitjobs = d.pop("grpsubmitjobs", UNSET)
        grpsubmitjobs: V0042Uint32NoValStruct | Unset
        if isinstance(_grpsubmitjobs, Unset):
            grpsubmitjobs = UNSET
        else:
            grpsubmitjobs = V0042Uint32NoValStruct.from_dict(_grpsubmitjobs)

        _grptres = d.pop("grptres", UNSET)
        grptres: list[V0042Tres] | Unset = UNSET
        if _grptres is not UNSET:
            grptres = []
            for componentsschemasv0_0_42_tres_list_item_data in _grptres:
                componentsschemasv0_0_42_tres_list_item = V0042Tres.from_dict(
                    componentsschemasv0_0_42_tres_list_item_data
                )

                grptres.append(componentsschemasv0_0_42_tres_list_item)

        _grptresmins = d.pop("grptresmins", UNSET)
        grptresmins: list[V0042Tres] | Unset = UNSET
        if _grptresmins is not UNSET:
            grptresmins = []
            for componentsschemasv0_0_42_tres_list_item_data in _grptresmins:
                componentsschemasv0_0_42_tres_list_item = V0042Tres.from_dict(
                    componentsschemasv0_0_42_tres_list_item_data
                )

                grptresmins.append(componentsschemasv0_0_42_tres_list_item)

        _grptresrunmins = d.pop("grptresrunmins", UNSET)
        grptresrunmins: list[V0042Tres] | Unset = UNSET
        if _grptresrunmins is not UNSET:
            grptresrunmins = []
            for componentsschemasv0_0_42_tres_list_item_data in _grptresrunmins:
                componentsschemasv0_0_42_tres_list_item = V0042Tres.from_dict(
                    componentsschemasv0_0_42_tres_list_item_data
                )

                grptresrunmins.append(componentsschemasv0_0_42_tres_list_item)

        _grpwall = d.pop("grpwall", UNSET)
        grpwall: V0042Uint32NoValStruct | Unset
        if isinstance(_grpwall, Unset):
            grpwall = UNSET
        else:
            grpwall = V0042Uint32NoValStruct.from_dict(_grpwall)

        _maxjobs = d.pop("maxjobs", UNSET)
        maxjobs: V0042Uint32NoValStruct | Unset
        if isinstance(_maxjobs, Unset):
            maxjobs = UNSET
        else:
            maxjobs = V0042Uint32NoValStruct.from_dict(_maxjobs)

        _maxjobsaccrue = d.pop("maxjobsaccrue", UNSET)
        maxjobsaccrue: V0042Uint32NoValStruct | Unset
        if isinstance(_maxjobsaccrue, Unset):
            maxjobsaccrue = UNSET
        else:
            maxjobsaccrue = V0042Uint32NoValStruct.from_dict(_maxjobsaccrue)

        _maxsubmitjobs = d.pop("maxsubmitjobs", UNSET)
        maxsubmitjobs: V0042Uint32NoValStruct | Unset
        if isinstance(_maxsubmitjobs, Unset):
            maxsubmitjobs = UNSET
        else:
            maxsubmitjobs = V0042Uint32NoValStruct.from_dict(_maxsubmitjobs)

        _maxtresminsperjob = d.pop("maxtresminsperjob", UNSET)
        maxtresminsperjob: list[V0042Tres] | Unset = UNSET
        if _maxtresminsperjob is not UNSET:
            maxtresminsperjob = []
            for componentsschemasv0_0_42_tres_list_item_data in _maxtresminsperjob:
                componentsschemasv0_0_42_tres_list_item = V0042Tres.from_dict(
                    componentsschemasv0_0_42_tres_list_item_data
                )

                maxtresminsperjob.append(componentsschemasv0_0_42_tres_list_item)

        _maxtresrunmins = d.pop("maxtresrunmins", UNSET)
        maxtresrunmins: list[V0042Tres] | Unset = UNSET
        if _maxtresrunmins is not UNSET:
            maxtresrunmins = []
            for componentsschemasv0_0_42_tres_list_item_data in _maxtresrunmins:
                componentsschemasv0_0_42_tres_list_item = V0042Tres.from_dict(
                    componentsschemasv0_0_42_tres_list_item_data
                )

                maxtresrunmins.append(componentsschemasv0_0_42_tres_list_item)

        _maxtresperjob = d.pop("maxtresperjob", UNSET)
        maxtresperjob: list[V0042Tres] | Unset = UNSET
        if _maxtresperjob is not UNSET:
            maxtresperjob = []
            for componentsschemasv0_0_42_tres_list_item_data in _maxtresperjob:
                componentsschemasv0_0_42_tres_list_item = V0042Tres.from_dict(
                    componentsschemasv0_0_42_tres_list_item_data
                )

                maxtresperjob.append(componentsschemasv0_0_42_tres_list_item)

        _maxtrespernode = d.pop("maxtrespernode", UNSET)
        maxtrespernode: list[V0042Tres] | Unset = UNSET
        if _maxtrespernode is not UNSET:
            maxtrespernode = []
            for componentsschemasv0_0_42_tres_list_item_data in _maxtrespernode:
                componentsschemasv0_0_42_tres_list_item = V0042Tres.from_dict(
                    componentsschemasv0_0_42_tres_list_item_data
                )

                maxtrespernode.append(componentsschemasv0_0_42_tres_list_item)

        _maxwalldurationperjob = d.pop("maxwalldurationperjob", UNSET)
        maxwalldurationperjob: V0042Uint32NoValStruct | Unset
        if isinstance(_maxwalldurationperjob, Unset):
            maxwalldurationperjob = UNSET
        else:
            maxwalldurationperjob = V0042Uint32NoValStruct.from_dict(_maxwalldurationperjob)

        _minpriothresh = d.pop("minpriothresh", UNSET)
        minpriothresh: V0042Uint32NoValStruct | Unset
        if isinstance(_minpriothresh, Unset):
            minpriothresh = UNSET
        else:
            minpriothresh = V0042Uint32NoValStruct.from_dict(_minpriothresh)

        parent = d.pop("parent", UNSET)

        _priority = d.pop("priority", UNSET)
        priority: V0042Uint32NoValStruct | Unset
        if isinstance(_priority, Unset):
            priority = UNSET
        else:
            priority = V0042Uint32NoValStruct.from_dict(_priority)

        qoslevel = cast(list[str], d.pop("qoslevel", UNSET))

        fairshare = d.pop("fairshare", UNSET)

        v0042_assoc_rec_set = cls(
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

        v0042_assoc_rec_set.additional_properties = d
        return v0042_assoc_rec_set

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
