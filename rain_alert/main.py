import requests

OWM_ENDPOINT = 'https://api.openweathermap.org/data/2.5/forecast'
API_KEY = '35868854d62bb9eff75fda9d312cdd68'
MY_LAT = 51.507351
MY_LONG = -0.127758
parameters = {
    'lat': MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY
}

response = requests.get(OWM_ENDPOINT, params=parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data['list']:
    condition_code = hour_data['weather'][0]['id']
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    print("Bring an umbrella.")