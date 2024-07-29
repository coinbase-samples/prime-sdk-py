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
from utils import PaginationParams, create_pagination_query_params
import json


class ListProductsRequest:
    def __init__(self, portfolio_id: str,
                 pagination: Optional[PaginationParams] = None):
        self.portfolio_id = portfolio_id
        self.pagination = pagination

    def to_json(self) -> Dict[str, Any]:
        return {
            "portfolio_id": self.portfolio_id,
            "pagination_params": self.pagination.to_dict() if self.pagination else None
        }


class ListProductsResponse:
    def __init__(self, data: Dict[str, Any], request: ListProductsRequest):
        self.response = data
        self.request = request

    def __str__(self):
        return json.dumps({"response": self.response,
                          "request": self.request.to_json()}, indent=4)


def list_products(client: Client,
                  request: ListProductsRequest) -> ListProductsResponse:
    base_path = f"/portfolios/{request.portfolio_id}/products"

    query_string = create_pagination_query_params(request.pagination)
    response = client.request("GET", base_path, query=query_string)
    return ListProductsResponse(response.json(), request)
