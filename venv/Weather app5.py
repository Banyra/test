import requests

def get_weather_data(city ="Tehran", app_id = "83e2477db62a388beaad80a254cdbdfd" ):
    URL = "https://api.openweathermap.org/data/2.5/weather"
    location = "delhi technological university"
    PARAMS = {"q": city , "appid" : app_id}
    r = requests.get(url = URL , params = PARAMS) 
    return r.json()

# print(get_weather_data())
data = {'coord': {'lon': 51.4215, 'lat': 35.6944}, 'weather': [{'id': 721, 'main': 'Haze', 'description': 'haze', 'icon': '50d'}], 'base': 'stations', 'main': {'temp': 279.88, 'feels_like': 278.48, 'temp_min': 279.66, 'temp_max': 280.94, 'pressure': 1011, 'humidity': 81}, 'visibility': 6000, 'wind': {'speed': 2.06, 'deg': 140}, 'clouds': {'all': 40}, 'dt': 1706359441, 'sys': {'type': 2, 'id': 47737, 'country': 'IR', 'sunrise': 1706326705, 'sunset': 1706363707}, 'timezone': 12600, 'id': 112931, 'name': 
'Tehran', 'cod': 200}
print ("temp:", data ['main']['temp'])
print ("humidity:", data ['main']['humidity'])
print ("datetime:", data ['dt'])
print ("city:", data ['name'])