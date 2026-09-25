from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.dbv_0037_job_info import Dbv0037JobInfo
from ...types import Response


def _get_kwargs(
    job_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/slurmdb/v0.0.37/job/{job_id}".format(
            job_id=quote(str(job_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | Dbv0037JobInfo:
    if response.status_code == 200:
        response_200 = Dbv0037JobInfo.from_dict(response.json())

        return response_200

    response_default = cast(Any, None)
    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | Dbv0037JobInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    job_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | Dbv0037JobInfo]:
    """Get job info

     This endpoint may return multiple job entries since job_id is not a unique key - only the tuple
    (cluster, job_id, start_time) is unique. If the requested job_id is a component of a heterogeneous
    job all components are returned.

    Args:
        job_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Dbv0037JobInfo]
    """

    kwargs = _get_kwargs(
        job_id=job_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    job_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Any | Dbv0037JobInfo | None:
    """Get job info

     This endpoint may return multiple job entries since job_id is not a unique key - only the tuple
    (cluster, job_id, start_time) is unique. If the requested job_id is a component of a heterogeneous
    job all components are returned.

    Args:
        job_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Dbv0037JobInfo
    """

    return sync_detailed(
        job_id=job_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    job_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | Dbv0037JobInfo]:
    """Get job info

     This endpoint may return multiple job entries since job_id is not a unique key - only the tuple
    (cluster, job_id, start_time) is unique. If the requested job_id is a component of a heterogeneous
    job all components are returned.

    Args:
        job_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Dbv0037JobInfo]
    """

    kwargs = _get_kwargs(
        job_id=job_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    job_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Any | Dbv0037JobInfo | None:
    """Get job info

     This endpoint may return multiple job entries since job_id is not a unique key - only the tuple
    (cluster, job_id, start_time) is unique. If the requested job_id is a component of a heterogeneous
    job all components are returned.

    Args:
        job_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Dbv0037JobInfo
    """

    return (
        await asyncio_detailed(
            job_id=job_id,
            client=client,
        )
    ).parsed
