import matplotlib as mpl
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np
import sqlite3
import pandas as pd
import sys
from dateutil import tz
from Normalizer import Normalizer
from ArgParsers.PlotterArgParser import PlotterArgParser
from Util.TimeUtil import TimeUtil
from Util.TempUtil import TempUtil

degree_sign = u'\N{DEGREE SIGN}'

args = PlotterArgParser.parseArgs(sys.argv[1:])
timezone = tz.gettz(args.timezone) #todo: parse in arg parser and fail if not valid
temp = args.temp
datrangeStr = args.daterange #todo: parse in arg parser and fail if not valid

fig, ax = plt.subplots() 

con = sqlite3.connect("pykinone.db")

queryString = """
    SELECT * FROM thermostat_info 
    ORDER BY timestamp ASC
"""
therm_info_df = pd.read_sql_query("SELECT * from thermostat_info", con)

times = therm_info_df['timestamp']
indoor_temps = therm_info_df['tempIndoor']
outdoor_temps = therm_info_df['tempOutdoor']

tempUnits = "C"
if temp.lower() == 'f' or temp.lower() == 'fahrenheit':
    indoor_temps = TempUtil.transformToFahrenheit(indoor_temps)
    outdoor_temps = TempUtil.transformToFahrenheit(outdoor_temps)

normalizer = Normalizer()
timesResult, indoorTempsResult = normalizer.normalizeTimedData(times, indoor_temps, 3*60)
timesResult = TimeUtil.transformUtcToTimezone(timesResult, timezone)
plt_times = mdates.date2num(timesResult)
ax.plot(plt_times, indoorTempsResult, linestyle='solid', label='Indoor Temperature')

outdoorTempsResult = normalizer.normalizeTimedData(times, outdoor_temps, 3*60)[1]
ax.plot(plt_times, outdoorTempsResult, linestyle='solid', label='Outdoor Temperature')

ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))
ax.xaxis.set_major_locator(mdates.MinuteLocator(interval=15))
ax.set_xlabel('Time [' + args.timezone + ']') #todo: better way to get timezone name
ax.set_ylabel('Temperature [' + tempUnits + degree_sign + ']')
ax.set_title('Historical Temperature Data')
ax.legend()
fig.autofmt_xdate()
fig.tight_layout()
plt.setp(ax.get_xticklabels(), rotation=90, horizontalalignment='right')
plt.show() 