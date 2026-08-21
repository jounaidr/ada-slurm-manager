from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.v0044_job_alloc_req import V0044JobAllocReq
from ...models.v0044_openapi_job_alloc_resp import V0044OpenapiJobAllocResp
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: V0044JobAllocReq | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/slurm/v0.0.44/job/allocate",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> V0044OpenapiJobAllocResp:
    if response.status_code == 200:
        response_200 = V0044OpenapiJobAllocResp.from_dict(response.json())

        return response_200

    response_default = V0044OpenapiJobAllocResp.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[V0044OpenapiJobAllocResp]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: V0044JobAllocReq | Unset = UNSET,
) -> Response[V0044OpenapiJobAllocResp]:
    """submit new job allocation without any steps that must be signaled to stop

    Args:
        body (V0044JobAllocReq | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[V0044OpenapiJobAllocResp]
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
    body: V0044JobAllocReq | Unset = UNSET,
) -> V0044OpenapiJobAllocResp | None:
    """submit new job allocation without any steps that must be signaled to stop

    Args:
        body (V0044JobAllocReq | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        V0044OpenapiJobAllocResp
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: V0044JobAllocReq | Unset = UNSET,
) -> Response[V0044OpenapiJobAllocResp]:
    """submit new job allocation without any steps that must be signaled to stop

    Args:
        body (V0044JobAllocReq | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[V0044OpenapiJobAllocResp]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: V0044JobAllocReq | Unset = UNSET,
) -> V0044OpenapiJobAllocResp | None:
    """submit new job allocation without any steps that must be signaled to stop

    Args:
        body (V0044JobAllocReq | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        V0044OpenapiJobAllocResp
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
