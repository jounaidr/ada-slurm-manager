from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.slurm_v0041_post_job_body import SlurmV0041PostJobBody
from ...models.slurm_v0041_post_job_response_200 import SlurmV0041PostJobResponse200
from ...models.slurm_v0041_post_job_response_default import SlurmV0041PostJobResponseDefault
from ...types import UNSET, Response, Unset


def _get_kwargs(
    job_id: str,
    *,
    body: SlurmV0041PostJobBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/slurm/v0.0.41/job/{job_id}".format(
            job_id=quote(str(job_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> SlurmV0041PostJobResponse200 | SlurmV0041PostJobResponseDefault:
    if response.status_code == 200:
        response_200 = SlurmV0041PostJobResponse200.from_dict(response.json())

        return response_200

    response_default = SlurmV0041PostJobResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[SlurmV0041PostJobResponse200 | SlurmV0041PostJobResponseDefault]:
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
    body: SlurmV0041PostJobBody | Unset = UNSET,
) -> Response[SlurmV0041PostJobResponse200 | SlurmV0041PostJobResponseDefault]:
    """update job

    Args:
        job_id (str):
        body (SlurmV0041PostJobBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SlurmV0041PostJobResponse200 | SlurmV0041PostJobResponseDefault]
    """

    kwargs = _get_kwargs(
        job_id=job_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    job_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SlurmV0041PostJobBody | Unset = UNSET,
) -> SlurmV0041PostJobResponse200 | SlurmV0041PostJobResponseDefault | None:
    """update job

    Args:
        job_id (str):
        body (SlurmV0041PostJobBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SlurmV0041PostJobResponse200 | SlurmV0041PostJobResponseDefault
    """

    return sync_detailed(
        job_id=job_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    job_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SlurmV0041PostJobBody | Unset = UNSET,
) -> Response[SlurmV0041PostJobResponse200 | SlurmV0041PostJobResponseDefault]:
    """update job

    Args:
        job_id (str):
        body (SlurmV0041PostJobBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SlurmV0041PostJobResponse200 | SlurmV0041PostJobResponseDefault]
    """

    kwargs = _get_kwargs(
        job_id=job_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    job_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SlurmV0041PostJobBody | Unset = UNSET,
) -> SlurmV0041PostJobResponse200 | SlurmV0041PostJobResponseDefault | None:
    """update job

    Args:
        job_id (str):
        body (SlurmV0041PostJobBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SlurmV0041PostJobResponse200 | SlurmV0041PostJobResponseDefault
    """

    return (
        await asyncio_detailed(
            job_id=job_id,
            client=client,
            body=body,
        )
    ).parsed
