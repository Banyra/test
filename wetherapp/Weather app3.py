import requests

URL = f"https://api.openweathermap.org/data/2.5/weather"
location = "delhi technological university"
PARAMS = {"q": "Tehran", "appid" : "83e2477db62a388beaad80a254cdbdfd"}
r = requests.get(url = URL , params = PARAMS) 
data = r.json()
print(data)