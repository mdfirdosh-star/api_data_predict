import pandas as pd
from model.p_model import model
def predict_output(user_input:dict):
    data=pd.DataFrame([user_input])
    pridict_df=model.predict(data)[0]
    return pridict_df
