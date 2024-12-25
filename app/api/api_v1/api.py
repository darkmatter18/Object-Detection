from fastapi import APIRouter

from .endpoints import detect


api_router = APIRouter()

api_router.include_router(detect.router, prefix="/detect", tags=["Detect Object"])
