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
from typing import Optional, Dict, Any
from datetime import datetime
import json
from client import Client
from utils import PaginationParams, append_query_param, append_pagination_params


@dataclass
class ListPortfolioTransactionsRequest:
    portfolio_id: str
    symbols: Optional[str] = None
    types: Optional[str] = None
    start: Optional[datetime] = None
    end: Optional[datetime] = None
    pagination: Optional[PaginationParams] = None

    def to_json(self) -> Dict[str, Any]:
        return {
            "portfolio_id": self.portfolio_id,
            "symbols": self.symbols,
            "types": self.types,
            "start_time": self.start.isoformat() + 'Z' if self.start else None,
            "end_time": self.end.isoformat() + 'Z' if self.end else None,
            "pagination_params": self.pagination.to_dict() if self.pagination else None}


@dataclass
class ListPortfolioTransactionsResponse:
    response: Dict[str, Any]
    request: ListPortfolioTransactionsRequest

    def __str__(self) -> str:
        return json.dumps({"response": self.response,
                          "request": self.request.to_json()}, indent=4)


def list_portfolio_transactions(
        client: Client,
        request: ListPortfolioTransactionsRequest) -> ListPortfolioTransactionsResponse:
    path = f"/portfolios/{request.portfolio_id}/transactions"

    query_params = ""
    query_params = append_query_param(query_params, 'symbols', request.symbols)
    query_params = append_query_param(query_params, 'types', request.types)

    if request.start:
        query_params = append_query_param(query_params, 'start_time', request.start.isoformat() + 'Z')
    if request.end:
        query_params = append_query_param(query_params, 'end_time', request.end.isoformat() + 'Z')

    query_params = append_pagination_params(query_params, request.pagination)

    response = client.request("GET", path, query=query_params)
    return ListPortfolioTransactionsResponse(response.json(), request)
