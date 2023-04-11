import fastf1
import pandas
fastf1.Cache.enable_cache('cache')
session = fastf1.get_session(2022, 'Monza', 'R')

session.load()
