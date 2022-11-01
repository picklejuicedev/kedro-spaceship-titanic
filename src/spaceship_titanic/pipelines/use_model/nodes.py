import pandas as pd

def apply_model(model, df):
    passengerId_list = df["PassengerId"]
    df_dropped = df.drop(columns=["PassengerId","Firstname","Lastname"])
    pred = model.predict(df_dropped)
    
    return passengerId_list, pred