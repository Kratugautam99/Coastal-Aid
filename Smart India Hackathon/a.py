import requests
import json
import time


api_url = "https://samudra.incois.gov.in/incoismobileappdata/rest/incois/hwassalatestdata"

def fetch_real_time_data():
    try:
        response = requests.get(api_url)
        
        if response.status_code == 200 or response.status_code == 202:
            print(f"Data fetched with status code {response.status_code}.")
            
            data = response.json()
            
            latest_date = data.get("LatestHWADate", "No date provided")
            high_wave_alerts = json.loads(data.get("HWAJson", "[]"))

            print(f"Latest Data Date: {latest_date}")
            for alert in high_wave_alerts:
                district = alert.get("District", "Unknown District")
                state = alert.get("STATE", "Unknown State")
                message = alert.get("Message", "No message provided")
                wave_height_range = message.split("range of ")[1].split(" meters")[0] if "range of " in message else "Unknown range"
                alert_type = alert.get("Alert", "No alert type")
                color_code = alert.get("Color", "No color code")
                issue_date = alert.get("Issue Date", "No issue date")

                print(f"District: {district}, State: {state}")
                print(f"Alert: {alert_type} ({color_code} alert)")
                print(f"Wave Height: {wave_height_range} meters")
                print(f"Issue Date: {issue_date}")
                print(f"Message: {message}\n")

        else:
            print(f"Unexpected status code received: {response.status_code}")
            print("Response content for debugging:", response.text)

    except Exception as e:
        print("An error occurred:", str(e))


if __name__ == "__main__":
    fetch_interval = 60 * 5  

    while True:
        fetch_real_time_data()
        time.sleep(fetch_interval)
