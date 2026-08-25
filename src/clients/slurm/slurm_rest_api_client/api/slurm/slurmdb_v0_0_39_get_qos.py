from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.slurmdb_v0039_get_qos_with_deleted import SlurmdbV0039GetQosWithDeleted
from ...models.status import Status
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    with_deleted: SlurmdbV0039GetQosWithDeleted | Unset = SlurmdbV0039GetQosWithDeleted.FALSE,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_with_deleted: str | Unset = UNSET
    if not isinstance(with_deleted, Unset):
        json_with_deleted = with_deleted.value

    params["with_deleted"] = json_with_deleted

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/slurmdb/v0.0.39/qos",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Status:
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
    *,
    client: AuthenticatedClient | Client,
    with_deleted: SlurmdbV0039GetQosWithDeleted | Unset = SlurmdbV0039GetQosWithDeleted.FALSE,
) -> Response[Status]:
    """Get QOS list

    Args:
        with_deleted (SlurmdbV0039GetQosWithDeleted | Unset):  Default:
            SlurmdbV0039GetQosWithDeleted.FALSE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Status]
    """

    kwargs = _get_kwargs(
        with_deleted=with_deleted,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    with_deleted: SlurmdbV0039GetQosWithDeleted | Unset = SlurmdbV0039GetQosWithDeleted.FALSE,
) -> Status | None:
    """Get QOS list

    Args:
        with_deleted (SlurmdbV0039GetQosWithDeleted | Unset):  Default:
            SlurmdbV0039GetQosWithDeleted.FALSE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Status
    """

    return sync_detailed(
        client=client,
        with_deleted=with_deleted,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    with_deleted: SlurmdbV0039GetQosWithDeleted | Unset = SlurmdbV0039GetQosWithDeleted.FALSE,
) -> Response[Status]:
    """Get QOS list

    Args:
        with_deleted (SlurmdbV0039GetQosWithDeleted | Unset):  Default:
            SlurmdbV0039GetQosWithDeleted.FALSE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Status]
    """

    kwargs = _get_kwargs(
        with_deleted=with_deleted,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    with_deleted: SlurmdbV0039GetQosWithDeleted | Unset = SlurmdbV0039GetQosWithDeleted.FALSE,
) -> Status | None:
    """Get QOS list

    Args:
        with_deleted (SlurmdbV0039GetQosWithDeleted | Unset):  Default:
            SlurmdbV0039GetQosWithDeleted.FALSE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Status
    """

    return (
        await asyncio_detailed(
            client=client,
            with_deleted=with_deleted,
        )
    ).parsed
