from typing import Union
from espy.data_models.position import Position

class Athlete:

    player_id: Union[int, str]
    first_name: str
    last_name: str
    sport: str
    height: Union[int, str, float]
    weight: Union[int, str, float]
    age: Union[int, str]
    dob: str
    position: Position
    debut_year: Union[int, str]
    birthplace: dict
    is_active: bool

    def __init__(self, player_id, first_name, last_name, full_name, sport, height, weight, age, dob, position, debut_year, birthplace, is_active):
        self.player_id = player_id
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = full_name
        self.sport = sport
        self.height = height
        self.weight = weight
        self.age = age
        self.dob = dob
        self.position = position
        self.debut_year = debut_year
        self.birthplace = birthplace
        self.is_active = is_active

    @classmethod
    def from_json(cls, d):
        return cls(
            d.get('id'),
            d.get('firstName'),
            d.get('lastName'),
            d.get('fullName'),
            d.get('type'),
            d.get('height'),
            d.get('weight'),
            d.get('age'),
            d.get('dateOfBirth'),
            Position.from_json(d.get('position')),
            d.get('debutYear'),
            d.get('birthPlace'),
            d.get('active'),
        )

