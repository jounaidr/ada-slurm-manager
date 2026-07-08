from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.v0044_openapi_accounts_resp import V0044OpenapiAccountsResp
from ...types import UNSET, Response, Unset


def _get_kwargs(
    account_name: str,
    *,
    with_assocs: str | Unset = UNSET,
    with_coords: str | Unset = UNSET,
    with_deleted: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["with_assocs"] = with_assocs

    params["with_coords"] = with_coords

    params["with_deleted"] = with_deleted

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/slurmdb/v0.0.44/account/{account_name}".format(
            account_name=quote(str(account_name), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> V0044OpenapiAccountsResp:
    if response.status_code == 200:
        response_200 = V0044OpenapiAccountsResp.from_dict(response.json())

        return response_200

    response_default = V0044OpenapiAccountsResp.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[V0044OpenapiAccountsResp]:
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
    with_assocs: str | Unset = UNSET,
    with_coords: str | Unset = UNSET,
    with_deleted: str | Unset = UNSET,
) -> Response[V0044OpenapiAccountsResp]:
    """Get account info

    Args:
        account_name (str):
        with_assocs (str | Unset):
        with_coords (str | Unset):
        with_deleted (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[V0044OpenapiAccountsResp]
    """

    kwargs = _get_kwargs(
        account_name=account_name,
        with_assocs=with_assocs,
        with_coords=with_coords,
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
    with_assocs: str | Unset = UNSET,
    with_coords: str | Unset = UNSET,
    with_deleted: str | Unset = UNSET,
) -> V0044OpenapiAccountsResp | None:
    """Get account info

    Args:
        account_name (str):
        with_assocs (str | Unset):
        with_coords (str | Unset):
        with_deleted (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        V0044OpenapiAccountsResp
    """

    return sync_detailed(
        account_name=account_name,
        client=client,
        with_assocs=with_assocs,
        with_coords=with_coords,
        with_deleted=with_deleted,
    ).parsed


async def asyncio_detailed(
    account_name: str,
    *,
    client: AuthenticatedClient | Client,
    with_assocs: str | Unset = UNSET,
    with_coords: str | Unset = UNSET,
    with_deleted: str | Unset = UNSET,
) -> Response[V0044OpenapiAccountsResp]:
    """Get account info

    Args:
        account_name (str):
        with_assocs (str | Unset):
        with_coords (str | Unset):
        with_deleted (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[V0044OpenapiAccountsResp]
    """

    kwargs = _get_kwargs(
        account_name=account_name,
        with_assocs=with_assocs,
        with_coords=with_coords,
        with_deleted=with_deleted,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_name: str,
    *,
    client: AuthenticatedClient | Client,
    with_assocs: str | Unset = UNSET,
    with_coords: str | Unset = UNSET,
    with_deleted: str | Unset = UNSET,
) -> V0044OpenapiAccountsResp | None:
    """Get account info

    Args:
        account_name (str):
        with_assocs (str | Unset):
        with_coords (str | Unset):
        with_deleted (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        V0044OpenapiAccountsResp
    """

    return (
        await asyncio_detailed(
            account_name=account_name,
            client=client,
            with_assocs=with_assocs,
            with_coords=with_coords,
            with_deleted=with_deleted,
        )
    ).parsed
