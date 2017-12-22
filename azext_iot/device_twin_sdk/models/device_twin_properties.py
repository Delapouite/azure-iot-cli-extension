# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class DeviceTwinProperties(Model):
    """Type representing properties that are part of an IoT Hub device twin.

    :param version: Version of device twin properties.
    :type version: long
    :param properties: Properties JSON element.
    :type properties: dict
    :param metadata: Metadata information for the properties JSON document.
    :type metadata: :class:`Metadata <device_twin.models.Metadata>`
    """

    _attribute_map = {
        'version': {'key': 'Version', 'type': 'long'},
        'properties': {'key': 'Properties', 'type': '{object}'},
        'metadata': {'key': 'Metadata', 'type': 'Metadata'},
    }

    def __init__(self, version=None, properties=None, metadata=None):
        self.version = version
        self.properties = properties
        self.metadata = metadata