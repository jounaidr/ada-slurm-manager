from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.slurmdb_v0041_post_users_association_body import SlurmdbV0041PostUsersAssociationBody
from ...models.slurmdb_v0041_post_users_association_flags import SlurmdbV0041PostUsersAssociationFlags
from ...models.slurmdb_v0041_post_users_association_response_200 import SlurmdbV0041PostUsersAssociationResponse200
from ...models.slurmdb_v0041_post_users_association_response_default import (
    SlurmdbV0041PostUsersAssociationResponseDefault,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: SlurmdbV0041PostUsersAssociationBody | Unset = UNSET,
    update_time: str | Unset = UNSET,
    flags: SlurmdbV0041PostUsersAssociationFlags | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["update_time"] = update_time

    json_flags: str | Unset = UNSET
    if not isinstance(flags, Unset):
        json_flags = flags.value

    params["flags"] = json_flags

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/slurmdb/v0.0.41/users_association/",
        "params": params,
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> SlurmdbV0041PostUsersAssociationResponse200 | SlurmdbV0041PostUsersAssociationResponseDefault:
    if response.status_code == 200:
        response_200 = SlurmdbV0041PostUsersAssociationResponse200.from_dict(response.json())

        return response_200

    response_default = SlurmdbV0041PostUsersAssociationResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[SlurmdbV0041PostUsersAssociationResponse200 | SlurmdbV0041PostUsersAssociationResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SlurmdbV0041PostUsersAssociationBody | Unset = UNSET,
    update_time: str | Unset = UNSET,
    flags: SlurmdbV0041PostUsersAssociationFlags | Unset = UNSET,
) -> Response[SlurmdbV0041PostUsersAssociationResponse200 | SlurmdbV0041PostUsersAssociationResponseDefault]:
    """Add users with conditional association

    Args:
        update_time (str | Unset):
        flags (SlurmdbV0041PostUsersAssociationFlags | Unset):
        body (SlurmdbV0041PostUsersAssociationBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SlurmdbV0041PostUsersAssociationResponse200 | SlurmdbV0041PostUsersAssociationResponseDefault]
    """

    kwargs = _get_kwargs(
        body=body,
        update_time=update_time,
        flags=flags,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: SlurmdbV0041PostUsersAssociationBody | Unset = UNSET,
    update_time: str | Unset = UNSET,
    flags: SlurmdbV0041PostUsersAssociationFlags | Unset = UNSET,
) -> SlurmdbV0041PostUsersAssociationResponse200 | SlurmdbV0041PostUsersAssociationResponseDefault | None:
    """Add users with conditional association

    Args:
        update_time (str | Unset):
        flags (SlurmdbV0041PostUsersAssociationFlags | Unset):
        body (SlurmdbV0041PostUsersAssociationBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SlurmdbV0041PostUsersAssociationResponse200 | SlurmdbV0041PostUsersAssociationResponseDefault
    """

    return sync_detailed(
        client=client,
        body=body,
        update_time=update_time,
        flags=flags,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SlurmdbV0041PostUsersAssociationBody | Unset = UNSET,
    update_time: str | Unset = UNSET,
    flags: SlurmdbV0041PostUsersAssociationFlags | Unset = UNSET,
) -> Response[SlurmdbV0041PostUsersAssociationResponse200 | SlurmdbV0041PostUsersAssociationResponseDefault]:
    """Add users with conditional association

    Args:
        update_time (str | Unset):
        flags (SlurmdbV0041PostUsersAssociationFlags | Unset):
        body (SlurmdbV0041PostUsersAssociationBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SlurmdbV0041PostUsersAssociationResponse200 | SlurmdbV0041PostUsersAssociationResponseDefault]
    """

    kwargs = _get_kwargs(
        body=body,
        update_time=update_time,
        flags=flags,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: SlurmdbV0041PostUsersAssociationBody | Unset = UNSET,
    update_time: str | Unset = UNSET,
    flags: SlurmdbV0041PostUsersAssociationFlags | Unset = UNSET,
) -> SlurmdbV0041PostUsersAssociationResponse200 | SlurmdbV0041PostUsersAssociationResponseDefault | None:
    """Add users with conditional association

    Args:
        update_time (str | Unset):
        flags (SlurmdbV0041PostUsersAssociationFlags | Unset):
        body (SlurmdbV0041PostUsersAssociationBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SlurmdbV0041PostUsersAssociationResponse200 | SlurmdbV0041PostUsersAssociationResponseDefault
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            update_time=update_time,
            flags=flags,
        )
    ).parsed
