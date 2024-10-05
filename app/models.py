from pydantic import BaseModel


class CelestialObject(BaseModel):
    distance_parsecs: float
    declination: float
    right_ascension: float
    name: str

class Exoplanet(CelestialObject):
    distance_light_years: float

class Star(CelestialObject):
    apparent_magnitude: float
    stellar_parallax: float
