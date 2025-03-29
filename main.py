# pyright: basic

import tomllib

from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter

geolocator = Nominatim(user_agent="your email adress")
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)

RATE_LIMIT = 0.5

with open("postcodes.toml", "rb") as f:
    file_contents = tomllib.load(f)

for i, (k, v) in enumerate(file_contents["postcodes"].items(), start=1):
    location = geocode(f"{v}, {k}, New Zealand", limit=RATE_LIMIT)
    if location:
        print(f"{v} - {k}:\t{location.latitude}, {location.longitude}")
    else:
        print(f"No coordinates for {v}, {k}")

    if i > 5:
        break
