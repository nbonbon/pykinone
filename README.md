# Overview
Python application to query the [Daikin One Open API](https://daikinone.com/openapi/)

## Current Status
This application currently will find all user devices and query for thermostat information according to the Daikin Open API. This information will be stored in a local sqlite database.

The application currently does **not** support the Daikin Open API functions for updating thermostat settings. This is planned for the _future_.

# Use

## Setup
Create a configuration file next to the `pykinone.py` named `pykinone.conf`. In `pykinone.conf` add the following fields and their corresponding values you retrieved for your system according to the Daikin One Open API documentation.

```
apiKey:'<api-key-from-daikin-one-app>'
integratorEmail:'<email-used-for-daikin-one-app>'
integratorToken:'<integrator-token-from-daikin-one-app>'
```

Note: data within `<>` above are meant to be replaced with your values (including the `<>` themselves)

## Execution
Run `python3 pykinone.py` in a terminal to execute the program 

## Prerequesites
- Python 3.3+

# Development

## Prerequesites
- Python 3.3+
- pytest
- unittest.mock

## Running Unit Tests
Execute `pytest` from the root project directory. pytest install location on your machine must be in your PATH.
