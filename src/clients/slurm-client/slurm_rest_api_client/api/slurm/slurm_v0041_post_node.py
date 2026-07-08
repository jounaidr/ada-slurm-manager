from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.v0041_openapi_resp import V0041OpenapiResp
from ...models.v0041_update_node_msg import V0041UpdateNodeMsg
from ...types import UNSET, Response, Unset


def _get_kwargs(
    node_name: str,
    *,
    body: V0041UpdateNodeMsg | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/slurm/v0.0.41/node/{node_name}".format(
            node_name=quote(str(node_name), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
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
    body: V0041UpdateNodeMsg | Unset = UNSET,
) -> Response[V0041OpenapiResp]:
    """update node properties

    Args:
        node_name (str):
        body (V0041UpdateNodeMsg | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[V0041OpenapiResp]
    """

    kwargs = _get_kwargs(
        node_name=node_name,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    node_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: V0041UpdateNodeMsg | Unset = UNSET,
) -> V0041OpenapiResp | None:
    """update node properties

    Args:
        node_name (str):
        body (V0041UpdateNodeMsg | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        V0041OpenapiResp
    """

    return sync_detailed(
        node_name=node_name,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    node_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: V0041UpdateNodeMsg | Unset = UNSET,
) -> Response[V0041OpenapiResp]:
    """update node properties

    Args:
        node_name (str):
        body (V0041UpdateNodeMsg | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[V0041OpenapiResp]
    """

    kwargs = _get_kwargs(
        node_name=node_name,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    node_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: V0041UpdateNodeMsg | Unset = UNSET,
) -> V0041OpenapiResp | None:
    """update node properties

    Args:
        node_name (str):
        body (V0041UpdateNodeMsg | Unset):

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
            body=body,
        )
    ).parsed
