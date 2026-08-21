from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.v0042_openapi_accounts_resp import V0042OpenapiAccountsResp
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    description: str | Unset = UNSET,
    deleted: str | Unset = UNSET,
    with_associations: str | Unset = UNSET,
    with_coordinators: str | Unset = UNSET,
    no_users_are_coords: str | Unset = UNSET,
    users_are_coords: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["description"] = description

    params["DELETED"] = deleted

    params["WithAssociations"] = with_associations

    params["WithCoordinators"] = with_coordinators

    params["NoUsersAreCoords"] = no_users_are_coords

    params["UsersAreCoords"] = users_are_coords

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/slurmdb/v0.0.42/accounts/",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> V0042OpenapiAccountsResp:
    if response.status_code == 200:
        response_200 = V0042OpenapiAccountsResp.from_dict(response.json())

        return response_200

    response_default = V0042OpenapiAccountsResp.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[V0042OpenapiAccountsResp]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    description: str | Unset = UNSET,
    deleted: str | Unset = UNSET,
    with_associations: str | Unset = UNSET,
    with_coordinators: str | Unset = UNSET,
    no_users_are_coords: str | Unset = UNSET,
    users_are_coords: str | Unset = UNSET,
) -> Response[V0042OpenapiAccountsResp]:
    """Get account list

    Args:
        description (str | Unset):
        deleted (str | Unset):
        with_associations (str | Unset):
        with_coordinators (str | Unset):
        no_users_are_coords (str | Unset):
        users_are_coords (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[V0042OpenapiAccountsResp]
    """

    kwargs = _get_kwargs(
        description=description,
        deleted=deleted,
        with_associations=with_associations,
        with_coordinators=with_coordinators,
        no_users_are_coords=no_users_are_coords,
        users_are_coords=users_are_coords,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    description: str | Unset = UNSET,
    deleted: str | Unset = UNSET,
    with_associations: str | Unset = UNSET,
    with_coordinators: str | Unset = UNSET,
    no_users_are_coords: str | Unset = UNSET,
    users_are_coords: str | Unset = UNSET,
) -> V0042OpenapiAccountsResp | None:
    """Get account list

    Args:
        description (str | Unset):
        deleted (str | Unset):
        with_associations (str | Unset):
        with_coordinators (str | Unset):
        no_users_are_coords (str | Unset):
        users_are_coords (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        V0042OpenapiAccountsResp
    """

    return sync_detailed(
        client=client,
        description=description,
        deleted=deleted,
        with_associations=with_associations,
        with_coordinators=with_coordinators,
        no_users_are_coords=no_users_are_coords,
        users_are_coords=users_are_coords,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    description: str | Unset = UNSET,
    deleted: str | Unset = UNSET,
    with_associations: str | Unset = UNSET,
    with_coordinators: str | Unset = UNSET,
    no_users_are_coords: str | Unset = UNSET,
    users_are_coords: str | Unset = UNSET,
) -> Response[V0042OpenapiAccountsResp]:
    """Get account list

    Args:
        description (str | Unset):
        deleted (str | Unset):
        with_associations (str | Unset):
        with_coordinators (str | Unset):
        no_users_are_coords (str | Unset):
        users_are_coords (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[V0042OpenapiAccountsResp]
    """

    kwargs = _get_kwargs(
        description=description,
        deleted=deleted,
        with_associations=with_associations,
        with_coordinators=with_coordinators,
        no_users_are_coords=no_users_are_coords,
        users_are_coords=users_are_coords,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    description: str | Unset = UNSET,
    deleted: str | Unset = UNSET,
    with_associations: str | Unset = UNSET,
    with_coordinators: str | Unset = UNSET,
    no_users_are_coords: str | Unset = UNSET,
    users_are_coords: str | Unset = UNSET,
) -> V0042OpenapiAccountsResp | None:
    """Get account list

    Args:
        description (str | Unset):
        deleted (str | Unset):
        with_associations (str | Unset):
        with_coordinators (str | Unset):
        no_users_are_coords (str | Unset):
        users_are_coords (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        V0042OpenapiAccountsResp
    """

    return (
        await asyncio_detailed(
            client=client,
            description=description,
            deleted=deleted,
            with_associations=with_associations,
            with_coordinators=with_coordinators,
            no_users_are_coords=no_users_are_coords,
            users_are_coords=users_are_coords,
        )
    ).parsed
