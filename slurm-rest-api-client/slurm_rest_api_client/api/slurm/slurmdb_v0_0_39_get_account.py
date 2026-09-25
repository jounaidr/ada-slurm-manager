from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.dbv_0039_account_info import Dbv0039AccountInfo
from ...models.slurmdb_v0039_get_account_with_deleted import SlurmdbV0039GetAccountWithDeleted
from ...models.status import Status
from ...types import UNSET, Response, Unset


def _get_kwargs(
    account_name: str,
    *,
    with_deleted: SlurmdbV0039GetAccountWithDeleted | Unset = SlurmdbV0039GetAccountWithDeleted.FALSE,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_with_deleted: str | Unset = UNSET
    if not isinstance(with_deleted, Unset):
        json_with_deleted = with_deleted.value

    params["with_deleted"] = json_with_deleted

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/slurmdb/v0.0.39/account/{account_name}".format(
            account_name=quote(str(account_name), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Dbv0039AccountInfo | Status:
    if response.status_code == 200:
        response_200 = Dbv0039AccountInfo.from_dict(response.json())

        return response_200

    response_default = Status.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Dbv0039AccountInfo | Status]:
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
    with_deleted: SlurmdbV0039GetAccountWithDeleted | Unset = SlurmdbV0039GetAccountWithDeleted.FALSE,
) -> Response[Dbv0039AccountInfo | Status]:
    """Get account info

    Args:
        account_name (str):
        with_deleted (SlurmdbV0039GetAccountWithDeleted | Unset):  Default:
            SlurmdbV0039GetAccountWithDeleted.FALSE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Dbv0039AccountInfo | Status]
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
    with_deleted: SlurmdbV0039GetAccountWithDeleted | Unset = SlurmdbV0039GetAccountWithDeleted.FALSE,
) -> Dbv0039AccountInfo | Status | None:
    """Get account info

    Args:
        account_name (str):
        with_deleted (SlurmdbV0039GetAccountWithDeleted | Unset):  Default:
            SlurmdbV0039GetAccountWithDeleted.FALSE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Dbv0039AccountInfo | Status
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
    with_deleted: SlurmdbV0039GetAccountWithDeleted | Unset = SlurmdbV0039GetAccountWithDeleted.FALSE,
) -> Response[Dbv0039AccountInfo | Status]:
    """Get account info

    Args:
        account_name (str):
        with_deleted (SlurmdbV0039GetAccountWithDeleted | Unset):  Default:
            SlurmdbV0039GetAccountWithDeleted.FALSE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Dbv0039AccountInfo | Status]
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
    with_deleted: SlurmdbV0039GetAccountWithDeleted | Unset = SlurmdbV0039GetAccountWithDeleted.FALSE,
) -> Dbv0039AccountInfo | Status | None:
    """Get account info

    Args:
        account_name (str):
        with_deleted (SlurmdbV0039GetAccountWithDeleted | Unset):  Default:
            SlurmdbV0039GetAccountWithDeleted.FALSE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Dbv0039AccountInfo | Status
    """

    return (
        await asyncio_detailed(
            account_name=account_name,
            client=client,
            with_deleted=with_deleted,
        )
    ).parsed
