from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.dbv_0038_error import Dbv0038Error
from ...models.dbv_0038_response_associations_delete import Dbv0038ResponseAssociationsDelete
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    cluster: str | Unset = UNSET,
    account: str | Unset = UNSET,
    user: str | Unset = UNSET,
    partition: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["cluster"] = cluster

    params["account"] = account

    params["user"] = user

    params["partition"] = partition

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/slurmdb/v0.0.38/associations",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Dbv0038ResponseAssociationsDelete | list[Dbv0038Error]:
    if response.status_code == 200:
        response_200 = Dbv0038ResponseAssociationsDelete.from_dict(response.json())

        return response_200

    response_default = []
    _response_default = response.json()
    for componentsschemasdbv0_0_38_errors_item_data in _response_default:
        componentsschemasdbv0_0_38_errors_item = Dbv0038Error.from_dict(componentsschemasdbv0_0_38_errors_item_data)

        response_default.append(componentsschemasdbv0_0_38_errors_item)

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Dbv0038ResponseAssociationsDelete | list[Dbv0038Error]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    cluster: str | Unset = UNSET,
    account: str | Unset = UNSET,
    user: str | Unset = UNSET,
    partition: str | Unset = UNSET,
) -> Response[Dbv0038ResponseAssociationsDelete | list[Dbv0038Error]]:
    """Delete associations

    Args:
        cluster (str | Unset):
        account (str | Unset):
        user (str | Unset):
        partition (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Dbv0038ResponseAssociationsDelete | list[Dbv0038Error]]
    """

    kwargs = _get_kwargs(
        cluster=cluster,
        account=account,
        user=user,
        partition=partition,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    cluster: str | Unset = UNSET,
    account: str | Unset = UNSET,
    user: str | Unset = UNSET,
    partition: str | Unset = UNSET,
) -> Dbv0038ResponseAssociationsDelete | list[Dbv0038Error] | None:
    """Delete associations

    Args:
        cluster (str | Unset):
        account (str | Unset):
        user (str | Unset):
        partition (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Dbv0038ResponseAssociationsDelete | list[Dbv0038Error]
    """

    return sync_detailed(
        client=client,
        cluster=cluster,
        account=account,
        user=user,
        partition=partition,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    cluster: str | Unset = UNSET,
    account: str | Unset = UNSET,
    user: str | Unset = UNSET,
    partition: str | Unset = UNSET,
) -> Response[Dbv0038ResponseAssociationsDelete | list[Dbv0038Error]]:
    """Delete associations

    Args:
        cluster (str | Unset):
        account (str | Unset):
        user (str | Unset):
        partition (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Dbv0038ResponseAssociationsDelete | list[Dbv0038Error]]
    """

    kwargs = _get_kwargs(
        cluster=cluster,
        account=account,
        user=user,
        partition=partition,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    cluster: str | Unset = UNSET,
    account: str | Unset = UNSET,
    user: str | Unset = UNSET,
    partition: str | Unset = UNSET,
) -> Dbv0038ResponseAssociationsDelete | list[Dbv0038Error] | None:
    """Delete associations

    Args:
        cluster (str | Unset):
        account (str | Unset):
        user (str | Unset):
        partition (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Dbv0038ResponseAssociationsDelete | list[Dbv0038Error]
    """

    return (
        await asyncio_detailed(
            client=client,
            cluster=cluster,
            account=account,
            user=user,
            partition=partition,
        )
    ).parsed
