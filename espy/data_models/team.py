from typing import Union
from espy.utils import split_id

class Team:

    id: Union[int, str]
    location: str
    name: str
    nickname: Union[str, None]
    abbreviation: str
    display_name: str
    color: str
    is_active: bool
    venue_id: Union[int, str]
    
    def __init__(self, id, location, name, nickname, abbreviation, display_name, color, is_active, venue_id):
        self.id = id
        self.location = location
        self.name = name
        self.nickname = nickname
        self.abbreviation = abbreviation
        self.display_name = display_name
        self.color = color
        self.is_active = is_active
        self.venue_id = venue_id

    @classmethod
    def from_espn_resp(cls, d):
        return cls(
            d['id'],
            d['location'],
            d['name'],
            d.get('nickname'),
            d['abbreviation'],
            d['displayName'],
            d['color'],
            d['isActive'],
            d['venue']['id']
        )
