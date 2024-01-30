import requests

def proccess_data(data):
    return {"city": data ['name'] ,"datetime": data ['dt'] ,"temp": data ['main']['temp'] ,"humidity": data ['main']['humidity']}
def get_weather_data(city ="Tehran", app_id = "83e2477db62a388beaad80a254cdbdfd" ):
    URL = "https://api.openweathermap.org/data/2.5/weather"
    location = "delhi technological university"
    PARAMS = {"q": city , "appid" : app_id}
    r = requests.get(url = URL , params = PARAMS) 
    return proccess_data (r.json())

print(get_weather_data("Tehran"))
