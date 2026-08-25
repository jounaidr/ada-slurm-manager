from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.status import Status
from ...types import UNSET, Response, Unset


def _get_kwargs(
    partition_name: str,
    *,
    update_time: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["update_time"] = update_time

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/slurm/v0.0.39/partition/{partition_name}".format(
            partition_name=quote(str(partition_name), safe=""),
        ),
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
    partition_name: str,
    *,
    client: AuthenticatedClient | Client,
    update_time: int | Unset = UNSET,
) -> Response[Status]:
    """get partition info

    Args:
        partition_name (str):
        update_time (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Status]
    """

    kwargs = _get_kwargs(
        partition_name=partition_name,
        update_time=update_time,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    partition_name: str,
    *,
    client: AuthenticatedClient | Client,
    update_time: int | Unset = UNSET,
) -> Status | None:
    """get partition info

    Args:
        partition_name (str):
        update_time (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Status
    """

    return sync_detailed(
        partition_name=partition_name,
        client=client,
        update_time=update_time,
    ).parsed


async def asyncio_detailed(
    partition_name: str,
    *,
    client: AuthenticatedClient | Client,
    update_time: int | Unset = UNSET,
) -> Response[Status]:
    """get partition info

    Args:
        partition_name (str):
        update_time (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Status]
    """

    kwargs = _get_kwargs(
        partition_name=partition_name,
        update_time=update_time,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    partition_name: str,
    *,
    client: AuthenticatedClient | Client,
    update_time: int | Unset = UNSET,
) -> Status | None:
    """get partition info

    Args:
        partition_name (str):
        update_time (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Status
    """

    return (
        await asyncio_detailed(
            partition_name=partition_name,
            client=client,
            update_time=update_time,
        )
    ).parsed
