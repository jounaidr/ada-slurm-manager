from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.v0042_kill_jobs_msg import V0042KillJobsMsg
from ...models.v0042_openapi_kill_jobs_resp import V0042OpenapiKillJobsResp
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: V0042KillJobsMsg | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/slurm/v0.0.42/jobs/",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> V0042OpenapiKillJobsResp:
    if response.status_code == 200:
        response_200 = V0042OpenapiKillJobsResp.from_dict(response.json())

        return response_200

    response_default = V0042OpenapiKillJobsResp.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[V0042OpenapiKillJobsResp]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: V0042KillJobsMsg | Unset = UNSET,
) -> Response[V0042OpenapiKillJobsResp]:
    """send signal to list of jobs

    Args:
        body (V0042KillJobsMsg | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[V0042OpenapiKillJobsResp]
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
    body: V0042KillJobsMsg | Unset = UNSET,
) -> V0042OpenapiKillJobsResp | None:
    """send signal to list of jobs

    Args:
        body (V0042KillJobsMsg | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        V0042OpenapiKillJobsResp
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: V0042KillJobsMsg | Unset = UNSET,
) -> Response[V0042OpenapiKillJobsResp]:
    """send signal to list of jobs

    Args:
        body (V0042KillJobsMsg | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[V0042OpenapiKillJobsResp]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: V0042KillJobsMsg | Unset = UNSET,
) -> V0042OpenapiKillJobsResp | None:
    """send signal to list of jobs

    Args:
        body (V0042KillJobsMsg | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        V0042OpenapiKillJobsResp
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
