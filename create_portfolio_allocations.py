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

from typing import Any, Dict, List
import json

from client import Client


class AllocationLeg:
    def __init__(self, leg_id: str,
                 destination_portfolio_id: str, amount: str):
        self.leg_id = leg_id
        self.destination_portfolio_id = destination_portfolio_id
        self.amount = amount

    def to_json(self) -> Dict[str, Any]:
        return {
            "allocation_leg_id": self.leg_id,
            "destination_portfolio_id": self.destination_portfolio_id,
            "amount": self.amount
        }


class CreatePortfolioAllocationsRequest:
    def __init__(self, allocation_id: str, source_portfolio_id: str, product_id: str,
                 order_ids: List[str], allocation_legs: List[AllocationLeg],
                 size_type: str, remainder_destination_portfolio_id: str):
        self.allocation_id = allocation_id
        self.source_portfolio_id = source_portfolio_id
        self.product_id = product_id
        self.order_ids = order_ids
        self.allocation_legs = allocation_legs
        self.size_type = size_type
        self.remainder_destination_portfolio_id = remainder_destination_portfolio_id

    def to_json(self) -> Dict[str, Any]:
        return {
            "allocation_id": self.allocation_id,
            "source_portfolio_id": self.source_portfolio_id,
            "product_id": self.product_id,
            "order_ids": self.order_ids,
            "allocation_legs": [leg.to_json() for leg in self.allocation_legs],
            "size_type": self.size_type,
            "remainder_destination_portfolio": self.remainder_destination_portfolio_id
        }


class CreatePortfolioAllocationsResponse:
    def __init__(self, data: Dict[str, Any],
                 request: CreatePortfolioAllocationsRequest):
        self.response = data
        self.request = request

    def __str__(self):
        return json.dumps({"response": self.response,
                          "request": self.request.to_json()}, indent=4)


def create_portfolio_allocations(
        client: Client, request: CreatePortfolioAllocationsRequest) -> CreatePortfolioAllocationsResponse:
    path = f"/allocations/{request.allocation_id}/order"
    body = request.to_json()
    response = client.request("POST", path, body=body)
    return CreatePortfolioAllocationsResponse(response.json(), request)
