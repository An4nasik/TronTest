from fastapi import FastAPI
from app.api.tron_router import router
import uvicorn
from app.core.database import init_db
from app.logging_config import setup_logging
import logging
from contextlib import asynccontextmanager

setup_logging()
logger = logging.getLogger("app")

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Application startup")
    await init_db()
    yield
    logger.info("Application shutdown")

app = FastAPI(lifespan=lifespan)
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        log_level="info",
    )