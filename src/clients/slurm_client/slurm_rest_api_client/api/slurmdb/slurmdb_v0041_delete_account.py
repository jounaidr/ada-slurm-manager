from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.slurmdb_v0041_delete_account_response_200 import SlurmdbV0041DeleteAccountResponse200
from ...models.slurmdb_v0041_delete_account_response_default import SlurmdbV0041DeleteAccountResponseDefault
from ...types import Response


def _get_kwargs(
    account_name: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/slurmdb/v0.0.41/account/{account_name}".format(
            account_name=quote(str(account_name), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> SlurmdbV0041DeleteAccountResponse200 | SlurmdbV0041DeleteAccountResponseDefault:
    if response.status_code == 200:
        response_200 = SlurmdbV0041DeleteAccountResponse200.from_dict(response.json())

        return response_200

    response_default = SlurmdbV0041DeleteAccountResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[SlurmdbV0041DeleteAccountResponse200 | SlurmdbV0041DeleteAccountResponseDefault]:
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
) -> Response[SlurmdbV0041DeleteAccountResponse200 | SlurmdbV0041DeleteAccountResponseDefault]:
    """Delete account

    Args:
        account_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SlurmdbV0041DeleteAccountResponse200 | SlurmdbV0041DeleteAccountResponseDefault]
    """

    kwargs = _get_kwargs(
        account_name=account_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> SlurmdbV0041DeleteAccountResponse200 | SlurmdbV0041DeleteAccountResponseDefault | None:
    """Delete account

    Args:
        account_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SlurmdbV0041DeleteAccountResponse200 | SlurmdbV0041DeleteAccountResponseDefault
    """

    return sync_detailed(
        account_name=account_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    account_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[SlurmdbV0041DeleteAccountResponse200 | SlurmdbV0041DeleteAccountResponseDefault]:
    """Delete account

    Args:
        account_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SlurmdbV0041DeleteAccountResponse200 | SlurmdbV0041DeleteAccountResponseDefault]
    """

    kwargs = _get_kwargs(
        account_name=account_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> SlurmdbV0041DeleteAccountResponse200 | SlurmdbV0041DeleteAccountResponseDefault | None:
    """Delete account

    Args:
        account_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SlurmdbV0041DeleteAccountResponse200 | SlurmdbV0041DeleteAccountResponseDefault
    """

    return (
        await asyncio_detailed(
            account_name=account_name,
            client=client,
        )
    ).parsed
