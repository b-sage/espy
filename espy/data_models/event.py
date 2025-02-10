from typing import List, Union
from datetime import datetime
from espy.utils import split_id

class Event:

    id: Union[int, str]
    date: str
    name: str
    short_name: str
    season: Union[int, str]
    season_type: Union[int, str]
    week: Union[int, str]
    time_valid: bool
    venue_ids: List[Union[int, str]]
    league: str

    def __init__(
        self,
        id,
        date,
        name,
        short_name,
        season,
        season_type,
        week,
        time_valid,
        venue_ids,
        league
    ):
        self.id = id
        self.date = date
        self.name = name
        self.short_name = short_name
        self.season = season
        self.season_type = season_type
        self.week = week
        self.time_valid = time_valid
        self.venue_ids = venue_ids
        self.league = league

    @classmethod
    def from_espn_resp(cls, d):
        return cls(
            d['id'],
            datetime.strptime(d['date'], "%Y-%m-%dT%H:%MZ"),
            d['name'],
            d['shortName'],
            split_id(d['season']['$ref']),
            split_id(d['seasonType']['$ref']),
            split_id(d['week']['$ref']),
            d['timeValid'],
            [split_id(item['$ref']) for item in d['venues']],
            split_id(d['league']['$ref'])
        )

