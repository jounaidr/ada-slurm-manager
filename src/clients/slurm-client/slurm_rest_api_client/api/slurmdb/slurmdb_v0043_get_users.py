from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.slurmdb_v0043_get_users_admin_level import SlurmdbV0043GetUsersAdminLevel
from ...models.v0043_openapi_users_resp import V0043OpenapiUsersResp
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    admin_level: SlurmdbV0043GetUsersAdminLevel | Unset = UNSET,
    default_account: str | Unset = UNSET,
    default_wckey: str | Unset = UNSET,
    with_assocs: str | Unset = UNSET,
    with_coords: str | Unset = UNSET,
    with_deleted: str | Unset = UNSET,
    with_wckeys: str | Unset = UNSET,
    without_defaults: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_admin_level: str | Unset = UNSET
    if not isinstance(admin_level, Unset):
        json_admin_level = admin_level.value

    params["admin_level"] = json_admin_level

    params["default_account"] = default_account

    params["default_wckey"] = default_wckey

    params["with_assocs"] = with_assocs

    params["with_coords"] = with_coords

    params["with_deleted"] = with_deleted

    params["with_wckeys"] = with_wckeys

    params["without_defaults"] = without_defaults

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/slurmdb/v0.0.43/users/",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> V0043OpenapiUsersResp:
    if response.status_code == 200:
        response_200 = V0043OpenapiUsersResp.from_dict(response.json())

        return response_200

    response_default = V0043OpenapiUsersResp.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[V0043OpenapiUsersResp]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    admin_level: SlurmdbV0043GetUsersAdminLevel | Unset = UNSET,
    default_account: str | Unset = UNSET,
    default_wckey: str | Unset = UNSET,
    with_assocs: str | Unset = UNSET,
    with_coords: str | Unset = UNSET,
    with_deleted: str | Unset = UNSET,
    with_wckeys: str | Unset = UNSET,
    without_defaults: str | Unset = UNSET,
) -> Response[V0043OpenapiUsersResp]:
    """Get user list

    Args:
        admin_level (SlurmdbV0043GetUsersAdminLevel | Unset):
        default_account (str | Unset):
        default_wckey (str | Unset):
        with_assocs (str | Unset):
        with_coords (str | Unset):
        with_deleted (str | Unset):
        with_wckeys (str | Unset):
        without_defaults (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[V0043OpenapiUsersResp]
    """

    kwargs = _get_kwargs(
        admin_level=admin_level,
        default_account=default_account,
        default_wckey=default_wckey,
        with_assocs=with_assocs,
        with_coords=with_coords,
        with_deleted=with_deleted,
        with_wckeys=with_wckeys,
        without_defaults=without_defaults,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    admin_level: SlurmdbV0043GetUsersAdminLevel | Unset = UNSET,
    default_account: str | Unset = UNSET,
    default_wckey: str | Unset = UNSET,
    with_assocs: str | Unset = UNSET,
    with_coords: str | Unset = UNSET,
    with_deleted: str | Unset = UNSET,
    with_wckeys: str | Unset = UNSET,
    without_defaults: str | Unset = UNSET,
) -> V0043OpenapiUsersResp | None:
    """Get user list

    Args:
        admin_level (SlurmdbV0043GetUsersAdminLevel | Unset):
        default_account (str | Unset):
        default_wckey (str | Unset):
        with_assocs (str | Unset):
        with_coords (str | Unset):
        with_deleted (str | Unset):
        with_wckeys (str | Unset):
        without_defaults (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        V0043OpenapiUsersResp
    """

    return sync_detailed(
        client=client,
        admin_level=admin_level,
        default_account=default_account,
        default_wckey=default_wckey,
        with_assocs=with_assocs,
        with_coords=with_coords,
        with_deleted=with_deleted,
        with_wckeys=with_wckeys,
        without_defaults=without_defaults,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    admin_level: SlurmdbV0043GetUsersAdminLevel | Unset = UNSET,
    default_account: str | Unset = UNSET,
    default_wckey: str | Unset = UNSET,
    with_assocs: str | Unset = UNSET,
    with_coords: str | Unset = UNSET,
    with_deleted: str | Unset = UNSET,
    with_wckeys: str | Unset = UNSET,
    without_defaults: str | Unset = UNSET,
) -> Response[V0043OpenapiUsersResp]:
    """Get user list

    Args:
        admin_level (SlurmdbV0043GetUsersAdminLevel | Unset):
        default_account (str | Unset):
        default_wckey (str | Unset):
        with_assocs (str | Unset):
        with_coords (str | Unset):
        with_deleted (str | Unset):
        with_wckeys (str | Unset):
        without_defaults (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[V0043OpenapiUsersResp]
    """

    kwargs = _get_kwargs(
        admin_level=admin_level,
        default_account=default_account,
        default_wckey=default_wckey,
        with_assocs=with_assocs,
        with_coords=with_coords,
        with_deleted=with_deleted,
        with_wckeys=with_wckeys,
        without_defaults=without_defaults,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    admin_level: SlurmdbV0043GetUsersAdminLevel | Unset = UNSET,
    default_account: str | Unset = UNSET,
    default_wckey: str | Unset = UNSET,
    with_assocs: str | Unset = UNSET,
    with_coords: str | Unset = UNSET,
    with_deleted: str | Unset = UNSET,
    with_wckeys: str | Unset = UNSET,
    without_defaults: str | Unset = UNSET,
) -> V0043OpenapiUsersResp | None:
    """Get user list

    Args:
        admin_level (SlurmdbV0043GetUsersAdminLevel | Unset):
        default_account (str | Unset):
        default_wckey (str | Unset):
        with_assocs (str | Unset):
        with_coords (str | Unset):
        with_deleted (str | Unset):
        with_wckeys (str | Unset):
        without_defaults (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        V0043OpenapiUsersResp
    """

    return (
        await asyncio_detailed(
            client=client,
            admin_level=admin_level,
            default_account=default_account,
            default_wckey=default_wckey,
            with_assocs=with_assocs,
            with_coords=with_coords,
            with_deleted=with_deleted,
            with_wckeys=with_wckeys,
            without_defaults=without_defaults,
        )
    ).parsed
