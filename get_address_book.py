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
from client import Client
from utils import PaginationParams, append_query_param, append_pagination_params
import json


@dataclass
class GetAddressBookRequest:
    portfolio_id: str
    currency_symbol: Optional[str] = None
    search: Optional[str] = None
    pagination: Optional[PaginationParams] = None

    def to_json(self) -> Dict[str, Any]:
        return {
            "portfolio_id": self.portfolio_id,
            "currency_symbol": self.currency_symbol,
            "search": self.search,
            "pagination_params": self.pagination.to_dict() if self.pagination else None}


@dataclass
class GetAddressBookResponse:
    response: Dict[str, Any]
    request: GetAddressBookRequest

    def __str__(self) -> str:
        return json.dumps({"response": self.response,
                          "request": self.request.to_json()}, indent=4)


def get_address_book(client: Client,
                     request: GetAddressBookRequest) -> GetAddressBookResponse:
    path = f"/portfolios/{request.portfolio_id}/address_book"

    query_params = ""
    query_params = append_query_param(query_params, 'currency_symbol', request.currency_symbol)
    query_params = append_query_param(query_params, 'search', request.search)
    query_params = append_pagination_params(query_params, request.pagination)

    response = client.request("GET", path, query=query_params)
    return GetAddressBookResponse(response.json(), request)
