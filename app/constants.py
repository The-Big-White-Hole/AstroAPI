import pathlib

ROOT_PATH = pathlib.Path(__file__).parent.parent

DATA_PATH = ROOT_PATH / "data"

PLANETS_FILE_PATH = DATA_PATH / "planets.csv"
STARS_FILE_PATH = DATA_PATH / "stars.csv"

FAPI_ROOT_PATH = "/api/v1"