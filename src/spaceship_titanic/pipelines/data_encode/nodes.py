from sklearn.preprocessing import LabelEncoder
import pandas as pd


def encode_train_data(df: pd.DataFrame) -> pd.DataFrame:
    cols = ['HomePlanet', "CryoSleep", "Deck", "Side", "Destination","VIP", "Firstname","Lastname"]
    df[cols] = df[cols].apply(LabelEncoder().fit_transform)

    return df