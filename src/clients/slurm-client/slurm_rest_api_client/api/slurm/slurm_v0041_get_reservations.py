from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.v0041_openapi_reservation_resp import V0041OpenapiReservationResp
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    update_time: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["update_time"] = update_time

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/slurm/v0.0.41/reservations/",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> V0041OpenapiReservationResp:
    if response.status_code == 200:
        response_200 = V0041OpenapiReservationResp.from_dict(response.json())

        return response_200

    response_default = V0041OpenapiReservationResp.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[V0041OpenapiReservationResp]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    update_time: str | Unset = UNSET,
) -> Response[V0041OpenapiReservationResp]:
    """get all reservation info

    Args:
        update_time (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[V0041OpenapiReservationResp]
    """

    kwargs = _get_kwargs(
        update_time=update_time,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    update_time: str | Unset = UNSET,
) -> V0041OpenapiReservationResp | None:
    """get all reservation info

    Args:
        update_time (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        V0041OpenapiReservationResp
    """

    return sync_detailed(
        client=client,
        update_time=update_time,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    update_time: str | Unset = UNSET,
) -> Response[V0041OpenapiReservationResp]:
    """get all reservation info

    Args:
        update_time (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[V0041OpenapiReservationResp]
    """

    kwargs = _get_kwargs(
        update_time=update_time,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    update_time: str | Unset = UNSET,
) -> V0041OpenapiReservationResp | None:
    """get all reservation info

    Args:
        update_time (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        V0041OpenapiReservationResp
    """

    return (
        await asyncio_detailed(
            client=client,
            update_time=update_time,
        )
    ).parsed
