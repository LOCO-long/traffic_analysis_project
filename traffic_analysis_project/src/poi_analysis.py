# src/poi_analysis.py
import requests

def get_poi_density(location, radius, keyword, key):
    url = "https://restapi.amap.com/v3/place/around"
    params = {
        "location": location,
        "radius": radius,
        "keywords": keyword,
        "key": key,
        "offset": 25,
        "page": 1
    }
    total = 0
    while True:
        res = requests.get(url, params=params).json()
        if res.get("status") != "1": break
        pois = res.get("pois", [])
        total += len(pois)
        if len(pois) < 25: break
        params["page"] += 1
    return total