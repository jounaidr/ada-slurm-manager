from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.v0037_signal import V0037Signal
from ...types import UNSET, Response, Unset


def _get_kwargs(
    job_id: str,
    *,
    signal: V0037Signal | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_signal: str | Unset = UNSET
    if not isinstance(signal, Unset):
        json_signal = signal.value

    params["signal"] = json_signal

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/slurm/v0.0.37/job/{job_id}".format(
            job_id=quote(str(job_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if response.status_code == 200:
        return None

    if response.status_code == 500:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    job_id: str,
    *,
    client: AuthenticatedClient | Client,
    signal: V0037Signal | Unset = UNSET,
) -> Response[Any]:
    """cancel or signal job

    Args:
        job_id (str):
        signal (V0037Signal | Unset): POSIX signal name

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        job_id=job_id,
        signal=signal,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    job_id: str,
    *,
    client: AuthenticatedClient | Client,
    signal: V0037Signal | Unset = UNSET,
) -> Response[Any]:
    """cancel or signal job

    Args:
        job_id (str):
        signal (V0037Signal | Unset): POSIX signal name

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        job_id=job_id,
        signal=signal,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
