import os
from typing import Union
from fastapi import FastAPI
import time
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import pymysql
import csv
import pytz

app = FastAPI()

origins = [
    "https://samdul07food.web.app",
    "http://localhost:8899",
    "http://127.0.0.1:8899"
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
    k_time = datetime.now(pytz.timezone('Asia/Seoul'))
    t = k_time.strftime('%Y-%m-%d %H:%M:%S')

    # df = pd.DataFrame([[t, name]], columns=['time', 'name'])
    path = get_path()

    dir_path = os.path.join(path, 'data')
    os.makedirs(dir_path, exist_ok=True)

    file_path = os.path.join(dir_path, 'food07.csv')

    data = {"food": name, "time": t}

    with open(file_path, 'a', newline='') as f:
        csv.DictWriter(f, fieldnames=['food', 'time']).writerow(data)
    
    import pymysql.cursors

    connection = pymysql.connect(
            host=os.getenv("DB_IP", "localhost"),
            user='food',
            password='1234',
            database='fooddb',
            port = int(os.getenv("DB_PORT", "33306")), 
            cursorclass=pymysql.cursors.DictCursor
    )
    
    sql = "INSERT INTO foodhistory(`username`, `foodname`, `dt`) VALUES(%s,%s,%s)"
    
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(sql, ('n07', name, t))
        connection.commit()

    '''
    db = pymysql.connect(
            host = '172.17.0.1',
            port = 13306,
            user = 'food',
            passwd = '1234',
            db = 'fooddb',
            charset = 'utf8'
    )

    cursor = db.cursor(pymysql.cursors.DictCursor)
    

    sql = "INSERT INTO foodhistory(username, foodname, dt) VALUES(%s, %s, %s)"
    cursor.execute(sql, ('n07', name, t))
    db.commit()
    # df.to_csv(file_path, mode='a', header=False, index=False)
    '''

    return data
