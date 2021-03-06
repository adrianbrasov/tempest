# Copyright 2018 ZTE Corporation.  All rights reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from tempest.lib.api_schema.response.compute.v2_1 import parameter_types

list_extensions = {
    'status_code': [200],
    'response_body': {
        'type': 'object',
        'properties': {
            'extensions': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'updated': parameter_types.date_time,
                        'description': {'type': 'string'},
                        'links': {'type': 'array'},
                        'namespace': {'type': 'string'},
                        'alias': {'type': 'string'},
                        'name': {'type': 'string'}
                    },
                    'additionalProperties': False,
                    'required': ['updated', 'links', 'alias', 'name',
                                 'description']
                }
            }
        },
        'additionalProperties': False,
        'required': ['extensions'],
    }
}
