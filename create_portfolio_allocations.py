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
class AllocationLeg:
    leg_id: str
    destination_portfolio_id: str
    amount: str
    allowed_status_codes: List[int] = None


@dataclass
class CreatePortfolioAllocationsRequest:
    allocation_id: str
    source_portfolio_id: str
    product_id: str
    order_ids: List[str]
    allocation_legs: List[AllocationLeg]
    size_type: str
    remainder_destination_portfolio_id: str
    allowed_status_codes: List[int] = None


@dataclass
class CreatePortfolioAllocationsResponse(BaseResponse):
    request: CreatePortfolioAllocationsRequest


class PrimeClient:
    def __init__(self, credentials: Credentials):
        self.client = Client(credentials)

    def create_portfolio_allocations(
            self,
            request: CreatePortfolioAllocationsRequest) -> CreatePortfolioAllocationsResponse:
        path = f"/allocations/{request.allocation_id}/order"

        body = asdict(request)
        body['allocation_legs'] = [asdict(leg) for leg in request.allocation_legs]

        response = self.client.request("POST", path, body=body, allowed_status_codes=request.allowed_status_codes)
        return CreatePortfolioAllocationsResponse(response.json(), request)
