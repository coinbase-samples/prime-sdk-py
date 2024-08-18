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
from typing import List
from credentials import Credentials


@dataclass
class CreateConversionRequest:
    portfolio_id: str
    wallet_id: str
    amount: str
    destination: str
    idempotency_key: str
    source_symbol: str
    destination_symbol: str
    allowed_status_codes: List[int] = None


@dataclass
class CreateConversionResponse(BaseResponse):
    request: CreateConversionRequest


class PrimeClient:
    def __init__(self, credentials: Credentials):
        self.client = Client(credentials)
        
    def create_conversion(self, request: CreateConversionRequest) -> CreateConversionResponse:
        path = f"/portfolios/{request.portfolio_id}/wallets/{request.wallet_id}/conversion"
        body = asdict(request)
        response = self.client.request("POST", path, body=body, allowed_status_codes=request.allowed_status_codes)
        return CreateConversionResponse(response.json(), request)
