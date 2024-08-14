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
from typing import Optional, List
from base_response import BaseResponse
from client import Client
from credentials import Credentials
from utils import PaginationParams, append_query_param, append_pagination_params


@dataclass
class ListWeb3WalletBalancesRequest:
    portfolio_id: str
    wallet_id: str
    visibility_statuses: Optional[str] = None
    pagination: Optional[PaginationParams] = None
    allowed_status_codes: List[int] = None


@dataclass
class ListWeb3WalletBalancesResponse(BaseResponse):
    request: ListWeb3WalletBalancesRequest


class PrimeClient:
    def __init__(self, credentials: Credentials):
        self.client = Client(credentials)

    def list_web3_wallet_balances(self, request: ListWeb3WalletBalancesRequest) -> ListWeb3WalletBalancesResponse:
        path = f"/portfolios/{request.portfolio_id}/wallets/{request.wallet_id}/web3_balances"

        query_params = append_query_param("", 'visibility_statuses', request.visibility_statuses)
        query_params = append_pagination_params(query_params, request.pagination)

        response = self.client.request("GET", path, query=query_params,
                                       allowed_status_codes=request.allowed_status_codes)
        return ListWeb3WalletBalancesResponse(response.json(), request)
