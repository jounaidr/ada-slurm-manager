from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.slurmdb_v0039_get_single_qos_with_deleted import SlurmdbV0039GetSingleQosWithDeleted
from ...models.status import Status
from ...types import UNSET, Response, Unset


def _get_kwargs(
    qos_name: str,
    *,
    with_deleted: SlurmdbV0039GetSingleQosWithDeleted | Unset = SlurmdbV0039GetSingleQosWithDeleted.FALSE,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_with_deleted: str | Unset = UNSET
    if not isinstance(with_deleted, Unset):
        json_with_deleted = with_deleted.value

    params["with_deleted"] = json_with_deleted

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/slurmdb/v0.0.39/qos/{qos_name}".format(
            qos_name=quote(str(qos_name), safe=""),
        ),
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
    qos_name: str,
    *,
    client: AuthenticatedClient | Client,
    with_deleted: SlurmdbV0039GetSingleQosWithDeleted | Unset = SlurmdbV0039GetSingleQosWithDeleted.FALSE,
) -> Response[Status]:
    """Get QOS info

    Args:
        qos_name (str):
        with_deleted (SlurmdbV0039GetSingleQosWithDeleted | Unset):  Default:
            SlurmdbV0039GetSingleQosWithDeleted.FALSE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Status]
    """

    kwargs = _get_kwargs(
        qos_name=qos_name,
        with_deleted=with_deleted,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    qos_name: str,
    *,
    client: AuthenticatedClient | Client,
    with_deleted: SlurmdbV0039GetSingleQosWithDeleted | Unset = SlurmdbV0039GetSingleQosWithDeleted.FALSE,
) -> Status | None:
    """Get QOS info

    Args:
        qos_name (str):
        with_deleted (SlurmdbV0039GetSingleQosWithDeleted | Unset):  Default:
            SlurmdbV0039GetSingleQosWithDeleted.FALSE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Status
    """

    return sync_detailed(
        qos_name=qos_name,
        client=client,
        with_deleted=with_deleted,
    ).parsed


async def asyncio_detailed(
    qos_name: str,
    *,
    client: AuthenticatedClient | Client,
    with_deleted: SlurmdbV0039GetSingleQosWithDeleted | Unset = SlurmdbV0039GetSingleQosWithDeleted.FALSE,
) -> Response[Status]:
    """Get QOS info

    Args:
        qos_name (str):
        with_deleted (SlurmdbV0039GetSingleQosWithDeleted | Unset):  Default:
            SlurmdbV0039GetSingleQosWithDeleted.FALSE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Status]
    """

    kwargs = _get_kwargs(
        qos_name=qos_name,
        with_deleted=with_deleted,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    qos_name: str,
    *,
    client: AuthenticatedClient | Client,
    with_deleted: SlurmdbV0039GetSingleQosWithDeleted | Unset = SlurmdbV0039GetSingleQosWithDeleted.FALSE,
) -> Status | None:
    """Get QOS info

    Args:
        qos_name (str):
        with_deleted (SlurmdbV0039GetSingleQosWithDeleted | Unset):  Default:
            SlurmdbV0039GetSingleQosWithDeleted.FALSE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Status
    """

    return (
        await asyncio_detailed(
            qos_name=qos_name,
            client=client,
            with_deleted=with_deleted,
        )
    ).parsed
