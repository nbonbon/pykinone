# Overview
Python application to query the [Daikin One Open API](https://daikinone.com/openapi/)

## Current Status
This application currently will find all user devices and query for thermostat information according to the Daikin Open API. This information will be stored in a local sqlite database.

The application currently does **not** support the Daikin Open API functions for updating thermostat settings. This is planned for the _future_.

# Use

## Download Dependencies
Execute `pip3 install -r requirements.txt` to install the projects needed dependencies.

## Data Collection

### Setup
Create a configuration file next to the `pykinone.py` named `pykinone.conf`. In `pykinone.conf` add the following fields and their corresponding values you retrieved for your system according to the Daikin One Open API documentation.

```
apiKey:'<api-key-from-daikin-one-app>'
integratorEmail:'<email-used-for-daikin-one-app>'
integratorToken:'<integrator-token-from-daikin-one-app>'
```

Note: data within `<>` above are meant to be replaced with your values (including the `<>` themselves)

### Execution
Execute `python3 pykinone.py` in a terminal to execute the program 

## Data Visualization

## Execution
Execute `python3 plotter -h` to see options.

Executing this program will current create a plot with one line for indoor temperatures vs time and another for outdooor temperatures vs time.

The program allows to supply you prefered timezone and temperature units (see the -h help dialog for options)

# Development

## Prerequesites
- python 3.3+

Dependencies can be downloaded via pip and the projects's requirements.txt file. See "Download Dependencies" section.

## Running Unit Tests
Execute `pytest` from the root project directory. pytest install location on your machine must be in your PATH.
