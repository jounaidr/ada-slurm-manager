from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.slurm_v0041_get_licenses_response_200 import SlurmV0041GetLicensesResponse200
from ...models.slurm_v0041_get_licenses_response_default import SlurmV0041GetLicensesResponseDefault
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/slurm/v0.0.41/licenses/",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> SlurmV0041GetLicensesResponse200 | SlurmV0041GetLicensesResponseDefault:
    if response.status_code == 200:
        response_200 = SlurmV0041GetLicensesResponse200.from_dict(response.json())

        return response_200

    response_default = SlurmV0041GetLicensesResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[SlurmV0041GetLicensesResponse200 | SlurmV0041GetLicensesResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[SlurmV0041GetLicensesResponse200 | SlurmV0041GetLicensesResponseDefault]:
    """get all Slurm tracked license info

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SlurmV0041GetLicensesResponse200 | SlurmV0041GetLicensesResponseDefault]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> SlurmV0041GetLicensesResponse200 | SlurmV0041GetLicensesResponseDefault | None:
    """get all Slurm tracked license info

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SlurmV0041GetLicensesResponse200 | SlurmV0041GetLicensesResponseDefault
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[SlurmV0041GetLicensesResponse200 | SlurmV0041GetLicensesResponseDefault]:
    """get all Slurm tracked license info

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SlurmV0041GetLicensesResponse200 | SlurmV0041GetLicensesResponseDefault]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> SlurmV0041GetLicensesResponse200 | SlurmV0041GetLicensesResponseDefault | None:
    """get all Slurm tracked license info

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SlurmV0041GetLicensesResponse200 | SlurmV0041GetLicensesResponseDefault
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
