from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.v0037_nodes_response import V0037NodesResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    update_time: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["update_time"] = update_time

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/slurm/v0.0.37/nodes",
        "params": params,
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
    *,
    client: AuthenticatedClient | Client,
    update_time: int | Unset = UNSET,
) -> Response[Any | V0037NodesResponse]:
    """get all node info

    Args:
        update_time (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | V0037NodesResponse]
    """

    kwargs = _get_kwargs(
        update_time=update_time,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    update_time: int | Unset = UNSET,
) -> Any | V0037NodesResponse | None:
    """get all node info

    Args:
        update_time (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | V0037NodesResponse
    """

    return sync_detailed(
        client=client,
        update_time=update_time,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    update_time: int | Unset = UNSET,
) -> Response[Any | V0037NodesResponse]:
    """get all node info

    Args:
        update_time (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | V0037NodesResponse]
    """

    kwargs = _get_kwargs(
        update_time=update_time,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    update_time: int | Unset = UNSET,
) -> Any | V0037NodesResponse | None:
    """get all node info

    Args:
        update_time (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | V0037NodesResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            update_time=update_time,
        )
    ).parsed
