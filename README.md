# Overview
Python application to query the [Daikin One Open API](https://daikinone.com/openapi/)

## Current Status
This application currently will find all user devices and query for thermostat information according to the Daikin Open API. This information will be stored in a local sqlite database.

The API is queried every 3 minutes as specified in the Open API documentation. If no data has changed a new datapoint will not be saved in the database. The plotter (see Data Visualization section) will dynamically add these points back in when plotting data.

The application currently does **not** support the Daikin Open API functions for updating thermostat settings. This is planned for the _future_.

# Use

## Download Dependencies
Execute `pip3 install -r requirements.txt` to install all dependencies.

### pipreqs
pipreqs is used to compile dependencies into the requirements.txt.

In the pykinone directory execute: `pipreqs --force`

The above will overwrite the existing requirements.txt.

https://github.com/bndr/pipreqs

## Data Collection

### Setup
Create a configuration file next to the `pykinone.py` named `pykinone.conf`. In `pykinone.conf` add the following fields and their corresponding values you retrieved for your system according to the Daikin One Open API documentation.

```
apiKey:'<api-key-from-daikin-one-app>'
integratorEmail:'<email-used-for-daikin-one-app>'
integratorToken:'<integrator-token-from-daikin-one-app>'
macs: {
    '<device-name-1>':'<device-mac-1>',
    '<device-name-2>':'<device-mac-2>'
}
meterToFollow: '<device-name-1>'
deviceIdOfMeter: '<device-id>'
```

This application allows the configuration of a Switchbot Meter device for the system to follow. Meaning this application will control the thermostat in such a way that the thermostat / HVAC system will be running off of the configured meter. This field is the 'meterToFollow' above. The value should correspond to the device name of a device specified in the macs configuration.

The mac keys correspond to the user defined naming of switchbot devices. The mac values correspond to the device macs of the switch bot meters. The mac value of a switchbot meter can be found in the Switchbot app device profile > Settings > Device Info > BLE MAC.

deviceIdOfMeter is the device id of the thermostat at the location where the meter is located. This can be obtained by inspection of the device table in the database. 

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
