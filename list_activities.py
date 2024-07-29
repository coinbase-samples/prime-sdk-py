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

from typing import Any, Dict, Optional
from datetime import datetime
from client import Client
from utils import PaginationParams
import utils
import json


class ListActivitiesRequest:
    def __init__(self,
                 portfolio_id: str,
                 symbols: Optional[str] = None,
                 categories: Optional[str] = None,
                 statuses: Optional[str] = None,
                 start_time: Optional[datetime] = None,
                 end_time: Optional[datetime] = None,
                 pagination: Optional[PaginationParams] = None):
        self.portfolio_id = portfolio_id
        self.symbols = symbols
        self.categories = categories
        self.statuses = statuses
        self.start_time = start_time
        self.end_time = end_time
        self.pagination = pagination

    def to_json(self) -> Dict[str, Any]:
        return {
            "portfolio_id": self.portfolio_id,
            "symbols": self.symbols,
            "categories": self.categories,
            "statuses": self.statuses,
            "start_time": self.start_time.isoformat() + 'Z' if self.start_time else None,
            "end_time": self.end_time.isoformat() + 'Z' if self.end_time else None,
            "pagination_params": self.pagination.to_dict() if self.pagination else None
        }


class ListActivitiesResponse:
    def __init__(self, data: Dict[str, Any], request: ListActivitiesRequest):
        self.response = data
        self.request = request

    def __str__(self):
        return json.dumps({"response": self.response,
                          "request": self.request.to_json()}, indent=4)


def list_activities(client: Client,
                    request: ListActivitiesRequest) -> ListActivitiesResponse:
    path = f"/portfolios/{request.portfolio_id}/activities"

    query_params = []
    utils.append_query_param(query_params, 'symbols', request.symbols)
    utils.append_query_param(query_params, 'categories', request.categories)
    utils.append_query_param(query_params, 'statuses', request.statuses)

    if request.start_time:
        utils.append_query_param(
            query_params,
            'start_time',
            request.start_time.isoformat() + 'Z')
    if request.end_time:
        utils.append_query_param(
            query_params,
            'end_time',
            request.end_time.isoformat() + 'Z')

    if request.pagination:
        if request.pagination.cursor:
            utils.append_query_param(
                query_params, 'cursor', request.pagination.cursor)
        if request.pagination.limit:
            utils.append_query_param(
                query_params, 'limit', request.pagination.limit)
        if request.pagination.sort_direction:
            utils.append_query_param(
                query_params,
                'sort_direction',
                request.pagination.sort_direction)

    query_string = "&".join(query_params)

    response = client.request("GET", path, query=query_string)
    return ListActivitiesResponse(response.json(), request)
