
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from lightgbm import LGBMClassifier

from sklearn.metrics import accuracy_score, log_loss, precision_score, recall_score, f1_score
from sklearn.model_selection import train_test_split,cross_validate,cross_val_score
from sklearn.preprocessing import StandardScaler

import pandas as pd


def make_model(df: pd.DataFrame):
    
    target_df = df["Transported"]
    
    X_train,X_test,y_train,y_test = train_test_split(df,target_df,test_size=0.3,random_state=1234)

    X_train = X_train.drop(columns=["PassengerId", "Firstname","Lastname", "Transported"])
    X_test = X_test.drop(columns=["Transported"])

    #clf = LogisticRegression(max_iter=3000)
    clf = LGBMClassifier()
    model = clf.fit(X_train, y_train)
    return model, X_test, y_test
