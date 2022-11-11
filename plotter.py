import matplotlib.pyplot as plt
import sqlite3
import pandas as pd
from Normalizer import Normalizer

con = sqlite3.connect("pykinone.db")

queryString = """
    SELECT * FROM thermostat_info 
    ORDER BY timestamp ASC
"""
therm_info_df = pd.read_sql_query("SELECT * from thermostat_info", con)

times = therm_info_df['timestamp']
indoor_temps = therm_info_df['tempIndoor']

print(times)
print(type(times[0]))

normalizer = Normalizer()
timesResult, tempsResult = normalizer.normalizeTimedData(times, indoor_temps, 3*60)

plt.plot_date(timesResult, tempsResult, linestyle='solid')
# plt.plot_date(times, indoor_temps, linestyle='solid')
plt.xticks(rotation=90)
# plt.plot(time, indoor_humidity)
# plt.plot(time, outdoor_temp)
# plt.plot(time, outdoor_humidity)

plt.tight_layout()
plt.show()