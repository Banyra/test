import requests

city = "Tehran"
app_id = "83e2477db62a388beaad80a254cdbdfd"

URL = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city , app_id)
location = "delhi technological university"
# PARAMS = {'address':location}
r = requests.get(url = URL) 
data = r.json()
print(data)