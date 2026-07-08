from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.slurmdb_v0044_post_users_association_flags import SlurmdbV0044PostUsersAssociationFlags
from ...models.v0044_openapi_users_add_cond_resp import V0044OpenapiUsersAddCondResp
from ...models.v0044_openapi_users_add_cond_resp_str import V0044OpenapiUsersAddCondRespStr
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: V0044OpenapiUsersAddCondResp | Unset = UNSET,
    update_time: str | Unset = UNSET,
    flags: SlurmdbV0044PostUsersAssociationFlags | Unset = UNSET,
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
        "url": "/slurmdb/v0.0.44/users_association/",
        "params": params,
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> V0044OpenapiUsersAddCondRespStr:
    if response.status_code == 200:
        response_200 = V0044OpenapiUsersAddCondRespStr.from_dict(response.json())

        return response_200

    response_default = V0044OpenapiUsersAddCondRespStr.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[V0044OpenapiUsersAddCondRespStr]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: V0044OpenapiUsersAddCondResp | Unset = UNSET,
    update_time: str | Unset = UNSET,
    flags: SlurmdbV0044PostUsersAssociationFlags | Unset = UNSET,
) -> Response[V0044OpenapiUsersAddCondRespStr]:
    """Add users with conditional association

    Args:
        update_time (str | Unset):
        flags (SlurmdbV0044PostUsersAssociationFlags | Unset):
        body (V0044OpenapiUsersAddCondResp | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[V0044OpenapiUsersAddCondRespStr]
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
    body: V0044OpenapiUsersAddCondResp | Unset = UNSET,
    update_time: str | Unset = UNSET,
    flags: SlurmdbV0044PostUsersAssociationFlags | Unset = UNSET,
) -> V0044OpenapiUsersAddCondRespStr | None:
    """Add users with conditional association

    Args:
        update_time (str | Unset):
        flags (SlurmdbV0044PostUsersAssociationFlags | Unset):
        body (V0044OpenapiUsersAddCondResp | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        V0044OpenapiUsersAddCondRespStr
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
    body: V0044OpenapiUsersAddCondResp | Unset = UNSET,
    update_time: str | Unset = UNSET,
    flags: SlurmdbV0044PostUsersAssociationFlags | Unset = UNSET,
) -> Response[V0044OpenapiUsersAddCondRespStr]:
    """Add users with conditional association

    Args:
        update_time (str | Unset):
        flags (SlurmdbV0044PostUsersAssociationFlags | Unset):
        body (V0044OpenapiUsersAddCondResp | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[V0044OpenapiUsersAddCondRespStr]
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
    body: V0044OpenapiUsersAddCondResp | Unset = UNSET,
    update_time: str | Unset = UNSET,
    flags: SlurmdbV0044PostUsersAssociationFlags | Unset = UNSET,
) -> V0044OpenapiUsersAddCondRespStr | None:
    """Add users with conditional association

    Args:
        update_time (str | Unset):
        flags (SlurmdbV0044PostUsersAssociationFlags | Unset):
        body (V0044OpenapiUsersAddCondResp | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        V0044OpenapiUsersAddCondRespStr
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            update_time=update_time,
            flags=flags,
        )
    ).parsed
