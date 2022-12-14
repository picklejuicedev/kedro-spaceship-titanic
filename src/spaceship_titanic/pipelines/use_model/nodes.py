def apply_model(model, df):
    passengerId_list = df["PassengerId"]
    df_dropped = df.drop(columns=["PassengerId", "Firstname", "Lastname"])

    if "Transported" in df_dropped.columns:
        df_dropped = df_dropped.drop(columns=["Transported"])

    pred = model.predict(df_dropped)

    return passengerId_list, pred
