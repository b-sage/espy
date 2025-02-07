from typing import Union
from espy.utils import split_id

class Athlete:

    player_id: Union[int, str]
    first_name: str
    last_name: str
    sport: str
    height: Union[int, str, float]
    weight: Union[int, str, float]
    age: Union[int, str]
    dob: str
    position_id: Union[int, str]
    team_id: Union[int, str]
    debut_year: Union[int, str]
    experience: Union[int, str]
    birthplace: dict
    is_active: bool

    def __init__(
            self, 
            player_id, 
            first_name, 
            last_name, 
            full_name, 
            sport, 
            height, 
            weight, 
            age, 
            dob, 
            position_id, 
            team_id,
            debut_year,
            experience,
            birthplace, 
            is_active
    ):
        self.player_id = player_id
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = full_name
        self.sport = sport
        self.height = height
        self.weight = weight
        self.age = age
        self.dob = dob
        self.position_id = position_id
        self.team_id = team_id
        self.debut_year = debut_year
        self.experience = experience
        self.birthplace = birthplace
        self.is_active = is_active

    @classmethod
    def from_espn_resp(cls, d):
        return cls(
            d['id'],
            d['firstName'],
            d['lastName'],
            d['fullName'],
            d['type'],
            d['height'],
            d['weight'],
            d['age'],
            d['dateOfBirth'],
            d['position']['id'],
            split_id(d['team']['$ref']),
            d['debutYear'],
            d['experience'].get('years', 0),
            d['birthPlace'],
            d['active'],
        )

