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

from msrest.serialization import Model


class Target(Model):
    """Target class.

    :param subject_metadata: Gets or sets the subject meta data.
    :type subject_metadata: ~pnp.models.SubjectMetadata
    :param subject: Gets or sets the subject.
    :type subject: ~pnp.models.Subject
    """

    _attribute_map = {
        'subject_metadata': {'key': 'subjectMetadata', 'type': 'SubjectMetadata'},
        'subject': {'key': 'subject', 'type': 'Subject'},
    }

    def __init__(self, **kwargs):
        super(Target, self).__init__(**kwargs)
        self.subject_metadata = kwargs.get('subject_metadata', None)
        self.subject = kwargs.get('subject', None)
