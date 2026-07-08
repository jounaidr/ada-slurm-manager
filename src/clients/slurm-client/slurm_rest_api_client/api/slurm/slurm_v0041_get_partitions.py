from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.slurm_v0041_get_partitions_flags import SlurmV0041GetPartitionsFlags
from ...models.v0041_openapi_partition_resp import V0041OpenapiPartitionResp
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    update_time: str | Unset = UNSET,
    flags: SlurmV0041GetPartitionsFlags | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["update_time"] = update_time

    json_flags: str | Unset = UNSET
    if not isinstance(flags, Unset):
        json_flags = flags.value

    params["flags"] = json_flags

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/slurm/v0.0.41/partitions/",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> V0041OpenapiPartitionResp:
    if response.status_code == 200:
        response_200 = V0041OpenapiPartitionResp.from_dict(response.json())

        return response_200

    response_default = V0041OpenapiPartitionResp.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[V0041OpenapiPartitionResp]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    update_time: str | Unset = UNSET,
    flags: SlurmV0041GetPartitionsFlags | Unset = UNSET,
) -> Response[V0041OpenapiPartitionResp]:
    """get all partition info

    Args:
        update_time (str | Unset):
        flags (SlurmV0041GetPartitionsFlags | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[V0041OpenapiPartitionResp]
    """

    kwargs = _get_kwargs(
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
    update_time: str | Unset = UNSET,
    flags: SlurmV0041GetPartitionsFlags | Unset = UNSET,
) -> V0041OpenapiPartitionResp | None:
    """get all partition info

    Args:
        update_time (str | Unset):
        flags (SlurmV0041GetPartitionsFlags | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        V0041OpenapiPartitionResp
    """

    return sync_detailed(
        client=client,
        update_time=update_time,
        flags=flags,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    update_time: str | Unset = UNSET,
    flags: SlurmV0041GetPartitionsFlags | Unset = UNSET,
) -> Response[V0041OpenapiPartitionResp]:
    """get all partition info

    Args:
        update_time (str | Unset):
        flags (SlurmV0041GetPartitionsFlags | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[V0041OpenapiPartitionResp]
    """

    kwargs = _get_kwargs(
        update_time=update_time,
        flags=flags,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    update_time: str | Unset = UNSET,
    flags: SlurmV0041GetPartitionsFlags | Unset = UNSET,
) -> V0041OpenapiPartitionResp | None:
    """get all partition info

    Args:
        update_time (str | Unset):
        flags (SlurmV0041GetPartitionsFlags | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        V0041OpenapiPartitionResp
    """

    return (
        await asyncio_detailed(
            client=client,
            update_time=update_time,
            flags=flags,
        )
    ).parsed
