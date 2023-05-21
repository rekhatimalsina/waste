from geopy.geocoders import Nominatim
import geocoder
from haversine import haversine, Unit
geolocator = Nominatim(user_agent="my-app") # Initialize the geolocator with a user agent

location = geolocator.geocode("") # Use an empty string to get the current location

if location:
    latitude = location.latitude
    longitude = location.longitude
    print("Latitude:", latitude)
    print("Longitude:", longitude)
else:
    print("Unable to get the current location.")



# Get the current location based on IP address
g = geocoder.ip('me')

# Print the latitude and longitude
print(g.latlng)
print(g.lat)
print(g.lng)



# Define the coordinates of the two points
point1 = (g.lat, g.lng)  # New York City
point2 = (27.743321799237393, 85.18806653815574)  # Los Angeles

# Calculate the distance between the two points
distance = haversine(point1, point2, unit=Unit.KILOMETERS)

# Print the distance in miles
print(distance)