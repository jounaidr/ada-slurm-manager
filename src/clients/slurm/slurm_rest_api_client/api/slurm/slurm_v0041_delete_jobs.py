from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.slurm_v0041_delete_jobs_body import SlurmV0041DeleteJobsBody
from ...models.slurm_v0041_delete_jobs_response_200 import SlurmV0041DeleteJobsResponse200
from ...models.slurm_v0041_delete_jobs_response_default import SlurmV0041DeleteJobsResponseDefault
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: SlurmV0041DeleteJobsBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/slurm/v0.0.41/jobs/",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> SlurmV0041DeleteJobsResponse200 | SlurmV0041DeleteJobsResponseDefault:
    if response.status_code == 200:
        response_200 = SlurmV0041DeleteJobsResponse200.from_dict(response.json())

        return response_200

    response_default = SlurmV0041DeleteJobsResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[SlurmV0041DeleteJobsResponse200 | SlurmV0041DeleteJobsResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SlurmV0041DeleteJobsBody | Unset = UNSET,
) -> Response[SlurmV0041DeleteJobsResponse200 | SlurmV0041DeleteJobsResponseDefault]:
    """send signal to list of jobs

    Args:
        body (SlurmV0041DeleteJobsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SlurmV0041DeleteJobsResponse200 | SlurmV0041DeleteJobsResponseDefault]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: SlurmV0041DeleteJobsBody | Unset = UNSET,
) -> SlurmV0041DeleteJobsResponse200 | SlurmV0041DeleteJobsResponseDefault | None:
    """send signal to list of jobs

    Args:
        body (SlurmV0041DeleteJobsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SlurmV0041DeleteJobsResponse200 | SlurmV0041DeleteJobsResponseDefault
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SlurmV0041DeleteJobsBody | Unset = UNSET,
) -> Response[SlurmV0041DeleteJobsResponse200 | SlurmV0041DeleteJobsResponseDefault]:
    """send signal to list of jobs

    Args:
        body (SlurmV0041DeleteJobsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SlurmV0041DeleteJobsResponse200 | SlurmV0041DeleteJobsResponseDefault]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: SlurmV0041DeleteJobsBody | Unset = UNSET,
) -> SlurmV0041DeleteJobsResponse200 | SlurmV0041DeleteJobsResponseDefault | None:
    """send signal to list of jobs

    Args:
        body (SlurmV0041DeleteJobsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SlurmV0041DeleteJobsResponse200 | SlurmV0041DeleteJobsResponseDefault
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
