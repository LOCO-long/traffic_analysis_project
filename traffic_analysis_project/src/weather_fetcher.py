# src/weather_fetcher.py
import requests

def get_weather(city, keys):
    url = "https://devapi.qweather.com/v7/weather/now"
    params = {
        "location": city,
        "key": keys["hefeng_key"]
    }
    res = requests.get(url, params=params).json()
    if res.get("code") == "200":
        now = res.get("now", {})
        return {
            "天气": now.get("text"),
            "温度": now.get("temp"),
            "风速": now.get("windSpeed")
        }
    return None
