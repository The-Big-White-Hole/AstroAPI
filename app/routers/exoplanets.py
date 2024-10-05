from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class Exoplanet(BaseModel):
    distance_parsecs: float
    distance_light_years: float
    declination: float
    right_ascension: float
    name: str


MOCK_EXOPLANETS = [
    Exoplanet(
        name="OGLE-2005-BLG-390L b",
        right_ascension=268.579958,
        declination=-30.3773056,
        distance_parsecs=6600.0,
        distance_light_years=21526.296,
    ),
    Exoplanet(
        name="K2-332 b",
        right_ascension=135.8832666,
        declination=14.2504994,
        distance_parsecs=123.202,
        distance_light_years=401.83071512,
    ),
]


@router.get("/exoplanets")
async def get_exoplanets() -> list[Exoplanet]:
    """
    This method returns a list of all available exoplanets.
    """
    return MOCK_EXOPLANETS
