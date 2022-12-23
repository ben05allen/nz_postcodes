from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
from postcodes import postcodes


geolocator = Nominatim(user_agent='your email adress')
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)


for i, (k, v) in enumerate(postcodes.items(), start=1):
    location = geocode(f'{v}, {k}, New Zealand', limit=1)
    if location:
        print(f'{v} - {k}::{location.latitude},{location.longitude}')
    else:
        print(f'No coordinates for {v}, {k}')


# location = geolocator.geocode('AUCKLAND, 2102')
# if location:
#     print(location.address)
#     print(f'Coordinates: {location.latitude}, {location.longitude}')

# next_location = geolocator.reverse(f'{location.latitude}, {location.longitude}')
# if next_location:
#     print(next_location.address)
