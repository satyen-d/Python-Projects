import requests
from win10toast import ToastNotifier
import json
import time

def updater():
    r = requests.get("https://coronavirus-19-api.herokuapp.com/all")
    data = r.json()
    text = f"Confirmed Cases : {data['cases']} \nDeaths: {data['deaths']}\nRecovered: {data['recovered']}"

    while True:
        t = ToastNotifier()
        t.show_toast("Corona virus rates", text, duration = 20)
        time.sleep(20)


updater()





