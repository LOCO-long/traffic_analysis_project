# src/route_fetcher.py
import requests

def get_routes(origin, destination, keys):
    routes = []
    # 百度路线
    baidu_url = "https://api.map.baidu.com/directionlite/v1/driving"
    baidu_params = {
        "origin": origin,
        "destination": destination,
        "ak": keys["baidu_key"]
    }
    baidu_res = requests.get(baidu_url, params=baidu_params).json()
    if baidu_res.get("status") == 0:
        route = baidu_res["result"]["routes"][0]
        routes.append({
            "platform": "baidu",
            "distance_km": route["distance"] / 1000,
            "duration_min": route["duration"] / 60
        })

    # 高德路线
    gaode_url = "https://restapi.amap.com/v3/direction/driving"
    gaode_params = {
        "origin": origin,
        "destination": destination,
        "key": keys["gaode_key"]
    }
    gaode_res = requests.get(gaode_url, params=gaode_params).json()
    if gaode_res.get("status") == "1":
        route = gaode_res["route"]["paths"][0]
        routes.append({
            "platform": "gaode",
            "distance_km": float(route["distance"]) / 1000,
            "duration_min": float(route["duration"]) / 60
        })
    print(response.url)
    print(response.text)
    return routes