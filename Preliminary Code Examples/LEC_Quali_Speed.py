import fastf1
fastf1.Cache.enable_cache('cache') 
session = fastf1.get_session(2019, 'Monza', 'Q')  # Enable caching to a folder called 'cache'

session.load()
fast_leclerc = session.laps.pick_driver('LEC').pick_fastest()
lec_car_data = fast_leclerc.get_car_data()
t = lec_car_data['Time']
vCar = lec_car_data['Speed']
print(type(vCar))
open('Data/lec_time_data.txt', 'w').write(str(t.to_numpy().astype('timedelta64[ms]')))
open('Data/lec_car_data.txt', 'w').write(str(vCar.to_numpy()))
speedData = vCar.to_numpy()
timeData = t.to_numpy().astype('timedelta64[ms]')