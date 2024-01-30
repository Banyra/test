import requests
import time
import sqlite3

def sql_connector():
    con = sqlite3.connect("weather.db")
    cur = con.cursor()
    return con, cur

def creat_table(con , cur):
    cur.execute("CREATE TABLE IF NOT EXISTS weather(name TEXT, datetime TEXT, temp TEXT, humidity TEXT)")
    con.commit()

def insert_data(con, cur, data):
    cur.execute("INSERT INTO weather values(?,?,?,?)", tuple ([v for k,v in "data.items"()]))
    con.commit()
    
def proccess_data(data):
    return {"city": data ['name'] ,"datetime": time.ctime (int(data ['dt'])) ,"temp": data ['main']['temp'] ,"humidity": data ['main']['humidity']}
def get_weather_data(city ="Tehran", app_id = "83e2477db62a388beaad80a254cdbdfd" ):
    URL = "https://api.openweathermap.org/data/2.5/weather"
    PARAMS = {"q": city , "appid" : app_id}
    r = requests.get(url = URL , params = PARAMS) 
    return proccess_data (r.json())

con , cur = sql_connector()
creat_table(con, cur)

while True:
    data_weather = get_weather_data("Tehran")
    insert_data(con,cur,'dataweather')
    print(data_weather)
    time.sleep(5)

