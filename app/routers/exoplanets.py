from fastapi import APIRouter

from app.constants import EXOPLANETS_FILE_PATH
from app.fixtures.collector import MOCKED_EXOPLANETS
from app.models import Exoplanet, Star
import pandas as pd

router = APIRouter()


@router.get("/exoplanets")
async def get_exoplanets():
    """
    This method returns a list of all available exoplanets.
    """
    planets_t = pd.read_csv(EXOPLANETS_FILE_PATH)
    return planets_t.to_dict()
