from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
import joblib
import pandas as pd

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
    
forest_pipeline = joblib.load("./models/best_Random Forest_model.pkl")
k_nearest_pipeline = joblib.load("./models/best_K-Nearest Neighbors_model.pkl")

@app.get('/')
def home():
    return{"status Health": "OK"}

@app.post('/predict_k_nearest')
def k_nearest_prediction(data:features):
    #convert model to a dictionary and then a dataframe
    df = pd.DataFrame([data.model_dump()])

    #make prediction
    prediction= k_nearest_pipeline.predict(df)

    #covert prediction array to int
    prediction = int(prediction[0])

    # Map numerical prediction to "Yes" or "No"
    prediction_label = "Yes" if prediction == 1 else "No"

    #extract probabilities
    probabilities = forest_pipeline.predict_proba(df)
    probabilities = probabilities[0]
    
    # convert probabilities to list
    probabilities = probabilities.tolist()
    

    return {'Prediction':prediction_label, 'Probabilities':probabilities}

@app.post('/predict_random_forest')
def random_forest_prediction(data:features):

    #convert model to a dictionary and then a dataframe
    df = pd.DataFrame([data.model_dump()])

    #make prediction
    prediction= forest_pipeline.predict(df)

    #covert prediction array to int
    prediction = int(prediction[0])

    # Map numerical prediction to "Yes" or "No"
    prediction_label = "Yes" if prediction == 1 else "No"

    #extract probabilities
    probabilities = forest_pipeline.predict_proba(df)
    probabilities = probabilities[0]
    
    # convert probabilities to list
    probabilities = probabilities.tolist()
    

    return {'Prediction':prediction_label, 'Probabilities':probabilities}

@app.get('/')
def documentation():
    return{'description':'All'}


    

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000, debug=True)