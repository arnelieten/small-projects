from geopy.geocoders import Nominatim
import math

geolocator = Nominatim(user_agent="arne lieten")
location_1 = geolocator.geocode(str(input('Enter city 1: ')))
location_2 = geolocator.geocode(str(input('Enter city 2: ')))

location_1_latitude = location_1.latitude*(math.pi/180)
location_1_longitude = location_1.longitude*(math.pi/180)
location_2_latitude = location_2.latitude*(math.pi/180)
location_2_longitude = location_2.longitude*(math.pi/180)

# haversine formula to calculate distance on a circle (earth)
distance = 1.852*3440.1*math.acos((math.sin(location_1_latitude)*math.sin(location_2_latitude))+(math.cos(location_1_latitude)*math.cos(location_2_latitude)*math.cos(location_1_longitude-location_2_longitude)))
distance = format(float(distance),'.1f')

print(distance,'km')