from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.v0037_nodes_response import V0037NodesResponse
from ...types import Response


def _get_kwargs(
    node_name: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/slurm/v0.0.37/node/{node_name}".format(
            node_name=quote(str(node_name), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | V0037NodesResponse:
    if response.status_code == 200:
        response_200 = V0037NodesResponse.from_dict(response.json())

        return response_200

    response_default = cast(Any, None)
    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | V0037NodesResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    node_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | V0037NodesResponse]:
    """get node info

    Args:
        node_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | V0037NodesResponse]
    """

    kwargs = _get_kwargs(
        node_name=node_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    node_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | V0037NodesResponse | None:
    """get node info

    Args:
        node_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | V0037NodesResponse
    """

    return sync_detailed(
        node_name=node_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    node_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | V0037NodesResponse]:
    """get node info

    Args:
        node_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | V0037NodesResponse]
    """

    kwargs = _get_kwargs(
        node_name=node_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    node_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | V0037NodesResponse | None:
    """get node info

    Args:
        node_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | V0037NodesResponse
    """

    return (
        await asyncio_detailed(
            node_name=node_name,
            client=client,
        )
    ).parsed
