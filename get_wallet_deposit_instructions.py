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
from utils import append_query_param
import json


@dataclass
class GetWalletDepositInstructionsRequest:
    portfolio_id: str
    wallet_id: str
    deposit_type: str

    def to_json(self) -> Dict[str, Any]:
        return {
            "portfolio_id": self.portfolio_id,
            "wallet_id": self.wallet_id,
            "deposit_type": self.deposit_type
        }


@dataclass
class GetWalletDepositInstructionsResponse:
    response: Dict[str, Any]
    request: GetWalletDepositInstructionsRequest

    def __str__(self) -> str:
        return json.dumps({"response": self.response,
                          "request": self.request.to_json()}, indent=4)


def get_wallet_deposit_instructions(
        client: Client,
        request: GetWalletDepositInstructionsRequest) -> GetWalletDepositInstructionsResponse:
    path = f"/portfolios/{request.portfolio_id}/wallets/{request.wallet_id}/deposit_instructions"

    query_params = ""
    query_params = append_query_param(query_params, 'deposit_type', request.deposit_type)

    response = client.request("GET", path, query=query_params)
    return GetWalletDepositInstructionsResponse(response.json(), request)
