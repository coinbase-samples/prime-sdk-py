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
from typing import Any, Dict

from base_response import BaseResponse
from client import Client


@dataclass
class GetPortfolioRequest:
    portfolio_id: str

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class GetPortfolioResponse(BaseResponse):
    request: GetPortfolioRequest


def get_portfolio(client: Client,
                  request: GetPortfolioRequest) -> GetPortfolioResponse:
    path = f"/portfolios/{request.portfolio_id}"
    response = client.request("GET", path, query=None)
    return GetPortfolioResponse(response.json(), request)
