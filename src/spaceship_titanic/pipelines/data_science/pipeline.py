"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.18.3
"""

from kedro.pipeline import Pipeline, node, pipeline

from .nodes import make_model

model_pipe = pipeline(
    [
            node(
                func=make_model,
                inputs="encoded",
                outputs="regressor",
                name="make_model",
            )
        ],
        inputs="encoded",
        outputs="regressor",
        namespace="model"
)

train_model = pipeline(
    pipe = model_pipe,
    outputs="regressor",
    namespace="train"
)

def create_pipeline(**kwargs) -> Pipeline:
    return train_model
