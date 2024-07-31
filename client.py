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

import hmac
import hashlib
import base64
import requests
import time
import json
from typing import Optional, Dict
from credentials import Credentials

DEFAULT_V1_API_BASE_URL = "https://api.prime.coinbase.com/v1"


class Client:
    def __init__(self, credentials: Credentials,
                 http_client: Optional[requests.Session] = None):
        self.http_base_url = DEFAULT_V1_API_BASE_URL
        self.credentials = credentials
        self.http_client = http_client if http_client else requests.Session()

    def generate_headers(self, method: str, path: str,
                         body: Optional[Dict] = None) -> Dict[str, str]:
        timestamp = str(int(time.time()))
        body_string = json.dumps(body) if body else ""
        message = f"{timestamp}{method}{path}{body_string}"
        signature = self.sign(message)

        return {
            "Accept": "application/json",
            "X-CB-ACCESS-KEY": self.credentials.access_key,
            "X-CB-ACCESS-PASSPHRASE": self.credentials.passphrase,
            "X-CB-ACCESS-SIGNATURE": signature,
            "X-CB-ACCESS-TIMESTAMP": timestamp,
        }

    def sign(self, message: str) -> str:
        h = hmac.new(
            self.credentials.signing_key.encode(),
            message.encode(),
            hashlib.sha256)
        return base64.b64encode(h.digest()).decode()

    def request(
            self,
            method: str,
            path: str,
            query: Optional[str] = "",
            body: Optional[Dict] = None,
            allowed_status_codes=None) -> requests.Response:
        if allowed_status_codes is None:
            allowed_status_codes = [200]
        full_path = f"{self.http_base_url}{path}"
        url = f"{full_path}?{query}" if query is not None else full_path

        headers = self.generate_headers(method, f"/v1{path}", body)
        response = self.http_client.request(
            method, url, headers=headers, json=body)

        if response.status_code not in allowed_status_codes:
            try:
                error_details = response.json()
                error_message = error_details.get('message', response.text)
            except ValueError:
                error_message = response.text
            raise Exception(
                f"Request failed with status {response.status_code}: {error_message}")

        return response
