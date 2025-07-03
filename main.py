import requests
from twilio.rest import Client
import smtplib
from email.message import EmailMessage

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

def send_email():
    email_adress = "<EMAIL>"
    email_pass = "<PASSWORD>"

    msg = EmailMessage()
    msg["Subject"] = "Weather forecast"
    msg["From"] = email_adress
    msg["To"] = email_adress
    msg.set_content("Seni çok seviyorum sevgilim. Bugün yağmur yağabilir. Şemsiyeni yanına al ki günün sorunsuz kuru ve mutlu geçsin.")

    with smtplib.SMTP("smtp.gmail.com", 465) as connection:
        connection.login(email_adress, email_pass)
        connection.send_message(msg)
        print("Email sent.")

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Bring an umbrella!",
        from_="number",
        to="number",
    )
    print(message.status)
    send_email()