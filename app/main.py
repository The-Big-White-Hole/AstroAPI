import os
from fastapi import FastAPI

from app.constants import FAPI_ROOT_PATH
from app.routers import stars, exoplanets

app = FastAPI(root_path=FAPI_ROOT_PATH)

app.include_router(stars.router)
app.include_router(exoplanets.router)


if __name__ == "__main__":
    import uvicorn

    port = int(os.getenv("PORT", 8090))

    uvicorn.run(app, host="0.0.0.0", port=port)
