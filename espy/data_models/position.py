from typing import Union
from espy.utils import split_id

class Position:

    position_id: Union[int, str]
    name: str
    display_name: str
    abbreviation: str
    parent_id: Union[int, str, None]

    def __init__(self, position_id, name, display_name, abbreviation, parent_id):
        self.position_id = position_id
        self.name = name
        self.display_name = display_name
        self.abbreviation = abbreviation
        self.parent_id = parent_id

    @classmethod
    def from_espn_resp(cls, d):
        return cls(
            d['id'],
            d['name'],
            d['displayName'],
            d['abbreviation'],
            split_id(d['parent']['$ref']) if d['leaf'] else None
        )
