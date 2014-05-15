"""
Example:

    python test2.py 33.634271,73.044834 33.659851,73.029041
    python test2.py 33.633876,73.044075 33.633880,73.044145

"""
from math import *
import sys

#Two Example GPS Locations
lat1, lon1 = sys.argv[1].split(',')
lat2, lon2 = sys.argv[2].split(',')
#lat1 = 53.32055555555556
#lat2 = 53.31861111111111
#lon1 = -1.7297222222222221
#lon2 = -1.6997222222222223
Aaltitude = 2000
Oppsite  = 2000

#Haversine Formuala to find vertical angle and distance
lon1, lat1, lon2, lat2 = map(float, [lon1, lat1, lon2, lat2])
lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

dlon = lon2 - lon1
dlat = lat2 - lat1
a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
c = 2 * atan2(sqrt(a), sqrt(1-a))
Base = 6371 * c

#Horisontal Bearing
def calcBearing(lat1, lon1, lat2, lon2):
    dLon = lon2 - lon1
    y = sin(dLon) * cos(lat2)
    x = cos(lat1) * sin(lat2) \
        - sin(lat1) * cos(lat2) * cos(dLon)
    return atan2(y, x)

Bearing = calcBearing(lat1, lon1, lat2, lon2)
Bearing = degrees(Bearing)

Base2 = Base * 1000
distance = Base * 2 + Oppsite * 2 / 2
Caltitude = Oppsite - Aaltitude


#Convertion from radians to decimals
a = Oppsite/Base
b = atan(a)
c = degrees(b)


#Convert meters into Kilometers
distance = distance / 1000


#Output the data
print("---------------------------------------")
print(":::::Auto Aim Directional Anntenna:::::")
print("---------------------------------------")
print("Horizontial Distance:", Base,"km")
print("   Vertical Distance:", distance,"km")
print("    Vertical Bearing:",c)
print(" Horizontial Bearing:",Bearing)
print("---------------------------------------")

