from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.slurmdb_v0041_delete_single_qos_response_200 import SlurmdbV0041DeleteSingleQosResponse200
from ...models.slurmdb_v0041_delete_single_qos_response_default import SlurmdbV0041DeleteSingleQosResponseDefault
from ...types import Response


def _get_kwargs(
    qos: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/slurmdb/v0.0.41/qos/{qos}".format(
            qos=quote(str(qos), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> SlurmdbV0041DeleteSingleQosResponse200 | SlurmdbV0041DeleteSingleQosResponseDefault:
    if response.status_code == 200:
        response_200 = SlurmdbV0041DeleteSingleQosResponse200.from_dict(response.json())

        return response_200

    response_default = SlurmdbV0041DeleteSingleQosResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[SlurmdbV0041DeleteSingleQosResponse200 | SlurmdbV0041DeleteSingleQosResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    qos: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[SlurmdbV0041DeleteSingleQosResponse200 | SlurmdbV0041DeleteSingleQosResponseDefault]:
    """Delete QOS

    Args:
        qos (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SlurmdbV0041DeleteSingleQosResponse200 | SlurmdbV0041DeleteSingleQosResponseDefault]
    """

    kwargs = _get_kwargs(
        qos=qos,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    qos: str,
    *,
    client: AuthenticatedClient | Client,
) -> SlurmdbV0041DeleteSingleQosResponse200 | SlurmdbV0041DeleteSingleQosResponseDefault | None:
    """Delete QOS

    Args:
        qos (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SlurmdbV0041DeleteSingleQosResponse200 | SlurmdbV0041DeleteSingleQosResponseDefault
    """

    return sync_detailed(
        qos=qos,
        client=client,
    ).parsed


async def asyncio_detailed(
    qos: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[SlurmdbV0041DeleteSingleQosResponse200 | SlurmdbV0041DeleteSingleQosResponseDefault]:
    """Delete QOS

    Args:
        qos (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SlurmdbV0041DeleteSingleQosResponse200 | SlurmdbV0041DeleteSingleQosResponseDefault]
    """

    kwargs = _get_kwargs(
        qos=qos,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    qos: str,
    *,
    client: AuthenticatedClient | Client,
) -> SlurmdbV0041DeleteSingleQosResponse200 | SlurmdbV0041DeleteSingleQosResponseDefault | None:
    """Delete QOS

    Args:
        qos (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SlurmdbV0041DeleteSingleQosResponse200 | SlurmdbV0041DeleteSingleQosResponseDefault
    """

    return (
        await asyncio_detailed(
            qos=qos,
            client=client,
        )
    ).parsed
