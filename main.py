import datetime
import time
from skyfield.api import load, Topos, EarthSatellite

TLE_FILE = "https://celestrak.com/NORAD/elements/active.txt" # DB file to download

MIN_DEGREE = 45
MIN_AZ = 50
MAX_AZ = 140

satellites = load.tle(TLE_FILE)
ts = load.timescale()
t = ts.now()

location_user = Topos('55.7522200 N', '37.6155600 E')

location_ship = Topos('66 N', '168.97 W')

m = []
for sat in satellites.values():
        difference_user = sat - location_user
        topocentric_user = difference_user.at(t)

        alt_user, az_user, distance_user = topocentric_user.altaz()


        azValue_user = int(str(az_user).replace('deg', '').split(" ")[0])

        if alt_user.degrees >= MIN_DEGREE and azValue_user >= MIN_AZ and azValue_user <= MAX_AZ:
            m.append([sat.name, alt_user, az_user])

for i in range(1,len(m),2):
    print(*m[i])

print("----------------------------------------------------------------------------------------------------")

n = []
for sat in satellites.values():
        difference_ship = sat - location_ship
        topocentric_ship = difference_ship.at(t)

        alt_ship, az_ship, distance_ship = topocentric_ship.altaz()


        azValue_ship = int(str(az_ship).replace('deg', '').split(" ")[0])

        if alt_ship.degrees >= 5 and azValue_ship >= MIN_AZ and azValue_ship <= MAX_AZ:
            n.append([sat.name, alt_ship, az_ship])

for i in range(1,len(n),2):
    print(*n[i])

print("----------------------------------------------------------------------------------------------------")

