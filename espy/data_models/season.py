from typing import Union
from datetime import datetime

class SeasonPart:

    id: Union[int, str]
    type: Union[int, str]
    name: str
    abbreviation: str
    year: Union[int, str]
    start_date: datetime
    end_date: datetime
    has_groups: bool
    has_standings: bool
    has_legs: bool

    def __init__(
        self,
        id,
        type,
        name,
        abbreviation,
        year,
        start_date,
        end_date,
        has_groups,
        has_standings,
        has_legs
    ):
        self.id = id
        self.type = type
        self.name = name
        self.abbreviation = abbreviation
        self.year = year
        self.start_date = start_date
        self.end_date = end_date
        self.has_groups = has_groups
        self.has_standings = has_standings
        self.has_legs = has_legs


    @classmethod
    def from_espn_resp(cls, d):
        return cls(
            d['id'],
            d['type'],
            d['name'],
            d['abbreviation'],
            d['year'],
            datetime.strptime(d['startDate'], "%Y-%m-%dT%H:%MZ"),
            datetime.strptime(d['endDate'], "%Y-%m-%dT%H:%MZ"),
            d['hasGroups'],
            d['hasStandings'],
            d['hasLegs']
        )

class Season:

    year: Union[int, str]
    start_date: datetime
    end_date: datetime
    display_name: str

    def __init__(self, year, start_date, end_date, display_name):
        self.year = year
        self.start_date = start_date
        self.end_date = end_date
        self.display_name = display_name

    @classmethod
    def from_espn_resp(cls, d):
        return cls(
            d['year'],
            d['startDate'],
            d['endDate'],
            d['displayName']
        )

