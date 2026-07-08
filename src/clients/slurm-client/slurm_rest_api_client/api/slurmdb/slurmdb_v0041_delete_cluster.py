from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.slurmdb_v0041_delete_cluster_classification import SlurmdbV0041DeleteClusterClassification
from ...models.slurmdb_v0041_delete_cluster_flags import SlurmdbV0041DeleteClusterFlags
from ...models.slurmdb_v0041_delete_cluster_response_200 import SlurmdbV0041DeleteClusterResponse200
from ...models.slurmdb_v0041_delete_cluster_response_default import SlurmdbV0041DeleteClusterResponseDefault
from ...types import UNSET, Response, Unset


def _get_kwargs(
    cluster_name: str,
    *,
    classification: SlurmdbV0041DeleteClusterClassification | Unset = UNSET,
    cluster: str | Unset = UNSET,
    federation: str | Unset = UNSET,
    flags: SlurmdbV0041DeleteClusterFlags | Unset = UNSET,
    format_: str | Unset = UNSET,
    rpc_version: str | Unset = UNSET,
    usage_end: str | Unset = UNSET,
    usage_start: str | Unset = UNSET,
    with_deleted: str | Unset = UNSET,
    with_usage: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_classification: str | Unset = UNSET
    if not isinstance(classification, Unset):
        json_classification = classification.value

    params["classification"] = json_classification

    params["cluster"] = cluster

    params["federation"] = federation

    json_flags: str | Unset = UNSET
    if not isinstance(flags, Unset):
        json_flags = flags.value

    params["flags"] = json_flags

    params["format"] = format_

    params["rpc_version"] = rpc_version

    params["usage_end"] = usage_end

    params["usage_start"] = usage_start

    params["with_deleted"] = with_deleted

    params["with_usage"] = with_usage

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/slurmdb/v0.0.41/cluster/{cluster_name}".format(
            cluster_name=quote(str(cluster_name), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> SlurmdbV0041DeleteClusterResponse200 | SlurmdbV0041DeleteClusterResponseDefault:
    if response.status_code == 200:
        response_200 = SlurmdbV0041DeleteClusterResponse200.from_dict(response.json())

        return response_200

    response_default = SlurmdbV0041DeleteClusterResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[SlurmdbV0041DeleteClusterResponse200 | SlurmdbV0041DeleteClusterResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    cluster_name: str,
    *,
    client: AuthenticatedClient | Client,
    classification: SlurmdbV0041DeleteClusterClassification | Unset = UNSET,
    cluster: str | Unset = UNSET,
    federation: str | Unset = UNSET,
    flags: SlurmdbV0041DeleteClusterFlags | Unset = UNSET,
    format_: str | Unset = UNSET,
    rpc_version: str | Unset = UNSET,
    usage_end: str | Unset = UNSET,
    usage_start: str | Unset = UNSET,
    with_deleted: str | Unset = UNSET,
    with_usage: str | Unset = UNSET,
) -> Response[SlurmdbV0041DeleteClusterResponse200 | SlurmdbV0041DeleteClusterResponseDefault]:
    """Delete cluster

    Args:
        cluster_name (str):
        classification (SlurmdbV0041DeleteClusterClassification | Unset):
        cluster (str | Unset):
        federation (str | Unset):
        flags (SlurmdbV0041DeleteClusterFlags | Unset):
        format_ (str | Unset):
        rpc_version (str | Unset):
        usage_end (str | Unset):
        usage_start (str | Unset):
        with_deleted (str | Unset):
        with_usage (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SlurmdbV0041DeleteClusterResponse200 | SlurmdbV0041DeleteClusterResponseDefault]
    """

    kwargs = _get_kwargs(
        cluster_name=cluster_name,
        classification=classification,
        cluster=cluster,
        federation=federation,
        flags=flags,
        format_=format_,
        rpc_version=rpc_version,
        usage_end=usage_end,
        usage_start=usage_start,
        with_deleted=with_deleted,
        with_usage=with_usage,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    cluster_name: str,
    *,
    client: AuthenticatedClient | Client,
    classification: SlurmdbV0041DeleteClusterClassification | Unset = UNSET,
    cluster: str | Unset = UNSET,
    federation: str | Unset = UNSET,
    flags: SlurmdbV0041DeleteClusterFlags | Unset = UNSET,
    format_: str | Unset = UNSET,
    rpc_version: str | Unset = UNSET,
    usage_end: str | Unset = UNSET,
    usage_start: str | Unset = UNSET,
    with_deleted: str | Unset = UNSET,
    with_usage: str | Unset = UNSET,
) -> SlurmdbV0041DeleteClusterResponse200 | SlurmdbV0041DeleteClusterResponseDefault | None:
    """Delete cluster

    Args:
        cluster_name (str):
        classification (SlurmdbV0041DeleteClusterClassification | Unset):
        cluster (str | Unset):
        federation (str | Unset):
        flags (SlurmdbV0041DeleteClusterFlags | Unset):
        format_ (str | Unset):
        rpc_version (str | Unset):
        usage_end (str | Unset):
        usage_start (str | Unset):
        with_deleted (str | Unset):
        with_usage (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SlurmdbV0041DeleteClusterResponse200 | SlurmdbV0041DeleteClusterResponseDefault
    """

    return sync_detailed(
        cluster_name=cluster_name,
        client=client,
        classification=classification,
        cluster=cluster,
        federation=federation,
        flags=flags,
        format_=format_,
        rpc_version=rpc_version,
        usage_end=usage_end,
        usage_start=usage_start,
        with_deleted=with_deleted,
        with_usage=with_usage,
    ).parsed


async def asyncio_detailed(
    cluster_name: str,
    *,
    client: AuthenticatedClient | Client,
    classification: SlurmdbV0041DeleteClusterClassification | Unset = UNSET,
    cluster: str | Unset = UNSET,
    federation: str | Unset = UNSET,
    flags: SlurmdbV0041DeleteClusterFlags | Unset = UNSET,
    format_: str | Unset = UNSET,
    rpc_version: str | Unset = UNSET,
    usage_end: str | Unset = UNSET,
    usage_start: str | Unset = UNSET,
    with_deleted: str | Unset = UNSET,
    with_usage: str | Unset = UNSET,
) -> Response[SlurmdbV0041DeleteClusterResponse200 | SlurmdbV0041DeleteClusterResponseDefault]:
    """Delete cluster

    Args:
        cluster_name (str):
        classification (SlurmdbV0041DeleteClusterClassification | Unset):
        cluster (str | Unset):
        federation (str | Unset):
        flags (SlurmdbV0041DeleteClusterFlags | Unset):
        format_ (str | Unset):
        rpc_version (str | Unset):
        usage_end (str | Unset):
        usage_start (str | Unset):
        with_deleted (str | Unset):
        with_usage (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SlurmdbV0041DeleteClusterResponse200 | SlurmdbV0041DeleteClusterResponseDefault]
    """

    kwargs = _get_kwargs(
        cluster_name=cluster_name,
        classification=classification,
        cluster=cluster,
        federation=federation,
        flags=flags,
        format_=format_,
        rpc_version=rpc_version,
        usage_end=usage_end,
        usage_start=usage_start,
        with_deleted=with_deleted,
        with_usage=with_usage,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    cluster_name: str,
    *,
    client: AuthenticatedClient | Client,
    classification: SlurmdbV0041DeleteClusterClassification | Unset = UNSET,
    cluster: str | Unset = UNSET,
    federation: str | Unset = UNSET,
    flags: SlurmdbV0041DeleteClusterFlags | Unset = UNSET,
    format_: str | Unset = UNSET,
    rpc_version: str | Unset = UNSET,
    usage_end: str | Unset = UNSET,
    usage_start: str | Unset = UNSET,
    with_deleted: str | Unset = UNSET,
    with_usage: str | Unset = UNSET,
) -> SlurmdbV0041DeleteClusterResponse200 | SlurmdbV0041DeleteClusterResponseDefault | None:
    """Delete cluster

    Args:
        cluster_name (str):
        classification (SlurmdbV0041DeleteClusterClassification | Unset):
        cluster (str | Unset):
        federation (str | Unset):
        flags (SlurmdbV0041DeleteClusterFlags | Unset):
        format_ (str | Unset):
        rpc_version (str | Unset):
        usage_end (str | Unset):
        usage_start (str | Unset):
        with_deleted (str | Unset):
        with_usage (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SlurmdbV0041DeleteClusterResponse200 | SlurmdbV0041DeleteClusterResponseDefault
    """

    return (
        await asyncio_detailed(
            cluster_name=cluster_name,
            client=client,
            classification=classification,
            cluster=cluster,
            federation=federation,
            flags=flags,
            format_=format_,
            rpc_version=rpc_version,
            usage_end=usage_end,
            usage_start=usage_start,
            with_deleted=with_deleted,
            with_usage=with_usage,
        )
    ).parsed
