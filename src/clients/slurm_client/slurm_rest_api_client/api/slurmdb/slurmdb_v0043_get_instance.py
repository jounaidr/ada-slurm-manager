from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.v0043_openapi_instances_resp import V0043OpenapiInstancesResp
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    cluster: str | Unset = UNSET,
    extra: str | Unset = UNSET,
    format_: str | Unset = UNSET,
    instance_id: str | Unset = UNSET,
    instance_type: str | Unset = UNSET,
    node_list: str | Unset = UNSET,
    time_end: str | Unset = UNSET,
    time_start: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["cluster"] = cluster

    params["extra"] = extra

    params["format"] = format_

    params["instance_id"] = instance_id

    params["instance_type"] = instance_type

    params["node_list"] = node_list

    params["time_end"] = time_end

    params["time_start"] = time_start

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/slurmdb/v0.0.43/instance/",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> V0043OpenapiInstancesResp:
    if response.status_code == 200:
        response_200 = V0043OpenapiInstancesResp.from_dict(response.json())

        return response_200

    response_default = V0043OpenapiInstancesResp.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[V0043OpenapiInstancesResp]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    cluster: str | Unset = UNSET,
    extra: str | Unset = UNSET,
    format_: str | Unset = UNSET,
    instance_id: str | Unset = UNSET,
    instance_type: str | Unset = UNSET,
    node_list: str | Unset = UNSET,
    time_end: str | Unset = UNSET,
    time_start: str | Unset = UNSET,
) -> Response[V0043OpenapiInstancesResp]:
    """Get instance info

    Args:
        cluster (str | Unset):
        extra (str | Unset):
        format_ (str | Unset):
        instance_id (str | Unset):
        instance_type (str | Unset):
        node_list (str | Unset):
        time_end (str | Unset):
        time_start (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[V0043OpenapiInstancesResp]
    """

    kwargs = _get_kwargs(
        cluster=cluster,
        extra=extra,
        format_=format_,
        instance_id=instance_id,
        instance_type=instance_type,
        node_list=node_list,
        time_end=time_end,
        time_start=time_start,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    cluster: str | Unset = UNSET,
    extra: str | Unset = UNSET,
    format_: str | Unset = UNSET,
    instance_id: str | Unset = UNSET,
    instance_type: str | Unset = UNSET,
    node_list: str | Unset = UNSET,
    time_end: str | Unset = UNSET,
    time_start: str | Unset = UNSET,
) -> V0043OpenapiInstancesResp | None:
    """Get instance info

    Args:
        cluster (str | Unset):
        extra (str | Unset):
        format_ (str | Unset):
        instance_id (str | Unset):
        instance_type (str | Unset):
        node_list (str | Unset):
        time_end (str | Unset):
        time_start (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        V0043OpenapiInstancesResp
    """

    return sync_detailed(
        client=client,
        cluster=cluster,
        extra=extra,
        format_=format_,
        instance_id=instance_id,
        instance_type=instance_type,
        node_list=node_list,
        time_end=time_end,
        time_start=time_start,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    cluster: str | Unset = UNSET,
    extra: str | Unset = UNSET,
    format_: str | Unset = UNSET,
    instance_id: str | Unset = UNSET,
    instance_type: str | Unset = UNSET,
    node_list: str | Unset = UNSET,
    time_end: str | Unset = UNSET,
    time_start: str | Unset = UNSET,
) -> Response[V0043OpenapiInstancesResp]:
    """Get instance info

    Args:
        cluster (str | Unset):
        extra (str | Unset):
        format_ (str | Unset):
        instance_id (str | Unset):
        instance_type (str | Unset):
        node_list (str | Unset):
        time_end (str | Unset):
        time_start (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[V0043OpenapiInstancesResp]
    """

    kwargs = _get_kwargs(
        cluster=cluster,
        extra=extra,
        format_=format_,
        instance_id=instance_id,
        instance_type=instance_type,
        node_list=node_list,
        time_end=time_end,
        time_start=time_start,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    cluster: str | Unset = UNSET,
    extra: str | Unset = UNSET,
    format_: str | Unset = UNSET,
    instance_id: str | Unset = UNSET,
    instance_type: str | Unset = UNSET,
    node_list: str | Unset = UNSET,
    time_end: str | Unset = UNSET,
    time_start: str | Unset = UNSET,
) -> V0043OpenapiInstancesResp | None:
    """Get instance info

    Args:
        cluster (str | Unset):
        extra (str | Unset):
        format_ (str | Unset):
        instance_id (str | Unset):
        instance_type (str | Unset):
        node_list (str | Unset):
        time_end (str | Unset):
        time_start (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        V0043OpenapiInstancesResp
    """

    return (
        await asyncio_detailed(
            client=client,
            cluster=cluster,
            extra=extra,
            format_=format_,
            instance_id=instance_id,
            instance_type=instance_type,
            node_list=node_list,
            time_end=time_end,
            time_start=time_start,
        )
    ).parsed
