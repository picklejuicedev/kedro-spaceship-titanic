"""
This is a boilerplate test file for pipeline 'data_proc'
generated using Kedro 0.18.3.
Please add your pipeline tests here.

Kedro recommends using `pytest` framework, more info about it can be found
in the official documentation:
https://docs.pytest.org/en/latest/getting-started.html
"""

import pytest
from kedro.pipeline import pipeline
from kedro.runner import SequentialRunner
from kedro.io import DataCatalog
import yaml
from spaceship_titanic.pipelines.data_proc.pipeline import base_proc
from pandas.testing import assert_frame_equal

# tests/conftest.py
@pytest.fixture
def seq_runner():
    return SequentialRunner()


@pytest.fixture
def catalog():
    config = yaml.safe_load(open("conf/base/test_catalog.yml"))
    cat = DataCatalog.from_config(config)
    # print(f"catalog: {cat.list()}")
    return cat


def test_data_proc_pipeline(seq_runner, catalog):
    # create the pipeline
    train_pipe = pipeline(pipe=base_proc)

    # run the pipeline
    seq_runner.run(train_pipe, catalog)

    # check preprocessed matches reference
    df_a = catalog.load("preprocessed")
    df_b = catalog.load("preprocessed_ref")
    assert_frame_equal(df_a, df_b)
