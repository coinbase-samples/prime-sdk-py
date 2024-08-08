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
class PaymentMethod:
    payment_method_id: str

    def to_dict(self) -> Dict[str, Any]:
        return {"payment_method_id": self.payment_method_id}


@dataclass
class BlockchainAddress:
    address: str
    account_identifier: Optional[str] = None
    allowed_status_codes: List[int] = None

    def to_dict(self) -> Dict[str, Any]:
        result = asdict(self)
        return {k: v for k, v in result.items() if v is not None}


@dataclass
class CreateWithdrawalRequest:
    portfolio_id: str
    wallet_id: str
    amount: str
    destination_type: str
    idempotency_key: str
    currency_symbol: str
    payment_method: Optional[PaymentMethod] = None
    blockchain_address: Optional[BlockchainAddress] = None

    def to_dict(self) -> Dict[str, Any]:
        result = asdict(self)
        if self.payment_method:
            result['payment_method'] = self.payment_method.to_dict()
        if self.blockchain_address:
            result['blockchain_address'] = self.blockchain_address.to_dict()
        return {k: v for k, v in result.items() if v is not None}


@dataclass
class CreateWithdrawalResponse(BaseResponse):
    request: CreateWithdrawalRequest


class PrimeClient:
    def __init__(self, credentials: Credentials):
        self.client = Client(credentials)
        
    def create_withdrawal(self, request: CreateWithdrawalRequest) -> CreateWithdrawalResponse:
        path = f"/portfolios/{request.portfolio_id}/wallets/{request.wallet_id}/withdrawals"
        body = request.to_dict()
        response = self.client.request("POST", path, body=body, allowed_status_codes=request.allowed_status_codes)
        return CreateWithdrawalResponse(response.json(), request)
