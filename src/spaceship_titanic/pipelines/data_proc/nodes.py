import pandas as pd


def create_alone_col(df: pd.DataFrame) -> pd.DataFrame:
    split_df = df["PassengerId"].str.split(pat="_", expand=True)
    alone = split_df[0].value_counts()
    split_df = split_df.merge(alone.rename("groupSize"), left_on=0, right_index=True)
    df["groupSize"] = split_df["groupSize"]
    return df


def split_cabin(df: pd.DataFrame) -> pd.DataFrame:
    df_cab = df["Cabin"].str.split(pat="/", expand=True)
    df["Deck"] = df_cab[0]
    df["Room"] = df_cab[1]
    df["Side"] = df_cab[2]
    df = df.drop("Cabin", axis=1)
    df["Room"] = df["Room"].fillna(0).astype("int64")
    return df


def remove_Nan_values(df: pd.DataFrame) -> pd.DataFrame:
    cols = ["RoomService", "FoodCourt", "ShoppingMall", "Spa", "VRDeck"]
    df[cols] = df[cols].fillna(0.0)
    df["Age"] = df["Age"].fillna(27)
    df["Name"] = df["Name"].fillna("No Name")
    df["Room"] = df["Room"].fillna(0)
    return df


def split_name(df: pd.DataFrame) -> pd.DataFrame:
    df_split = df["Name"].str.split(expand=True)
    df["Firstname"] = df_split[0]
    df["Lastname"] = df_split[1]
    df = df.drop("Name", axis=1)
    return df
