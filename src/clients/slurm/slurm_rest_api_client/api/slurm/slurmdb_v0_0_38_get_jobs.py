from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.dbv_0038_error import Dbv0038Error
from ...models.dbv_0038_job_info import Dbv0038JobInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    submit_time: str | Unset = UNSET,
    start_time: str | Unset = UNSET,
    end_time: str | Unset = UNSET,
    account: str | Unset = UNSET,
    association: str | Unset = UNSET,
    cluster: str | Unset = UNSET,
    constraints: str | Unset = UNSET,
    cpus_max: str | Unset = UNSET,
    cpus_min: str | Unset = UNSET,
    skip_steps: bool | Unset = UNSET,
    disable_wait_for_result: bool | Unset = UNSET,
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

    params["submit_time"] = submit_time

    params["start_time"] = start_time

    params["end_time"] = end_time

    params["account"] = account

    params["association"] = association

    params["cluster"] = cluster

    params["constraints"] = constraints

    params["cpus_max"] = cpus_max

    params["cpus_min"] = cpus_min

    params["skip_steps"] = skip_steps

    params["disable_wait_for_result"] = disable_wait_for_result

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
        "url": "/slurmdb/v0.0.38/jobs",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Dbv0038JobInfo | list[Dbv0038Error]:
    if response.status_code == 200:
        response_200 = Dbv0038JobInfo.from_dict(response.json())

        return response_200

    response_default = []
    _response_default = response.json()
    for componentsschemasdbv0_0_38_errors_item_data in _response_default:
        componentsschemasdbv0_0_38_errors_item = Dbv0038Error.from_dict(componentsschemasdbv0_0_38_errors_item_data)

        response_default.append(componentsschemasdbv0_0_38_errors_item)

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Dbv0038JobInfo | list[Dbv0038Error]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    submit_time: str | Unset = UNSET,
    start_time: str | Unset = UNSET,
    end_time: str | Unset = UNSET,
    account: str | Unset = UNSET,
    association: str | Unset = UNSET,
    cluster: str | Unset = UNSET,
    constraints: str | Unset = UNSET,
    cpus_max: str | Unset = UNSET,
    cpus_min: str | Unset = UNSET,
    skip_steps: bool | Unset = UNSET,
    disable_wait_for_result: bool | Unset = UNSET,
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
) -> Response[Dbv0038JobInfo | list[Dbv0038Error]]:
    """Get job list

    Args:
        submit_time (str | Unset):
        start_time (str | Unset):
        end_time (str | Unset):
        account (str | Unset):
        association (str | Unset):
        cluster (str | Unset):
        constraints (str | Unset):
        cpus_max (str | Unset):
        cpus_min (str | Unset):
        skip_steps (bool | Unset):
        disable_wait_for_result (bool | Unset):
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
        Response[Dbv0038JobInfo | list[Dbv0038Error]]
    """

    kwargs = _get_kwargs(
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
    submit_time: str | Unset = UNSET,
    start_time: str | Unset = UNSET,
    end_time: str | Unset = UNSET,
    account: str | Unset = UNSET,
    association: str | Unset = UNSET,
    cluster: str | Unset = UNSET,
    constraints: str | Unset = UNSET,
    cpus_max: str | Unset = UNSET,
    cpus_min: str | Unset = UNSET,
    skip_steps: bool | Unset = UNSET,
    disable_wait_for_result: bool | Unset = UNSET,
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
) -> Dbv0038JobInfo | list[Dbv0038Error] | None:
    """Get job list

    Args:
        submit_time (str | Unset):
        start_time (str | Unset):
        end_time (str | Unset):
        account (str | Unset):
        association (str | Unset):
        cluster (str | Unset):
        constraints (str | Unset):
        cpus_max (str | Unset):
        cpus_min (str | Unset):
        skip_steps (bool | Unset):
        disable_wait_for_result (bool | Unset):
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
        Dbv0038JobInfo | list[Dbv0038Error]
    """

    return sync_detailed(
        client=client,
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
    submit_time: str | Unset = UNSET,
    start_time: str | Unset = UNSET,
    end_time: str | Unset = UNSET,
    account: str | Unset = UNSET,
    association: str | Unset = UNSET,
    cluster: str | Unset = UNSET,
    constraints: str | Unset = UNSET,
    cpus_max: str | Unset = UNSET,
    cpus_min: str | Unset = UNSET,
    skip_steps: bool | Unset = UNSET,
    disable_wait_for_result: bool | Unset = UNSET,
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
) -> Response[Dbv0038JobInfo | list[Dbv0038Error]]:
    """Get job list

    Args:
        submit_time (str | Unset):
        start_time (str | Unset):
        end_time (str | Unset):
        account (str | Unset):
        association (str | Unset):
        cluster (str | Unset):
        constraints (str | Unset):
        cpus_max (str | Unset):
        cpus_min (str | Unset):
        skip_steps (bool | Unset):
        disable_wait_for_result (bool | Unset):
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
        Response[Dbv0038JobInfo | list[Dbv0038Error]]
    """

    kwargs = _get_kwargs(
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
    submit_time: str | Unset = UNSET,
    start_time: str | Unset = UNSET,
    end_time: str | Unset = UNSET,
    account: str | Unset = UNSET,
    association: str | Unset = UNSET,
    cluster: str | Unset = UNSET,
    constraints: str | Unset = UNSET,
    cpus_max: str | Unset = UNSET,
    cpus_min: str | Unset = UNSET,
    skip_steps: bool | Unset = UNSET,
    disable_wait_for_result: bool | Unset = UNSET,
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
) -> Dbv0038JobInfo | list[Dbv0038Error] | None:
    """Get job list

    Args:
        submit_time (str | Unset):
        start_time (str | Unset):
        end_time (str | Unset):
        account (str | Unset):
        association (str | Unset):
        cluster (str | Unset):
        constraints (str | Unset):
        cpus_max (str | Unset):
        cpus_min (str | Unset):
        skip_steps (bool | Unset):
        disable_wait_for_result (bool | Unset):
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
        Dbv0038JobInfo | list[Dbv0038Error]
    """

    return (
        await asyncio_detailed(
            client=client,
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
