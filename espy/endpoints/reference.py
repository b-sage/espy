from base import BaseEndpoints

class ReferenceSportsEndpoints(BaseEndpoints):
    base_url = "https://sports.core.api.espn.com/v2/sports/{}/leagues/{}/"
    supported_sports = ["football", "basketball", "baseball"]
    supported_leagues = ["mlb", "nba", "nfl"]

    def __init__(self, sport: str, league: str):
        super().__init__(sport, league)
        self.base_url = self.base_url.format(sport, league)

    def get_athletes(self, limit: int=1000, active: bool=True, page: int=1):
        query = self._build_query(False, limit=limit, active=active, page=page)
        return self._execute_request("athletes" + query)


class ReferenceSiteEndpoints(BaseEndpoints):
    pass
    
