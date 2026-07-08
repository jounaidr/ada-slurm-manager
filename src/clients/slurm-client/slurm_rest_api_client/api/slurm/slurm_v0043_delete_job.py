from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.slurm_v0043_delete_job_flags import SlurmV0043DeleteJobFlags
from ...models.v0043_openapi_kill_job_resp import V0043OpenapiKillJobResp
from ...types import UNSET, Response, Unset


def _get_kwargs(
    job_id: str,
    *,
    signal: str | Unset = UNSET,
    flags: SlurmV0043DeleteJobFlags | Unset = UNSET,
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
        "url": "/slurm/v0.0.43/job/{job_id}".format(
            job_id=quote(str(job_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> V0043OpenapiKillJobResp:
    if response.status_code == 200:
        response_200 = V0043OpenapiKillJobResp.from_dict(response.json())

        return response_200

    response_default = V0043OpenapiKillJobResp.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[V0043OpenapiKillJobResp]:
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
    flags: SlurmV0043DeleteJobFlags | Unset = UNSET,
) -> Response[V0043OpenapiKillJobResp]:
    """cancel or signal job

    Args:
        job_id (str):
        signal (str | Unset):
        flags (SlurmV0043DeleteJobFlags | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[V0043OpenapiKillJobResp]
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
    flags: SlurmV0043DeleteJobFlags | Unset = UNSET,
) -> V0043OpenapiKillJobResp | None:
    """cancel or signal job

    Args:
        job_id (str):
        signal (str | Unset):
        flags (SlurmV0043DeleteJobFlags | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        V0043OpenapiKillJobResp
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
    flags: SlurmV0043DeleteJobFlags | Unset = UNSET,
) -> Response[V0043OpenapiKillJobResp]:
    """cancel or signal job

    Args:
        job_id (str):
        signal (str | Unset):
        flags (SlurmV0043DeleteJobFlags | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[V0043OpenapiKillJobResp]
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
    flags: SlurmV0043DeleteJobFlags | Unset = UNSET,
) -> V0043OpenapiKillJobResp | None:
    """cancel or signal job

    Args:
        job_id (str):
        signal (str | Unset):
        flags (SlurmV0043DeleteJobFlags | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        V0043OpenapiKillJobResp
    """

    return (
        await asyncio_detailed(
            job_id=job_id,
            client=client,
            signal=signal,
            flags=flags,
        )
    ).parsed
