from typing import Union

class Competitor:

    id: Union[int, str]
    type: str
    order: int
    home_away: str
    winner: bool
    
    def __init__(self, id, type, order, home_away, winner):
        self.id = id
        self.type = type
        self.order = order
        self.home_away = home_away
        self.winner = winner

    @classmethod
    def from_espn_resp(cls, d):
        return cls(
            d['id'],
            d['type'],
            d['order'],
            d['homeAway'],
            d['winner']
        )

