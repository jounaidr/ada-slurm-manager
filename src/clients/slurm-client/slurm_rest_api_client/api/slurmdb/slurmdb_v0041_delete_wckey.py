from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.slurmdb_v0041_delete_wckey_response_200 import SlurmdbV0041DeleteWckeyResponse200
from ...models.slurmdb_v0041_delete_wckey_response_default import SlurmdbV0041DeleteWckeyResponseDefault
from ...types import Response


def _get_kwargs(
    id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/slurmdb/v0.0.41/wckey/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> SlurmdbV0041DeleteWckeyResponse200 | SlurmdbV0041DeleteWckeyResponseDefault:
    if response.status_code == 200:
        response_200 = SlurmdbV0041DeleteWckeyResponse200.from_dict(response.json())

        return response_200

    response_default = SlurmdbV0041DeleteWckeyResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[SlurmdbV0041DeleteWckeyResponse200 | SlurmdbV0041DeleteWckeyResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[SlurmdbV0041DeleteWckeyResponse200 | SlurmdbV0041DeleteWckeyResponseDefault]:
    """Delete wckey

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SlurmdbV0041DeleteWckeyResponse200 | SlurmdbV0041DeleteWckeyResponseDefault]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> SlurmdbV0041DeleteWckeyResponse200 | SlurmdbV0041DeleteWckeyResponseDefault | None:
    """Delete wckey

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SlurmdbV0041DeleteWckeyResponse200 | SlurmdbV0041DeleteWckeyResponseDefault
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[SlurmdbV0041DeleteWckeyResponse200 | SlurmdbV0041DeleteWckeyResponseDefault]:
    """Delete wckey

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SlurmdbV0041DeleteWckeyResponse200 | SlurmdbV0041DeleteWckeyResponseDefault]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> SlurmdbV0041DeleteWckeyResponse200 | SlurmdbV0041DeleteWckeyResponseDefault | None:
    """Delete wckey

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SlurmdbV0041DeleteWckeyResponse200 | SlurmdbV0041DeleteWckeyResponseDefault
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
