# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.log import get_logger
from knack.util import CLIError
from typing import List
from azext_iot.central.models.enum import ApiVersion
from azext_iot.constants import CENTRAL_ENDPOINT
from azext_iot.central import services as central_services


logger = get_logger(__name__)


class CentralUserProvider:
    def __init__(self, cmd, app_id: str, api_version: str, token=None):
        """
        Provider for device APIs

        Args:
            cmd: command passed into az
            app_id: name of app (used for forming request URL)
            api_version: API version (appendend to request URL)
            token: (OPTIONAL) authorization token to fetch device details from IoTC.
                MUST INCLUDE type (e.g. 'SharedAccessToken ...', 'Bearer ...')
                Useful in scenarios where user doesn't own the app
                therefore AAD token won't work, but a SAS token generated by owner will
        """
        self._cmd = cmd
        self._app_id = app_id
        self._token = token
        self._api_version = api_version

    def add_service_principal(
        self,
        assignee: str,
        tenant_id: str,
        object_id: str,
        role: str,
        org_id: str,
        central_dns_suffix=CENTRAL_ENDPOINT,
    ) -> central_services.user.User:
        if not tenant_id:
            raise CLIError("Must specify --tenant-id when adding a service principal")

        if not object_id:
            raise CLIError("Must specify --object-id when adding a service principal")

        if org_id and self._api_version == ApiVersion.v1_1_preview.value:
            roles = rf"{org_id}\{role}"
        else:
            roles = role

        return central_services.user.add_or_update_service_principal_user(
            cmd=self._cmd,
            app_id=self._app_id,
            assignee=assignee,
            tenant_id=tenant_id,
            object_id=object_id,
            roles=roles,
            token=self._token,
            central_dns_suffix=central_dns_suffix,
            api_version=self._api_version,
        )

    def update_service_principal(
        self,
        assignee: str,
        tenant_id: str,
        object_id: str,
        roles: str,
        central_dns_suffix=CENTRAL_ENDPOINT,
    ) -> central_services.user.User:
        if not tenant_id:
            raise CLIError("Must specify --tenant-id when adding a service principal")

        if not object_id:
            raise CLIError("Must specify --object-id when adding a service principal")

        return central_services.user.add_or_update_service_principal_user(
            cmd=self._cmd,
            app_id=self._app_id,
            assignee=assignee,
            tenant_id=tenant_id,
            object_id=object_id,
            roles=roles,
            token=self._token,
            update=True,
            central_dns_suffix=central_dns_suffix,
            api_version=self._api_version,
        )

    def get_user_list(
        self,
        central_dns_suffix=CENTRAL_ENDPOINT,
    ) -> List[central_services.user.User]:
        return central_services.user.get_user_list(
            cmd=self._cmd,
            app_id=self._app_id,
            token=self._token,
            central_dns_suffix=central_dns_suffix,
            api_version=self._api_version,
        )

    def get_user(
        self,
        assignee,
        central_dns_suffix=CENTRAL_ENDPOINT,
    ) -> central_services.user.User:
        return central_services.user.get_user(
            cmd=self._cmd,
            app_id=self._app_id,
            assignee=assignee,
            token=self._token,
            central_dns_suffix=central_dns_suffix,
            api_version=self._api_version,
        )

    def delete_user(
        self,
        assignee,
        central_dns_suffix=CENTRAL_ENDPOINT,
    ) -> dict:
        return central_services.user.delete_user(
            cmd=self._cmd,
            app_id=self._app_id,
            assignee=assignee,
            token=self._token,
            central_dns_suffix=central_dns_suffix,
            api_version=self._api_version,
        )

    def add_email(
        self,
        assignee: str,
        email: str,
        role: str,
        org_id: str,
        central_dns_suffix=CENTRAL_ENDPOINT,
    ) -> central_services.user.User:
        if not email:
            raise CLIError("Must specify --email when adding a user by email")

        if org_id and self._api_version == ApiVersion.v1_1_preview.value:
            roles = rf"{org_id}\{role}"
        else:
            roles = role

        return central_services.user.add_or_update_email_user(
            cmd=self._cmd,
            app_id=self._app_id,
            assignee=assignee,
            email=email,
            roles=roles,
            token=self._token,
            central_dns_suffix=central_dns_suffix,
            api_version=self._api_version,
        )

    def update_email_user(
        self,
        assignee: str,
        email: str,
        roles: str,
        central_dns_suffix=CENTRAL_ENDPOINT,
    ) -> central_services.user.User:
        if not email:
            raise CLIError("Must specify --email when adding a user by email")

        return central_services.user.add_or_update_email_user(
            cmd=self._cmd,
            app_id=self._app_id,
            assignee=assignee,
            email=email,
            roles=roles,
            update=True,
            token=self._token,
            central_dns_suffix=central_dns_suffix,
            api_version=self._api_version,
        )
