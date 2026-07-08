from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.v0042_job_desc_msg import V0042JobDescMsg
from ...models.v0042_openapi_job_post_response import V0042OpenapiJobPostResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    job_id: str,
    *,
    body: V0042JobDescMsg | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/slurm/v0.0.42/job/{job_id}".format(
            job_id=quote(str(job_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> V0042OpenapiJobPostResponse:
    if response.status_code == 200:
        response_200 = V0042OpenapiJobPostResponse.from_dict(response.json())

        return response_200

    response_default = V0042OpenapiJobPostResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[V0042OpenapiJobPostResponse]:
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
    body: V0042JobDescMsg | Unset = UNSET,
) -> Response[V0042OpenapiJobPostResponse]:
    """update job

    Args:
        job_id (str):
        body (V0042JobDescMsg | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[V0042OpenapiJobPostResponse]
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
    body: V0042JobDescMsg | Unset = UNSET,
) -> V0042OpenapiJobPostResponse | None:
    """update job

    Args:
        job_id (str):
        body (V0042JobDescMsg | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        V0042OpenapiJobPostResponse
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
    body: V0042JobDescMsg | Unset = UNSET,
) -> Response[V0042OpenapiJobPostResponse]:
    """update job

    Args:
        job_id (str):
        body (V0042JobDescMsg | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[V0042OpenapiJobPostResponse]
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
    body: V0042JobDescMsg | Unset = UNSET,
) -> V0042OpenapiJobPostResponse | None:
    """update job

    Args:
        job_id (str):
        body (V0042JobDescMsg | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        V0042OpenapiJobPostResponse
    """

    return (
        await asyncio_detailed(
            job_id=job_id,
            client=client,
            body=body,
        )
    ).parsed
