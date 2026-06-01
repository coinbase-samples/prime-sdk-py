# Prime Python SDK README

> **Deprecation notice:** This repository is deprecated. Use the official repository at [coinbase/prime-sdk-py](https://github.com/coinbase/prime-sdk-py) for issues, contributions, and future releases. The PyPI package name remains `prime-sdk-py`; install with `pip install prime-sdk-py` — releases after 1.7.2 will be published from the coinbase org repository.

## Overview

The *Prime Python SDK* is a sample library that demonstrates the usage of the [Coinbase Prime](https://prime.coinbase.com/) API via its [REST APIs](https://docs.cdp.coinbase.com/prime/reference). This SDK provides a structured way to integrate Coinbase Prime functionalities into your Python applications.

## Installation

### From PyPI (Recommended)

```bash
pip install prime-sdk-py
```

### From Source

```bash
git clone https://github.com/coinbase-samples/prime-sdk-py.git
cd prime-sdk-py
pip install -e .
```

## Usage

### Setting Up Credentials

To use the *Prime Python SDK*, initialize the [Credentials](prime_sdk/credentials.py) class with your Prime API credentials. This class is designed to facilitate the secure handling of sensitive information required to authenticate API requests.

Ensure that your API credentials are stored securely and are not hard-coded directly in your source code. The Credentials class supports creating credentials from a JSON string or directly from environment variables, providing flexibility and enhancing security.

#### Example Initialization:
```python
from prime_sdk.credentials import Credentials

credentials = Credentials.from_env()
```

#### Environment Variable Format

The SDK supports two formats for credentials configuration:

##### New Format

Set separate environment variables for better security separation:

```bash
export PRIME_CREDENTIALS='{
  "accessKey": "your-access-key",
  "passphrase": "your-passphrase", 
  "signingKey": "your-signing-key",
  "svcAccountId": "your-service-account-id"
}'

export PRIME_PORTFOLIO_ID="your-portfolio-id"
export PRIME_ENTITY_ID="your-entity-id"
```

##### Legacy Format (Backwards Compatible)

All credentials in a single environment variable:

```bash
export PRIME_CREDENTIALS='{
  "accessKey": "your-access-key",
  "passphrase": "your-passphrase",
  "signingKey": "your-signing-key", 
  "portfolioId": "your-portfolio-id",
  "svcAccountId": "your-service-account-id",
  "entityId": "your-entity-id"
}'
```

The SDK will automatically detect which format you're using. If `PRIME_PORTFOLIO_ID` and `PRIME_ENTITY_ID` are set, it will use the new format; otherwise, it falls back to the legacy format.

### Obtaining API Credentials 

Coinbase Prime API credentials can be created in the Prime web console under Settings -> APIs. While not immediately necessary for most endpoints, your entity ID can be retrieved by calling [List Portfolios](https://docs.cdp.coinbase.com/prime/reference/primerestapi_getportfolios).

### Making API Calls

The SDK is organized into service modules that group related functionality. Each service provides methods for specific API operations.

#### Service-Based Architecture

The SDK uses a service-based architecture where each domain (portfolios, orders, transactions, etc.) has its own service class:

```python
from prime_sdk.credentials import Credentials
from prime_sdk.client import Client
from prime_sdk.services.portfolios import PortfoliosService, ListPortfoliosRequest

# Initialize credentials and client
credentials = Credentials.from_env("PRIME_CREDENTIALS")
client = Client(credentials)

# Create the service
portfolios_service = PortfoliosService(client)

# Make the API call
request = ListPortfoliosRequest()
try:
    response = portfolios_service.list_portfolios(request)
    print(response)
except Exception as e:
    print(f"Failed to list portfolios: {e}")
```

#### Available Services

The SDK provides the following services:

- **PortfoliosService** - Portfolio management (`prime_sdk.services.portfolios`)
- **OrdersService** - Order management (`prime_sdk.services.orders`) 
- **TransactionsService** - Transaction operations (`prime_sdk.services.transactions`)
- **WalletsService** - Wallet management (`prime_sdk.services.wallets`)
- **ActivitiesService** - Activity tracking (`prime_sdk.services.activities`)
- **AssetsService** - Asset information (`prime_sdk.services.assets`)
- **BalancesService** - Balance queries (`prime_sdk.services.balances`)
- **UsersService** - User management (`prime_sdk.services.users`)
- **ProductsService** - Product information (`prime_sdk.services.products`)
- **StakingService** - Staking operations (`prime_sdk.services.staking`)

#### Complete Example: Creating a Transfer

```python
from prime_sdk.credentials import Credentials
from prime_sdk.client import Client
from prime_sdk.services.transactions import (
    TransactionsService, 
    CreateTransferRequest
)

def main():
    # Initialize credentials and client
    credentials = Credentials.from_env("PRIME_CREDENTIALS")
    client = Client(credentials)
    
    # Create the transactions service
    transactions_service = TransactionsService(client)
    
    # Create a transfer request
    request = CreateTransferRequest(
        portfolio_id="your-portfolio-id",
        wallet_id="your-wallet-id",
        amount="0.01",
        destination="your-destination-wallet-id",
        currency_symbol="ETH",
        idempotency_key=str(uuid.uuid4())
    )
    
    try:
        response = transactions_service.create_transfer(request)
        print(f"Transfer created: {response}")
    except Exception as e:
        print(f"Failed to create transfer: {e}")

if __name__ == "__main__":
    main()
```

## Services Client (Recommended)

For most use cases, we recommend using the **PrimeServicesClient** which provides a more convenient way to access all Prime services through a single client interface. This approach eliminates the need to manually create individual service instances.

### Quick Start with Services Client

```python
from prime_sdk.client_services import PrimeServicesClient

# Create client from environment variables
client = PrimeServicesClient.from_env()

# Access any service directly
portfolios = client.portfolios.list_portfolios(request)
orders = client.orders.create_order(request)
transactions = client.transactions.create_transfer(request)
```

### Complete Example with Services Client

```python
import os
from prime_sdk.client_services import PrimeServicesClient
from prime_sdk.services.transactions import CreateTransferRequest

def main():
    # Create client from environment
    client = PrimeServicesClient.from_env()
    
    # Create transfer request
    request = CreateTransferRequest(
        portfolio_id="your-portfolio_id",
        wallet_id="your-wallet-id", 
        amount="0.01",
        destination="your-destination-wallet-id",
        currency_symbol="USD",
        idempotency_key=str(uuid.uuid4())
    )
    
    try:
        # Use the services client - no need to create individual services
        response = client.transactions.create_transfer(request)
        print(f"Transfer created: {response}")
    except Exception as e:
        print(f"Failed to create transfer: {e}")

if __name__ == "__main__":
    main()
```

### Services Client vs Individual Services

**Use Services Client when:**
- Building applications that use multiple Prime services
- You want a simple, unified interface
- You prefer convenience over fine-grained control

**Use Individual Services when:**
- You only need one or two specific services
- You want explicit control over service instantiation
- You're building a minimal application with specific performance requirements

### Supported Versions
The SDK is tested and confirmed to work with Python version 3.7 and newer.

## Local Development

### Making Changes to the SDK

If you need to make modifications to the SDK for your specific use case, follow these steps:

#### 1. Clone and Setup

```bash
git clone https://github.com/coinbase-samples/prime-sdk-py.git
cd prime-sdk-py
```

#### 2. Install in Development Mode

```bash
pip install -e .
```

This installs the SDK in "editable" mode, meaning changes to the source code will be immediately reflected without reinstallation.

#### 3. Running Tests

```bash
# Install test dependencies
pip install pytest

# Run tests
pytest tests/
```

#### 4. Code Structure

The SDK follows this structure:

```
prime_sdk/
├── credentials.py          # Authentication handling
├── client.py              # HTTP client
├── base_response.py       # Base response classes
├── utils.py               # Utility functions
├── enums.py               # Common enumerations
└── services/              # Service modules
    ├── portfolios/        # Portfolio operations
    ├── orders/            # Order management
    ├── transactions/      # Transaction operations
    ├── wallets/           # Wallet management
    └── ...                # Other services
```

Each service directory contains:
- `service.py` - The main service class with API methods
- Individual request/response modules (e.g., `list_portfolios.py`)
- `__init__.py` - Exports for the service

## 🚨 Security and Bug Reports

If you discover a security vulnerability within this SDK, please see our [Security Policy](SECURITY.md) for disclosure information.

## 📧 Contact

- [GitHub Issues](https://github.com/coinbase-samples/prime-sdk-py/issues)

## Maintenance status

This repository is deprecated and will not receive new tags or PyPI releases after version 1.7.2. For ongoing development and releases, use [coinbase/prime-sdk-py](https://github.com/coinbase/prime-sdk-py).

## License

The *Prime Python SDK* sample library is free and open source and released under the [Apache License, Version 2.0](LICENSE).
