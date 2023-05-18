from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

import pickle
import pandas as pd
from fastapi.encoders import jsonable_encoder

import os

app = FastAPI(version="0.1.0", title="Edvai Semana 8", description="Proyecto para Bootcamp de EDVAI")


MAIN_FOLDER = os.path.dirname(__file__)
MODEL_PATH = os.path.join(MAIN_FOLDER, "model/rf.pkl")
with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)


class Answer(BaseModel):
    Age: int
    EmploymentType: int
    GraduateOrNot: int
    AnnualIncome: int
    FamilyMembers: int
    ChronicDiseases: int
    FrequentFlyer: int
    EverTravelledAbroad: int


@app.get("/")
async def root():
    return {"message": "Proyecto para Bootcamp de EDVAI"}


@app.post("/prediccion")
def predict_satisfaction_flight(answer: Answer):

    answer_dict = jsonable_encoder(answer)
    
    for key, value in answer_dict.items():
        answer_dict[key] = [value]
    
    single_instance = pd.DataFrame.from_dict(answer_dict)
    
    prediction = model.predict(single_instance)
    # Cast numpy.int64 to just a int
    score = int(prediction[0])
    
    response = {"score": score}
    
    return response


# Corre en http://127.0.0.1:8000 o http://0.0.0.0:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=5000)
