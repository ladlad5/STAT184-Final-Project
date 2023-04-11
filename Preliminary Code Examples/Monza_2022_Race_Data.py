import fastf1
import numpy as np
import pandas
import csv
fastf1.Cache.enable_cache('cache')
session = fastf1.get_session(2022, 'Monza', 'R')

session.load()
lapDataHAM = session.laps.pick_driver('HAM')
lapDataVER = session.laps.pick_driver('VER')
HAMLapTimes = lapDataHAM['LapTime'].tolist()
HAMLapTimes = HAMLapTimes[1:]
for x in range(len(HAMLapTimes)):
    HAMLapTimes[x] = str(HAMLapTimes[x].to_numpy().astype('timedelta64[ms]'))
    HAMLapTimes[x] = HAMLapTimes[x].replace(' milliseconds', '')
VERLapTimes = lapDataVER['LapTime'].tolist()
VERLapTimes = VERLapTimes[1:]
for x in range(len(VERLapTimes)):
    VERLapTimes[x] = str(VERLapTimes[x].to_numpy().astype('timedelta64[ms]'))
    VERLapTimes[x] = VERLapTimes[x].replace(' milliseconds', '')
HAMCompound = lapDataHAM['Compound'].tolist()
VERCompound = lapDataVER['Compound'].tolist()
