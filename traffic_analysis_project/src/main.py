# src/main.py
from route_fetcher import get_routes
from weather_fetcher import get_weather
from poi_analysis import get_poi_density
from utils import load_keys
import csv, os

cases = [
    {"origin": "116.3281,39.9835", "destination": "116.3974,39.9087", "city": "北京"},
    {"origin": "121.4737,31.2304", "destination": "121.4998,31.2397", "city": "上海"}
]

if __name__ == '__main__':
    keys = load_keys()
    out_path = "data/processed/route_comparison.csv"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)

    with open(out_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["origin", "destination", "platform", "distance_km", "duration_min", "weather", "poi_density"])

        for case in cases:
            routes = get_routes(case["origin"], case["destination"], keys)
            weather = get_weather(case["city"], keys)
            poi_density = get_poi_density(case["origin"], 1000, "商场", keys["gaode_key"])
            for r in routes:
                writer.writerow([
                    case["origin"],
                    case["destination"],
                    r["platform"],
                    r["distance_km"],
                    r["duration_min"],
                    weather["天气"] if weather else "",
                    poi_density
                ])
    print("✅ 采集完成")
