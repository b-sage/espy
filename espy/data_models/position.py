from typing import Union

class Position:

    position_id: Union[int, str]
    name: str
    display_name: str
    abbreviation: str

    def __init__(self, position_id, name, display_name, abbreviation):
        self.position_id = position_id
        self.name = name
        self.display_name = display_name
        self.abbreviation = abbreviation

    @classmethod
    def from_json(cls, d):
        return cls(
            d.get('id'),
            d.get('name'),
            d.get('displayName'),
            d.get('abbreviation')
        )
