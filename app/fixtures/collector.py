import polars as pl
import app.constants
from app.models import Exoplanet, Star

planets_df = pl.read_csv(app.constants.PLANETS_FILE_PATH)



PLANET_NAME_FIELD = "pl_name"
RIGHT_ASCENSION_FIELD = "ra"
DECLINATION_FIELD = "dec"
DISTANCE_PARSECS_FIELD = "sy_dist"
DISTANCE_LIGHT_YEARS_FIELD = "sy_dist_ly"

def get_exoplanet_from_entry(planet_entry):
    return Exoplanet(name=planet_entry[PLANET_NAME_FIELD],
                     right_ascension=planet_entry[RIGHT_ASCENSION_FIELD],
                     declination=planet_entry[DECLINATION_FIELD],
                     distance_parsecs=planet_entry[DISTANCE_PARSECS_FIELD],
                     distance_light_years=planet_entry[DISTANCE_LIGHT_YEARS_FIELD])




def get_star_from_entry(star_entry):
    return Star(name=star_entry[PLANET_NAME_FIELD],
                right_ascension=star_entry[RIGHT_ASCENSION_FIELD],
                declination=star_entry[DECLINATION_FIELD],
                distance_parsecs=star_entry[DISTANCE_PARSECS_FIELD],
                distance_light_years=star_entry[DISTANCE_LIGHT_YEARS_FIELD])


MOCKED_EXOPLANETS = []

for planet_entry in planets_df.iter_rows(named=True):
    MOCKED_EXOPLANETS.append(get_exoplanet_from_entry(planet_entry))


stars_df = pl.read_csv(app.constants.STARS_FILE_PATH)




MOCKED_STARS = []

for star_entry in stars_df.iter_rows(named=True):
    MOCKED_STARS.append(get_star_from_entry(star_entry))
