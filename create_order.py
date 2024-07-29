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
from client import Client
from typing import Any, Dict, Optional
import json


@dataclass
class CreateOrderRequest:
    portfolio_id: str
    side: str
    client_order_id: str
    product_id: str
    type: str
    base_quantity: Optional[str] = None
    quote_value: Optional[str] = None
    limit_price: Optional[str] = None
    start_time: Optional[str] = None
    expiry_time: Optional[str] = None
    time_in_force: Optional[str] = None
    stp_id: Optional[str] = None
    display_quote_size: Optional[str] = None
    display_base_size: Optional[str] = None
    is_raise_exact: Optional[str] = None
    historical_pov: Optional[str] = None

    def to_json(self) -> Dict[str, Any]:
        return {
            "portfolio_id": self.portfolio_id,
            "side": self.side,
            "client_order_id": self.client_order_id,
            "product_id": self.product_id,
            "type": self.type,
            "base_quantity": self.base_quantity or None,
            "quote_value": self.quote_value or None,
            "limit_price": self.limit_price or None,
            "start_time": self.start_time or None,
            "expiry_time": self.expiry_time or None,
            "time_in_force": self.time_in_force or None,
            "stp_id": self.stp_id or None,
            "display_quote_size": self.display_quote_size or None,
            "display_base_size": self.display_base_size or None,
            "is_raise_exact": self.is_raise_exact or None,
            "historical_pov": self.historical_pov or None
        }


@dataclass
class CreateOrderResponse:
    response: Dict[str, Any]
    request: CreateOrderRequest

    def __str__(self) -> str:
        return json.dumps({"response": self.response,
                          "request": self.request.to_json()}, indent=4)


def create_order(client: Client,
                 request: CreateOrderRequest) -> CreateOrderResponse:
    path = f"/portfolios/{request.portfolio_id}/order"
    body = request.to_json()
    response = client.request("POST", path, body=body)
    return CreateOrderResponse(response.json(), request)
