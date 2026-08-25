from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.dbv_0037_cluster_info import Dbv0037ClusterInfo
from ...types import Response


def _get_kwargs(
    cluster_name: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/slurmdb/v0.0.37/cluster/{cluster_name}".format(
            cluster_name=quote(str(cluster_name), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | Dbv0037ClusterInfo:
    if response.status_code == 200:
        response_200 = Dbv0037ClusterInfo.from_dict(response.json())

        return response_200

    response_default = cast(Any, None)
    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | Dbv0037ClusterInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    cluster_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | Dbv0037ClusterInfo]:
    """Get cluster info

    Args:
        cluster_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Dbv0037ClusterInfo]
    """

    kwargs = _get_kwargs(
        cluster_name=cluster_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    cluster_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | Dbv0037ClusterInfo | None:
    """Get cluster info

    Args:
        cluster_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Dbv0037ClusterInfo
    """

    return sync_detailed(
        cluster_name=cluster_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    cluster_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | Dbv0037ClusterInfo]:
    """Get cluster info

    Args:
        cluster_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Dbv0037ClusterInfo]
    """

    kwargs = _get_kwargs(
        cluster_name=cluster_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    cluster_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | Dbv0037ClusterInfo | None:
    """Get cluster info

    Args:
        cluster_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Dbv0037ClusterInfo
    """

    return (
        await asyncio_detailed(
            cluster_name=cluster_name,
            client=client,
        )
    ).parsed
