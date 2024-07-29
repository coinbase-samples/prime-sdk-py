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

from typing import Optional, Dict, Any
import json

import utils
from client import Client
from utils import PaginationParams


class ListWeb3WalletBalancesRequest:
    def __init__(self,
                 portfolio_id: str,
                 wallet_id: str,
                 visibility_statuses: Optional[str] = None,
                 pagination: Optional[PaginationParams] = None):
        self.portfolio_id = portfolio_id
        self.pagination = pagination
        self.wallet_id = wallet_id
        self.visibility_statuses = visibility_statuses

    def to_json(self) -> Dict[str, Any]:
        return {
            "portfolio_id": self.portfolio_id,
            "wallet_id": self.wallet_id,
            "visibility_statuses": self.visibility_statuses,
            "pagination_params": self.pagination.to_dict() if self.pagination else None
        }


class ListWeb3WalletBalancesResponse:
    def __init__(self, data: Dict[str, Any],
                 request: ListWeb3WalletBalancesRequest):
        self.response = data
        self.request = request

    def __str__(self):
        return json.dumps({"response": self.response,
                          "request": self.request.to_json()}, indent=4)


def list_web3_wallet_balances(
        client: Client, request: ListWeb3WalletBalancesRequest) -> ListWeb3WalletBalancesResponse:
    path = f"/portfolios/{request.portfolio_id}/wallets/{request.wallet_id}/web3_balances"

    query_params = []
    utils.append_query_param(
        query_params,
        'visibility_statuses',
        request.visibility_statuses)

    if request.pagination:
        if request.pagination.cursor:
            utils.append_query_param(
                query_params, 'cursor', request.pagination.cursor)
        if request.pagination.limit:
            utils.append_query_param(
                query_params, 'limit', request.pagination.limit)

    query_string = "&".join(query_params)

    response = client.request("GET", path, query=query_string)
    return ListWeb3WalletBalancesResponse(response.json(), request)
