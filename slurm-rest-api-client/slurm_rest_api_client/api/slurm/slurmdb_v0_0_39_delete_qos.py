from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.status import Status
from ...types import Response


def _get_kwargs(
    qos_name: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/slurmdb/v0.0.39/qos/{qos_name}".format(
            qos_name=quote(str(qos_name), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Status:
    if response.status_code == 200:
        response_200 = Status.from_dict(response.json())

        return response_200

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
    qos_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Status]:
    """Delete QOS

    Args:
        qos_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Status]
    """

    kwargs = _get_kwargs(
        qos_name=qos_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    qos_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Status | None:
    """Delete QOS

    Args:
        qos_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Status
    """

    return sync_detailed(
        qos_name=qos_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    qos_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Status]:
    """Delete QOS

    Args:
        qos_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Status]
    """

    kwargs = _get_kwargs(
        qos_name=qos_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    qos_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Status | None:
    """Delete QOS

    Args:
        qos_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Status
    """

    return (
        await asyncio_detailed(
            qos_name=qos_name,
            client=client,
        )
    ).parsed
