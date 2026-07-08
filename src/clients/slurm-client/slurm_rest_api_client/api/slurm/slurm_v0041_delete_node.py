from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.v0041_openapi_resp import V0041OpenapiResp
from ...types import Response


def _get_kwargs(
    node_name: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/slurm/v0.0.41/node/{node_name}".format(
            node_name=quote(str(node_name), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> V0041OpenapiResp:
    if response.status_code == 200:
        response_200 = V0041OpenapiResp.from_dict(response.json())

        return response_200

    response_default = V0041OpenapiResp.from_dict(response.json())

    return response_default


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[V0041OpenapiResp]:
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
) -> Response[V0041OpenapiResp]:
    """delete node

    Args:
        node_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[V0041OpenapiResp]
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
) -> V0041OpenapiResp | None:
    """delete node

    Args:
        node_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        V0041OpenapiResp
    """

    return sync_detailed(
        node_name=node_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    node_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[V0041OpenapiResp]:
    """delete node

    Args:
        node_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[V0041OpenapiResp]
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
) -> V0041OpenapiResp | None:
    """delete node

    Args:
        node_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        V0041OpenapiResp
    """

    return (
        await asyncio_detailed(
            node_name=node_name,
            client=client,
        )
    ).parsed
