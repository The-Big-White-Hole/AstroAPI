from fastapi import APIRouter

from app.constants import EXOPLANETS_FILE_PATH, DATA_PATH
from app.fixtures.collector import MOCKED_EXOPLANETS
from app.models import Exoplanet, Star
import pandas as pd
from fastapi.responses import FileResponse


router = APIRouter()


@router.get("/exoplanets")
async def get_exoplanets():
    """
    This method returns a list of all available exoplanets.
    """
    planets_t = pd.read_csv(EXOPLANETS_FILE_PATH)
    return planets_t.to_dict()

@router.get("/exoplanets/{planet_name}/print")
async def get_exoplanet_pdf(planet_name: str):
    planet_namepath = planet_name + ".pdf"
    filepath = DATA_PATH / planet_namepath
    return FileResponse(filepath)
