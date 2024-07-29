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

from typing import Dict, Any
import json

from client import Client


class GetWalletBalanceRequest:
    def __init__(self,
                 portfolio_id: str,
                 wallet_id: str):
        self.portfolio_id = portfolio_id
        self.wallet_id = wallet_id

    def to_json(self) -> Dict[str, Any]:
        return {
            "portfolio_id": self.portfolio_id,
            "wallet_id": self.wallet_id
        }


class GetWalletBalanceResponse:
    def __init__(self, data: Dict[str, Any], request: GetWalletBalanceRequest):
        self.response = data
        self.request = request

    def __str__(self):
        return json.dumps({"response": self.response,
                          "request": self.request.to_json()}, indent=4)


def get_wallet_balance(
        client: Client, request: GetWalletBalanceRequest) -> GetWalletBalanceResponse:
    path = f"/portfolios/{request.portfolio_id}/wallets/{request.wallet_id}/balance"

    response = client.request("GET", path, query=None)
    return GetWalletBalanceResponse(response.json(), request)
