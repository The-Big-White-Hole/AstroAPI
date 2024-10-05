from pydantic import BaseModel


class CelestialObject(BaseModel):
    distance_parsecs: float
    distance_light_years: float
    declination: float
    right_ascension: float
    name: str


class Exoplanet(CelestialObject):
    pass

class Star(CelestialObject):
    pass