from typing import Union
from datetime import datetime

class SeasonPart:

    id: Union[int, str]
    type: Union[int, str]
    name: str
    abbreviation: str
    start_date: datetime
    end_date: datetime



