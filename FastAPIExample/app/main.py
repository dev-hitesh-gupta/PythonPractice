from fastapi import FastAPI
from FastAPIExample.app.controllers import router

app = FastAPI()

app.include_router(router)
