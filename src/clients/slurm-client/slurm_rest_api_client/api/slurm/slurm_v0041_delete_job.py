from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.slurm_v0041_delete_job_flags import SlurmV0041DeleteJobFlags
from ...models.v0041_openapi_resp import V0041OpenapiResp
from ...types import UNSET, Response, Unset


def _get_kwargs(
    job_id: str,
    *,
    signal: str | Unset = UNSET,
    flags: SlurmV0041DeleteJobFlags | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["signal"] = signal

    json_flags: str | Unset = UNSET
    if not isinstance(flags, Unset):
        json_flags = flags.value

    params["flags"] = json_flags

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/slurm/v0.0.41/job/{job_id}".format(
            job_id=quote(str(job_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> V0041OpenapiResp:
    if response.status_code == 200:
        response_200 = V0041OpenapiResp.from_dict(response.json())

        return response_200

    response_default = V0041OpenapiResp.from_dict(response.json())

    return response_default


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[V0041OpenapiResp]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    job_id: str,
    *,
    client: AuthenticatedClient | Client,
    signal: str | Unset = UNSET,
    flags: SlurmV0041DeleteJobFlags | Unset = UNSET,
) -> Response[V0041OpenapiResp]:
    """cancel or signal job

    Args:
        job_id (str):
        signal (str | Unset):
        flags (SlurmV0041DeleteJobFlags | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[V0041OpenapiResp]
    """

    kwargs = _get_kwargs(
        job_id=job_id,
        signal=signal,
        flags=flags,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    job_id: str,
    *,
    client: AuthenticatedClient | Client,
    signal: str | Unset = UNSET,
    flags: SlurmV0041DeleteJobFlags | Unset = UNSET,
) -> V0041OpenapiResp | None:
    """cancel or signal job

    Args:
        job_id (str):
        signal (str | Unset):
        flags (SlurmV0041DeleteJobFlags | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        V0041OpenapiResp
    """

    return sync_detailed(
        job_id=job_id,
        client=client,
        signal=signal,
        flags=flags,
    ).parsed


async def asyncio_detailed(
    job_id: str,
    *,
    client: AuthenticatedClient | Client,
    signal: str | Unset = UNSET,
    flags: SlurmV0041DeleteJobFlags | Unset = UNSET,
) -> Response[V0041OpenapiResp]:
    """cancel or signal job

    Args:
        job_id (str):
        signal (str | Unset):
        flags (SlurmV0041DeleteJobFlags | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[V0041OpenapiResp]
    """

    kwargs = _get_kwargs(
        job_id=job_id,
        signal=signal,
        flags=flags,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    job_id: str,
    *,
    client: AuthenticatedClient | Client,
    signal: str | Unset = UNSET,
    flags: SlurmV0041DeleteJobFlags | Unset = UNSET,
) -> V0041OpenapiResp | None:
    """cancel or signal job

    Args:
        job_id (str):
        signal (str | Unset):
        flags (SlurmV0041DeleteJobFlags | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        V0041OpenapiResp
    """

    return (
        await asyncio_detailed(
            job_id=job_id,
            client=client,
            signal=signal,
            flags=flags,
        )
    ).parsed
