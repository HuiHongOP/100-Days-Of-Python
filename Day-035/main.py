import requests

api_key = 'yourownapikey'

# api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API key}
LAT = 40.712776
LONG = 74.005974

parameters = {
    'lat': LAT,
    'lon': LONG,
    'appid':api_key,
    'cnt': 4
}


response = requests.get(url='https://api.openweathermap.org/data/2.5/forecast', params=parameters)
response.raise_for_status()
data = response.json()


will_rain = False
for hour_data in data['list']:
    condition_code = hour_data['weather'][0]['id']
    if int(condition_code) < 700:
        will_rain = True
        
if will_rain:
    print("Bring an umbrella.")