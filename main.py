import requests
from twilio.rest import Client

api_key = "2e0bf1a62041d45b315023c5acce8fbf"
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
account_sid = "<KEY>"
auth_token = "<PASSWORD>"

weather_parameters = {
    "lat":40.822729,
    "lon":29.394481,
    "appid":api_key,
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params=weather_parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Bring an umbrella!",
        from_="number",
        to="number",
    )
    print(message.status)