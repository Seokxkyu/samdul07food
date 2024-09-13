import os

app = FastAPI()


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
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return {"food": name, "time": time}
