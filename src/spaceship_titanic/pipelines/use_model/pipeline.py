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
            outputs="predicted",
            name="use_model",
        )
    ],
    inputs=["regressor","encoded"],
    outputs="predicted",
    namespace="use_model"
)

predict_test_pipe = pipeline(
    pipe=use_model_pipe,
    inputs="regressor",
    namespace="test"
)

def create_pipeline(**kwargs) -> Pipeline:
    return predict_test_pipe
