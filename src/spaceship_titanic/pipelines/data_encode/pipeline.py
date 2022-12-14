"""
This is a boilerplate pipeline 'data_encode'
generated using Kedro 0.18.3
"""

from kedro.pipeline import Pipeline, node, pipeline

from .nodes import encode_train_data

encode_pipe = pipeline(
    [
        node(
            func=encode_train_data,
            inputs="preprocessed",
            outputs="encoded",
            name="encode_categorical_data",
        )
    ],
    inputs="preprocessed",
    outputs="encoded",
    namespace="encode",
)

train_encode = pipeline(pipe=encode_pipe, namespace="train")

test_encode = pipeline(pipe=encode_pipe, namespace="test")


def create_pipeline(**kwargs) -> Pipeline:
    return train_encode + test_encode
