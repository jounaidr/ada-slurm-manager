from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.dbv_0038_error import Dbv0038Error
from ...models.dbv_0038_response_wckey_add import Dbv0038ResponseWckeyAdd
from ...models.dbv_0038_wckey_info import Dbv0038WckeyInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: Dbv0038WckeyInfo | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/slurmdb/v0.0.38/wckeys",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Dbv0038ResponseWckeyAdd | list[Dbv0038Error]:
    if response.status_code == 200:
        response_200 = Dbv0038ResponseWckeyAdd.from_dict(response.json())

        return response_200

    response_default = []
    _response_default = response.json()
    for componentsschemasdbv0_0_38_errors_item_data in _response_default:
        componentsschemasdbv0_0_38_errors_item = Dbv0038Error.from_dict(componentsschemasdbv0_0_38_errors_item_data)

        response_default.append(componentsschemasdbv0_0_38_errors_item)

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Dbv0038ResponseWckeyAdd | list[Dbv0038Error]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: Dbv0038WckeyInfo | Unset = UNSET,
) -> Response[Dbv0038ResponseWckeyAdd | list[Dbv0038Error]]:
    """Add wckeys

    Args:
        body (Dbv0038WckeyInfo | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Dbv0038ResponseWckeyAdd | list[Dbv0038Error]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: Dbv0038WckeyInfo | Unset = UNSET,
) -> Dbv0038ResponseWckeyAdd | list[Dbv0038Error] | None:
    """Add wckeys

    Args:
        body (Dbv0038WckeyInfo | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Dbv0038ResponseWckeyAdd | list[Dbv0038Error]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: Dbv0038WckeyInfo | Unset = UNSET,
) -> Response[Dbv0038ResponseWckeyAdd | list[Dbv0038Error]]:
    """Add wckeys

    Args:
        body (Dbv0038WckeyInfo | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Dbv0038ResponseWckeyAdd | list[Dbv0038Error]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: Dbv0038WckeyInfo | Unset = UNSET,
) -> Dbv0038ResponseWckeyAdd | list[Dbv0038Error] | None:
    """Add wckeys

    Args:
        body (Dbv0038WckeyInfo | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Dbv0038ResponseWckeyAdd | list[Dbv0038Error]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
