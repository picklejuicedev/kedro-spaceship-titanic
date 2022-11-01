"""
This is a boilerplate pipeline 'use_model'
generated using Kedro 0.18.3
"""

from kedro.pipeline import Pipeline, node, pipeline

from .nodes import apply_model

use_model_pipe = pipeline(
    [
        node(
            func=apply_model,
            inputs=["regressor","encoded"],
            outputs=["passenderId_list","predicted"],
            name="use_model",
        )
    ],
    inputs=["regressor","encoded"],
    outputs=["passenderId_list","predicted"],
    namespace="use_model"
)

predict_test_pipe = pipeline(
    pipe=use_model_pipe,
    inputs="regressor",
    namespace="test"
)

use_model_train_pipe = pipeline(
    [
        node(
            func=apply_model,
            inputs=["regressor","X_test"],
            outputs=["passenderId_list","predicted"],
            name="use_model",
        )
    ],
    inputs=["regressor","X_test"],
    outputs=["passenderId_list","predicted"],
    namespace="use_model"
)

predict_train_pipe = pipeline(
    pipe=use_model_train_pipe,
    inputs="regressor",
    namespace="train"
)

def create_pipeline(**kwargs) -> Pipeline:
    return predict_test_pipe + predict_train_pipe
