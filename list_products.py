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
from utils import PaginationParams, append_pagination_params
import json


@dataclass
class ListProductsRequest:
    portfolio_id: str
    pagination: Optional[PaginationParams] = None

    def to_json(self) -> Dict[str, Any]:
        return {
            "portfolio_id": self.portfolio_id,
            "pagination_params": self.pagination.to_dict() if self.pagination else None}


@dataclass
class ListProductsResponse:
    response: Dict[str, Any]
    request: ListProductsRequest

    def __str__(self) -> str:
        return json.dumps({"response": self.response,
                          "request": self.request.to_json()}, indent=4)


def list_products(client: Client,
                  request: ListProductsRequest) -> ListProductsResponse:
    path = f"/portfolios/{request.portfolio_id}/products"

    query_params = append_pagination_params("", request.pagination)
    response = client.request("GET", path, query=query_params)
    return ListProductsResponse(response.json(), request)
