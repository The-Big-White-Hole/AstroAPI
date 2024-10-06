from fastapi import APIRouter, Query

from app.fixtures.collector import MOCKED_STARS
from app.models import Star

router = APIRouter()


@router.get("/exoplanets/{planet_name}/stars")
def get_stars(planet_name: str):
    """
    Returns array of stars and their coordinates.
    """
    return {"mocha": planet_name}
