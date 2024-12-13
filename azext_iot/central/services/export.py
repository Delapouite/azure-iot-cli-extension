# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
from typing import List, Union
from knack.log import get_logger

from azure.cli.core.azclierror import AzureResponseError
from azext_iot.constants import CENTRAL_ENDPOINT
from azext_iot.central.models.v2022_06_30_preview import ExportPreview
from azext_iot.central.services import _utility
from azext_iot.central.common import API_VERSION_PREVIEW

logger = get_logger(__name__)

BASE_PATH = "api/dataExport/exports"


def add_export(
    cmd,
    app_id: str,
    export_id: str,
    payload: str,
    token: str,
    api_version=API_VERSION_PREVIEW,
    central_dns_suffix=CENTRAL_ENDPOINT,
) -> Union[dict, ExportPreview]:
    """
    Add and data export to IoT Central app

    Args:
        cmd: command passed into az
        app_id: name of app (used for forming request URL)
        export_id: unique identifier for export
        payload: export definition in JSON
        token: (OPTIONAL) authorization token to fetch device details from IoTC.
            MUST INCLUDE type (e.g. 'SharedAccessToken ...', 'Bearer ...')
        central_dns_suffix: {centralDnsSuffixInPath} as found in docs

    Returns:
        Export
    """
    api_version = API_VERSION_PREVIEW

    url = "https://{}.{}/{}/{}".format(app_id, central_dns_suffix, BASE_PATH, export_id)

    return _utility.make_api_call(
        cmd,
        app_id,
        method="PUT",
        url=url,
        payload=payload,
        token=token,
        api_version=api_version,
        central_dnx_suffix=central_dns_suffix,
    )


def update_export(
    cmd,
    app_id: str,
    export_id: str,
    payload: str,
    token: str,
    api_version=API_VERSION_PREVIEW,
    central_dns_suffix=CENTRAL_ENDPOINT,
) -> Union[dict, ExportPreview]:
    """
    Update and data export in IoT Central app

    Args:
        cmd: command passed into az
        app_id: name of app (used for forming request URL)
        export_id: unique identifier for export
        payload: export definition in JSON
        token: (OPTIONAL) authorization token to fetch device details from IoTC.
            MUST INCLUDE type (e.g. 'SharedAccessToken ...', 'Bearer ...')
        central_dns_suffix: {centralDnsSuffixInPath} as found in docs

    Returns:
        Export
    """
    api_version = API_VERSION_PREVIEW

    url = "https://{}.{}/{}/{}".format(app_id, central_dns_suffix, BASE_PATH, export_id)

    return _utility.make_api_call(
        cmd,
        app_id,
        method="PATCH",
        url=url,
        payload=payload,
        token=token,
        api_version=api_version,
        central_dnx_suffix=central_dns_suffix,
    )


def list_exports(
    cmd,
    app_id: str,
    token: str,
    max_pages=0,
    api_version=API_VERSION_PREVIEW,
    central_dns_suffix=CENTRAL_ENDPOINT,
) -> List[Union[dict, ExportPreview]]:
    """
    Get the list of exports for a central app.

    Args:
        cmd: command passed into az
        app_id: name of app (used for forming request URL)
        max_pages: max return result pages
        token: (OPTIONAL) authorization token to fetch device details from IoTC.
            MUST INCLUDE type (e.g. 'SharedAccessToken ...', 'Bearer ...')
        central_dns_suffix: {centralDnsSuffixInPath} as found in docs

    Returns:
        List of Export
    """
    api_version = API_VERSION_PREVIEW

    exports = []

    url = "https://{}.{}/{}".format(app_id, central_dns_suffix, BASE_PATH)
    pages_processed = 0
    while (max_pages == 0 or pages_processed < max_pages) and url:
        result = _utility.make_api_call(
            cmd,
            app_id,
            method="GET",
            url=url,
            payload=None,
            token=token,
            api_version=api_version,
            central_dnx_suffix=central_dns_suffix,
        )

        if "value" not in result:
            raise AzureResponseError("Value is not present in body: {}".format(result))

        exports.extend(result.get("value", []))

        url = result.get("nextLink", None)
        pages_processed = pages_processed + 1

    return exports


def get_export(
    cmd,
    app_id: str,
    export_id: str,
    token: str,
    api_version=API_VERSION_PREVIEW,
    central_dns_suffix=CENTRAL_ENDPOINT,
) -> Union[dict, ExportPreview]:
    """
    Get information about a specified export.

    Args:
        cmd: command passed into az
        app_id: name of app (used for forming request URL)
        export_id: unique identifier for export
        token: (OPTIONAL) authorization token to fetch device details from IoTC.
            MUST INCLUDE type (e.g. 'SharedAccessToken ...', 'Bearer ...')
        central_dns_suffix: {centralDnsSuffixInPath} as found in docs

    Returns:
        Export
    """
    api_version = API_VERSION_PREVIEW

    url = "https://{}.{}/{}/{}".format(app_id, central_dns_suffix, BASE_PATH, export_id)

    return _utility.make_api_call(
        cmd,
        app_id,
        method="GET",
        url=url,
        payload=None,
        token=token,
        api_version=api_version,
        central_dnx_suffix=central_dns_suffix,
    )


def delete_export(
    cmd,
    app_id: str,
    export_id: str,
    token: str,
    api_version=API_VERSION_PREVIEW,
    central_dns_suffix=CENTRAL_ENDPOINT,
) -> dict:
    """
    Delete data export export from Central app.

    Args:
        cmd: command passed into az
        app_id: name of app (used for forming request URL)
        export_id: unique identifier for export
        token: (OPTIONAL) authorization token to fetch device details from IoTC.
            MUST INCLUDE type (e.g. 'SharedAccessToken ...', 'Bearer ...')
        central_dns_suffix: {centralDnsSuffixInPath} as found in docs

    Returns:
        Response dict
    """
    api_version = API_VERSION_PREVIEW

    url = "https://{}.{}/{}/{}".format(app_id, central_dns_suffix, BASE_PATH, export_id)

    return _utility.make_api_call(
        cmd,
        app_id,
        method="DELETE",
        url=url,
        payload=None,
        token=token,
        api_version=api_version,
        central_dnx_suffix=central_dns_suffix,
    )
