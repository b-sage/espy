import requests
from typing import List

class BaseEndpoints:

    base_url: str
    supported_sports: List[str]
    supported_leagues: List[str]
    are_enabled: bool
    
    def __init__(self, sport: str, league: str):
        self.session = requests.Session()
        if sport not in self.supported_sports or league not in self.supported_leagues:
            self.are_enabled = False
        else:
            self.are_enabled = True

    def _execute_request(self, endpoint):
        if not self.are_enabled:
            assert False, "Add a real error here, we're trying to call a disabled endpoint"
        res = self.session.get(self.base_url + endpoint)
        assert res.status_code == 200, f"Bad status code: {res.status_code}"
        return res.json()

    def _build_query(self, has_query: bool, **kwargs):
        if all(not v for v in kwargs.values()):
            return ''
        start = '&' if has_query else '?'
        return start + '&'.join([f"{k}={v}" for k, v in kwargs.items() if v is not None])
    
