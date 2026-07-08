from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.v0044_openapi_slurmdbd_qos_removed_resp import V0044OpenapiSlurmdbdQosRemovedResp
from ...types import Response


def _get_kwargs(
    qos: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/slurmdb/v0.0.44/qos/{qos}".format(
            qos=quote(str(qos), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> V0044OpenapiSlurmdbdQosRemovedResp:
    if response.status_code == 200:
        response_200 = V0044OpenapiSlurmdbdQosRemovedResp.from_dict(response.json())

        return response_200

    response_default = V0044OpenapiSlurmdbdQosRemovedResp.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[V0044OpenapiSlurmdbdQosRemovedResp]:
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
) -> Response[V0044OpenapiSlurmdbdQosRemovedResp]:
    """Delete QOS

    Args:
        qos (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[V0044OpenapiSlurmdbdQosRemovedResp]
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
) -> V0044OpenapiSlurmdbdQosRemovedResp | None:
    """Delete QOS

    Args:
        qos (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        V0044OpenapiSlurmdbdQosRemovedResp
    """

    return sync_detailed(
        qos=qos,
        client=client,
    ).parsed


async def asyncio_detailed(
    qos: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[V0044OpenapiSlurmdbdQosRemovedResp]:
    """Delete QOS

    Args:
        qos (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[V0044OpenapiSlurmdbdQosRemovedResp]
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
) -> V0044OpenapiSlurmdbdQosRemovedResp | None:
    """Delete QOS

    Args:
        qos (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        V0044OpenapiSlurmdbdQosRemovedResp
    """

    return (
        await asyncio_detailed(
            qos=qos,
            client=client,
        )
    ).parsed
