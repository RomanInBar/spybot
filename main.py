from fastapi import FastAPI

from app.routers import router as urls_router


api = FastAPI(
    title='Spybot'
)
api.include_router(urls_router)
