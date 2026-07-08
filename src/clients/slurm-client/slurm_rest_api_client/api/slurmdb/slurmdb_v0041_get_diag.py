from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.slurmdb_v0041_get_diag_response_200 import SlurmdbV0041GetDiagResponse200
from ...models.slurmdb_v0041_get_diag_response_default import SlurmdbV0041GetDiagResponseDefault
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/slurmdb/v0.0.41/diag/",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> SlurmdbV0041GetDiagResponse200 | SlurmdbV0041GetDiagResponseDefault:
    if response.status_code == 200:
        response_200 = SlurmdbV0041GetDiagResponse200.from_dict(response.json())

        return response_200

    response_default = SlurmdbV0041GetDiagResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[SlurmdbV0041GetDiagResponse200 | SlurmdbV0041GetDiagResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[SlurmdbV0041GetDiagResponse200 | SlurmdbV0041GetDiagResponseDefault]:
    """Get slurmdb diagnostics

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SlurmdbV0041GetDiagResponse200 | SlurmdbV0041GetDiagResponseDefault]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> SlurmdbV0041GetDiagResponse200 | SlurmdbV0041GetDiagResponseDefault | None:
    """Get slurmdb diagnostics

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SlurmdbV0041GetDiagResponse200 | SlurmdbV0041GetDiagResponseDefault
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[SlurmdbV0041GetDiagResponse200 | SlurmdbV0041GetDiagResponseDefault]:
    """Get slurmdb diagnostics

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SlurmdbV0041GetDiagResponse200 | SlurmdbV0041GetDiagResponseDefault]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> SlurmdbV0041GetDiagResponse200 | SlurmdbV0041GetDiagResponseDefault | None:
    """Get slurmdb diagnostics

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SlurmdbV0041GetDiagResponse200 | SlurmdbV0041GetDiagResponseDefault
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
