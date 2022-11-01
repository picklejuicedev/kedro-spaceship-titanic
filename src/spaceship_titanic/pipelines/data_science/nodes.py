
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score, log_loss, precision_score, recall_score, f1_score
from sklearn.model_selection import train_test_split,cross_validate,cross_val_score
from sklearn.preprocessing import StandardScaler

import pandas as pd


def make_model(df: pd.DataFrame):
    train_df = df.drop(columns=["PassengerId", "Firstname","Lastname", "Transported"])
    target_df = df["Transported"]
    
    clf = RandomForestClassifier()
    return clf.fit(train_df, target_df)