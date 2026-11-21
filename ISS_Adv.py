import time, math
from urllib.request import urlopen
import json

R_EARTH = 6371.0  # km

def get_position():
    with urlopen("http://api.open-notify.org/iss-now.json", timeout=10) as r:
        d = json.load(r)
    p = d["iss_position"]
    return d["timestamp"], float(p["latitude"]), float(p["longitude"]) 

def haversine(lat1, lon1, lat2, lon2):
  
    p1, p2 = math.radians(lat1), math.radians(lat2)
    dphi = p2 - p1
    dlmb = math.radians(lon2 - lon1)
    a = math.sin(dphi / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dlmb / 2) ** 2
    return 2 * R_EARTH * math.asin(math.sqrt(a))

log = [get_position()]
max_lat = 0.0
while True:
    time.sleep(5)
    t, lat, lon = get_position()
    t0, lat0, lon0 = log[-1]
    if t == t0:
        continue                
    speed = haversine(lat0, lon0, lat, lon) / (t - t0)
    max_lat = max(max_lat, abs(lat))
    log.append((t, lat, lon))
    print(f"ground speed {speed:.2f} km/s | max |lat| so far {max_lat:.1f}")