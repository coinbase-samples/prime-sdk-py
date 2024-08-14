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

from dataclasses import dataclass
from base_response import BaseResponse
from client import Client
from typing import Optional, List
from datetime import datetime
from credentials import Credentials
from utils import PaginationParams, append_query_param, append_pagination_params


@dataclass
class ListActivitiesRequest:
    portfolio_id: str
    symbols: Optional[str] = None
    categories: Optional[str] = None
    statuses: Optional[str] = None
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    pagination: Optional[PaginationParams] = None
    allowed_status_codes: List[int] = None


@dataclass
class ListActivitiesResponse(BaseResponse):
    request: ListActivitiesRequest


class PrimeClient:
    def __init__(self, credentials: Credentials):
        self.client = Client(credentials)

    def list_activities(self, request: ListActivitiesRequest) -> ListActivitiesResponse:
        path = f"/portfolios/{request.portfolio_id}/activities"

        query_params = append_query_param("", 'symbols', request.symbols)
        query_params = append_query_param(query_params, 'categories', request.categories)
        query_params = append_query_param(query_params, 'statuses', request.statuses)

        if request.start_time:
            query_params = append_query_param(
                query_params,
                'start_time',
                request.start_time.isoformat() + 'Z')
        if request.end_time:
            query_params = append_query_param(
                query_params,
                'end_time',
                request.end_time.isoformat() + 'Z')

        query_params = append_pagination_params(query_params, request.pagination)

        response = self.client.request("GET", path, query=query_params,
                                       allowed_status_codes=request.allowed_status_codes)
        return ListActivitiesResponse(response.json(), request)
