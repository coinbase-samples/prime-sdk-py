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
from client import Client
from utils import PaginationParams
import utils
import json


class GetAddressBookRequest:
    def __init__(self,
                 portfolio_id: str,
                 currency_symbol: Optional[str] = None,
                 search: Optional[str] = None,
                 pagination: Optional[PaginationParams] = None):
        self.portfolio_id = portfolio_id
        self.currency_symbol = currency_symbol
        self.search = search
        self.pagination = pagination

    def to_json(self) -> Dict[str, Any]:
        return {
            "portfolio_id": self.portfolio_id,
            "currency_symbol": self.currency_symbol,
            "search": self.search,
            "pagination_params": self.pagination.to_dict() if self.pagination else None
        }


class GetAddressBookResponse:
    def __init__(self, data: Dict[str, Any], request: GetAddressBookRequest):
        self.response = data
        self.request = request

    def __str__(self):
        return json.dumps({"response": self.response,
                          "request": self.request.to_json()}, indent=4)


def get_address_book(client: Client,
                     request: GetAddressBookRequest) -> GetAddressBookResponse:
    path = f"/portfolios/{request.portfolio_id}/address_book"

    query_params = []
    utils.append_query_param(
        query_params,
        'currency_symbol',
        request.currency_symbol)
    utils.append_query_param(query_params, 'search', request.search)

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
    return GetAddressBookResponse(response.json(), request)
