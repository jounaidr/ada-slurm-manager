from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.slurm_v0044_get_job_flags import SlurmV0044GetJobFlags
from ...models.v0044_openapi_job_info_resp import V0044OpenapiJobInfoResp
from ...types import UNSET, Response, Unset


def _get_kwargs(
    job_id: str,
    *,
    update_time: str | Unset = UNSET,
    flags: SlurmV0044GetJobFlags | Unset = UNSET,
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
        "url": "/slurm/v0.0.44/job/{job_id}".format(
            job_id=quote(str(job_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> V0044OpenapiJobInfoResp:
    if response.status_code == 200:
        response_200 = V0044OpenapiJobInfoResp.from_dict(response.json())

        return response_200

    response_default = V0044OpenapiJobInfoResp.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[V0044OpenapiJobInfoResp]:
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
    update_time: str | Unset = UNSET,
    flags: SlurmV0044GetJobFlags | Unset = UNSET,
) -> Response[V0044OpenapiJobInfoResp]:
    """get job info

    Args:
        job_id (str):
        update_time (str | Unset):
        flags (SlurmV0044GetJobFlags | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[V0044OpenapiJobInfoResp]
    """

    kwargs = _get_kwargs(
        job_id=job_id,
        update_time=update_time,
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
    update_time: str | Unset = UNSET,
    flags: SlurmV0044GetJobFlags | Unset = UNSET,
) -> V0044OpenapiJobInfoResp | None:
    """get job info

    Args:
        job_id (str):
        update_time (str | Unset):
        flags (SlurmV0044GetJobFlags | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        V0044OpenapiJobInfoResp
    """

    return sync_detailed(
        job_id=job_id,
        client=client,
        update_time=update_time,
        flags=flags,
    ).parsed


async def asyncio_detailed(
    job_id: str,
    *,
    client: AuthenticatedClient | Client,
    update_time: str | Unset = UNSET,
    flags: SlurmV0044GetJobFlags | Unset = UNSET,
) -> Response[V0044OpenapiJobInfoResp]:
    """get job info

    Args:
        job_id (str):
        update_time (str | Unset):
        flags (SlurmV0044GetJobFlags | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[V0044OpenapiJobInfoResp]
    """

    kwargs = _get_kwargs(
        job_id=job_id,
        update_time=update_time,
        flags=flags,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    job_id: str,
    *,
    client: AuthenticatedClient | Client,
    update_time: str | Unset = UNSET,
    flags: SlurmV0044GetJobFlags | Unset = UNSET,
) -> V0044OpenapiJobInfoResp | None:
    """get job info

    Args:
        job_id (str):
        update_time (str | Unset):
        flags (SlurmV0044GetJobFlags | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        V0044OpenapiJobInfoResp
    """

    return (
        await asyncio_detailed(
            job_id=job_id,
            client=client,
            update_time=update_time,
            flags=flags,
        )
    ).parsed
