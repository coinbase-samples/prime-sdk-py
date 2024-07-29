# Copyright 2024-present Coinbase Global, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
#  limitations under the License.

import json
from typing import Optional, List, Union
from urllib.parse import urlencode


class PaginationParams:
    def __init__(self, cursor: str = '', limit: str = '',
                 sort_direction: str = ''):
        self.cursor = cursor
        self.limit = limit
        self.sort_direction = sort_direction

    def to_dict(self):
        return {
            "cursor": self.cursor,
            "limit": self.limit,
            "sort_direction": self.sort_direction
        }


def append_query_param(
        query_params: List[str], key: str, values: Optional[Union[List[str], str]]):
    if values:
        if isinstance(values, list):
            query_params.extend([f"{key}={value}" for value in values])
        else:
            query_params.append(f"{key}={values}")


def create_pagination_query_params(
        pagination: Optional[PaginationParams]) -> str:
    query_params = {}
    if pagination:
        if pagination.cursor:
            query_params['cursor'] = pagination.cursor
        if pagination.limit:
            query_params['limit'] = pagination.limit
        if pagination.sort_direction:
            query_params['sort_direction'] = pagination.sort_direction
    return urlencode(query_params)


def serialize_to_json(obj):
    data = {k: v for k, v in obj.__dict__.items() if not k.startswith('_')}
    return json.dumps(data, indent=4)
