# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .external_resource_py3 import ExternalResource


class IntegrationResource(ExternalResource):
    """IoTHub integration resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The resource identifier.
    :vartype id: str
    :ivar name: Extension resource name.
    :vartype name: str
    :ivar type: The resource type.
    :vartype type: str
    :ivar provisioning_state: DigitalTwinsInstance - IoTHub link state.
     Possible values include: 'Provisioning', 'Deleting', 'Succeeded',
     'Failed', 'Canceled'
    :vartype provisioning_state: str or
     ~digitaltwins-arm.models.IntegrationResourceState
    :param resource_id: Fully qualified resource identifier of the
     DigitalTwins Azure resource.
    :type resource_id: str
    :ivar created_time: Time when the IoTHub was added to
     DigitalTwinsInstance.
    :vartype created_time: datetime
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True, 'pattern': r'^(?![0-9]+$)(?!-)[a-zA-Z0-9-]{2,49}[a-zA-Z0-9]$'},
        'type': {'readonly': True},
        'provisioning_state': {'readonly': True},
        'created_time': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'resource_id': {'key': 'properties.resourceId', 'type': 'str'},
        'created_time': {'key': 'properties.createdTime', 'type': 'iso-8601'},
    }

    def __init__(self, *, resource_id: str=None, **kwargs) -> None:
        super(IntegrationResource, self).__init__(**kwargs)
        self.provisioning_state = None
        self.resource_id = resource_id
        self.created_time = None
