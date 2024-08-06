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
from typing import Any, Dict, Optional
from credentials import Credentials


@dataclass
class CreateOrderPreviewRequest:
    portfolio_id: str
    side: str
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

    def to_dict(self) -> Dict[str, Any]:
        result = asdict(self)
        return {k: v for k, v in result.items() if v is not None}


@dataclass
class CreateOrderPreviewResponse(BaseResponse):
    request: CreateOrderPreviewRequest


class PrimeClient:
    def __init__(self, credentials: Credentials):
        self.client = Client(credentials)
        
    def create_order_preview(self, request: CreateOrderPreviewRequest) -> CreateOrderPreviewResponse:
        path = f"/portfolios/{request.portfolio_id}/order_preview"
        body = request.to_dict()
        response = self.client.request("POST", path, body=body)
        return CreateOrderPreviewResponse(response.json(), request)
