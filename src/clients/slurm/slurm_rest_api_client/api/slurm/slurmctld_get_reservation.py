from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.v0037_reservations_response import V0037ReservationsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    reservation_name: str,
    *,
    update_time: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["update_time"] = update_time

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/slurm/v0.0.37/reservation/{reservation_name}".format(
            reservation_name=quote(str(reservation_name), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | V0037ReservationsResponse:
    if response.status_code == 200:
        response_200 = V0037ReservationsResponse.from_dict(response.json())

        return response_200

    response_default = cast(Any, None)
    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | V0037ReservationsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    reservation_name: str,
    *,
    client: AuthenticatedClient | Client,
    update_time: int | Unset = UNSET,
) -> Response[Any | V0037ReservationsResponse]:
    """get reservation info

    Args:
        reservation_name (str):
        update_time (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | V0037ReservationsResponse]
    """

    kwargs = _get_kwargs(
        reservation_name=reservation_name,
        update_time=update_time,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    reservation_name: str,
    *,
    client: AuthenticatedClient | Client,
    update_time: int | Unset = UNSET,
) -> Any | V0037ReservationsResponse | None:
    """get reservation info

    Args:
        reservation_name (str):
        update_time (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | V0037ReservationsResponse
    """

    return sync_detailed(
        reservation_name=reservation_name,
        client=client,
        update_time=update_time,
    ).parsed


async def asyncio_detailed(
    reservation_name: str,
    *,
    client: AuthenticatedClient | Client,
    update_time: int | Unset = UNSET,
) -> Response[Any | V0037ReservationsResponse]:
    """get reservation info

    Args:
        reservation_name (str):
        update_time (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | V0037ReservationsResponse]
    """

    kwargs = _get_kwargs(
        reservation_name=reservation_name,
        update_time=update_time,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    reservation_name: str,
    *,
    client: AuthenticatedClient | Client,
    update_time: int | Unset = UNSET,
) -> Any | V0037ReservationsResponse | None:
    """get reservation info

    Args:
        reservation_name (str):
        update_time (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | V0037ReservationsResponse
    """

    return (
        await asyncio_detailed(
            reservation_name=reservation_name,
            client=client,
            update_time=update_time,
        )
    ).parsed
