import os
from fastapi import FastAPI

from app.constants import FAPI_ROOT_PATH
from app.routers import stars, exoplanets

from fastapi.middleware.cors import CORSMiddleware


origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://127.0.0.1",
    "http://127.0.0.1:3000",
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "https://localhost",
    "https://127.0.0.1",
    "*",
]


app = FastAPI(root_path=FAPI_ROOT_PATH)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(stars.router)
app.include_router(exoplanets.router)


if __name__ == "__main__":
    import uvicorn

    port = int(os.getenv("PORT", 8090))

    uvicorn.run(app, host="0.0.0.0", port=port)
