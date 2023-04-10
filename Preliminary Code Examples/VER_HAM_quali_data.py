import fastf1
fastf1.Cache.enable_cache('cache')
session = fastf1.get_session(2021, 'Monza', 'Q')

session.load()
fast_hamilton = session.laps.pick_driver('HAM').pick_fastest()
ham_car_data = fast_hamilton.get_car_data()
HAMt = ham_car_data['Time']
HAMvCar = ham_car_data['Speed']
fast_verstappen = session.laps.pick_driver('VER').pick_fastest()
ver_car_data = fast_verstappen.get_car_data()
VERt = ver_car_data['Time']
VERvCar = ver_car_data['Speed']
open('Data/ham_time_data_2021.txt', 'w').write(str(HAMt.to_numpy().astype('timedelta64[ms]')))
open('Data/ham_car_data_2021.txt', 'w').write(str(HAMvCar.to_numpy()))
open('Data/ver_time_data_2021.txt', 'w').write(str(VERt.to_numpy().astype('timedelta64[ms]')))
open('Data/ver_car_data_2021.txt', 'w').write(str(VERvCar.to_numpy()))
with open('Data/ham_car_data_2021.txt', 'r') as infile, open('Data/ham_car_data_2021_clean.txt', 'w') as outfile:
    for line in infile:
        cleaned_line = line.replace('[', '').replace(']', '')
        outfile.write(cleaned_line)

with open('Data/ham_time_data_2021.txt', 'r') as infile, open('Data/ham_time_data_2021_clean.txt', 'w') as outfile:
    for line in infile:
        cleaned_line = line.replace('[', '').replace(']', '')
        outfile.write(cleaned_line)

with open('Data/ver_car_data_2021.txt', 'r') as infile, open('Data/ver_car_data_2021_clean.txt', 'w') as outfile:
    for line in infile:
        cleaned_line = line.replace('[', '').replace(']', '')
        outfile.write(cleaned_line)

with open('Data/ver_time_data_2021.txt', 'r') as infile, open('Data/ver_time_data_2021_clean.txt', 'w') as outfile:
    for line in infile:
        cleaned_line = line.replace('[', '').replace(']', '')
        outfile.write(cleaned_line)

session2022 = fastf1.get_session(2022, 'Monza', 'Q')
session2022.load()
fast_hamilton = session2022.laps.pick_driver('HAM').pick_fastest()
ham_car_data = fast_hamilton.get_car_data()
HAMt = ham_car_data['Time']
HAMvCar = ham_car_data['Speed']
fast_verstappen = session2022.laps.pick_driver('VER').pick_fastest()
ver_car_data = fast_verstappen.get_car_data()
VERt = ver_car_data['Time']
VERvCar = ver_car_data['Speed']
open('Data/ham_time_data_2022.txt', 'w').write(str(HAMt.to_numpy().astype('timedelta64[ms]')))
open('Data/ham_car_data_2022.txt', 'w').write(str(HAMvCar.to_numpy()))
open('Data/ver_time_data_2022.txt', 'w').write(str(VERt.to_numpy().astype('timedelta64[ms]')))
open('Data/ver_car_data_2022.txt', 'w').write(str(VERvCar.to_numpy()))

with open('Data/ham_car_data_2022.txt', 'r') as infile, open('Data/ham_car_data_2022_clean.txt', 'w') as outfile:
    for line in infile:
        cleaned_line = line.replace('[', '').replace(']', '')
        outfile.write(cleaned_line)

with open('Data/ham_time_data_2022.txt', 'r') as infile, open('Data/ham_time_data_2022_clean.txt', 'w') as outfile:
    for line in infile:
        cleaned_line = line.replace('[', '').replace(']', '')
        outfile.write(cleaned_line)

with open('Data/ver_car_data_2022.txt', 'r') as infile, open('Data/ver_car_data_2022_clean.txt', 'w') as outfile:
    for line in infile:
        cleaned_line = line.replace('[', '').replace(']', '')
        outfile.write(cleaned_line)

with open('Data/ver_time_data_2022.txt', 'r') as infile, open('Data/ver_time_data_2022_clean.txt', 'w') as outfile:
    for line in infile:
        cleaned_line = line.replace('[', '').replace(']', '')
        outfile.write(cleaned_line)