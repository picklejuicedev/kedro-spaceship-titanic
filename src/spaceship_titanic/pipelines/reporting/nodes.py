import pandas as pd
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
)


def report_kaggle(
    passengerId_list: pd.Series, predicted_target: pd.Series
) -> pd.DataFrame:
    df_out = pd.DataFrame(
        {"PassengerId": passengerId_list, "Transported": predicted_target}
    )
    return df_out


def report_accuracy(y_test, y_pred):
    print("Accuracy =", "%.2f" % (accuracy_score(y_test, y_pred) * 100), "%")
    print("Precision =", "%.2f" % (precision_score(y_test, y_pred) * 100), "%")
    print("Recall =", "%.2f" % (recall_score(y_test, y_pred) * 100), "%")
    print("F1-Score =", "%.2f" % (f1_score(y_test, y_pred) * 100), "%")
