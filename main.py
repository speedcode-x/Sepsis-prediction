from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel


app = FastAPI()

class features(BaseModel):
    PRG:int
    Age:int
    PL:int
    PR:int
    SK:int
    TS:int
    M11:float
    BD2:float
    

@app.get('/')
def home():
    return{"status Health": "OK"}


def random_forest_prediction(data:features):
    pass

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000, debug=True)