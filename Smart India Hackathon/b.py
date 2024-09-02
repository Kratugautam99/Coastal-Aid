import requests
import json

# URL of the INCOIS Tsunami API
url = "https://gemini.incois.gov.in/api/ws/tsunami"
# Send a GET request to the API
response = requests.get(url)
# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    # Example of accessing specific data
    for feature in data['features']:
        properties = feature['properties']
        print(f"Event ID: {properties['EVID']}")
        print(f"Region: {properties['REGIONNAME']}")
        print(f"Evaluation: {properties['EVALUATION']}")
        print(f"Details: {properties['detail']}\n")
else:
    print(f"Failed to retrieve data. HTTP Status code: {response.status_code}")
