from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.slurm_v0041_post_job_allocate_body_job_rlimits_as import SlurmV0041PostJobAllocateBodyJobRlimitsAs
    from ..models.slurm_v0041_post_job_allocate_body_job_rlimits_core import SlurmV0041PostJobAllocateBodyJobRlimitsCore
    from ..models.slurm_v0041_post_job_allocate_body_job_rlimits_cpu import SlurmV0041PostJobAllocateBodyJobRlimitsCpu
    from ..models.slurm_v0041_post_job_allocate_body_job_rlimits_data import SlurmV0041PostJobAllocateBodyJobRlimitsData
    from ..models.slurm_v0041_post_job_allocate_body_job_rlimits_fsize import (
        SlurmV0041PostJobAllocateBodyJobRlimitsFsize,
    )
    from ..models.slurm_v0041_post_job_allocate_body_job_rlimits_memlock import (
        SlurmV0041PostJobAllocateBodyJobRlimitsMemlock,
    )
    from ..models.slurm_v0041_post_job_allocate_body_job_rlimits_nofile import (
        SlurmV0041PostJobAllocateBodyJobRlimitsNofile,
    )
    from ..models.slurm_v0041_post_job_allocate_body_job_rlimits_nproc import (
        SlurmV0041PostJobAllocateBodyJobRlimitsNproc,
    )
    from ..models.slurm_v0041_post_job_allocate_body_job_rlimits_rss import SlurmV0041PostJobAllocateBodyJobRlimitsRss
    from ..models.slurm_v0041_post_job_allocate_body_job_rlimits_stack import (
        SlurmV0041PostJobAllocateBodyJobRlimitsStack,
    )


T = TypeVar("T", bound="SlurmV0041PostJobAllocateBodyJobRlimits")


@_attrs_define
class SlurmV0041PostJobAllocateBodyJobRlimits:
    """
    Attributes:
        cpu (SlurmV0041PostJobAllocateBodyJobRlimitsCpu | Unset): Per-process CPU limit, in seconds.
        fsize (SlurmV0041PostJobAllocateBodyJobRlimitsFsize | Unset): Largest file that can be created, in bytes.
        data (SlurmV0041PostJobAllocateBodyJobRlimitsData | Unset): Maximum size of data segment, in bytes.
        stack (SlurmV0041PostJobAllocateBodyJobRlimitsStack | Unset): Maximum size of stack segment, in bytes.
        core (SlurmV0041PostJobAllocateBodyJobRlimitsCore | Unset): Largest core file that can be created, in bytes.
        rss (SlurmV0041PostJobAllocateBodyJobRlimitsRss | Unset): Largest resident set size, in bytes. This affects
            swapping; processes that are exceeding their resident set size will be more likely to have physical memory taken
            from them.
        nproc (SlurmV0041PostJobAllocateBodyJobRlimitsNproc | Unset): Number of processes.
        nofile (SlurmV0041PostJobAllocateBodyJobRlimitsNofile | Unset): Number of open files.
        memlock (SlurmV0041PostJobAllocateBodyJobRlimitsMemlock | Unset): Locked-in-memory address space
        as_ (SlurmV0041PostJobAllocateBodyJobRlimitsAs | Unset): Address space limit.
    """

    cpu: SlurmV0041PostJobAllocateBodyJobRlimitsCpu | Unset = UNSET
    fsize: SlurmV0041PostJobAllocateBodyJobRlimitsFsize | Unset = UNSET
    data: SlurmV0041PostJobAllocateBodyJobRlimitsData | Unset = UNSET
    stack: SlurmV0041PostJobAllocateBodyJobRlimitsStack | Unset = UNSET
    core: SlurmV0041PostJobAllocateBodyJobRlimitsCore | Unset = UNSET
    rss: SlurmV0041PostJobAllocateBodyJobRlimitsRss | Unset = UNSET
    nproc: SlurmV0041PostJobAllocateBodyJobRlimitsNproc | Unset = UNSET
    nofile: SlurmV0041PostJobAllocateBodyJobRlimitsNofile | Unset = UNSET
    memlock: SlurmV0041PostJobAllocateBodyJobRlimitsMemlock | Unset = UNSET
    as_: SlurmV0041PostJobAllocateBodyJobRlimitsAs | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cpu: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cpu, Unset):
            cpu = self.cpu.to_dict()

        fsize: dict[str, Any] | Unset = UNSET
        if not isinstance(self.fsize, Unset):
            fsize = self.fsize.to_dict()

        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        stack: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stack, Unset):
            stack = self.stack.to_dict()

        core: dict[str, Any] | Unset = UNSET
        if not isinstance(self.core, Unset):
            core = self.core.to_dict()

        rss: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rss, Unset):
            rss = self.rss.to_dict()

        nproc: dict[str, Any] | Unset = UNSET
        if not isinstance(self.nproc, Unset):
            nproc = self.nproc.to_dict()

        nofile: dict[str, Any] | Unset = UNSET
        if not isinstance(self.nofile, Unset):
            nofile = self.nofile.to_dict()

        memlock: dict[str, Any] | Unset = UNSET
        if not isinstance(self.memlock, Unset):
            memlock = self.memlock.to_dict()

        as_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.as_, Unset):
            as_ = self.as_.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cpu is not UNSET:
            field_dict["cpu"] = cpu
        if fsize is not UNSET:
            field_dict["fsize"] = fsize
        if data is not UNSET:
            field_dict["data"] = data
        if stack is not UNSET:
            field_dict["stack"] = stack
        if core is not UNSET:
            field_dict["core"] = core
        if rss is not UNSET:
            field_dict["rss"] = rss
        if nproc is not UNSET:
            field_dict["nproc"] = nproc
        if nofile is not UNSET:
            field_dict["nofile"] = nofile
        if memlock is not UNSET:
            field_dict["memlock"] = memlock
        if as_ is not UNSET:
            field_dict["as"] = as_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.slurm_v0041_post_job_allocate_body_job_rlimits_as import SlurmV0041PostJobAllocateBodyJobRlimitsAs
        from ..models.slurm_v0041_post_job_allocate_body_job_rlimits_core import (
            SlurmV0041PostJobAllocateBodyJobRlimitsCore,
        )
        from ..models.slurm_v0041_post_job_allocate_body_job_rlimits_cpu import (
            SlurmV0041PostJobAllocateBodyJobRlimitsCpu,
        )
        from ..models.slurm_v0041_post_job_allocate_body_job_rlimits_data import (
            SlurmV0041PostJobAllocateBodyJobRlimitsData,
        )
        from ..models.slurm_v0041_post_job_allocate_body_job_rlimits_fsize import (
            SlurmV0041PostJobAllocateBodyJobRlimitsFsize,
        )
        from ..models.slurm_v0041_post_job_allocate_body_job_rlimits_memlock import (
            SlurmV0041PostJobAllocateBodyJobRlimitsMemlock,
        )
        from ..models.slurm_v0041_post_job_allocate_body_job_rlimits_nofile import (
            SlurmV0041PostJobAllocateBodyJobRlimitsNofile,
        )
        from ..models.slurm_v0041_post_job_allocate_body_job_rlimits_nproc import (
            SlurmV0041PostJobAllocateBodyJobRlimitsNproc,
        )
        from ..models.slurm_v0041_post_job_allocate_body_job_rlimits_rss import (
            SlurmV0041PostJobAllocateBodyJobRlimitsRss,
        )
        from ..models.slurm_v0041_post_job_allocate_body_job_rlimits_stack import (
            SlurmV0041PostJobAllocateBodyJobRlimitsStack,
        )

        d = dict(src_dict)
        _cpu = d.pop("cpu", UNSET)
        cpu: SlurmV0041PostJobAllocateBodyJobRlimitsCpu | Unset
        if isinstance(_cpu, Unset):
            cpu = UNSET
        else:
            cpu = SlurmV0041PostJobAllocateBodyJobRlimitsCpu.from_dict(_cpu)

        _fsize = d.pop("fsize", UNSET)
        fsize: SlurmV0041PostJobAllocateBodyJobRlimitsFsize | Unset
        if isinstance(_fsize, Unset):
            fsize = UNSET
        else:
            fsize = SlurmV0041PostJobAllocateBodyJobRlimitsFsize.from_dict(_fsize)

        _data = d.pop("data", UNSET)
        data: SlurmV0041PostJobAllocateBodyJobRlimitsData | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = SlurmV0041PostJobAllocateBodyJobRlimitsData.from_dict(_data)

        _stack = d.pop("stack", UNSET)
        stack: SlurmV0041PostJobAllocateBodyJobRlimitsStack | Unset
        if isinstance(_stack, Unset):
            stack = UNSET
        else:
            stack = SlurmV0041PostJobAllocateBodyJobRlimitsStack.from_dict(_stack)

        _core = d.pop("core", UNSET)
        core: SlurmV0041PostJobAllocateBodyJobRlimitsCore | Unset
        if isinstance(_core, Unset):
            core = UNSET
        else:
            core = SlurmV0041PostJobAllocateBodyJobRlimitsCore.from_dict(_core)

        _rss = d.pop("rss", UNSET)
        rss: SlurmV0041PostJobAllocateBodyJobRlimitsRss | Unset
        if isinstance(_rss, Unset):
            rss = UNSET
        else:
            rss = SlurmV0041PostJobAllocateBodyJobRlimitsRss.from_dict(_rss)

        _nproc = d.pop("nproc", UNSET)
        nproc: SlurmV0041PostJobAllocateBodyJobRlimitsNproc | Unset
        if isinstance(_nproc, Unset):
            nproc = UNSET
        else:
            nproc = SlurmV0041PostJobAllocateBodyJobRlimitsNproc.from_dict(_nproc)

        _nofile = d.pop("nofile", UNSET)
        nofile: SlurmV0041PostJobAllocateBodyJobRlimitsNofile | Unset
        if isinstance(_nofile, Unset):
            nofile = UNSET
        else:
            nofile = SlurmV0041PostJobAllocateBodyJobRlimitsNofile.from_dict(_nofile)

        _memlock = d.pop("memlock", UNSET)
        memlock: SlurmV0041PostJobAllocateBodyJobRlimitsMemlock | Unset
        if isinstance(_memlock, Unset):
            memlock = UNSET
        else:
            memlock = SlurmV0041PostJobAllocateBodyJobRlimitsMemlock.from_dict(_memlock)

        _as_ = d.pop("as", UNSET)
        as_: SlurmV0041PostJobAllocateBodyJobRlimitsAs | Unset
        if isinstance(_as_, Unset):
            as_ = UNSET
        else:
            as_ = SlurmV0041PostJobAllocateBodyJobRlimitsAs.from_dict(_as_)

        slurm_v0041_post_job_allocate_body_job_rlimits = cls(
            cpu=cpu,
            fsize=fsize,
            data=data,
            stack=stack,
            core=core,
            rss=rss,
            nproc=nproc,
            nofile=nofile,
            memlock=memlock,
            as_=as_,
        )

        slurm_v0041_post_job_allocate_body_job_rlimits.additional_properties = d
        return slurm_v0041_post_job_allocate_body_job_rlimits

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
