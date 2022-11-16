import matplotlib as mpl
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np
import sqlite3
import pandas as pd
from Normalizer import Normalizer

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
indoor_humidity = therm_info_df['humIndoor']
outdoor_humidity = therm_info_df['humOutdoor']

normalizer = Normalizer()
timesResult, indoorTempsResult = normalizer.normalizeTimedData(times, indoor_temps, 3*60)
plt_times = mdates.date2num(timesResult)
ax.plot(plt_times, indoorTempsResult, linestyle='solid', label='Indoor Temperature')

outdoorTempsResult = normalizer.normalizeTimedData(times, outdoor_temps, 3*60)[1]
ax.plot(plt_times, outdoorTempsResult, linestyle='solid', label='Outdoor Temperature')

ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))
ax.xaxis.set_major_locator(mdates.MinuteLocator(interval=15))
ax.set_xlabel('Time')
ax.set_ylabel('Temperature')
ax.set_title('Historical Temperature Data')
ax.legend()
fig.autofmt_xdate()
fig.tight_layout()
plt.setp(ax.get_xticklabels(), rotation=90, horizontalalignment='right')
plt.show()