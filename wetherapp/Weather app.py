
import requests


URL ="https://api.openweathermap.org/data/2.5/weather?q=Isfahan&appid=83e2477db62a388beaad80a254cdbdfd"
location = "delhi technological university"
# PARAMS = {'address':location} 
r = requests.get(url = URL) 
data = r.json()
print(data)


