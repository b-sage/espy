from typing import Union

class Venue:

    venue_id: Union[int, str]
    full_name: str
    address: dict
    grass: bool
    indoor: bool

    def __init__(self, venue_id, full_name, address, grass, indoor):
        self.venue_id = venue_id
        self.full_name = full_name
        self.address = address
        self.grass = grass
        self.indoor = indoor

    @classmethod
    def from_json(cls, d):
        return cls(
            d.get('id'),
            d.get('fullName'),
            d.get('address'),
            d.get('grass'),
            d.get('indoor')
        )
