from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.dbv_0037_response_user_delete import Dbv0037ResponseUserDelete
from ...types import Response


def _get_kwargs(
    user_name: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/slurmdb/v0.0.37/user/{user_name}".format(
            user_name=quote(str(user_name), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | Dbv0037ResponseUserDelete:
    if response.status_code == 200:
        response_200 = Dbv0037ResponseUserDelete.from_dict(response.json())

        return response_200

    response_default = cast(Any, None)
    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | Dbv0037ResponseUserDelete]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | Dbv0037ResponseUserDelete]:
    """Delete user

    Args:
        user_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Dbv0037ResponseUserDelete]
    """

    kwargs = _get_kwargs(
        user_name=user_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | Dbv0037ResponseUserDelete | None:
    """Delete user

    Args:
        user_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Dbv0037ResponseUserDelete
    """

    return sync_detailed(
        user_name=user_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    user_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | Dbv0037ResponseUserDelete]:
    """Delete user

    Args:
        user_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Dbv0037ResponseUserDelete]
    """

    kwargs = _get_kwargs(
        user_name=user_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | Dbv0037ResponseUserDelete | None:
    """Delete user

    Args:
        user_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Dbv0037ResponseUserDelete
    """

    return (
        await asyncio_detailed(
            user_name=user_name,
            client=client,
        )
    ).parsed
