from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.slurmdb_v0044_post_qos_preempt_mode import SlurmdbV0044PostQosPreemptMode
from ...models.v0044_openapi_resp import V0044OpenapiResp
from ...models.v0044_openapi_slurmdbd_qos_resp import V0044OpenapiSlurmdbdQosResp
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: V0044OpenapiSlurmdbdQosResp | Unset = UNSET,
    description: str | Unset = UNSET,
    include_deleted_qos: str | Unset = UNSET,
    id: str | Unset = UNSET,
    format_: str | Unset = UNSET,
    name: str | Unset = UNSET,
    preempt_mode: SlurmdbV0044PostQosPreemptMode | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["description"] = description

    params["Include deleted QOS"] = include_deleted_qos

    params["id"] = id

    params["format"] = format_

    params["name"] = name

    json_preempt_mode: str | Unset = UNSET
    if not isinstance(preempt_mode, Unset):
        json_preempt_mode = preempt_mode.value

    params["preempt_mode"] = json_preempt_mode

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/slurmdb/v0.0.44/qos/",
        "params": params,
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> V0044OpenapiResp:
    if response.status_code == 200:
        response_200 = V0044OpenapiResp.from_dict(response.json())

        return response_200

    response_default = V0044OpenapiResp.from_dict(response.json())

    return response_default


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[V0044OpenapiResp]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: V0044OpenapiSlurmdbdQosResp | Unset = UNSET,
    description: str | Unset = UNSET,
    include_deleted_qos: str | Unset = UNSET,
    id: str | Unset = UNSET,
    format_: str | Unset = UNSET,
    name: str | Unset = UNSET,
    preempt_mode: SlurmdbV0044PostQosPreemptMode | Unset = UNSET,
) -> Response[V0044OpenapiResp]:
    """Add or update QOSs

    Args:
        description (str | Unset):
        include_deleted_qos (str | Unset):
        id (str | Unset):
        format_ (str | Unset):
        name (str | Unset):
        preempt_mode (SlurmdbV0044PostQosPreemptMode | Unset):
        body (V0044OpenapiSlurmdbdQosResp | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[V0044OpenapiResp]
    """

    kwargs = _get_kwargs(
        body=body,
        description=description,
        include_deleted_qos=include_deleted_qos,
        id=id,
        format_=format_,
        name=name,
        preempt_mode=preempt_mode,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: V0044OpenapiSlurmdbdQosResp | Unset = UNSET,
    description: str | Unset = UNSET,
    include_deleted_qos: str | Unset = UNSET,
    id: str | Unset = UNSET,
    format_: str | Unset = UNSET,
    name: str | Unset = UNSET,
    preempt_mode: SlurmdbV0044PostQosPreemptMode | Unset = UNSET,
) -> V0044OpenapiResp | None:
    """Add or update QOSs

    Args:
        description (str | Unset):
        include_deleted_qos (str | Unset):
        id (str | Unset):
        format_ (str | Unset):
        name (str | Unset):
        preempt_mode (SlurmdbV0044PostQosPreemptMode | Unset):
        body (V0044OpenapiSlurmdbdQosResp | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        V0044OpenapiResp
    """

    return sync_detailed(
        client=client,
        body=body,
        description=description,
        include_deleted_qos=include_deleted_qos,
        id=id,
        format_=format_,
        name=name,
        preempt_mode=preempt_mode,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: V0044OpenapiSlurmdbdQosResp | Unset = UNSET,
    description: str | Unset = UNSET,
    include_deleted_qos: str | Unset = UNSET,
    id: str | Unset = UNSET,
    format_: str | Unset = UNSET,
    name: str | Unset = UNSET,
    preempt_mode: SlurmdbV0044PostQosPreemptMode | Unset = UNSET,
) -> Response[V0044OpenapiResp]:
    """Add or update QOSs

    Args:
        description (str | Unset):
        include_deleted_qos (str | Unset):
        id (str | Unset):
        format_ (str | Unset):
        name (str | Unset):
        preempt_mode (SlurmdbV0044PostQosPreemptMode | Unset):
        body (V0044OpenapiSlurmdbdQosResp | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[V0044OpenapiResp]
    """

    kwargs = _get_kwargs(
        body=body,
        description=description,
        include_deleted_qos=include_deleted_qos,
        id=id,
        format_=format_,
        name=name,
        preempt_mode=preempt_mode,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: V0044OpenapiSlurmdbdQosResp | Unset = UNSET,
    description: str | Unset = UNSET,
    include_deleted_qos: str | Unset = UNSET,
    id: str | Unset = UNSET,
    format_: str | Unset = UNSET,
    name: str | Unset = UNSET,
    preempt_mode: SlurmdbV0044PostQosPreemptMode | Unset = UNSET,
) -> V0044OpenapiResp | None:
    """Add or update QOSs

    Args:
        description (str | Unset):
        include_deleted_qos (str | Unset):
        id (str | Unset):
        format_ (str | Unset):
        name (str | Unset):
        preempt_mode (SlurmdbV0044PostQosPreemptMode | Unset):
        body (V0044OpenapiSlurmdbdQosResp | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        V0044OpenapiResp
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            description=description,
            include_deleted_qos=include_deleted_qos,
            id=id,
            format_=format_,
            name=name,
            preempt_mode=preempt_mode,
        )
    ).parsed
