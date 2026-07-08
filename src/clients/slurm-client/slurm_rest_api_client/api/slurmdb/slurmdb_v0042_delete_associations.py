from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.v0042_openapi_assocs_removed_resp import V0042OpenapiAssocsRemovedResp
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    account: str | Unset = UNSET,
    cluster: str | Unset = UNSET,
    default_qos: str | Unset = UNSET,
    include_deleted_associations: str | Unset = UNSET,
    include_usage: str | Unset = UNSET,
    filter_to_only_defaults: str | Unset = UNSET,
    include_the_raw_qos_or_delta_qos: str | Unset = UNSET,
    include_sub_acct_information: str | Unset = UNSET,
    exclude_parent_idname: str | Unset = UNSET,
    exclude_limits_from_parents: str | Unset = UNSET,
    format_: str | Unset = UNSET,
    id: str | Unset = UNSET,
    parent_account: str | Unset = UNSET,
    partition: str | Unset = UNSET,
    qos: str | Unset = UNSET,
    usage_end: str | Unset = UNSET,
    usage_start: str | Unset = UNSET,
    user: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["account"] = account

    params["cluster"] = cluster

    params["default_qos"] = default_qos

    params["Include deleted associations"] = include_deleted_associations

    params["Include usage"] = include_usage

    params["Filter to only defaults"] = filter_to_only_defaults

    params["Include the raw QOS or delta_qos"] = include_the_raw_qos_or_delta_qos

    params["Include sub acct information"] = include_sub_acct_information

    params["Exclude parent id/name"] = exclude_parent_idname

    params["Exclude limits from parents"] = exclude_limits_from_parents

    params["format"] = format_

    params["id"] = id

    params["parent_account"] = parent_account

    params["partition"] = partition

    params["qos"] = qos

    params["usage_end"] = usage_end

    params["usage_start"] = usage_start

    params["user"] = user

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/slurmdb/v0.0.42/associations/",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> V0042OpenapiAssocsRemovedResp:
    if response.status_code == 200:
        response_200 = V0042OpenapiAssocsRemovedResp.from_dict(response.json())

        return response_200

    response_default = V0042OpenapiAssocsRemovedResp.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[V0042OpenapiAssocsRemovedResp]:
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
    include_deleted_associations: str | Unset = UNSET,
    include_usage: str | Unset = UNSET,
    filter_to_only_defaults: str | Unset = UNSET,
    include_the_raw_qos_or_delta_qos: str | Unset = UNSET,
    include_sub_acct_information: str | Unset = UNSET,
    exclude_parent_idname: str | Unset = UNSET,
    exclude_limits_from_parents: str | Unset = UNSET,
    format_: str | Unset = UNSET,
    id: str | Unset = UNSET,
    parent_account: str | Unset = UNSET,
    partition: str | Unset = UNSET,
    qos: str | Unset = UNSET,
    usage_end: str | Unset = UNSET,
    usage_start: str | Unset = UNSET,
    user: str | Unset = UNSET,
) -> Response[V0042OpenapiAssocsRemovedResp]:
    """Delete associations

    Args:
        account (str | Unset):
        cluster (str | Unset):
        default_qos (str | Unset):
        include_deleted_associations (str | Unset):
        include_usage (str | Unset):
        filter_to_only_defaults (str | Unset):
        include_the_raw_qos_or_delta_qos (str | Unset):
        include_sub_acct_information (str | Unset):
        exclude_parent_idname (str | Unset):
        exclude_limits_from_parents (str | Unset):
        format_ (str | Unset):
        id (str | Unset):
        parent_account (str | Unset):
        partition (str | Unset):
        qos (str | Unset):
        usage_end (str | Unset):
        usage_start (str | Unset):
        user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[V0042OpenapiAssocsRemovedResp]
    """

    kwargs = _get_kwargs(
        account=account,
        cluster=cluster,
        default_qos=default_qos,
        include_deleted_associations=include_deleted_associations,
        include_usage=include_usage,
        filter_to_only_defaults=filter_to_only_defaults,
        include_the_raw_qos_or_delta_qos=include_the_raw_qos_or_delta_qos,
        include_sub_acct_information=include_sub_acct_information,
        exclude_parent_idname=exclude_parent_idname,
        exclude_limits_from_parents=exclude_limits_from_parents,
        format_=format_,
        id=id,
        parent_account=parent_account,
        partition=partition,
        qos=qos,
        usage_end=usage_end,
        usage_start=usage_start,
        user=user,
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
    include_deleted_associations: str | Unset = UNSET,
    include_usage: str | Unset = UNSET,
    filter_to_only_defaults: str | Unset = UNSET,
    include_the_raw_qos_or_delta_qos: str | Unset = UNSET,
    include_sub_acct_information: str | Unset = UNSET,
    exclude_parent_idname: str | Unset = UNSET,
    exclude_limits_from_parents: str | Unset = UNSET,
    format_: str | Unset = UNSET,
    id: str | Unset = UNSET,
    parent_account: str | Unset = UNSET,
    partition: str | Unset = UNSET,
    qos: str | Unset = UNSET,
    usage_end: str | Unset = UNSET,
    usage_start: str | Unset = UNSET,
    user: str | Unset = UNSET,
) -> V0042OpenapiAssocsRemovedResp | None:
    """Delete associations

    Args:
        account (str | Unset):
        cluster (str | Unset):
        default_qos (str | Unset):
        include_deleted_associations (str | Unset):
        include_usage (str | Unset):
        filter_to_only_defaults (str | Unset):
        include_the_raw_qos_or_delta_qos (str | Unset):
        include_sub_acct_information (str | Unset):
        exclude_parent_idname (str | Unset):
        exclude_limits_from_parents (str | Unset):
        format_ (str | Unset):
        id (str | Unset):
        parent_account (str | Unset):
        partition (str | Unset):
        qos (str | Unset):
        usage_end (str | Unset):
        usage_start (str | Unset):
        user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        V0042OpenapiAssocsRemovedResp
    """

    return sync_detailed(
        client=client,
        account=account,
        cluster=cluster,
        default_qos=default_qos,
        include_deleted_associations=include_deleted_associations,
        include_usage=include_usage,
        filter_to_only_defaults=filter_to_only_defaults,
        include_the_raw_qos_or_delta_qos=include_the_raw_qos_or_delta_qos,
        include_sub_acct_information=include_sub_acct_information,
        exclude_parent_idname=exclude_parent_idname,
        exclude_limits_from_parents=exclude_limits_from_parents,
        format_=format_,
        id=id,
        parent_account=parent_account,
        partition=partition,
        qos=qos,
        usage_end=usage_end,
        usage_start=usage_start,
        user=user,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    account: str | Unset = UNSET,
    cluster: str | Unset = UNSET,
    default_qos: str | Unset = UNSET,
    include_deleted_associations: str | Unset = UNSET,
    include_usage: str | Unset = UNSET,
    filter_to_only_defaults: str | Unset = UNSET,
    include_the_raw_qos_or_delta_qos: str | Unset = UNSET,
    include_sub_acct_information: str | Unset = UNSET,
    exclude_parent_idname: str | Unset = UNSET,
    exclude_limits_from_parents: str | Unset = UNSET,
    format_: str | Unset = UNSET,
    id: str | Unset = UNSET,
    parent_account: str | Unset = UNSET,
    partition: str | Unset = UNSET,
    qos: str | Unset = UNSET,
    usage_end: str | Unset = UNSET,
    usage_start: str | Unset = UNSET,
    user: str | Unset = UNSET,
) -> Response[V0042OpenapiAssocsRemovedResp]:
    """Delete associations

    Args:
        account (str | Unset):
        cluster (str | Unset):
        default_qos (str | Unset):
        include_deleted_associations (str | Unset):
        include_usage (str | Unset):
        filter_to_only_defaults (str | Unset):
        include_the_raw_qos_or_delta_qos (str | Unset):
        include_sub_acct_information (str | Unset):
        exclude_parent_idname (str | Unset):
        exclude_limits_from_parents (str | Unset):
        format_ (str | Unset):
        id (str | Unset):
        parent_account (str | Unset):
        partition (str | Unset):
        qos (str | Unset):
        usage_end (str | Unset):
        usage_start (str | Unset):
        user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[V0042OpenapiAssocsRemovedResp]
    """

    kwargs = _get_kwargs(
        account=account,
        cluster=cluster,
        default_qos=default_qos,
        include_deleted_associations=include_deleted_associations,
        include_usage=include_usage,
        filter_to_only_defaults=filter_to_only_defaults,
        include_the_raw_qos_or_delta_qos=include_the_raw_qos_or_delta_qos,
        include_sub_acct_information=include_sub_acct_information,
        exclude_parent_idname=exclude_parent_idname,
        exclude_limits_from_parents=exclude_limits_from_parents,
        format_=format_,
        id=id,
        parent_account=parent_account,
        partition=partition,
        qos=qos,
        usage_end=usage_end,
        usage_start=usage_start,
        user=user,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    account: str | Unset = UNSET,
    cluster: str | Unset = UNSET,
    default_qos: str | Unset = UNSET,
    include_deleted_associations: str | Unset = UNSET,
    include_usage: str | Unset = UNSET,
    filter_to_only_defaults: str | Unset = UNSET,
    include_the_raw_qos_or_delta_qos: str | Unset = UNSET,
    include_sub_acct_information: str | Unset = UNSET,
    exclude_parent_idname: str | Unset = UNSET,
    exclude_limits_from_parents: str | Unset = UNSET,
    format_: str | Unset = UNSET,
    id: str | Unset = UNSET,
    parent_account: str | Unset = UNSET,
    partition: str | Unset = UNSET,
    qos: str | Unset = UNSET,
    usage_end: str | Unset = UNSET,
    usage_start: str | Unset = UNSET,
    user: str | Unset = UNSET,
) -> V0042OpenapiAssocsRemovedResp | None:
    """Delete associations

    Args:
        account (str | Unset):
        cluster (str | Unset):
        default_qos (str | Unset):
        include_deleted_associations (str | Unset):
        include_usage (str | Unset):
        filter_to_only_defaults (str | Unset):
        include_the_raw_qos_or_delta_qos (str | Unset):
        include_sub_acct_information (str | Unset):
        exclude_parent_idname (str | Unset):
        exclude_limits_from_parents (str | Unset):
        format_ (str | Unset):
        id (str | Unset):
        parent_account (str | Unset):
        partition (str | Unset):
        qos (str | Unset):
        usage_end (str | Unset):
        usage_start (str | Unset):
        user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        V0042OpenapiAssocsRemovedResp
    """

    return (
        await asyncio_detailed(
            client=client,
            account=account,
            cluster=cluster,
            default_qos=default_qos,
            include_deleted_associations=include_deleted_associations,
            include_usage=include_usage,
            filter_to_only_defaults=filter_to_only_defaults,
            include_the_raw_qos_or_delta_qos=include_the_raw_qos_or_delta_qos,
            include_sub_acct_information=include_sub_acct_information,
            exclude_parent_idname=exclude_parent_idname,
            exclude_limits_from_parents=exclude_limits_from_parents,
            format_=format_,
            id=id,
            parent_account=parent_account,
            partition=partition,
            qos=qos,
            usage_end=usage_end,
            usage_start=usage_start,
            user=user,
        )
    ).parsed
