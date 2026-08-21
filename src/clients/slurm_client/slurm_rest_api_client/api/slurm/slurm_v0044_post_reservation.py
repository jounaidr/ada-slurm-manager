from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.v0044_openapi_reservation_mod_resp import V0044OpenapiReservationModResp
from ...models.v0044_reservation_desc_msg import V0044ReservationDescMsg
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: V0044ReservationDescMsg | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/slurm/v0.0.44/reservation",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> V0044OpenapiReservationModResp:
    if response.status_code == 200:
        response_200 = V0044OpenapiReservationModResp.from_dict(response.json())

        return response_200

    response_default = V0044OpenapiReservationModResp.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[V0044OpenapiReservationModResp]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: V0044ReservationDescMsg | Unset = UNSET,
) -> Response[V0044OpenapiReservationModResp]:
    """create or update a reservation

    Args:
        body (V0044ReservationDescMsg | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[V0044OpenapiReservationModResp]
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
    body: V0044ReservationDescMsg | Unset = UNSET,
) -> V0044OpenapiReservationModResp | None:
    """create or update a reservation

    Args:
        body (V0044ReservationDescMsg | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        V0044OpenapiReservationModResp
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: V0044ReservationDescMsg | Unset = UNSET,
) -> Response[V0044OpenapiReservationModResp]:
    """create or update a reservation

    Args:
        body (V0044ReservationDescMsg | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[V0044OpenapiReservationModResp]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: V0044ReservationDescMsg | Unset = UNSET,
) -> V0044OpenapiReservationModResp | None:
    """create or update a reservation

    Args:
        body (V0044ReservationDescMsg | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        V0044OpenapiReservationModResp
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
