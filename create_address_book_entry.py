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
from typing import Any, Dict, Optional, List
from credentials import Credentials


@dataclass
class CreateAddressBookEntryRequest:
    portfolio_id: str
    address: str
    currency_symbol: str
    name: str
    account_identifier: Optional[str] = None
    allowed_status_codes: List[int] = None

    def to_dict(self) -> Dict[str, Any]:
        result = asdict(self)
        return {k: v for k, v in result.items() if v is not None}


@dataclass
class CreateAddressBookEntryResponse(BaseResponse):
    request: CreateAddressBookEntryRequest


class PrimeClient:
    def __init__(self, credentials: Credentials):
        self.client = Client(credentials)
        
    def create_address_book_entry(self, request: CreateAddressBookEntryRequest) -> CreateAddressBookEntryResponse:
        path = f"/portfolios/{request.portfolio_id}/address_book"
        body = request.to_dict()
        response = self.client.request("POST", path, body=body, allowed_status_codes=request.allowed_status_codes)
        return CreateAddressBookEntryResponse(response.json(), request)
