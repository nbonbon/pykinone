import matplotlib as mpl
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np
import sqlite3
import pandas as pd
import sys
from Normalizer import Normalizer
from ArgParsers.PlotterArgParser import PlotterArgParser
from Util.TimeUtil import TimeUtil
from Util.TempUtil import TempUtil
from Util.TimezoneUtil import TimezoneUtil
from Entity.TemperatureUnit import TemperatureUnit

degree_sign = u'\N{DEGREE SIGN}'

parser = PlotterArgParser()
parser.parseArgs(sys.argv[1:])
timezone = parser.timezone
tempUnits = parser.temperatureUnits
startDate = parser.startDate
endDate = parser.endDate
databaseFile = parser.databaseFile

fig, ax = plt.subplots() 

con = sqlite3.connect(databaseFile)

queryString = """
    SELECT * FROM thermostat_info 
    WHERE timestamp 
    BETWEEN '{start}' AND '{end}'
    ORDER BY timestamp ASC
""".format(start=startDate, end=endDate)
therm_info_df = pd.read_sql_query(queryString, con)

if therm_info_df.empty:
    print("No data found")
    exit(0)

times = therm_info_df['timestamp']
indoor_temps = therm_info_df['tempIndoor']
outdoor_temps = therm_info_df['tempOutdoor']

tempUnits = TemperatureUnit.Celsius
if parser.temperatureUnits == TemperatureUnit.Fahrenheit:
    indoor_temps = TempUtil.transformToFahrenheit(indoor_temps)
    outdoor_temps = TempUtil.transformToFahrenheit(outdoor_temps)

normalizer = Normalizer()
timesResult, indoorTempsResult = normalizer.normalizeTimedData(times, indoor_temps, 3*60)
timesResult = TimeUtil.transformUtcToTimezone(timesResult, parser.timezone)
plt_times = mdates.date2num(timesResult)
ax.plot(plt_times, indoorTempsResult, linestyle='solid', label='Indoor Temperature')

outdoorTempsResult = normalizer.normalizeTimedData(times, outdoor_temps, 3*60)[1]
ax.plot(plt_times, outdoorTempsResult, linestyle='solid', label='Outdoor Temperature')

ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))
ax.xaxis.set_major_locator(mdates.MinuteLocator(interval=15))
ax.set_xlabel('Time [' + TimezoneUtil.getTimezoneString(timezone) + ']') 
ax.set_ylabel('Temperature [' + degree_sign + tempUnits.upper() + ']')
ax.set_title('Historical Temperature Data for ' + startDate.isoformat(" ","seconds") + ' to ' + endDate.isoformat(" ","seconds"))
ax.legend()
fig.autofmt_xdate()
fig.tight_layout()
plt.setp(ax.get_xticklabels(), rotation=90, horizontalalignment='right')
plt.show() 
