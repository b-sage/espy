from typing import Union
from datetime import datetime
from espy.utils import split_id

class Athlete:

    id: Union[int, str]
    first_name: str
    last_name: str
    sport: str
    height: Union[int, str, float]
    weight: Union[int, str, float]
    age: Union[int, str]
    dob: datetime
    position_id: Union[int, str]
    team_id: Union[int, str]
    debut_year: Union[int, str]
    experience: Union[int, str] 
    birth_city: Union[str, None]
    birth_state: Union[str, None]
    birth_country: Union[str, None]
    is_active: bool

    def __init__(
            self, 
            id, 
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
            birth_city,
            birth_state,
            birth_country,
            is_active
    ):
        self.id = id
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
            datetime.strptime(d['dateOfBirth'], "%Y-%m-%dT%H:%MZ"),
            d['position']['id'],
            split_id(d['team']['$ref']),
            d['debutYear'],
            d['experience'].get('years', 0),
            d['birthPlace'].get('city'),
            d['birthPlace'].get('state'),
            d['birthPlace'].get('country'),
            d['active'],
        )

