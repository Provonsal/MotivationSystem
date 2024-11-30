from contextlib import asynccontextmanager
from fastapi import FastAPI
from sql.base import init_models

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_models()
    yield
    

app = FastAPI(lifespan=lifespan)
