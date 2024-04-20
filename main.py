from urllib.parse import quote_plus

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from yaml import load, FullLoader

import domain.file_system.file_system_controller
from domain.mongo.conn import mongo

with open('config.yaml') as f:
    configs = load(f, Loader=FullLoader)

MongoUri = "mongodb://%s:%s@%s" % (
    quote_plus(configs["Mongo"]["MongoUser"]), quote_plus(configs["Mongo"]["MongoPassword"]), configs["Mongo"]["MongoHost"]
)

# Use Like Singleton
mongo.init_app(uri=MongoUri, port=configs["Mongo"]["MongoPort"])

app = FastAPI()

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(domain.file_system.file_system_controller.router)
