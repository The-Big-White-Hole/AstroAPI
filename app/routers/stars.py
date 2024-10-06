from fastapi import APIRouter, Query

from app.constants import DATA_PATH
from app.fixtures.collector import MOCKED_STARS
from app.models import Star
import pandas as pd

router = APIRouter()


@router.get("/exoplanets/{planet_name}/stars")
def get_stars(planet_name: str):
    """
    Returns array of stars and their coordinates.
    """
    planet_namepath = planet_name + ".json"
    filepath = DATA_PATH / planet_namepath
    star_file = pd.read_json(filepath)
    return star_file.to_dict()
