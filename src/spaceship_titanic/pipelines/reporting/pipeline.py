"""
This is a boilerplate pipeline 'reporting'
generated using Kedro 0.18.3
"""

from kedro.pipeline import Pipeline, node, pipeline

from .nodes import report_kaggle, report_accuracy

report_kaggle_pipe = pipeline(
    [
        node(
            func=report_kaggle,
            inputs=["passenderId_list","predicted"],
            outputs="reported",
            name="report_kaggle",
        )
        
    ],
    inputs=["passenderId_list","predicted"],
    outputs="reported",
    namespace="report_kaggle",
)

kaggle_output = pipeline(
    pipe=report_kaggle_pipe,
    namespace="test"
)

report_train_pipe = pipeline(
    [
        node(
            func=report_accuracy,
            inputs=["y_test","predicted"],
            outputs=None,
            name="report_train",
        )
    ],
    inputs=["y_test","predicted"],
    outputs=None,
    namespace="report_train",
)

train_output = pipeline(
    pipe=report_train_pipe,
    namespace="train"
)

def create_pipeline(**kwargs) -> Pipeline:
    return kaggle_output + train_output
