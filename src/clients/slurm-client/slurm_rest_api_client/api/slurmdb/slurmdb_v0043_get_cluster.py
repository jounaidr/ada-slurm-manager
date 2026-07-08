from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.slurmdb_v0043_get_cluster_classification import SlurmdbV0043GetClusterClassification
from ...models.slurmdb_v0043_get_cluster_flags import SlurmdbV0043GetClusterFlags
from ...models.v0043_openapi_clusters_resp import V0043OpenapiClustersResp
from ...types import UNSET, Response, Unset


def _get_kwargs(
    cluster_name: str,
    *,
    classification: SlurmdbV0043GetClusterClassification | Unset = UNSET,
    cluster: str | Unset = UNSET,
    federation: str | Unset = UNSET,
    flags: SlurmdbV0043GetClusterFlags | Unset = UNSET,
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
        "method": "get",
        "url": "/slurmdb/v0.0.43/cluster/{cluster_name}".format(
            cluster_name=quote(str(cluster_name), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> V0043OpenapiClustersResp:
    if response.status_code == 200:
        response_200 = V0043OpenapiClustersResp.from_dict(response.json())

        return response_200

    response_default = V0043OpenapiClustersResp.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[V0043OpenapiClustersResp]:
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
    classification: SlurmdbV0043GetClusterClassification | Unset = UNSET,
    cluster: str | Unset = UNSET,
    federation: str | Unset = UNSET,
    flags: SlurmdbV0043GetClusterFlags | Unset = UNSET,
    format_: str | Unset = UNSET,
    rpc_version: str | Unset = UNSET,
    usage_end: str | Unset = UNSET,
    usage_start: str | Unset = UNSET,
    with_deleted: str | Unset = UNSET,
    with_usage: str | Unset = UNSET,
) -> Response[V0043OpenapiClustersResp]:
    """Get cluster info

    Args:
        cluster_name (str):
        classification (SlurmdbV0043GetClusterClassification | Unset):
        cluster (str | Unset):
        federation (str | Unset):
        flags (SlurmdbV0043GetClusterFlags | Unset):
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
        Response[V0043OpenapiClustersResp]
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
    classification: SlurmdbV0043GetClusterClassification | Unset = UNSET,
    cluster: str | Unset = UNSET,
    federation: str | Unset = UNSET,
    flags: SlurmdbV0043GetClusterFlags | Unset = UNSET,
    format_: str | Unset = UNSET,
    rpc_version: str | Unset = UNSET,
    usage_end: str | Unset = UNSET,
    usage_start: str | Unset = UNSET,
    with_deleted: str | Unset = UNSET,
    with_usage: str | Unset = UNSET,
) -> V0043OpenapiClustersResp | None:
    """Get cluster info

    Args:
        cluster_name (str):
        classification (SlurmdbV0043GetClusterClassification | Unset):
        cluster (str | Unset):
        federation (str | Unset):
        flags (SlurmdbV0043GetClusterFlags | Unset):
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
        V0043OpenapiClustersResp
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
    classification: SlurmdbV0043GetClusterClassification | Unset = UNSET,
    cluster: str | Unset = UNSET,
    federation: str | Unset = UNSET,
    flags: SlurmdbV0043GetClusterFlags | Unset = UNSET,
    format_: str | Unset = UNSET,
    rpc_version: str | Unset = UNSET,
    usage_end: str | Unset = UNSET,
    usage_start: str | Unset = UNSET,
    with_deleted: str | Unset = UNSET,
    with_usage: str | Unset = UNSET,
) -> Response[V0043OpenapiClustersResp]:
    """Get cluster info

    Args:
        cluster_name (str):
        classification (SlurmdbV0043GetClusterClassification | Unset):
        cluster (str | Unset):
        federation (str | Unset):
        flags (SlurmdbV0043GetClusterFlags | Unset):
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
        Response[V0043OpenapiClustersResp]
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
    classification: SlurmdbV0043GetClusterClassification | Unset = UNSET,
    cluster: str | Unset = UNSET,
    federation: str | Unset = UNSET,
    flags: SlurmdbV0043GetClusterFlags | Unset = UNSET,
    format_: str | Unset = UNSET,
    rpc_version: str | Unset = UNSET,
    usage_end: str | Unset = UNSET,
    usage_start: str | Unset = UNSET,
    with_deleted: str | Unset = UNSET,
    with_usage: str | Unset = UNSET,
) -> V0043OpenapiClustersResp | None:
    """Get cluster info

    Args:
        cluster_name (str):
        classification (SlurmdbV0043GetClusterClassification | Unset):
        cluster (str | Unset):
        federation (str | Unset):
        flags (SlurmdbV0043GetClusterFlags | Unset):
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
        V0043OpenapiClustersResp
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
