from typing import Union
from espy.data_models.venue import Venue
from espy.data_models.weather import Weather

class Competition:

    competition_id: Union[int, str]
    date: str
    attendance: Union[int, str]
    time_valid: bool
    date_valid: bool
    neutral_site: bool
    division_competition: bool
    conference_competition: bool
    preview_available: bool
    recap_available: bool
    boxscore_avilable: bool
    lineup_available: bool
    gamecast_available: bool
    play_by_play_available: bool
    conversation_available: bool
    commentary_available: bool
    pickcenter_available: bool
    summary_availabe: bool
    live_available: bool
    tickets_available: bool
    shotchart_available: bool
    timeouts_available: bool
    posession_arrow_available: bool
    on_watch_espn: bool
    recent: bool
    bracket_available: bool
    wallclock_available: bool
    venue: Venue
    weather: Weather
