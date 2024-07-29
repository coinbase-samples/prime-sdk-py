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
from typing import Any, Dict
import json


@dataclass
class CreateTransferRequest:
    portfolio_id: str
    wallet_id: str
    amount: str
    destination: str
    idempotency_key: str
    currency_symbol: str

    def to_json(self) -> Dict[str, Any]:
        return {
            "portfolio_id": self.portfolio_id,
            "wallet_id": self.wallet_id,
            "amount": self.amount,
            "destination": self.destination,
            "idempotency_key": self.idempotency_key,
            "currency_symbol": self.currency_symbol or None
        }


@dataclass
class CreateTransferResponse:
    response: Dict[str, Any]
    request: CreateTransferRequest

    def __str__(self) -> str:
        return json.dumps({"response": self.response,
                          "request": self.request.to_json()}, indent=4)


def create_transfer(client: Client,
                    request: CreateTransferRequest) -> CreateTransferResponse:
    path = f"/portfolios/{request.portfolio_id}/wallets/{request.wallet_id}/transfers"
    body = request.to_json()
    response = client.request("POST", path, body=body)
    return CreateTransferResponse(response.json(), request)
