from fastapi import FastAPI,HTTPException
from fastapi.responses import JSONResponse
import numpy as np
import pandas as pd
from pydantic_data.pydnatic_d import student_details
from model.p_model import model
from predict.pridict_output import predict_output



app=FastAPI()


#get request
@app.get("/")
def home():
    return{"message":"welcome to my student data predictions "}

@app.get("/create")
def view_predict_data(d:student_details):
    user_input={
    "age":d.age,
    "gender":d.gender,
    "p_class":d.p_class,
    "study_hours":d.study_hours,
    "attendance":d.attendance,
    "math_score":d.math_score,
    "science_score":d.science_score,
    "english_score":d.english_score,
    "passed":d.passed }

    try:
        prediction=predict_output(user_input)[0]
        return JSONResponse(status_code=200,content={"Responce":str(prediction)})
    except Exception as e:
        return JSONResponse(status_code=500,content=str(e)) 

#post 

@app.post("/create")
def predict_data(d:student_details):
    user_input=pd.DataFrame([{
    "age":d.age,
    "gender":d.gender,
    "p_class":d.p_class,
    "study_hours":d.study_hours,
    "attendance":d.attendance,
    "math_score":d.math_score,
    "science_score":d.science_score,
    "english_score":d.english_score,
    "passed":d.passed }])

    try:
        prediction=model.predict(user_input)[0]
        return JSONResponse(status_code=200,content={"Pass the Exam":str(prediction)})
    except Exception as e:
        return JSONResponse(status_code=500,content=str(e)) 