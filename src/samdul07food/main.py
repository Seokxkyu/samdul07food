import os
from typing import Union
from fastapi import FastAPI
import time
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

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
    
    df = pd.DataFrame([[t, name]], columns=['time', 'name'])
    
    dir_path = get_path()

    os.makedirs(dir_path, exist_ok=True)

    file_path = os.path.join(dir_path, 'food07.csv')

    df.to_csv(file_path, mode='a', header=False, index=False)
    
    return {"food": name, "time": t}

