from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.slurmdb_v0039_get_jobs_disable_wait_for_result import SlurmdbV0039GetJobsDisableWaitForResult
from ...models.slurmdb_v0039_get_jobs_skip_steps import SlurmdbV0039GetJobsSkipSteps
from ...models.status import Status
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    users: str | Unset = UNSET,
    submit_time: str | Unset = UNSET,
    start_time: str | Unset = UNSET,
    end_time: str | Unset = UNSET,
    account: str | Unset = UNSET,
    association: str | Unset = UNSET,
    cluster: str | Unset = UNSET,
    constraints: str | Unset = UNSET,
    cpus_max: str | Unset = UNSET,
    cpus_min: str | Unset = UNSET,
    skip_steps: SlurmdbV0039GetJobsSkipSteps | Unset = SlurmdbV0039GetJobsSkipSteps.FALSE,
    disable_wait_for_result: SlurmdbV0039GetJobsDisableWaitForResult
    | Unset = SlurmdbV0039GetJobsDisableWaitForResult.FALSE,
    exit_code: str | Unset = UNSET,
    format_: str | Unset = UNSET,
    group: str | Unset = UNSET,
    job_name: str | Unset = UNSET,
    nodes_max: str | Unset = UNSET,
    nodes_min: str | Unset = UNSET,
    partition: str | Unset = UNSET,
    qos: str | Unset = UNSET,
    reason: str | Unset = UNSET,
    reservation: str | Unset = UNSET,
    state: str | Unset = UNSET,
    step: str | Unset = UNSET,
    node: str | Unset = UNSET,
    wckey: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["users"] = users

    params["submit_time"] = submit_time

    params["start_time"] = start_time

    params["end_time"] = end_time

    params["account"] = account

    params["association"] = association

    params["cluster"] = cluster

    params["constraints"] = constraints

    params["cpus_max"] = cpus_max

    params["cpus_min"] = cpus_min

    json_skip_steps: str | Unset = UNSET
    if not isinstance(skip_steps, Unset):
        json_skip_steps = skip_steps.value

    params["skip_steps"] = json_skip_steps

    json_disable_wait_for_result: str | Unset = UNSET
    if not isinstance(disable_wait_for_result, Unset):
        json_disable_wait_for_result = disable_wait_for_result.value

    params["disable_wait_for_result"] = json_disable_wait_for_result

    params["exit_code"] = exit_code

    params["format"] = format_

    params["group"] = group

    params["job_name"] = job_name

    params["nodes_max"] = nodes_max

    params["nodes_min"] = nodes_min

    params["partition"] = partition

    params["qos"] = qos

    params["reason"] = reason

    params["reservation"] = reservation

    params["state"] = state

    params["step"] = step

    params["node"] = node

    params["wckey"] = wckey

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/slurmdb/v0.0.39/jobs",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Status:
    response_default = Status.from_dict(response.json())

    return response_default


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Status]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    users: str | Unset = UNSET,
    submit_time: str | Unset = UNSET,
    start_time: str | Unset = UNSET,
    end_time: str | Unset = UNSET,
    account: str | Unset = UNSET,
    association: str | Unset = UNSET,
    cluster: str | Unset = UNSET,
    constraints: str | Unset = UNSET,
    cpus_max: str | Unset = UNSET,
    cpus_min: str | Unset = UNSET,
    skip_steps: SlurmdbV0039GetJobsSkipSteps | Unset = SlurmdbV0039GetJobsSkipSteps.FALSE,
    disable_wait_for_result: SlurmdbV0039GetJobsDisableWaitForResult
    | Unset = SlurmdbV0039GetJobsDisableWaitForResult.FALSE,
    exit_code: str | Unset = UNSET,
    format_: str | Unset = UNSET,
    group: str | Unset = UNSET,
    job_name: str | Unset = UNSET,
    nodes_max: str | Unset = UNSET,
    nodes_min: str | Unset = UNSET,
    partition: str | Unset = UNSET,
    qos: str | Unset = UNSET,
    reason: str | Unset = UNSET,
    reservation: str | Unset = UNSET,
    state: str | Unset = UNSET,
    step: str | Unset = UNSET,
    node: str | Unset = UNSET,
    wckey: str | Unset = UNSET,
) -> Response[Status]:
    """Get job list

    Args:
        users (str | Unset):
        submit_time (str | Unset):
        start_time (str | Unset):
        end_time (str | Unset):
        account (str | Unset):
        association (str | Unset):
        cluster (str | Unset):
        constraints (str | Unset):
        cpus_max (str | Unset):
        cpus_min (str | Unset):
        skip_steps (SlurmdbV0039GetJobsSkipSteps | Unset):  Default:
            SlurmdbV0039GetJobsSkipSteps.FALSE.
        disable_wait_for_result (SlurmdbV0039GetJobsDisableWaitForResult | Unset):  Default:
            SlurmdbV0039GetJobsDisableWaitForResult.FALSE.
        exit_code (str | Unset):
        format_ (str | Unset):
        group (str | Unset):
        job_name (str | Unset):
        nodes_max (str | Unset):
        nodes_min (str | Unset):
        partition (str | Unset):
        qos (str | Unset):
        reason (str | Unset):
        reservation (str | Unset):
        state (str | Unset):
        step (str | Unset):
        node (str | Unset):
        wckey (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Status]
    """

    kwargs = _get_kwargs(
        users=users,
        submit_time=submit_time,
        start_time=start_time,
        end_time=end_time,
        account=account,
        association=association,
        cluster=cluster,
        constraints=constraints,
        cpus_max=cpus_max,
        cpus_min=cpus_min,
        skip_steps=skip_steps,
        disable_wait_for_result=disable_wait_for_result,
        exit_code=exit_code,
        format_=format_,
        group=group,
        job_name=job_name,
        nodes_max=nodes_max,
        nodes_min=nodes_min,
        partition=partition,
        qos=qos,
        reason=reason,
        reservation=reservation,
        state=state,
        step=step,
        node=node,
        wckey=wckey,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    users: str | Unset = UNSET,
    submit_time: str | Unset = UNSET,
    start_time: str | Unset = UNSET,
    end_time: str | Unset = UNSET,
    account: str | Unset = UNSET,
    association: str | Unset = UNSET,
    cluster: str | Unset = UNSET,
    constraints: str | Unset = UNSET,
    cpus_max: str | Unset = UNSET,
    cpus_min: str | Unset = UNSET,
    skip_steps: SlurmdbV0039GetJobsSkipSteps | Unset = SlurmdbV0039GetJobsSkipSteps.FALSE,
    disable_wait_for_result: SlurmdbV0039GetJobsDisableWaitForResult
    | Unset = SlurmdbV0039GetJobsDisableWaitForResult.FALSE,
    exit_code: str | Unset = UNSET,
    format_: str | Unset = UNSET,
    group: str | Unset = UNSET,
    job_name: str | Unset = UNSET,
    nodes_max: str | Unset = UNSET,
    nodes_min: str | Unset = UNSET,
    partition: str | Unset = UNSET,
    qos: str | Unset = UNSET,
    reason: str | Unset = UNSET,
    reservation: str | Unset = UNSET,
    state: str | Unset = UNSET,
    step: str | Unset = UNSET,
    node: str | Unset = UNSET,
    wckey: str | Unset = UNSET,
) -> Status | None:
    """Get job list

    Args:
        users (str | Unset):
        submit_time (str | Unset):
        start_time (str | Unset):
        end_time (str | Unset):
        account (str | Unset):
        association (str | Unset):
        cluster (str | Unset):
        constraints (str | Unset):
        cpus_max (str | Unset):
        cpus_min (str | Unset):
        skip_steps (SlurmdbV0039GetJobsSkipSteps | Unset):  Default:
            SlurmdbV0039GetJobsSkipSteps.FALSE.
        disable_wait_for_result (SlurmdbV0039GetJobsDisableWaitForResult | Unset):  Default:
            SlurmdbV0039GetJobsDisableWaitForResult.FALSE.
        exit_code (str | Unset):
        format_ (str | Unset):
        group (str | Unset):
        job_name (str | Unset):
        nodes_max (str | Unset):
        nodes_min (str | Unset):
        partition (str | Unset):
        qos (str | Unset):
        reason (str | Unset):
        reservation (str | Unset):
        state (str | Unset):
        step (str | Unset):
        node (str | Unset):
        wckey (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Status
    """

    return sync_detailed(
        client=client,
        users=users,
        submit_time=submit_time,
        start_time=start_time,
        end_time=end_time,
        account=account,
        association=association,
        cluster=cluster,
        constraints=constraints,
        cpus_max=cpus_max,
        cpus_min=cpus_min,
        skip_steps=skip_steps,
        disable_wait_for_result=disable_wait_for_result,
        exit_code=exit_code,
        format_=format_,
        group=group,
        job_name=job_name,
        nodes_max=nodes_max,
        nodes_min=nodes_min,
        partition=partition,
        qos=qos,
        reason=reason,
        reservation=reservation,
        state=state,
        step=step,
        node=node,
        wckey=wckey,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    users: str | Unset = UNSET,
    submit_time: str | Unset = UNSET,
    start_time: str | Unset = UNSET,
    end_time: str | Unset = UNSET,
    account: str | Unset = UNSET,
    association: str | Unset = UNSET,
    cluster: str | Unset = UNSET,
    constraints: str | Unset = UNSET,
    cpus_max: str | Unset = UNSET,
    cpus_min: str | Unset = UNSET,
    skip_steps: SlurmdbV0039GetJobsSkipSteps | Unset = SlurmdbV0039GetJobsSkipSteps.FALSE,
    disable_wait_for_result: SlurmdbV0039GetJobsDisableWaitForResult
    | Unset = SlurmdbV0039GetJobsDisableWaitForResult.FALSE,
    exit_code: str | Unset = UNSET,
    format_: str | Unset = UNSET,
    group: str | Unset = UNSET,
    job_name: str | Unset = UNSET,
    nodes_max: str | Unset = UNSET,
    nodes_min: str | Unset = UNSET,
    partition: str | Unset = UNSET,
    qos: str | Unset = UNSET,
    reason: str | Unset = UNSET,
    reservation: str | Unset = UNSET,
    state: str | Unset = UNSET,
    step: str | Unset = UNSET,
    node: str | Unset = UNSET,
    wckey: str | Unset = UNSET,
) -> Response[Status]:
    """Get job list

    Args:
        users (str | Unset):
        submit_time (str | Unset):
        start_time (str | Unset):
        end_time (str | Unset):
        account (str | Unset):
        association (str | Unset):
        cluster (str | Unset):
        constraints (str | Unset):
        cpus_max (str | Unset):
        cpus_min (str | Unset):
        skip_steps (SlurmdbV0039GetJobsSkipSteps | Unset):  Default:
            SlurmdbV0039GetJobsSkipSteps.FALSE.
        disable_wait_for_result (SlurmdbV0039GetJobsDisableWaitForResult | Unset):  Default:
            SlurmdbV0039GetJobsDisableWaitForResult.FALSE.
        exit_code (str | Unset):
        format_ (str | Unset):
        group (str | Unset):
        job_name (str | Unset):
        nodes_max (str | Unset):
        nodes_min (str | Unset):
        partition (str | Unset):
        qos (str | Unset):
        reason (str | Unset):
        reservation (str | Unset):
        state (str | Unset):
        step (str | Unset):
        node (str | Unset):
        wckey (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Status]
    """

    kwargs = _get_kwargs(
        users=users,
        submit_time=submit_time,
        start_time=start_time,
        end_time=end_time,
        account=account,
        association=association,
        cluster=cluster,
        constraints=constraints,
        cpus_max=cpus_max,
        cpus_min=cpus_min,
        skip_steps=skip_steps,
        disable_wait_for_result=disable_wait_for_result,
        exit_code=exit_code,
        format_=format_,
        group=group,
        job_name=job_name,
        nodes_max=nodes_max,
        nodes_min=nodes_min,
        partition=partition,
        qos=qos,
        reason=reason,
        reservation=reservation,
        state=state,
        step=step,
        node=node,
        wckey=wckey,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    users: str | Unset = UNSET,
    submit_time: str | Unset = UNSET,
    start_time: str | Unset = UNSET,
    end_time: str | Unset = UNSET,
    account: str | Unset = UNSET,
    association: str | Unset = UNSET,
    cluster: str | Unset = UNSET,
    constraints: str | Unset = UNSET,
    cpus_max: str | Unset = UNSET,
    cpus_min: str | Unset = UNSET,
    skip_steps: SlurmdbV0039GetJobsSkipSteps | Unset = SlurmdbV0039GetJobsSkipSteps.FALSE,
    disable_wait_for_result: SlurmdbV0039GetJobsDisableWaitForResult
    | Unset = SlurmdbV0039GetJobsDisableWaitForResult.FALSE,
    exit_code: str | Unset = UNSET,
    format_: str | Unset = UNSET,
    group: str | Unset = UNSET,
    job_name: str | Unset = UNSET,
    nodes_max: str | Unset = UNSET,
    nodes_min: str | Unset = UNSET,
    partition: str | Unset = UNSET,
    qos: str | Unset = UNSET,
    reason: str | Unset = UNSET,
    reservation: str | Unset = UNSET,
    state: str | Unset = UNSET,
    step: str | Unset = UNSET,
    node: str | Unset = UNSET,
    wckey: str | Unset = UNSET,
) -> Status | None:
    """Get job list

    Args:
        users (str | Unset):
        submit_time (str | Unset):
        start_time (str | Unset):
        end_time (str | Unset):
        account (str | Unset):
        association (str | Unset):
        cluster (str | Unset):
        constraints (str | Unset):
        cpus_max (str | Unset):
        cpus_min (str | Unset):
        skip_steps (SlurmdbV0039GetJobsSkipSteps | Unset):  Default:
            SlurmdbV0039GetJobsSkipSteps.FALSE.
        disable_wait_for_result (SlurmdbV0039GetJobsDisableWaitForResult | Unset):  Default:
            SlurmdbV0039GetJobsDisableWaitForResult.FALSE.
        exit_code (str | Unset):
        format_ (str | Unset):
        group (str | Unset):
        job_name (str | Unset):
        nodes_max (str | Unset):
        nodes_min (str | Unset):
        partition (str | Unset):
        qos (str | Unset):
        reason (str | Unset):
        reservation (str | Unset):
        state (str | Unset):
        step (str | Unset):
        node (str | Unset):
        wckey (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Status
    """

    return (
        await asyncio_detailed(
            client=client,
            users=users,
            submit_time=submit_time,
            start_time=start_time,
            end_time=end_time,
            account=account,
            association=association,
            cluster=cluster,
            constraints=constraints,
            cpus_max=cpus_max,
            cpus_min=cpus_min,
            skip_steps=skip_steps,
            disable_wait_for_result=disable_wait_for_result,
            exit_code=exit_code,
            format_=format_,
            group=group,
            job_name=job_name,
            nodes_max=nodes_max,
            nodes_min=nodes_min,
            partition=partition,
            qos=qos,
            reason=reason,
            reservation=reservation,
            state=state,
            step=step,
            node=node,
            wckey=wckey,
        )
    ).parsed
