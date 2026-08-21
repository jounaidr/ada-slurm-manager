from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.v0041_openapi_assocs_removed_resp import V0041OpenapiAssocsRemovedResp
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    account: str | Unset = UNSET,
    cluster: str | Unset = UNSET,
    default_qos: str | Unset = UNSET,
    format_: str | Unset = UNSET,
    id: str | Unset = UNSET,
    only_defaults: str | Unset = UNSET,
    parent_account: str | Unset = UNSET,
    partition: str | Unset = UNSET,
    qos: str | Unset = UNSET,
    usage_end: str | Unset = UNSET,
    usage_start: str | Unset = UNSET,
    user: str | Unset = UNSET,
    with_usage: str | Unset = UNSET,
    with_deleted: str | Unset = UNSET,
    with_raw_qos: str | Unset = UNSET,
    with_sub_accts: str | Unset = UNSET,
    without_parent_info: str | Unset = UNSET,
    without_parent_limits: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["account"] = account

    params["cluster"] = cluster

    params["default_qos"] = default_qos

    params["format"] = format_

    params["id"] = id

    params["only_defaults"] = only_defaults

    params["parent_account"] = parent_account

    params["partition"] = partition

    params["qos"] = qos

    params["usage_end"] = usage_end

    params["usage_start"] = usage_start

    params["user"] = user

    params["with_usage"] = with_usage

    params["with_deleted"] = with_deleted

    params["with_raw_qos"] = with_raw_qos

    params["with_sub_accts"] = with_sub_accts

    params["without_parent_info"] = without_parent_info

    params["without_parent_limits"] = without_parent_limits

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/slurmdb/v0.0.41/associations/",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> V0041OpenapiAssocsRemovedResp:
    if response.status_code == 200:
        response_200 = V0041OpenapiAssocsRemovedResp.from_dict(response.json())

        return response_200

    response_default = V0041OpenapiAssocsRemovedResp.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[V0041OpenapiAssocsRemovedResp]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    account: str | Unset = UNSET,
    cluster: str | Unset = UNSET,
    default_qos: str | Unset = UNSET,
    format_: str | Unset = UNSET,
    id: str | Unset = UNSET,
    only_defaults: str | Unset = UNSET,
    parent_account: str | Unset = UNSET,
    partition: str | Unset = UNSET,
    qos: str | Unset = UNSET,
    usage_end: str | Unset = UNSET,
    usage_start: str | Unset = UNSET,
    user: str | Unset = UNSET,
    with_usage: str | Unset = UNSET,
    with_deleted: str | Unset = UNSET,
    with_raw_qos: str | Unset = UNSET,
    with_sub_accts: str | Unset = UNSET,
    without_parent_info: str | Unset = UNSET,
    without_parent_limits: str | Unset = UNSET,
) -> Response[V0041OpenapiAssocsRemovedResp]:
    """Delete associations

    Args:
        account (str | Unset):
        cluster (str | Unset):
        default_qos (str | Unset):
        format_ (str | Unset):
        id (str | Unset):
        only_defaults (str | Unset):
        parent_account (str | Unset):
        partition (str | Unset):
        qos (str | Unset):
        usage_end (str | Unset):
        usage_start (str | Unset):
        user (str | Unset):
        with_usage (str | Unset):
        with_deleted (str | Unset):
        with_raw_qos (str | Unset):
        with_sub_accts (str | Unset):
        without_parent_info (str | Unset):
        without_parent_limits (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[V0041OpenapiAssocsRemovedResp]
    """

    kwargs = _get_kwargs(
        account=account,
        cluster=cluster,
        default_qos=default_qos,
        format_=format_,
        id=id,
        only_defaults=only_defaults,
        parent_account=parent_account,
        partition=partition,
        qos=qos,
        usage_end=usage_end,
        usage_start=usage_start,
        user=user,
        with_usage=with_usage,
        with_deleted=with_deleted,
        with_raw_qos=with_raw_qos,
        with_sub_accts=with_sub_accts,
        without_parent_info=without_parent_info,
        without_parent_limits=without_parent_limits,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    account: str | Unset = UNSET,
    cluster: str | Unset = UNSET,
    default_qos: str | Unset = UNSET,
    format_: str | Unset = UNSET,
    id: str | Unset = UNSET,
    only_defaults: str | Unset = UNSET,
    parent_account: str | Unset = UNSET,
    partition: str | Unset = UNSET,
    qos: str | Unset = UNSET,
    usage_end: str | Unset = UNSET,
    usage_start: str | Unset = UNSET,
    user: str | Unset = UNSET,
    with_usage: str | Unset = UNSET,
    with_deleted: str | Unset = UNSET,
    with_raw_qos: str | Unset = UNSET,
    with_sub_accts: str | Unset = UNSET,
    without_parent_info: str | Unset = UNSET,
    without_parent_limits: str | Unset = UNSET,
) -> V0041OpenapiAssocsRemovedResp | None:
    """Delete associations

    Args:
        account (str | Unset):
        cluster (str | Unset):
        default_qos (str | Unset):
        format_ (str | Unset):
        id (str | Unset):
        only_defaults (str | Unset):
        parent_account (str | Unset):
        partition (str | Unset):
        qos (str | Unset):
        usage_end (str | Unset):
        usage_start (str | Unset):
        user (str | Unset):
        with_usage (str | Unset):
        with_deleted (str | Unset):
        with_raw_qos (str | Unset):
        with_sub_accts (str | Unset):
        without_parent_info (str | Unset):
        without_parent_limits (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        V0041OpenapiAssocsRemovedResp
    """

    return sync_detailed(
        client=client,
        account=account,
        cluster=cluster,
        default_qos=default_qos,
        format_=format_,
        id=id,
        only_defaults=only_defaults,
        parent_account=parent_account,
        partition=partition,
        qos=qos,
        usage_end=usage_end,
        usage_start=usage_start,
        user=user,
        with_usage=with_usage,
        with_deleted=with_deleted,
        with_raw_qos=with_raw_qos,
        with_sub_accts=with_sub_accts,
        without_parent_info=without_parent_info,
        without_parent_limits=without_parent_limits,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    account: str | Unset = UNSET,
    cluster: str | Unset = UNSET,
    default_qos: str | Unset = UNSET,
    format_: str | Unset = UNSET,
    id: str | Unset = UNSET,
    only_defaults: str | Unset = UNSET,
    parent_account: str | Unset = UNSET,
    partition: str | Unset = UNSET,
    qos: str | Unset = UNSET,
    usage_end: str | Unset = UNSET,
    usage_start: str | Unset = UNSET,
    user: str | Unset = UNSET,
    with_usage: str | Unset = UNSET,
    with_deleted: str | Unset = UNSET,
    with_raw_qos: str | Unset = UNSET,
    with_sub_accts: str | Unset = UNSET,
    without_parent_info: str | Unset = UNSET,
    without_parent_limits: str | Unset = UNSET,
) -> Response[V0041OpenapiAssocsRemovedResp]:
    """Delete associations

    Args:
        account (str | Unset):
        cluster (str | Unset):
        default_qos (str | Unset):
        format_ (str | Unset):
        id (str | Unset):
        only_defaults (str | Unset):
        parent_account (str | Unset):
        partition (str | Unset):
        qos (str | Unset):
        usage_end (str | Unset):
        usage_start (str | Unset):
        user (str | Unset):
        with_usage (str | Unset):
        with_deleted (str | Unset):
        with_raw_qos (str | Unset):
        with_sub_accts (str | Unset):
        without_parent_info (str | Unset):
        without_parent_limits (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[V0041OpenapiAssocsRemovedResp]
    """

    kwargs = _get_kwargs(
        account=account,
        cluster=cluster,
        default_qos=default_qos,
        format_=format_,
        id=id,
        only_defaults=only_defaults,
        parent_account=parent_account,
        partition=partition,
        qos=qos,
        usage_end=usage_end,
        usage_start=usage_start,
        user=user,
        with_usage=with_usage,
        with_deleted=with_deleted,
        with_raw_qos=with_raw_qos,
        with_sub_accts=with_sub_accts,
        without_parent_info=without_parent_info,
        without_parent_limits=without_parent_limits,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    account: str | Unset = UNSET,
    cluster: str | Unset = UNSET,
    default_qos: str | Unset = UNSET,
    format_: str | Unset = UNSET,
    id: str | Unset = UNSET,
    only_defaults: str | Unset = UNSET,
    parent_account: str | Unset = UNSET,
    partition: str | Unset = UNSET,
    qos: str | Unset = UNSET,
    usage_end: str | Unset = UNSET,
    usage_start: str | Unset = UNSET,
    user: str | Unset = UNSET,
    with_usage: str | Unset = UNSET,
    with_deleted: str | Unset = UNSET,
    with_raw_qos: str | Unset = UNSET,
    with_sub_accts: str | Unset = UNSET,
    without_parent_info: str | Unset = UNSET,
    without_parent_limits: str | Unset = UNSET,
) -> V0041OpenapiAssocsRemovedResp | None:
    """Delete associations

    Args:
        account (str | Unset):
        cluster (str | Unset):
        default_qos (str | Unset):
        format_ (str | Unset):
        id (str | Unset):
        only_defaults (str | Unset):
        parent_account (str | Unset):
        partition (str | Unset):
        qos (str | Unset):
        usage_end (str | Unset):
        usage_start (str | Unset):
        user (str | Unset):
        with_usage (str | Unset):
        with_deleted (str | Unset):
        with_raw_qos (str | Unset):
        with_sub_accts (str | Unset):
        without_parent_info (str | Unset):
        without_parent_limits (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        V0041OpenapiAssocsRemovedResp
    """

    return (
        await asyncio_detailed(
            client=client,
            account=account,
            cluster=cluster,
            default_qos=default_qos,
            format_=format_,
            id=id,
            only_defaults=only_defaults,
            parent_account=parent_account,
            partition=partition,
            qos=qos,
            usage_end=usage_end,
            usage_start=usage_start,
            user=user,
            with_usage=with_usage,
            with_deleted=with_deleted,
            with_raw_qos=with_raw_qos,
            with_sub_accts=with_sub_accts,
            without_parent_info=without_parent_info,
            without_parent_limits=without_parent_limits,
        )
    ).parsed
