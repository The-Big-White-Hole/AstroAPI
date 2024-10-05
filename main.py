from fastapi import FastAPI

from pydantic import BaseModel


app = FastAPI()


class Exoplanet(BaseModel):
    distance: float
    declination: float
    right_ascension: float


@app.get("/")
async def read_root():
    return {"Astro": "API"}


@app.get("/exoplanets")
async def get_exoplanets():
    return None
