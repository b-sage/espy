from typing import Union

class Weather:

    type: str
    display_value: str
    zip_code: Union[int, str]
    last_updated: str
    wind_speed: Union[int, str]
    wind_direction: str
    temperature: Union[int, str]
    high_temperature: Union[int, str]
    low_temperature: Union[int, str]
    condition_id: Union[int, str]
    gust: Union[int, str]
    precipitation: Union[int, str]

    def __init__(
        self,
        display_value,
        zip_code,
        last_updated,
        wind_speed,
        wind_direction,
        temperature,
        high_temp,
        low_temp,
        condition_id,
        gust,
        precipitation
    ):
        self.display_value = display_value
        self.zip_code = zip_code
        self.last_updated = last_updated
        self.wind_speed = wind_speed
        self.wind_direction = wind_direction
        self.temperature = temperature
        self.high_temperature = high_temp
        self.low_temperature = low_temp
        self.condition_id = condition_id
        self.gust = gust
        self.precipitation = precipiation

    @classmethod
    def from_json(cls, d):
        return cls(
            d.get('displayValue'),
            d.get('zipCode'),
            d.get('lastUpdated'),
            d.get('windSpeed'),
            d.get('windDirection'),
            d.get('temperature'),
            d.get('highTemperature'),
            d.get('lowTemperature'),
            d.get('condition_id'),
            d.get('gust'),
            d.get('precipiation')
        )
