from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.slurmdb_v0041_get_qos_preempt_mode import SlurmdbV0041GetQosPreemptMode
from ...models.v0041_openapi_slurmdbd_qos_resp import V0041OpenapiSlurmdbdQosResp
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    description: str | Unset = UNSET,
    id: str | Unset = UNSET,
    format_: str | Unset = UNSET,
    name: str | Unset = UNSET,
    preempt_mode: SlurmdbV0041GetQosPreemptMode | Unset = UNSET,
    with_deleted: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["description"] = description

    params["id"] = id

    params["format"] = format_

    params["name"] = name

    json_preempt_mode: str | Unset = UNSET
    if not isinstance(preempt_mode, Unset):
        json_preempt_mode = preempt_mode.value

    params["preempt_mode"] = json_preempt_mode

    params["with_deleted"] = with_deleted

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/slurmdb/v0.0.41/qos/",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> V0041OpenapiSlurmdbdQosResp:
    if response.status_code == 200:
        response_200 = V0041OpenapiSlurmdbdQosResp.from_dict(response.json())

        return response_200

    response_default = V0041OpenapiSlurmdbdQosResp.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[V0041OpenapiSlurmdbdQosResp]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    description: str | Unset = UNSET,
    id: str | Unset = UNSET,
    format_: str | Unset = UNSET,
    name: str | Unset = UNSET,
    preempt_mode: SlurmdbV0041GetQosPreemptMode | Unset = UNSET,
    with_deleted: str | Unset = UNSET,
) -> Response[V0041OpenapiSlurmdbdQosResp]:
    """Get QOS list

    Args:
        description (str | Unset):
        id (str | Unset):
        format_ (str | Unset):
        name (str | Unset):
        preempt_mode (SlurmdbV0041GetQosPreemptMode | Unset):
        with_deleted (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[V0041OpenapiSlurmdbdQosResp]
    """

    kwargs = _get_kwargs(
        description=description,
        id=id,
        format_=format_,
        name=name,
        preempt_mode=preempt_mode,
        with_deleted=with_deleted,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    description: str | Unset = UNSET,
    id: str | Unset = UNSET,
    format_: str | Unset = UNSET,
    name: str | Unset = UNSET,
    preempt_mode: SlurmdbV0041GetQosPreemptMode | Unset = UNSET,
    with_deleted: str | Unset = UNSET,
) -> V0041OpenapiSlurmdbdQosResp | None:
    """Get QOS list

    Args:
        description (str | Unset):
        id (str | Unset):
        format_ (str | Unset):
        name (str | Unset):
        preempt_mode (SlurmdbV0041GetQosPreemptMode | Unset):
        with_deleted (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        V0041OpenapiSlurmdbdQosResp
    """

    return sync_detailed(
        client=client,
        description=description,
        id=id,
        format_=format_,
        name=name,
        preempt_mode=preempt_mode,
        with_deleted=with_deleted,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    description: str | Unset = UNSET,
    id: str | Unset = UNSET,
    format_: str | Unset = UNSET,
    name: str | Unset = UNSET,
    preempt_mode: SlurmdbV0041GetQosPreemptMode | Unset = UNSET,
    with_deleted: str | Unset = UNSET,
) -> Response[V0041OpenapiSlurmdbdQosResp]:
    """Get QOS list

    Args:
        description (str | Unset):
        id (str | Unset):
        format_ (str | Unset):
        name (str | Unset):
        preempt_mode (SlurmdbV0041GetQosPreemptMode | Unset):
        with_deleted (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[V0041OpenapiSlurmdbdQosResp]
    """

    kwargs = _get_kwargs(
        description=description,
        id=id,
        format_=format_,
        name=name,
        preempt_mode=preempt_mode,
        with_deleted=with_deleted,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    description: str | Unset = UNSET,
    id: str | Unset = UNSET,
    format_: str | Unset = UNSET,
    name: str | Unset = UNSET,
    preempt_mode: SlurmdbV0041GetQosPreemptMode | Unset = UNSET,
    with_deleted: str | Unset = UNSET,
) -> V0041OpenapiSlurmdbdQosResp | None:
    """Get QOS list

    Args:
        description (str | Unset):
        id (str | Unset):
        format_ (str | Unset):
        name (str | Unset):
        preempt_mode (SlurmdbV0041GetQosPreemptMode | Unset):
        with_deleted (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        V0041OpenapiSlurmdbdQosResp
    """

    return (
        await asyncio_detailed(
            client=client,
            description=description,
            id=id,
            format_=format_,
            name=name,
            preempt_mode=preempt_mode,
            with_deleted=with_deleted,
        )
    ).parsed
