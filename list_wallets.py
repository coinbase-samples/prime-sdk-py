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
from credentials import Credentials
from utils import PaginationParams, append_query_param, append_pagination_params


@dataclass
class ListWalletsRequest:
    portfolio_id: str
    type: str = None
    symbols: Optional[str] = None
    pagination: Optional[PaginationParams] = None
    allowed_status_codes: List[int] = None

    def to_dict(self) -> Dict[str, Any]:
        result = asdict(self)
        if self.pagination:
            result['pagination_params'] = self.pagination.to_dict()
        return {k: v for k, v in result.items() if v is not None}


@dataclass
class ListWalletsResponse(BaseResponse):
    request: ListWalletsRequest


class PrimeClient:
    def __init__(self, credentials: Credentials):
        self.client = Client(credentials)

    def list_wallets(self, request: ListWalletsRequest) -> ListWalletsResponse:
        path = f"/portfolios/{request.portfolio_id}/wallets"

        query_params = append_query_param("", 'symbols', request.symbols)
        query_params = append_query_param(query_params, 'type', request.type)
        query_params = append_pagination_params(query_params, request.pagination)

        response = self.client.request("GET", path, query=query_params,
                                       allowed_status_codes=request.allowed_status_codes)
        return ListWalletsResponse(response.json(), request)
