from base import BaseEndpoints

class ReferenceSportsEndpoints(BaseEndpoints):
    base_url = "https://sports.core.api.espn.com/v2/sports/{}/leagues/{}/"
    supported_sports = ["football", "basketball", "baseball"]
    supported_leagues = ["mlb", "nba", "nfl"]

    def __init__(self, sport: str, league: str):
        super().__init__(sport, league)
        self.base_url = self.base_url.format(sport, league)
    
    #TODO: active flag doesn't seem to work.
    def _get_athletes(self, limit: int=1000, active: bool=True, page: int=1):
        query = self._build_query(False, limit=limit, active=active, page=page)
        return self._execute_request("athletes" + query)

    #kind of annoying we're going to end up parsing a bunch of urls just to rebuild them later...
    def get_athlete_ids(self):
        ids = []
        pg = 1
        while True:
            athletes = self._get_athletes(page=pg)
            ids += [item['$ref'].split('/')[-1].split('?')[0] for item in athletes['items']]
            if athletes['pageIndex'] == athletes['pageCount']:
                return ids
            pg += 1

    def _get_teams(self, limit: int=32, page: int=1):
        query = self._build_query(False, limit=limit, page=page)
        return self._execute_request("teams" + query)

    def get_team_ids(self):
        ids = []
        pg = 1
        while True:
            teams = self._get_teams(page=pg)
            ids += [item['$ref'].split('/')[-1].split('?')[0] for item in teams['items']]
            if teams['pageIndex'] == teams['pageCount']:
                return ids
            pg += 1


class ReferenceSiteEndpoints(BaseEndpoints):
    pass
    
