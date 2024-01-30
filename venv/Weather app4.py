import requests

def get_weather_data(city ="Tehran", app_id = "83e2477db62a388beaad80a254cdbdfd" ):
    URL = "https://api.openweathermap.org/data/2.5/weather"
    location = "delhi technological university"
    PARAMS = {"q": city , "appid" : app_id}
    r = requests.get(url = URL , params = PARAMS) 
    return r.json()

print(get_weather_data())