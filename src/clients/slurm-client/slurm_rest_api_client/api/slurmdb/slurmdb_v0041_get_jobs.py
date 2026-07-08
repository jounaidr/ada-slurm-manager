from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.v0041_openapi_slurmdbd_jobs_resp import V0041OpenapiSlurmdbdJobsResp
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    account: str | Unset = UNSET,
    association: str | Unset = UNSET,
    cluster: str | Unset = UNSET,
    constraints: str | Unset = UNSET,
    scheduler_unset: str | Unset = UNSET,
    scheduled_on_submit: str | Unset = UNSET,
    scheduled_by_main: str | Unset = UNSET,
    scheduled_by_backfill: str | Unset = UNSET,
    job_started: str | Unset = UNSET,
    exit_code: str | Unset = UNSET,
    show_duplicates: str | Unset = UNSET,
    skip_steps: str | Unset = UNSET,
    disable_truncate_usage_time: str | Unset = UNSET,
    whole_hetjob: str | Unset = UNSET,
    disable_whole_hetjob: str | Unset = UNSET,
    disable_wait_for_result: str | Unset = UNSET,
    usage_time_as_submit_time: str | Unset = UNSET,
    show_batch_script: str | Unset = UNSET,
    show_job_environment: str | Unset = UNSET,
    format_: str | Unset = UNSET,
    groups: str | Unset = UNSET,
    job_name: str | Unset = UNSET,
    partition: str | Unset = UNSET,
    qos: str | Unset = UNSET,
    reason: str | Unset = UNSET,
    reservation: str | Unset = UNSET,
    reservation_id: str | Unset = UNSET,
    state: str | Unset = UNSET,
    step: str | Unset = UNSET,
    end_time: str | Unset = UNSET,
    start_time: str | Unset = UNSET,
    node: str | Unset = UNSET,
    users: str | Unset = UNSET,
    wckey: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["account"] = account

    params["association"] = association

    params["cluster"] = cluster

    params["constraints"] = constraints

    params["scheduler_unset"] = scheduler_unset

    params["scheduled_on_submit"] = scheduled_on_submit

    params["scheduled_by_main"] = scheduled_by_main

    params["scheduled_by_backfill"] = scheduled_by_backfill

    params["job_started"] = job_started

    params["exit_code"] = exit_code

    params["show_duplicates"] = show_duplicates

    params["skip_steps"] = skip_steps

    params["disable_truncate_usage_time"] = disable_truncate_usage_time

    params["whole_hetjob"] = whole_hetjob

    params["disable_whole_hetjob"] = disable_whole_hetjob

    params["disable_wait_for_result"] = disable_wait_for_result

    params["usage_time_as_submit_time"] = usage_time_as_submit_time

    params["show_batch_script"] = show_batch_script

    params["show_job_environment"] = show_job_environment

    params["format"] = format_

    params["groups"] = groups

    params["job_name"] = job_name

    params["partition"] = partition

    params["qos"] = qos

    params["reason"] = reason

    params["reservation"] = reservation

    params["reservation_id"] = reservation_id

    params["state"] = state

    params["step"] = step

    params["end_time"] = end_time

    params["start_time"] = start_time

    params["node"] = node

    params["users"] = users

    params["wckey"] = wckey

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/slurmdb/v0.0.41/jobs/",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> V0041OpenapiSlurmdbdJobsResp:
    if response.status_code == 200:
        response_200 = V0041OpenapiSlurmdbdJobsResp.from_dict(response.json())

        return response_200

    response_default = V0041OpenapiSlurmdbdJobsResp.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[V0041OpenapiSlurmdbdJobsResp]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    account: str | Unset = UNSET,
    association: str | Unset = UNSET,
    cluster: str | Unset = UNSET,
    constraints: str | Unset = UNSET,
    scheduler_unset: str | Unset = UNSET,
    scheduled_on_submit: str | Unset = UNSET,
    scheduled_by_main: str | Unset = UNSET,
    scheduled_by_backfill: str | Unset = UNSET,
    job_started: str | Unset = UNSET,
    exit_code: str | Unset = UNSET,
    show_duplicates: str | Unset = UNSET,
    skip_steps: str | Unset = UNSET,
    disable_truncate_usage_time: str | Unset = UNSET,
    whole_hetjob: str | Unset = UNSET,
    disable_whole_hetjob: str | Unset = UNSET,
    disable_wait_for_result: str | Unset = UNSET,
    usage_time_as_submit_time: str | Unset = UNSET,
    show_batch_script: str | Unset = UNSET,
    show_job_environment: str | Unset = UNSET,
    format_: str | Unset = UNSET,
    groups: str | Unset = UNSET,
    job_name: str | Unset = UNSET,
    partition: str | Unset = UNSET,
    qos: str | Unset = UNSET,
    reason: str | Unset = UNSET,
    reservation: str | Unset = UNSET,
    reservation_id: str | Unset = UNSET,
    state: str | Unset = UNSET,
    step: str | Unset = UNSET,
    end_time: str | Unset = UNSET,
    start_time: str | Unset = UNSET,
    node: str | Unset = UNSET,
    users: str | Unset = UNSET,
    wckey: str | Unset = UNSET,
) -> Response[V0041OpenapiSlurmdbdJobsResp]:
    """Get job list

    Args:
        account (str | Unset):
        association (str | Unset):
        cluster (str | Unset):
        constraints (str | Unset):
        scheduler_unset (str | Unset):
        scheduled_on_submit (str | Unset):
        scheduled_by_main (str | Unset):
        scheduled_by_backfill (str | Unset):
        job_started (str | Unset):
        exit_code (str | Unset):
        show_duplicates (str | Unset):
        skip_steps (str | Unset):
        disable_truncate_usage_time (str | Unset):
        whole_hetjob (str | Unset):
        disable_whole_hetjob (str | Unset):
        disable_wait_for_result (str | Unset):
        usage_time_as_submit_time (str | Unset):
        show_batch_script (str | Unset):
        show_job_environment (str | Unset):
        format_ (str | Unset):
        groups (str | Unset):
        job_name (str | Unset):
        partition (str | Unset):
        qos (str | Unset):
        reason (str | Unset):
        reservation (str | Unset):
        reservation_id (str | Unset):
        state (str | Unset):
        step (str | Unset):
        end_time (str | Unset):
        start_time (str | Unset):
        node (str | Unset):
        users (str | Unset):
        wckey (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[V0041OpenapiSlurmdbdJobsResp]
    """

    kwargs = _get_kwargs(
        account=account,
        association=association,
        cluster=cluster,
        constraints=constraints,
        scheduler_unset=scheduler_unset,
        scheduled_on_submit=scheduled_on_submit,
        scheduled_by_main=scheduled_by_main,
        scheduled_by_backfill=scheduled_by_backfill,
        job_started=job_started,
        exit_code=exit_code,
        show_duplicates=show_duplicates,
        skip_steps=skip_steps,
        disable_truncate_usage_time=disable_truncate_usage_time,
        whole_hetjob=whole_hetjob,
        disable_whole_hetjob=disable_whole_hetjob,
        disable_wait_for_result=disable_wait_for_result,
        usage_time_as_submit_time=usage_time_as_submit_time,
        show_batch_script=show_batch_script,
        show_job_environment=show_job_environment,
        format_=format_,
        groups=groups,
        job_name=job_name,
        partition=partition,
        qos=qos,
        reason=reason,
        reservation=reservation,
        reservation_id=reservation_id,
        state=state,
        step=step,
        end_time=end_time,
        start_time=start_time,
        node=node,
        users=users,
        wckey=wckey,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    account: str | Unset = UNSET,
    association: str | Unset = UNSET,
    cluster: str | Unset = UNSET,
    constraints: str | Unset = UNSET,
    scheduler_unset: str | Unset = UNSET,
    scheduled_on_submit: str | Unset = UNSET,
    scheduled_by_main: str | Unset = UNSET,
    scheduled_by_backfill: str | Unset = UNSET,
    job_started: str | Unset = UNSET,
    exit_code: str | Unset = UNSET,
    show_duplicates: str | Unset = UNSET,
    skip_steps: str | Unset = UNSET,
    disable_truncate_usage_time: str | Unset = UNSET,
    whole_hetjob: str | Unset = UNSET,
    disable_whole_hetjob: str | Unset = UNSET,
    disable_wait_for_result: str | Unset = UNSET,
    usage_time_as_submit_time: str | Unset = UNSET,
    show_batch_script: str | Unset = UNSET,
    show_job_environment: str | Unset = UNSET,
    format_: str | Unset = UNSET,
    groups: str | Unset = UNSET,
    job_name: str | Unset = UNSET,
    partition: str | Unset = UNSET,
    qos: str | Unset = UNSET,
    reason: str | Unset = UNSET,
    reservation: str | Unset = UNSET,
    reservation_id: str | Unset = UNSET,
    state: str | Unset = UNSET,
    step: str | Unset = UNSET,
    end_time: str | Unset = UNSET,
    start_time: str | Unset = UNSET,
    node: str | Unset = UNSET,
    users: str | Unset = UNSET,
    wckey: str | Unset = UNSET,
) -> V0041OpenapiSlurmdbdJobsResp | None:
    """Get job list

    Args:
        account (str | Unset):
        association (str | Unset):
        cluster (str | Unset):
        constraints (str | Unset):
        scheduler_unset (str | Unset):
        scheduled_on_submit (str | Unset):
        scheduled_by_main (str | Unset):
        scheduled_by_backfill (str | Unset):
        job_started (str | Unset):
        exit_code (str | Unset):
        show_duplicates (str | Unset):
        skip_steps (str | Unset):
        disable_truncate_usage_time (str | Unset):
        whole_hetjob (str | Unset):
        disable_whole_hetjob (str | Unset):
        disable_wait_for_result (str | Unset):
        usage_time_as_submit_time (str | Unset):
        show_batch_script (str | Unset):
        show_job_environment (str | Unset):
        format_ (str | Unset):
        groups (str | Unset):
        job_name (str | Unset):
        partition (str | Unset):
        qos (str | Unset):
        reason (str | Unset):
        reservation (str | Unset):
        reservation_id (str | Unset):
        state (str | Unset):
        step (str | Unset):
        end_time (str | Unset):
        start_time (str | Unset):
        node (str | Unset):
        users (str | Unset):
        wckey (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        V0041OpenapiSlurmdbdJobsResp
    """

    return sync_detailed(
        client=client,
        account=account,
        association=association,
        cluster=cluster,
        constraints=constraints,
        scheduler_unset=scheduler_unset,
        scheduled_on_submit=scheduled_on_submit,
        scheduled_by_main=scheduled_by_main,
        scheduled_by_backfill=scheduled_by_backfill,
        job_started=job_started,
        exit_code=exit_code,
        show_duplicates=show_duplicates,
        skip_steps=skip_steps,
        disable_truncate_usage_time=disable_truncate_usage_time,
        whole_hetjob=whole_hetjob,
        disable_whole_hetjob=disable_whole_hetjob,
        disable_wait_for_result=disable_wait_for_result,
        usage_time_as_submit_time=usage_time_as_submit_time,
        show_batch_script=show_batch_script,
        show_job_environment=show_job_environment,
        format_=format_,
        groups=groups,
        job_name=job_name,
        partition=partition,
        qos=qos,
        reason=reason,
        reservation=reservation,
        reservation_id=reservation_id,
        state=state,
        step=step,
        end_time=end_time,
        start_time=start_time,
        node=node,
        users=users,
        wckey=wckey,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    account: str | Unset = UNSET,
    association: str | Unset = UNSET,
    cluster: str | Unset = UNSET,
    constraints: str | Unset = UNSET,
    scheduler_unset: str | Unset = UNSET,
    scheduled_on_submit: str | Unset = UNSET,
    scheduled_by_main: str | Unset = UNSET,
    scheduled_by_backfill: str | Unset = UNSET,
    job_started: str | Unset = UNSET,
    exit_code: str | Unset = UNSET,
    show_duplicates: str | Unset = UNSET,
    skip_steps: str | Unset = UNSET,
    disable_truncate_usage_time: str | Unset = UNSET,
    whole_hetjob: str | Unset = UNSET,
    disable_whole_hetjob: str | Unset = UNSET,
    disable_wait_for_result: str | Unset = UNSET,
    usage_time_as_submit_time: str | Unset = UNSET,
    show_batch_script: str | Unset = UNSET,
    show_job_environment: str | Unset = UNSET,
    format_: str | Unset = UNSET,
    groups: str | Unset = UNSET,
    job_name: str | Unset = UNSET,
    partition: str | Unset = UNSET,
    qos: str | Unset = UNSET,
    reason: str | Unset = UNSET,
    reservation: str | Unset = UNSET,
    reservation_id: str | Unset = UNSET,
    state: str | Unset = UNSET,
    step: str | Unset = UNSET,
    end_time: str | Unset = UNSET,
    start_time: str | Unset = UNSET,
    node: str | Unset = UNSET,
    users: str | Unset = UNSET,
    wckey: str | Unset = UNSET,
) -> Response[V0041OpenapiSlurmdbdJobsResp]:
    """Get job list

    Args:
        account (str | Unset):
        association (str | Unset):
        cluster (str | Unset):
        constraints (str | Unset):
        scheduler_unset (str | Unset):
        scheduled_on_submit (str | Unset):
        scheduled_by_main (str | Unset):
        scheduled_by_backfill (str | Unset):
        job_started (str | Unset):
        exit_code (str | Unset):
        show_duplicates (str | Unset):
        skip_steps (str | Unset):
        disable_truncate_usage_time (str | Unset):
        whole_hetjob (str | Unset):
        disable_whole_hetjob (str | Unset):
        disable_wait_for_result (str | Unset):
        usage_time_as_submit_time (str | Unset):
        show_batch_script (str | Unset):
        show_job_environment (str | Unset):
        format_ (str | Unset):
        groups (str | Unset):
        job_name (str | Unset):
        partition (str | Unset):
        qos (str | Unset):
        reason (str | Unset):
        reservation (str | Unset):
        reservation_id (str | Unset):
        state (str | Unset):
        step (str | Unset):
        end_time (str | Unset):
        start_time (str | Unset):
        node (str | Unset):
        users (str | Unset):
        wckey (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[V0041OpenapiSlurmdbdJobsResp]
    """

    kwargs = _get_kwargs(
        account=account,
        association=association,
        cluster=cluster,
        constraints=constraints,
        scheduler_unset=scheduler_unset,
        scheduled_on_submit=scheduled_on_submit,
        scheduled_by_main=scheduled_by_main,
        scheduled_by_backfill=scheduled_by_backfill,
        job_started=job_started,
        exit_code=exit_code,
        show_duplicates=show_duplicates,
        skip_steps=skip_steps,
        disable_truncate_usage_time=disable_truncate_usage_time,
        whole_hetjob=whole_hetjob,
        disable_whole_hetjob=disable_whole_hetjob,
        disable_wait_for_result=disable_wait_for_result,
        usage_time_as_submit_time=usage_time_as_submit_time,
        show_batch_script=show_batch_script,
        show_job_environment=show_job_environment,
        format_=format_,
        groups=groups,
        job_name=job_name,
        partition=partition,
        qos=qos,
        reason=reason,
        reservation=reservation,
        reservation_id=reservation_id,
        state=state,
        step=step,
        end_time=end_time,
        start_time=start_time,
        node=node,
        users=users,
        wckey=wckey,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    account: str | Unset = UNSET,
    association: str | Unset = UNSET,
    cluster: str | Unset = UNSET,
    constraints: str | Unset = UNSET,
    scheduler_unset: str | Unset = UNSET,
    scheduled_on_submit: str | Unset = UNSET,
    scheduled_by_main: str | Unset = UNSET,
    scheduled_by_backfill: str | Unset = UNSET,
    job_started: str | Unset = UNSET,
    exit_code: str | Unset = UNSET,
    show_duplicates: str | Unset = UNSET,
    skip_steps: str | Unset = UNSET,
    disable_truncate_usage_time: str | Unset = UNSET,
    whole_hetjob: str | Unset = UNSET,
    disable_whole_hetjob: str | Unset = UNSET,
    disable_wait_for_result: str | Unset = UNSET,
    usage_time_as_submit_time: str | Unset = UNSET,
    show_batch_script: str | Unset = UNSET,
    show_job_environment: str | Unset = UNSET,
    format_: str | Unset = UNSET,
    groups: str | Unset = UNSET,
    job_name: str | Unset = UNSET,
    partition: str | Unset = UNSET,
    qos: str | Unset = UNSET,
    reason: str | Unset = UNSET,
    reservation: str | Unset = UNSET,
    reservation_id: str | Unset = UNSET,
    state: str | Unset = UNSET,
    step: str | Unset = UNSET,
    end_time: str | Unset = UNSET,
    start_time: str | Unset = UNSET,
    node: str | Unset = UNSET,
    users: str | Unset = UNSET,
    wckey: str | Unset = UNSET,
) -> V0041OpenapiSlurmdbdJobsResp | None:
    """Get job list

    Args:
        account (str | Unset):
        association (str | Unset):
        cluster (str | Unset):
        constraints (str | Unset):
        scheduler_unset (str | Unset):
        scheduled_on_submit (str | Unset):
        scheduled_by_main (str | Unset):
        scheduled_by_backfill (str | Unset):
        job_started (str | Unset):
        exit_code (str | Unset):
        show_duplicates (str | Unset):
        skip_steps (str | Unset):
        disable_truncate_usage_time (str | Unset):
        whole_hetjob (str | Unset):
        disable_whole_hetjob (str | Unset):
        disable_wait_for_result (str | Unset):
        usage_time_as_submit_time (str | Unset):
        show_batch_script (str | Unset):
        show_job_environment (str | Unset):
        format_ (str | Unset):
        groups (str | Unset):
        job_name (str | Unset):
        partition (str | Unset):
        qos (str | Unset):
        reason (str | Unset):
        reservation (str | Unset):
        reservation_id (str | Unset):
        state (str | Unset):
        step (str | Unset):
        end_time (str | Unset):
        start_time (str | Unset):
        node (str | Unset):
        users (str | Unset):
        wckey (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        V0041OpenapiSlurmdbdJobsResp
    """

    return (
        await asyncio_detailed(
            client=client,
            account=account,
            association=association,
            cluster=cluster,
            constraints=constraints,
            scheduler_unset=scheduler_unset,
            scheduled_on_submit=scheduled_on_submit,
            scheduled_by_main=scheduled_by_main,
            scheduled_by_backfill=scheduled_by_backfill,
            job_started=job_started,
            exit_code=exit_code,
            show_duplicates=show_duplicates,
            skip_steps=skip_steps,
            disable_truncate_usage_time=disable_truncate_usage_time,
            whole_hetjob=whole_hetjob,
            disable_whole_hetjob=disable_whole_hetjob,
            disable_wait_for_result=disable_wait_for_result,
            usage_time_as_submit_time=usage_time_as_submit_time,
            show_batch_script=show_batch_script,
            show_job_environment=show_job_environment,
            format_=format_,
            groups=groups,
            job_name=job_name,
            partition=partition,
            qos=qos,
            reason=reason,
            reservation=reservation,
            reservation_id=reservation_id,
            state=state,
            step=step,
            end_time=end_time,
            start_time=start_time,
            node=node,
            users=users,
            wckey=wckey,
        )
    ).parsed
