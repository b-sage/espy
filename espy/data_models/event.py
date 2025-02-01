from typing import Union
from espy.data_models.venue import Venue

class Event:

    event_id: Union[int, str]
    date: str
    name: str
    short_name: str
    venues: Venue

    def __init__(self, event_id, date, name, short_name, venues):
        self.event_id = event_id
        self.date = date
        self.name = name
        self.short_name = short_name
        self.venues = venues


