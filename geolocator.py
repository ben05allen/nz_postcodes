from geopy.geocoders import Nominatim
from .sporty_models import Address


geolocator = Nominatim(user_agent='your email adress')


def find_coords(address: Address):
    address_string = ', '.join((getattr(address, attr)) 
                            for attr in ['street', 'suburb', 'city', 'country']
                            if getattr(address, attr))
    location = geolocator.geocode(address_string)
    return location.latitude, location.longitude
