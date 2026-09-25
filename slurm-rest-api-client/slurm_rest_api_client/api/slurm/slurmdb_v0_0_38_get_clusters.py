from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.dbv_0038_cluster_info import Dbv0038ClusterInfo
from ...models.dbv_0038_error import Dbv0038Error
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/slurmdb/v0.0.38/clusters",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Dbv0038ClusterInfo | list[Dbv0038Error]:
    if response.status_code == 200:
        response_200 = Dbv0038ClusterInfo.from_dict(response.json())

        return response_200

    response_default = []
    _response_default = response.json()
    for componentsschemasdbv0_0_38_errors_item_data in _response_default:
        componentsschemasdbv0_0_38_errors_item = Dbv0038Error.from_dict(componentsschemasdbv0_0_38_errors_item_data)

        response_default.append(componentsschemasdbv0_0_38_errors_item)

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Dbv0038ClusterInfo | list[Dbv0038Error]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[Dbv0038ClusterInfo | list[Dbv0038Error]]:
    """Get cluster list

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Dbv0038ClusterInfo | list[Dbv0038Error]]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> Dbv0038ClusterInfo | list[Dbv0038Error] | None:
    """Get cluster list

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Dbv0038ClusterInfo | list[Dbv0038Error]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[Dbv0038ClusterInfo | list[Dbv0038Error]]:
    """Get cluster list

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Dbv0038ClusterInfo | list[Dbv0038Error]]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> Dbv0038ClusterInfo | list[Dbv0038Error] | None:
    """Get cluster list

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Dbv0038ClusterInfo | list[Dbv0038Error]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
