from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.dbv_0037_associations_info import Dbv0037AssociationsInfo
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
        "method": "get",
        "url": "/slurmdb/v0.0.37/association",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | Dbv0037AssociationsInfo:
    if response.status_code == 200:
        response_200 = Dbv0037AssociationsInfo.from_dict(response.json())

        return response_200

    response_default = cast(Any, None)
    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | Dbv0037AssociationsInfo]:
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
) -> Response[Any | Dbv0037AssociationsInfo]:
    """Get association info

    Args:
        cluster (str | Unset):
        account (str | Unset):
        user (str | Unset):
        partition (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Dbv0037AssociationsInfo]
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
) -> Any | Dbv0037AssociationsInfo | None:
    """Get association info

    Args:
        cluster (str | Unset):
        account (str | Unset):
        user (str | Unset):
        partition (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Dbv0037AssociationsInfo
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
) -> Response[Any | Dbv0037AssociationsInfo]:
    """Get association info

    Args:
        cluster (str | Unset):
        account (str | Unset):
        user (str | Unset):
        partition (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Dbv0037AssociationsInfo]
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
) -> Any | Dbv0037AssociationsInfo | None:
    """Get association info

    Args:
        cluster (str | Unset):
        account (str | Unset):
        user (str | Unset):
        partition (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Dbv0037AssociationsInfo
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
