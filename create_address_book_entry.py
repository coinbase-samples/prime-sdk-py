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
class CreateAddressBookEntryRequest:
    portfolio_id: str
    address: str
    currency_symbol: str
    name: str
    account_identifier: Optional[str] = None

    def to_json(self) -> Dict[str, Any]:
        return {
            "portfolio_id": self.portfolio_id,
            "address": self.address,
            "currency_symbol": self.currency_symbol,
            "name": self.name,
            "account_identifier": self.account_identifier or None
        }


@dataclass
class CreateAddressBookEntryResponse:
    response: Dict[str, Any]
    request: CreateAddressBookEntryRequest

    def __str__(self) -> str:
        return json.dumps({"response": self.response,
                          "request": self.request.to_json()}, indent=4)


def create_address_book_entry(
        client: Client,
        request: CreateAddressBookEntryRequest) -> CreateAddressBookEntryResponse:
    path = f"/portfolios/{request.portfolio_id}/address_book"
    body = request.to_json()
    response = client.request("POST", path, body=body)
    return CreateAddressBookEntryResponse(response.json(), request)
