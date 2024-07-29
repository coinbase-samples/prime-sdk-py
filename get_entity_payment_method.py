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


class GetEntityPaymentMethodRequest:
    def __init__(self,
                 entity_id: str,
                 payment_method_id: str):
        self.entity_id = entity_id
        self.payment_method_id = payment_method_id

    def to_json(self) -> Dict[str, Any]:
        return {
            "entity_id": self.entity_id,
            "payment_method_id": self.payment_method_id
        }


class GetEntityPaymentMethodResponse:
    def __init__(self, data: Dict[str, Any],
                 request: GetEntityPaymentMethodRequest):
        self.response = data
        self.request = request

    def __str__(self):
        return json.dumps({"response": self.response,
                          "request": self.request.to_json()}, indent=4)


def get_entity_payment_method(
        client: Client, request: GetEntityPaymentMethodRequest) -> GetEntityPaymentMethodResponse:
    path = f"/entities/{request.entity_id}/payment-methods/{request.payment_method_id}"

    response = client.request("GET", path, query=None)
    return GetEntityPaymentMethodResponse(response.json(), request)