# Prime Python SDK README

## Overview

The *Prime Python SDK* is a sample library that demonstrates the usage of the [Coinbase Prime](https://prime.coinbase.com/) API via its [REST APIs](https://docs.cdp.coinbase.com/prime/reference). This SDK provides a structured way to integrate Coinbase Prime functionalities into your Python applications.

## License

The *Prime Python SDK* sample library is free and open source and released under the [Apache License, Version 2.0](LICENSE).

The application and code are only available for demonstration purposes.

## Usage

### Setting Up Credentials

To use the *Prime Python SDK*, initialize the [Credentials](credentials.py) class with your Prime API credentials. This class is designed to facilitate the secure handling of sensitive information required to authenticate API requests.

Ensure that your API credentials are stored securely and are not hard-coded directly in your source code. The Credentials class supports creating credentials from a JSON string or directly from environment variables, providing flexibility and enhancing security.

#### Example Initialization:
```python
from credentials import Credentials
from client import Client

credentials = Credentials.from_env("PRIME_CREDENTIALS")
client = Client(credentials)
```

#### Environment Variable Format: 

The JSON format expected for `PRIME_CREDENTIALS` is:

```
{
  "accessKey": "",
  "passphrase": "",
  "signingKey": "",
  "portfolioId": "",
  "svcAccountId": "",
  "entityId": ""
}
```

### Obtaining API Credentials 

Coinbase Prime API credentials can be created in the Prime web console under Settings -> APIs. While not immediately necessary for most endpoints, your entity ID can be retrieved by calling [List Portfolios](https://docs.cdp.coinbase.com/prime/reference/primerestapi_getportfolios).

### Making API Calls
Once the client is initialized, make the desired call. For example, to [list portfolios](https://github.com/coinbase-samples/prime-sdk-py/blob/main/list_portfolios.py),
pass in the request object, check for an error, and if nil, process the response.


```python
from list_portfolios import PrimeClient, ListPortfoliosRequest

credentials = Credentials.from_env("PRIME_CREDENTIALS")
prime_client = PrimeClient(credentials)
    
request = ListPortfoliosRequest()
try:
    response = prime_client.list_portfolios(request)
    print(response)
except Exception as e:
    print(f"failed to list portfolios: {e}")

```

### Supported Versions
The SDK is tested and confirmed to work with Python version 3.7 and newer.
