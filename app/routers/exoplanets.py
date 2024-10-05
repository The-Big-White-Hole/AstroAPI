from fastapi import APIRouter
from app.fixtures.collector import MOCKED_EXOPLANETS
from app.models import Exoplanet, Star

router = APIRouter()




@router.get("/exoplanets")
async def get_exoplanets() -> list[Exoplanet]:
    """
    This method returns a list of all available exoplanets.
    """
    return MOCKED_EXOPLANETS
