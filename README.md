# Overview
Python application to query the [Daikin One Open API](https://daikinone.com/openapi/)

# Setup
Create a configuration file next to the `pykinone.py` named `pykinone.conf`. In `pykinone.conf` add the following fields and their corresponding values you retrieved for your system according to the Daikin One Open API documentation.

```
apiKey:'<api-key-from-daikin-one-app>'
integratorEmail:'<email-used-for-daikin-one-app>'
integratorToken:'<integrator-token-from-daikin-one-app>'
```

Note: data within `<>` above are meant to be replaced with your values (including the `<>` themselves)

# Execution
Run `python3 pykinone.py` in a terminal to execute the program 

# Prerequesites
- Python3
