import os
from typing import Union
from fastapi import FastAPI
from datetime import datetime
import time
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:8899",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_path():
    file_path = __file__
    dirpath = os.path.dirname(file_path)
    print(dirpath)
    return dirpath

@app.get("/")
def read_root():
    return {"Hello": "n07"}

@app.get("/food")
def food(name: str):

    # 시간을 구함
    t = time.strftime("%Y-%m-%d %H:%M:%S")
    print(t)
    return {"food": name, "time": t}

