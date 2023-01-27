# Overview
Python application to query the [Daikin One Open API](https://daikinone.com/openapi/), log, and graph data.

The application also allows the configuration of a SwitchBot Meter Plus device to run the thermostat off of instead of the system thermostat.

This can be used as a solution to rooms becoming to hot compared to the room where the thermostat is located.

## Current Status
This application currently will find all user devices and query for thermostat information according to the Daikin Open API. This information will be stored in a local sqlite database.

The API is queried every 3 minutes as specified in the Open API documentation. If no data has changed a new datapoint will not be saved in the database. The plotter (see Data Visualization section) will dynamically add these points back in when plotting data.

The application currently does **not** support the Daikin Open API functions for updating thermostat settings when in cool mode. This is planned for the _future_.

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
Create a configuration file next to the `pykinone.py` named `pykinone.conf`. In `pykinone.conf` add the following fields.

Note: data within `<>` above are meant to be replaced with your values (including the `<>` themselves)

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
heatMinThreshold: 1
heatMaxThreshold: 2
```

#### apiKey | integratorEmail | integratorToken

These values can be retrieved for your system according to the Daikin One Open API documentation and Daikin One mobile phone application.

#### macs 

This field specifies what MAC addresses to observe Bluetooth Low Energy (BLE) advertisement packets for [SwitchBot Meter Plus](https://us.switch-bot.com/products/switchbot-meter-plus) temperature monitoring devices (henceforth refered to as meter)

The mac keys correspond to the user defined naming of meter devices. The mac values correspond to the device macs of the meter devices. The mac value of a meter device can be found in the SwitchBot mobile phone application under: device profile > Settings > Device Info > BLE MAC.

#### meterToFollow

The meterToFollow field corresponds to a mac key from the macs configuration above. This field will designate a meter device to base the thermostat setting off of. This application will change the system mode depending upon this meters temperature value in relation to the heat set point.

#### heatMinTheshold

The heatMinThreshold field specifies the offset from the heatSetPoint on the thermostat (in degrees Celsius) that should be allowed before the system mode is set to heating. Essentially the heat set point - the heatMinTheshold will be the min temperature allowed in the room where the meter is placed before the system mode is changed to heat.

#### heatMaxTheshold

The heatMaxTheshold field specifies the offset from the heatSetPoint on the thermostat (in degrees Celsius) that should be allowed before the system mode is set to off. Essentially the heat set point + the heatMaxThreshold will be the max temperature allowed in the room where the meter is placed before the system mode is changed to off.

#### deviceIdOfMeter
The deviceIdOfMeter field is the device id of the thermostat at the daikin mobile application defined location where the meter device is located. This can be obtained by inspection of the device table in the database of this application. 



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
