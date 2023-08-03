import phonenumbers
import folium
from phonenumbers import geocoder, carrier
from opencage.geocoder import OpenCageGeocode

# Replace 'number' with the phone number you want to look up
number = "+9412345678"

# Parse the phone number
hakNumber = phonenumbers.parse(number, "US")

# Get the location information
yourLocation = geocoder.description_for_number(hakNumber, "en")
print("Location:", yourLocation)

# Get the service provider information
service_provider = carrier.name_for_number(hakNumber, "en")
print("Service Provider:", service_provider)

# Initialize the OpenCage Geocoder with your API key
Key = 'Your Key'
geocoder = OpenCageGeocode(Key)

# Query the location information to get latitude and longitude
query = str(yourLocation)
results = geocoder.geocode(query)

# Extract latitude and longitude
if results and len(results) > 0:
    lat = results[0]['geometry']['lat']
    lng = results[0]['geometry']['lng']
    print("Latitude:", lat)
    print("Longitude:", lng)

    # Create a map and add a marker for the location
    myMap = folium.Map(location=[lat, lng], zoom_start=9)
    folium.Marker([lat, lng], popup=yourLocation).add_to(myMap)

    # Save the map to an HTML file
    myMap.save("myLocation.html")
else:
    print("Location not found.")
