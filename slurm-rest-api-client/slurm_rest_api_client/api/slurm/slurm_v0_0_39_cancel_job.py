from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.slurm_v0039_cancel_job_signal import SlurmV0039CancelJobSignal
from ...models.status import Status
from ...types import UNSET, Response, Unset


def _get_kwargs(
    job_id: str,
    *,
    signal: SlurmV0039CancelJobSignal | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_signal: str | Unset = UNSET
    if not isinstance(signal, Unset):
        json_signal = signal.value

    params["signal"] = json_signal

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/slurm/v0.0.39/job/{job_id}".format(
            job_id=quote(str(job_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Status:
    if response.status_code == 200:
        response_200 = Status.from_dict(response.json())

        return response_200

    response_default = Status.from_dict(response.json())

    return response_default


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Status]:
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
    signal: SlurmV0039CancelJobSignal | Unset = UNSET,
) -> Response[Status]:
    """cancel or signal job

    Args:
        job_id (str):
        signal (SlurmV0039CancelJobSignal | Unset): POSIX signal name

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Status]
    """

    kwargs = _get_kwargs(
        job_id=job_id,
        signal=signal,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    job_id: str,
    *,
    client: AuthenticatedClient | Client,
    signal: SlurmV0039CancelJobSignal | Unset = UNSET,
) -> Status | None:
    """cancel or signal job

    Args:
        job_id (str):
        signal (SlurmV0039CancelJobSignal | Unset): POSIX signal name

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Status
    """

    return sync_detailed(
        job_id=job_id,
        client=client,
        signal=signal,
    ).parsed


async def asyncio_detailed(
    job_id: str,
    *,
    client: AuthenticatedClient | Client,
    signal: SlurmV0039CancelJobSignal | Unset = UNSET,
) -> Response[Status]:
    """cancel or signal job

    Args:
        job_id (str):
        signal (SlurmV0039CancelJobSignal | Unset): POSIX signal name

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Status]
    """

    kwargs = _get_kwargs(
        job_id=job_id,
        signal=signal,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    job_id: str,
    *,
    client: AuthenticatedClient | Client,
    signal: SlurmV0039CancelJobSignal | Unset = UNSET,
) -> Status | None:
    """cancel or signal job

    Args:
        job_id (str):
        signal (SlurmV0039CancelJobSignal | Unset): POSIX signal name

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Status
    """

    return (
        await asyncio_detailed(
            job_id=job_id,
            client=client,
            signal=signal,
        )
    ).parsed
