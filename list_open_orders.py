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

from dataclasses import dataclass, asdict
from base_response import BaseResponse
from client import Client
from typing import Optional, Dict, Any, List
from datetime import datetime
from credentials import Credentials
from utils import append_query_param


@dataclass
class ListOpenOrdersRequest:
    portfolio_id: str
    order_statuses: Optional[str] = None
    product_ids: Optional[str] = None
    order_type: Optional[str] = None
    order_side: Optional[str] = None
    start_date: datetime = None
    end_date: Optional[datetime] = None
    allowed_status_codes: List[int] = None

    def to_dict(self) -> Dict[str, Any]:
        result = asdict(self)
        if self.start_date:
            result['start_date'] = self.start_date.isoformat() + 'Z'
        if self.end_date:
            result['end_date'] = self.end_date.isoformat() + 'Z'
        return {k: v for k, v in result.items() if v is not None}


@dataclass
class ListOpenOrdersResponse(BaseResponse):
    request: ListOpenOrdersRequest


class PrimeClient:
    def __init__(self, credentials: Credentials):
        self.client = Client(credentials)

    def list_open_orders(self, request: ListOpenOrdersRequest) -> ListOpenOrdersResponse:
        path = f"/portfolios/{request.portfolio_id}/open_orders"

        query_params = append_query_param("", 'product_ids', request.product_ids)
        query_params = append_query_param(query_params, 'order_type', request.order_type)
        query_params = append_query_param(query_params, 'order_side', request.order_side)

        if request.start_date:
            query_params = append_query_param(
                query_params,
                'start_date',
                request.start_date.isoformat() + 'Z')
        if request.end_date:
            query_params = append_query_param(
                query_params,
                'end_date',
                request.end_date.isoformat() + 'Z')

        response = self.client.request("GET", path, query=query_params,
                                       allowed_status_codes=request.allowed_status_codes)
        return ListOpenOrdersResponse(response.json(), request)
