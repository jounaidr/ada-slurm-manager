from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.dbv_0039_wckey_info import Dbv0039WckeyInfo
from ...models.status import Status
from ...types import Response


def _get_kwargs(
    wckey: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/slurmdb/v0.0.39/wckey/{wckey}".format(
            wckey=quote(str(wckey), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Dbv0039WckeyInfo | Status:
    if response.status_code == 200:
        response_200 = Dbv0039WckeyInfo.from_dict(response.json())

        return response_200

    response_default = Status.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Dbv0039WckeyInfo | Status]:
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
) -> Response[Dbv0039WckeyInfo | Status]:
    """Get wckey info

    Args:
        wckey (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Dbv0039WckeyInfo | Status]
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
) -> Dbv0039WckeyInfo | Status | None:
    """Get wckey info

    Args:
        wckey (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Dbv0039WckeyInfo | Status
    """

    return sync_detailed(
        wckey=wckey,
        client=client,
    ).parsed


async def asyncio_detailed(
    wckey: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Dbv0039WckeyInfo | Status]:
    """Get wckey info

    Args:
        wckey (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Dbv0039WckeyInfo | Status]
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
) -> Dbv0039WckeyInfo | Status | None:
    """Get wckey info

    Args:
        wckey (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Dbv0039WckeyInfo | Status
    """

    return (
        await asyncio_detailed(
            wckey=wckey,
            client=client,
        )
    ).parsed
