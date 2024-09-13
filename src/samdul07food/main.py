from typing import Union
from fastapi import FastAPI
import pickle
import pandas as pd
from datetime import datetime

app = FastAPI()


def get_path():
    file_path = __file__
    dirpath = os.path.dirname(file_path)
    return dirpath

@app.get("/")
def read_root():
    return {"Hello": "n07"}

@app.get("/food")
def food(name: str):
    
    # 시간을 구함
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    df = pd.DataFrame([[name, time]], columns=['food', 'time'])
    
    dir_path = get_path()    
    file_path = os.path.join(dir_path, 'food07.csv')
    
    os.makedirs(dir_path, exist_ok=True)
    
    # 음식 이름과 시간을 csv로 저장 -> /code/data/food.csv
    df.to_csv(file_path, mode='a', header=False, index=False)

    return {"food": name, "time": time}

