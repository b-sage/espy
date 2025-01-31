from .base import BaseEndpoints

class GameNightEndpoints(BaseEndpoints):

    base_url = "https://site.api.espn.com/apis/site/v2/"
    supported_sports = ["football"]
    supported_leagues = ["nfl"]

    def get_monday_games(self):
        return self._execute_request("mondaynightfootball")

    def get_thursday_games(self):
        return self._execute_request("thursdaynightfootball")

    def get_sunday_games(self):
        return self._execute_request("sundaynightfootball")
