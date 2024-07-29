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
import json

from client import Client


class PaymentMethod:
    def __init__(self, payment_method_id: Optional[str] = None):
        self.payment_method_id = payment_method_id

    def to_json(self) -> Dict[str, Any]:
        if self.payment_method_id:
            return {"payment_method_id": self.payment_method_id}
        return {}


class BlockchainAddress:
    def __init__(self, address: Optional[str] = None,
                 account_identifier: Optional[str] = None):
        self.address = address
        self.account_identifier = account_identifier

    def to_json(self) -> Dict[str, Any]:
        return {
            "address": self.address or None,
            "account_identifier": self.account_identifier or None
        }


class CreateWithdrawalRequest:
    def __init__(self, portfolio_id: str, wallet_id: str, amount: str, destination_type: str,
                 idempotency_key: str, currency_symbol: str, payment_method: Optional[PaymentMethod] = None,
                 blockchain_address: Optional[BlockchainAddress] = None):
        self.portfolio_id = portfolio_id
        self.wallet_id = wallet_id
        self.amount = amount
        self.destination_type = destination_type
        self.idempotency_key = idempotency_key
        self.currency_symbol = currency_symbol
        self.payment_method = payment_method
        self.blockchain_address = blockchain_address

    def to_json(self) -> Dict[str, Any]:
        data = {
            "portfolio_id": self.portfolio_id,
            "wallet_id": self.wallet_id,
            "amount": self.amount,
            "destination_type": self.destination_type,
            "idempotency_key": self.idempotency_key,
            "currency_symbol": self.currency_symbol
        }
        if self.payment_method:
            data["payment_method"] = self.payment_method.to_json()
        if self.blockchain_address:
            data["blockchain_address"] = self.blockchain_address.to_json()
        return data


class CreateWithdrawalResponse:
    def __init__(self, data: Dict[str, Any], request: CreateWithdrawalRequest):
        self.response = data
        self.request = request

    def __str__(self):
        return json.dumps({"response": self.response,
                          "request": self.request.to_json()}, indent=4)


def create_withdrawal(
        client: Client, request: CreateWithdrawalRequest) -> CreateWithdrawalResponse:
    path = f"/portfolios/{request.portfolio_id}/wallets/{request.wallet_id}/withdrawals"

    body = request.to_json()
    response = client.request("POST", path, body=body)
    return CreateWithdrawalResponse(response.json(), request)
