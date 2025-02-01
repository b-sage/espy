from espy.endpoints.base import BaseEndpoints
from espy.data_models.athlete import Athlete
from espy.data_models.team import Team
from espy.data_models.venue import Venue
from espy.data_models.position import Position
from typing import Union

def split_id(url):
    return url.split('/')[-1].split('?')[0]

#TODO: should probably use a seperate object for the response parsing eg get_athlete_ids
class ReferenceSportsEndpoints(BaseEndpoints):
    base_url = "https://sports.core.api.espn.com/v2/sports/{}/leagues/{}/"
    supported_sports = ["football", "basketball", "baseball"]
    supported_leagues = ["mlb", "nba", "nfl"]

    def __init__(self, sport: str, league: str):
        super().__init__(sport, league)
        self.base_url = self.base_url.format(sport, league)
    
    def _extract_ids(self, func):
        ids = []
        pg = 1
        while True:
            result = func(page=pg)
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
        return Athlete.from_json(self._execute_request(f"athletes/{id_}"))




    def _get_teams(self, limit: int=32, page: int=1):
        query = self._build_query(False, limit=limit, page=page)
        return self._execute_request("teams" + query)

    def get_team_ids(self):
        return self._extract_ids(self._get_teams)

    def get_team(self, id_: Union[int, str]):
        result = self._execute_request(f"teams/{id_}")
        venue_id = result['venue']['id']
        return Team.from_json(self._execute_request(f"teams/{id_}"))




    def _get_positions(self, limit: int=75, page: int=1):
        query = self._build_query(False, limit=limit, page=page)
        return self._execute_request("positions" + query)

    def get_position_ids(self):
        return self._extract_ids(self._get_positions)

    def get_position(self, id_: Union[int, str]):
        return Position.from_json(self._execute_request(f"positions/{id_}"))




    def _get_venues(self, limit: int=700, page: int=1):
        query = self._build_query(False, limit=limit, page=page)
        return self._execute_request("venues" + query)

    def get_venue_ids(self):
        return self._extract_ids(self._get_venues)

    def get_venue(self, id_: Union[int, str]):
        return Venue.from_json(self._execute_request(f"venues/{id_}"))




    def _get_leaders(self, limit: int=100, page: int=1):
        query = self._build_query(False, limit=limit, page=page)
        return self._execute_request("leaders" + query)



    def _get_seasons(self, limit: int=100, page: int=1):
        query = self._build_query(False, limit=limit, page=page)
        return self._execute_request("seasons" + query)

    def get_seasons(self):
        return self._extract_ids(self._get_seasons)

    def get_season(self, year: Union[int, str]):
        return self._execute_request(f"seasons/{year}")

    


    def get_event(self, id_: Union[int, str]):
        return self._execute_request(f"events/{id_}")


class ReferenceSiteEndpoints(BaseEndpoints):
    pass
    
