
import pandas as pd


def report_kaggle(passengerId_list: pd.Series, predicted_series: pd.Series) -> pd.DataFrame:
    df_out = pd.DataFrame(
            {
            'PassengerId': passengerId_list,
            'Transported': predicted_series
            }
        )
    return df_out