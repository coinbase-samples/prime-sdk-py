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
import json
from client import Client
from utils import PaginationParams, append_query_param, append_pagination_params


@dataclass
class ListWeb3WalletBalancesRequest:
    portfolio_id: str
    wallet_id: str
    visibility_statuses: Optional[str] = None
    pagination: Optional[PaginationParams] = None

    def to_json(self) -> Dict[str, Any]:
        return {
            "portfolio_id": self.portfolio_id,
            "wallet_id": self.wallet_id,
            "visibility_statuses": self.visibility_statuses,
            "pagination_params": self.pagination.to_dict() if self.pagination else None}


@dataclass
class ListWeb3WalletBalancesResponse:
    response: Dict[str, Any]
    request: ListWeb3WalletBalancesRequest

    def __str__(self) -> str:
        return json.dumps({"response": self.response,
                          "request": self.request.to_json()}, indent=4)


def list_web3_wallet_balances(
        client: Client,
        request: ListWeb3WalletBalancesRequest) -> ListWeb3WalletBalancesResponse:
    path = f"/portfolios/{request.portfolio_id}/wallets/{request.wallet_id}/web3_balances"

    query_params = ""
    query_params = append_query_param(query_params, 'visibility_statuses', request.visibility_statuses)
    query_params = append_pagination_params(query_params, request.pagination)

    response = client.request("GET", path, query=query_params)
    return ListWeb3WalletBalancesResponse(response.json(), request)
