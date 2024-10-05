from fastapi import APIRouter, Query

from app.fixtures.collector import MOCKED_STARS
from app.models import Star

router = APIRouter()


@router.get("/stars")
def get_stars(count: int = Query(100, title="Number of Stars", ge=1, le=10000)) -> list[Star]:
    """
    Returns array of stars and their coordinates.
    Parameters:
      - count (int): Stars count (100 by default, minimal is 1, maximal is 10000).
    """
    return MOCKED_STARS[:count]
