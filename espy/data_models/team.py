from typing import Union
from espy.data_models.venue import Venue

class Team:

    team_id: Union[int, str]
    location: str
    name: str
    nickname: str
    abbreviation: str
    display_name: str
    color: str
    is_active: bool
    venue: Venue
    
    def __init__(self, team_id, location, name, nickname, abbreviation, display_name, color, is_active, venue):
        self.team_id = team_id
        self.location = location
        self.name = name
        self.nickname = nickname
        self.abbreviation = abbreviation
        self.display_name = display_name
        self.color = color
        self.is_active = is_active
        self.venue = venue

    @classmethod
    def from_json(cls, d):
        return cls(
            d.get('id'),
            d.get('location'),
            d.get('name'),
            d.get('nickname'),
            d.get('abbreviation'),
            d.get('displayName'),
            d.get('color'),
            d.get('isActive'),
            Venue.from_json(d.get('venue'))
        )
