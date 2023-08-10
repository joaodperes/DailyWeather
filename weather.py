import requests
import config
import yagmail
from datetime import datetime

API_KEY = config.API_KEY
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
GEO_URL = "http://api.openweathermap.org/geo/1.0/direct"

city = config.city
limit = 1
lang = config.lang

geo_link = f"{GEO_URL}?q={city}&limit={limit}&appid={API_KEY}"
geo_response = requests.get(geo_link)

if geo_response.status_code == 200:
    geo_data = geo_response.json()

    lat = geo_data[0]['lat']
    lon = geo_data[0]['lon']

    request_url = f"{BASE_URL}?lat={lat}&lon={lon}&appid={API_KEY}&lang={lang}"
    weather_response = requests.get(request_url)

    if weather_response.status_code == 200:
        weather_data = weather_response.json()
        weather = weather_data['weather'][0]['description']
        temperature = round(weather_data["main"]["temp"] - 273.15, 1)
        realfeel = round(weather_data["main"]["feels_like"] - 273.15, 1)
        max_temp = round(weather_data["main"]["temp_max"] - 273.15, 1)
        min_temp = round(weather_data["main"]["temp_min"] - 273.15, 1)

        weather_info = (
                    f"Previsão: {weather.title()}\n"
                    f"Temperatura: {temperature} ºC; Máx: {max_temp} ºC e Min: {min_temp} ºC\n"
                    f"Real-feel: {realfeel} ºC"
                )

        t = datetime.now()
        send_to = config.send_to

        yag = config.yag
        subject = f"Meteorologia - {t.strftime('%d-%m-%y')}"
        contents = [weather_info]
        yag.send(send_to, subject, contents)

    else:
        print("An error occurred while fetching weather data.")
else:
    print("An error occurred while fetching location data.")



