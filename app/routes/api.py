from fastapi import APIRouter
from controllers import shortUrlController

routers = APIRouter()
routers.include_router(shortUrlController.router)