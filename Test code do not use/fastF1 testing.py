from matplotlib import pyplot as plt
import fastf1
import fastf1.plotting

fastf1.plotting.setup_mpl()
fastf1.Cache.enable_cache('cache') 
session = fastf1.get_session(2019, 'Monza', 'Q')  # Enable caching to a folder called 'cache'

session.load()
fast_leclerc = session.laps.pick_driver('LEC').pick_fastest()
lec_car_data = fast_leclerc.get_car_data()
t = lec_car_data['Time']
vCar = lec_car_data['Speed']
print(type(vCar))
open('lec_time_data.txt', 'w').write(str(t.to_numpy().astype('timedelta64[ms]')))
open('lec_car_data.txt', 'w').write(str(vCar.to_numpy()))
test = vCar.to_numpy()
testTime = t.to_numpy().astype('timedelta64[ms]')
print(len(test))
print(len(testTime))

# The rest is just plotting
fig, ax = plt.subplots()
ax.plot(t, vCar, label='Fast')
ax.set_xlabel('Time')
ax.set_ylabel('Speed [Km/h]')
ax.set_title('Leclerc is')
ax.legend()
plt.show()