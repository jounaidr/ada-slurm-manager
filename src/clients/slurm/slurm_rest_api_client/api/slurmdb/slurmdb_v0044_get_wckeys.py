from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.v0044_openapi_wckey_resp import V0044OpenapiWckeyResp
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    cluster: str | Unset = UNSET,
    format_: str | Unset = UNSET,
    id: str | Unset = UNSET,
    name: str | Unset = UNSET,
    only_defaults: str | Unset = UNSET,
    usage_end: str | Unset = UNSET,
    usage_start: str | Unset = UNSET,
    user: str | Unset = UNSET,
    with_usage: str | Unset = UNSET,
    with_deleted: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["cluster"] = cluster

    params["format"] = format_

    params["id"] = id

    params["name"] = name

    params["only_defaults"] = only_defaults

    params["usage_end"] = usage_end

    params["usage_start"] = usage_start

    params["user"] = user

    params["with_usage"] = with_usage

    params["with_deleted"] = with_deleted

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/slurmdb/v0.0.44/wckeys/",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> V0044OpenapiWckeyResp:
    if response.status_code == 200:
        response_200 = V0044OpenapiWckeyResp.from_dict(response.json())

        return response_200

    response_default = V0044OpenapiWckeyResp.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[V0044OpenapiWckeyResp]:
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
    format_: str | Unset = UNSET,
    id: str | Unset = UNSET,
    name: str | Unset = UNSET,
    only_defaults: str | Unset = UNSET,
    usage_end: str | Unset = UNSET,
    usage_start: str | Unset = UNSET,
    user: str | Unset = UNSET,
    with_usage: str | Unset = UNSET,
    with_deleted: str | Unset = UNSET,
) -> Response[V0044OpenapiWckeyResp]:
    """Get wckey list

    Args:
        cluster (str | Unset):
        format_ (str | Unset):
        id (str | Unset):
        name (str | Unset):
        only_defaults (str | Unset):
        usage_end (str | Unset):
        usage_start (str | Unset):
        user (str | Unset):
        with_usage (str | Unset):
        with_deleted (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[V0044OpenapiWckeyResp]
    """

    kwargs = _get_kwargs(
        cluster=cluster,
        format_=format_,
        id=id,
        name=name,
        only_defaults=only_defaults,
        usage_end=usage_end,
        usage_start=usage_start,
        user=user,
        with_usage=with_usage,
        with_deleted=with_deleted,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    cluster: str | Unset = UNSET,
    format_: str | Unset = UNSET,
    id: str | Unset = UNSET,
    name: str | Unset = UNSET,
    only_defaults: str | Unset = UNSET,
    usage_end: str | Unset = UNSET,
    usage_start: str | Unset = UNSET,
    user: str | Unset = UNSET,
    with_usage: str | Unset = UNSET,
    with_deleted: str | Unset = UNSET,
) -> V0044OpenapiWckeyResp | None:
    """Get wckey list

    Args:
        cluster (str | Unset):
        format_ (str | Unset):
        id (str | Unset):
        name (str | Unset):
        only_defaults (str | Unset):
        usage_end (str | Unset):
        usage_start (str | Unset):
        user (str | Unset):
        with_usage (str | Unset):
        with_deleted (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        V0044OpenapiWckeyResp
    """

    return sync_detailed(
        client=client,
        cluster=cluster,
        format_=format_,
        id=id,
        name=name,
        only_defaults=only_defaults,
        usage_end=usage_end,
        usage_start=usage_start,
        user=user,
        with_usage=with_usage,
        with_deleted=with_deleted,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    cluster: str | Unset = UNSET,
    format_: str | Unset = UNSET,
    id: str | Unset = UNSET,
    name: str | Unset = UNSET,
    only_defaults: str | Unset = UNSET,
    usage_end: str | Unset = UNSET,
    usage_start: str | Unset = UNSET,
    user: str | Unset = UNSET,
    with_usage: str | Unset = UNSET,
    with_deleted: str | Unset = UNSET,
) -> Response[V0044OpenapiWckeyResp]:
    """Get wckey list

    Args:
        cluster (str | Unset):
        format_ (str | Unset):
        id (str | Unset):
        name (str | Unset):
        only_defaults (str | Unset):
        usage_end (str | Unset):
        usage_start (str | Unset):
        user (str | Unset):
        with_usage (str | Unset):
        with_deleted (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[V0044OpenapiWckeyResp]
    """

    kwargs = _get_kwargs(
        cluster=cluster,
        format_=format_,
        id=id,
        name=name,
        only_defaults=only_defaults,
        usage_end=usage_end,
        usage_start=usage_start,
        user=user,
        with_usage=with_usage,
        with_deleted=with_deleted,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    cluster: str | Unset = UNSET,
    format_: str | Unset = UNSET,
    id: str | Unset = UNSET,
    name: str | Unset = UNSET,
    only_defaults: str | Unset = UNSET,
    usage_end: str | Unset = UNSET,
    usage_start: str | Unset = UNSET,
    user: str | Unset = UNSET,
    with_usage: str | Unset = UNSET,
    with_deleted: str | Unset = UNSET,
) -> V0044OpenapiWckeyResp | None:
    """Get wckey list

    Args:
        cluster (str | Unset):
        format_ (str | Unset):
        id (str | Unset):
        name (str | Unset):
        only_defaults (str | Unset):
        usage_end (str | Unset):
        usage_start (str | Unset):
        user (str | Unset):
        with_usage (str | Unset):
        with_deleted (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        V0044OpenapiWckeyResp
    """

    return (
        await asyncio_detailed(
            client=client,
            cluster=cluster,
            format_=format_,
            id=id,
            name=name,
            only_defaults=only_defaults,
            usage_end=usage_end,
            usage_start=usage_start,
            user=user,
            with_usage=with_usage,
            with_deleted=with_deleted,
        )
    ).parsed
