from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.dbv_0038_account_info import Dbv0038AccountInfo
from ...models.dbv_0038_error import Dbv0038Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    account_name: str,
    *,
    with_deleted: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["with_deleted"] = with_deleted

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/slurmdb/v0.0.38/account/{account_name}".format(
            account_name=quote(str(account_name), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Dbv0038AccountInfo | list[Dbv0038Error]:
    if response.status_code == 200:
        response_200 = Dbv0038AccountInfo.from_dict(response.json())

        return response_200

    response_default = []
    _response_default = response.json()
    for componentsschemasdbv0_0_38_errors_item_data in _response_default:
        componentsschemasdbv0_0_38_errors_item = Dbv0038Error.from_dict(componentsschemasdbv0_0_38_errors_item_data)

        response_default.append(componentsschemasdbv0_0_38_errors_item)

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Dbv0038AccountInfo | list[Dbv0038Error]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    account_name: str,
    *,
    client: AuthenticatedClient | Client,
    with_deleted: bool | Unset = UNSET,
) -> Response[Dbv0038AccountInfo | list[Dbv0038Error]]:
    """Get account info

    Args:
        account_name (str):
        with_deleted (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Dbv0038AccountInfo | list[Dbv0038Error]]
    """

    kwargs = _get_kwargs(
        account_name=account_name,
        with_deleted=with_deleted,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_name: str,
    *,
    client: AuthenticatedClient | Client,
    with_deleted: bool | Unset = UNSET,
) -> Dbv0038AccountInfo | list[Dbv0038Error] | None:
    """Get account info

    Args:
        account_name (str):
        with_deleted (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Dbv0038AccountInfo | list[Dbv0038Error]
    """

    return sync_detailed(
        account_name=account_name,
        client=client,
        with_deleted=with_deleted,
    ).parsed


async def asyncio_detailed(
    account_name: str,
    *,
    client: AuthenticatedClient | Client,
    with_deleted: bool | Unset = UNSET,
) -> Response[Dbv0038AccountInfo | list[Dbv0038Error]]:
    """Get account info

    Args:
        account_name (str):
        with_deleted (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Dbv0038AccountInfo | list[Dbv0038Error]]
    """

    kwargs = _get_kwargs(
        account_name=account_name,
        with_deleted=with_deleted,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_name: str,
    *,
    client: AuthenticatedClient | Client,
    with_deleted: bool | Unset = UNSET,
) -> Dbv0038AccountInfo | list[Dbv0038Error] | None:
    """Get account info

    Args:
        account_name (str):
        with_deleted (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Dbv0038AccountInfo | list[Dbv0038Error]
    """

    return (
        await asyncio_detailed(
            account_name=account_name,
            client=client,
            with_deleted=with_deleted,
        )
    ).parsed
