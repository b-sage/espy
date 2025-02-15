from espy.endpoints.base import BaseEndpoints
from espy.utils import split_id
from espy.parameters import SeasonType
from espy.data_models.athlete import Athlete
from espy.data_models.team import Team
from espy.data_models.venue import Venue
from espy.data_models.position import Position
from espy.data_models.event import Event
from espy.data_models.season import SeasonPart, Season
from typing import Union

#TODO: should probably use a seperate object for the response parsing eg get_athlete_ids
#TODO: need to think through cases of whether its better to require multiple calls to get the data we need or if just splicing out
#some ID within the object and passing that through is fine. IDs are probably enough in a lot of cases, since we can use for lookups.
#E.g. when we request a season, we don't need to return all of the event/competition objects, just the ids
class ReferenceSportsEndpoints(BaseEndpoints):
    base_url = "https://sports.core.api.espn.com/v2/sports/{}/leagues/{}/"
    supported_sports = ["football", "basketball", "baseball"]
    supported_leagues = ["mlb", "nba", "nfl"]

    def __init__(self, sport: str, league: str):
        super().__init__(sport, league)
        self.base_url = self.base_url.format(sport, league)
    
    def _extract_ids(self, func, **kwargs):
        ids = []
        pg = 1
        while True:
            result = func(page=pg, **kwargs)
            ids += [split_id(item['$ref']) for item in result['items']]
            if result['pageIndex'] == result['pageCount']:
                return ids
            pg += 1

    #TODO: active flag doesn't seem to work.
    def _get_athletes(self, limit: int=1000, active: bool=True, page: int=1):
        query = self._build_query(False, limit=limit, active=active, page=page)
        return self._execute_request("athletes" + query)

    #kind of annoying we're going to end up parsing a bunch of urls just to rebuild them later...
    def get_athlete_ids(self):
        return self._extract_ids(self._get_athletes)

    def get_athlete(self, id_: Union[int, str]):
        return Athlete.from_espn_resp(self._execute_request(f"athletes/{id_}"))




    def _get_teams(self, limit: int=32, page: int=1):
        query = self._build_query(False, limit=limit, page=page)
        return self._execute_request("teams" + query)

    def get_team_ids(self):
        return self._extract_ids(self._get_teams)

    def get_team(self, id_: Union[int, str]):
        return Team.from_espn_resp(self._execute_request(f"teams/{id_}"))




    def _get_positions(self, limit: int=75, page: int=1):
        query = self._build_query(False, limit=limit, page=page)
        return self._execute_request("positions" + query)

    def get_position_ids(self):
        return self._extract_ids(self._get_positions)

    def get_position(self, id_: Union[int, str]):
        return Position.from_espn_resp(self._execute_request(f"positions/{id_}"))




    def _get_venues(self, limit: int=700, page: int=1):
        query = self._build_query(False, limit=limit, page=page)
        return self._execute_request("venues" + query)

    def get_venue_ids(self):
        return self._extract_ids(self._get_venues)

    def get_venue(self, id_: Union[int, str]):
        return Venue.from_espn_resp(self._execute_request(f"venues/{id_}"))




    def _get_leaders(self, limit: int=100, page: int=1):
        query = self._build_query(False, limit=limit, page=page)
        return self._execute_request("leaders" + query)



    def _get_seasons(self, limit: int=100, page: int=1):
        query = self._build_query(False, limit=limit, page=page)
        return self._execute_request("seasons" + query)

    def get_season_ids(self):
        return self._extract_ids(self._get_seasons)

    def get_season(self, year: Union[int, str]):
        return Season.from_espn_resp(self._execute_request(f"seasons/{year}"))

    def get_season_part(self, year: Union[int, str], type_: SeasonType):
        return SeasonPart.from_espn_resp(self._execute_request(f"seasons/{year}/types/{type_.value}"))




    def _get_events_by_season_and_week(self, year: Union[int, str], week: Union[int, str], season_type: Union[int, str], limit: int=100, page: int=1):
        query = self._build_query(False, limit=limit, page=page)
        return self._execute_request(f"seasons/{year}/types/{season_type}/weeks/{week}/events" + query)

    def get_event_ids_by_season_and_week(self, year: Union[int, str], week: Union[int, str], season_type: Union[int, str]=2):
        return self._extract_ids(self._get_events_by_season_and_week, year=year, week=week, season_type=season_type)

    def get_event(self, id_: Union[int, str]):
        return Event.from_espn_resp(self._execute_request(f"events/{id_}"))


class ReferenceSiteEndpoints(BaseEndpoints):
    pass
    
