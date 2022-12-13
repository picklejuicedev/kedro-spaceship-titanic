"""
This is a boilerplate pipeline 'data_proc'
generated using Kedro 0.18.3
"""

from kedro.pipeline import Pipeline, node, pipeline

from .nodes import create_alone_col, split_name, split_cabin, remove_Nan_values

base_proc = pipeline(
    [
        node(
            func=create_alone_col,
            inputs="input",
            outputs="train_post_alone",
            name="create_alone_column",
        ),
        node(
            func=split_cabin,
            inputs="train_post_alone",
            outputs="train_post_split_cabin",
            name="split_cabin_id",
        ),
        node(
            func=remove_Nan_values,
            inputs="train_post_split_cabin",
            outputs="train_post_Nan",
            name="remove_nan_values",
        ),
        node(
            func=split_name,
            inputs="train_post_Nan",
            outputs="preprocessed",
            name="split_name",
        ),
    ],
    namespace="preproc",
    inputs="input",
    outputs="preprocessed",
)

train_pipe = pipeline(pipe=base_proc, namespace="train")

test_pipe = pipeline(pipe=base_proc, namespace="test")


def create_pipeline(**kwargs) -> Pipeline:
    return train_pipe + test_pipe
