from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.dbv_0037_response_wckey_delete import Dbv0037ResponseWckeyDelete
from ...types import Response


def _get_kwargs(
    wckey: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/slurmdb/v0.0.37/wckey/{wckey}".format(
            wckey=quote(str(wckey), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | Dbv0037ResponseWckeyDelete:
    if response.status_code == 200:
        response_200 = Dbv0037ResponseWckeyDelete.from_dict(response.json())

        return response_200

    response_default = cast(Any, None)
    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | Dbv0037ResponseWckeyDelete]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    wckey: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | Dbv0037ResponseWckeyDelete]:
    """Delete wckey

    Args:
        wckey (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Dbv0037ResponseWckeyDelete]
    """

    kwargs = _get_kwargs(
        wckey=wckey,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    wckey: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | Dbv0037ResponseWckeyDelete | None:
    """Delete wckey

    Args:
        wckey (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Dbv0037ResponseWckeyDelete
    """

    return sync_detailed(
        wckey=wckey,
        client=client,
    ).parsed


async def asyncio_detailed(
    wckey: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | Dbv0037ResponseWckeyDelete]:
    """Delete wckey

    Args:
        wckey (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Dbv0037ResponseWckeyDelete]
    """

    kwargs = _get_kwargs(
        wckey=wckey,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    wckey: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | Dbv0037ResponseWckeyDelete | None:
    """Delete wckey

    Args:
        wckey (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Dbv0037ResponseWckeyDelete
    """

    return (
        await asyncio_detailed(
            wckey=wckey,
            client=client,
        )
    ).parsed
