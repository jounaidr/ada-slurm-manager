from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.v0038_error import V0038Error
from ...models.v0038_job_submission import V0038JobSubmission
from ...models.v0038_job_submission_response import V0038JobSubmissionResponse
from ...types import Response


def _get_kwargs(
    *,
    body: V0038JobSubmission,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/slurm/v0.0.38/job/submit",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> V0038JobSubmissionResponse | list[V0038Error]:
    if response.status_code == 200:
        response_200 = V0038JobSubmissionResponse.from_dict(response.json())

        return response_200

    response_default = []
    _response_default = response.json()
    for componentsschemasv0_0_38_errors_item_data in _response_default:
        componentsschemasv0_0_38_errors_item = V0038Error.from_dict(componentsschemasv0_0_38_errors_item_data)

        response_default.append(componentsschemasv0_0_38_errors_item)

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[V0038JobSubmissionResponse | list[V0038Error]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: V0038JobSubmission,
) -> Response[V0038JobSubmissionResponse | list[V0038Error]]:
    """submit new job

    Args:
        body (V0038JobSubmission):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[V0038JobSubmissionResponse | list[V0038Error]]
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
    body: V0038JobSubmission,
) -> V0038JobSubmissionResponse | list[V0038Error] | None:
    """submit new job

    Args:
        body (V0038JobSubmission):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        V0038JobSubmissionResponse | list[V0038Error]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: V0038JobSubmission,
) -> Response[V0038JobSubmissionResponse | list[V0038Error]]:
    """submit new job

    Args:
        body (V0038JobSubmission):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[V0038JobSubmissionResponse | list[V0038Error]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: V0038JobSubmission,
) -> V0038JobSubmissionResponse | list[V0038Error] | None:
    """submit new job

    Args:
        body (V0038JobSubmission):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        V0038JobSubmissionResponse | list[V0038Error]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
