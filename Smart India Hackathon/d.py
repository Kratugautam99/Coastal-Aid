import requests

# Define the API endpoint
url = "https://samudra.incois.gov.in/incoismobileappdata/rest/incois/districtpolygons"

# Make a GET request to the API
response = requests.get(url)

# Check if the request was successful

    # Parse the JSON response
data = response.json()
    
    # Extract and print state and district for each feature

for feature in data['features']:
    state = feature['properties']['STATE']
    district = feature['properties']['District']
    if state == 'MAHARASHTRA' and district == 'THANE, MUMBAI SUBURBAN, MUMBAI CITY':
        coordinates = feature['geometry']['coordinates']
        print(f"State: {state}, District: {district}, Coordinates: {coordinates}")







