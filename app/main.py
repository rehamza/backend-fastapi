import uvicorn
import models
from fastapi import FastAPI
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from routes.api import routers as api_routers
from config import config
from config.database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

setting = config.Settings()

origins=[setting.ORIGIN_URL1]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(api_routers)

if __name__ == '__main__':
    uvicorn.run("main:app", host=setting.HOST, port=setting.PORT, log_level="info", reload=True)
    print("running")