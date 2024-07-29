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
from client import Client
from utils import PaginationParams
import utils
import json


class ListInvoicesRequest:
    def __init__(self,
                 entity_id: str,
                 states: Optional[str] = None,
                 billing_year: Optional[int] = None,
                 billing_month: Optional[str] = None,
                 pagination: Optional[PaginationParams] = None):
        self.entity_id = entity_id
        self.states = states
        self.billing_year = billing_year
        self.billing_month = billing_month
        self.pagination = pagination

    def to_json(self) -> Dict[str, Any]:
        return {
            "entity_id": self.entity_id,
            "states": self.states,
            "billing_year": self.billing_year,
            "billing_month": self.billing_month,
            "pagination_params": self.pagination.to_dict() if self.pagination else None
        }


class ListInvoicesResponse:
    def __init__(self, data: Dict[str, Any], request: ListInvoicesRequest):
        self.response = data
        self.request = request

    def __str__(self):
        return json.dumps({"response": self.response,
                          "request": self.request.to_json()}, indent=4)


def list_invoices(client: Client,
                  request: ListInvoicesRequest) -> ListInvoicesResponse:
    path = f"/entities/{request.entity_id}/invoices"

    query_params = []
    utils.append_query_param(query_params, 'states', request.states)
    utils.append_query_param(
        query_params,
        'billing_year',
        request.billing_year)
    utils.append_query_param(
        query_params,
        'billing_month',
        request.billing_month)

    if request.pagination:
        if request.pagination.cursor:
            utils.append_query_param(
                query_params, 'cursor', request.pagination.cursor)
        if request.pagination.limit:
            utils.append_query_param(
                query_params, 'limit', request.pagination.limit)

    query_string = "&".join(query_params)

    response = client.request("GET", path, query=query_string)
    return ListInvoicesResponse(response.json(), request)
