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

from typing import Optional, List, Dict, Any, Union
from datetime import datetime
import json

import utils
from client import Client
from utils import PaginationParams


class ListWalletsRequest:
    def __init__(self,
                 portfolio_id: str,
                 type: str = None,
                 symbols: Optional[str] = None,
                 pagination: Optional[PaginationParams] = None):
        self.portfolio_id = portfolio_id
        self.symbols = symbols
        self.type = type
        self.pagination = pagination

    def to_json(self) -> Dict[str, Any]:
        return {
            "portfolio_id": self.portfolio_id,
            "symbols": self.symbols,
            "type": self.type,
            "pagination_params": self.pagination.to_dict() if self.pagination else None
        }


class ListWalletsResponse:
    def __init__(self, data: Dict[str, Any], request: ListWalletsRequest):
        self.response = data
        self.request = request

    def __str__(self):
        return json.dumps({"response": self.response,
                          "request": self.request.to_json()}, indent=4)


def list_wallets(client: Client,
                 request: ListWalletsRequest) -> ListWalletsResponse:
    path = f"/portfolios/{request.portfolio_id}/wallets"

    query_params = []
    utils.append_query_param(query_params, 'symbols', request.symbols)
    utils.append_query_param(query_params, 'type', request.type)

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
    return ListWalletsResponse(response.json(), request)
