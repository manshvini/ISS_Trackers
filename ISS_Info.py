import json
from urllib.request import urlopen

def iss_current_location():
    with urlopen("http://api.open-notify.org/iss-now.json", timeout=10) as response:
        return json.load(response)