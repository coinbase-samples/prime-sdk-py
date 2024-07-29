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
from typing import Any, Dict, Optional
from datetime import datetime
from client import Client
from utils import PaginationParams, append_query_param, append_pagination_params
import json


@dataclass
class ListPortfolioAllocationsRequest:
    portfolio_id: str
    product_ids: Optional[str] = None
    order_side: Optional[str] = None
    start_date: datetime = None
    end_date: Optional[datetime] = None
    pagination: Optional[PaginationParams] = None

    def to_json(self) -> Dict[str, Any]:
        return {
            "portfolio_id": self.portfolio_id,
            "product_ids": self.product_ids,
            "order_side": self.order_side,
            "start_date": self.start_date.isoformat() +
            'Z' if self.start_date else None,
            "end_date": self.end_date.isoformat() +
            'Z' if self.end_date else None,
            "pagination_params": self.pagination.to_dict() if self.pagination else None}


@dataclass
class ListPortfolioAllocationsResponse:
    response: Dict[str, Any]
    request: ListPortfolioAllocationsRequest

    def __str__(self) -> str:
        return json.dumps({"response": self.response,
                          "request": self.request.to_json()}, indent=4)


def list_portfolio_allocations(
        client: Client,
        request: ListPortfolioAllocationsRequest) -> ListPortfolioAllocationsResponse:
    path = f"/portfolios/{request.portfolio_id}/allocations"

    query_params = ""
    query_params = append_query_param(query_params, 'product_ids', request.product_ids)
    query_params = append_query_param(query_params, 'order_side', request.order_side)

    if request.start_date:
        query_params = append_query_param(query_params, 'start_date', request.start_date.isoformat() + 'Z')
    if request.end_date:
        query_params = append_query_param(query_params, 'end_date', request.end_date.isoformat() + 'Z')

    query_params = append_pagination_params(query_params, request.pagination)

    response = client.request("GET", path, query=query_params)
    return ListPortfolioAllocationsResponse(response.json(), request)
