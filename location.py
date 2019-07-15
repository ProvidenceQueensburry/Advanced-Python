#!/usr/bin/python
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="specify_your_app_name_here")
locationA = geolocator.geocode("cape coast")
print(locationA)
print((locationA.latitude, locationA.longitude))

locationB = geolocator.geocode("Takoradi")
print(locationB)
print((locationB.latitude, locationB.longitude))

#finding distance btn capecoast and takoradi
from geopy.distance import geodesic
cape_coast = (locationA.latitude,locationA.longitude )
Takoradi = (locationB.latitude, locationB.longitude)
print(geodesic(cape_coast,Takoradi ).miles)
