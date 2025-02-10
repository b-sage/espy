from typing import Union

class Venue:

    id: Union[int, str]
    full_name: str
    city: Union[str, None]
    state: Union[str, None]
    zip_code: Union[int, str, None]
    grass: bool
    indoor: bool

    def __init__(self, id, full_name, city, state, zip_code, grass, indoor):
        self.id = id
        self.full_name = full_name
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.grass = grass
        self.indoor = indoor

    @classmethod
    def from_espn_resp(cls, d):
        return cls(
            d['id'],
            d['fullName'],
            d['address'].get('city'),
            d['address'].get('state'),
            d['address'].get('zipCode'),
            d['grass'],
            d['indoor']
        )
