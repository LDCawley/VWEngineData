import pandas as pd
import matplotlib.pyplot as plt
import math
import numpy as np

VW_engine_data = pd.read_excel('/Users/larrydcj/Documents/Programming and IT/Projects/VWEngineData/session_8.xlsx', header=4) #reads file from path, marks title row

print(VW_engine_data.columns)

fuel_rail_pressure_actual = VW_engine_data['Fuel Rail Pressure (actual) (MPa)'] #creates and assigns fuel rail pressure to correct column
low_side_fuel_pressure_actual = VW_engine_data['Low Side Fuel Pressure (actual) (kPa)']
timestamp = VW_engine_data['timestamp(ms)'] / 1000 #to display seconds vs milliseconds

x = timestamp.to_numpy()
y2 = low_side_fuel_pressure_actual.to_numpy()
y = fuel_rail_pressure_actual.to_numpy()

fig, ax1 = plt.subplots()

color='tab:red'
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Fuel Rail Pressure (actual) (MPa)', color=color)
ax1.plot(x,y, color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()

color='tab:blue'
ax2.set_ylabel('Low Side Fuel Pressure (actual) (kPa)', color=color)  # we already handled the x-label with ax1
ax2.plot(x,y2, color=color)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()
plt.show()
