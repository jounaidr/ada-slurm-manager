from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v0044_job_modify_comment import V0044JobModifyComment
    from ..models.v0044_job_modify_tres import V0044JobModifyTres
    from ..models.v0044_process_exit_code_verbose import V0044ProcessExitCodeVerbose


T = TypeVar("T", bound="V0044JobModify")


@_attrs_define
class V0044JobModify:
    """
    Attributes:
        comment (V0044JobModifyComment | Unset):
        derived_exit_code (V0044ProcessExitCodeVerbose | Unset):
        extra (str | Unset): Arbitrary string used for node filtering if extra constraints are enabled
        tres (V0044JobModifyTres | Unset):
        wckey (str | Unset): Workload characterization key
    """

    comment: V0044JobModifyComment | Unset = UNSET
    derived_exit_code: V0044ProcessExitCodeVerbose | Unset = UNSET
    extra: str | Unset = UNSET
    tres: V0044JobModifyTres | Unset = UNSET
    wckey: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        comment: dict[str, Any] | Unset = UNSET
        if not isinstance(self.comment, Unset):
            comment = self.comment.to_dict()

        derived_exit_code: dict[str, Any] | Unset = UNSET
        if not isinstance(self.derived_exit_code, Unset):
            derived_exit_code = self.derived_exit_code.to_dict()

        extra = self.extra

        tres: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tres, Unset):
            tres = self.tres.to_dict()

        wckey = self.wckey

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if comment is not UNSET:
            field_dict["comment"] = comment
        if derived_exit_code is not UNSET:
            field_dict["derived_exit_code"] = derived_exit_code
        if extra is not UNSET:
            field_dict["extra"] = extra
        if tres is not UNSET:
            field_dict["tres"] = tres
        if wckey is not UNSET:
            field_dict["wckey"] = wckey

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v0044_job_modify_comment import V0044JobModifyComment
        from ..models.v0044_job_modify_tres import V0044JobModifyTres
        from ..models.v0044_process_exit_code_verbose import V0044ProcessExitCodeVerbose

        d = dict(src_dict)
        _comment = d.pop("comment", UNSET)
        comment: V0044JobModifyComment | Unset
        if isinstance(_comment, Unset):
            comment = UNSET
        else:
            comment = V0044JobModifyComment.from_dict(_comment)

        _derived_exit_code = d.pop("derived_exit_code", UNSET)
        derived_exit_code: V0044ProcessExitCodeVerbose | Unset
        if isinstance(_derived_exit_code, Unset):
            derived_exit_code = UNSET
        else:
            derived_exit_code = V0044ProcessExitCodeVerbose.from_dict(_derived_exit_code)

        extra = d.pop("extra", UNSET)

        _tres = d.pop("tres", UNSET)
        tres: V0044JobModifyTres | Unset
        if isinstance(_tres, Unset):
            tres = UNSET
        else:
            tres = V0044JobModifyTres.from_dict(_tres)

        wckey = d.pop("wckey", UNSET)

        v0044_job_modify = cls(
            comment=comment,
            derived_exit_code=derived_exit_code,
            extra=extra,
            tres=tres,
            wckey=wckey,
        )

        v0044_job_modify.additional_properties = d
        return v0044_job_modify

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
