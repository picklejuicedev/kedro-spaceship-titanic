import pytest
from kedro.pipeline import pipeline


from spaceship_titanic.pipelines.use_model.pipeline import (
    use_model_pipe,
    use_model_train_pipe,
)
from kedro.io import MemoryDataSet

from tests.conftest import seq_runner, catalog  # noqa: F401


@pytest.mark.parametrize("filepath", ["conf/test/catalog_use_model.yml"])
def test_use_model_pipeline(seq_runner, catalog):  # noqa: F811
    # create the pipeline
    pipe = pipeline(pipe=use_model_pipe)

    catalog.add("passenderId_list", MemoryDataSet())
    catalog.add("predicted", MemoryDataSet())

    # run the pipeline
    seq_runner.run(pipe, catalog)

    # check passengerId_list and predicted
    passengerId_list = catalog.load("passenderId_list")
    predicted = catalog.load("predicted")

    # assert passengerId_list
    # assert predicted


@pytest.mark.parametrize("filepath", ["conf/test/catalog_use_model.yml"])
def test_use_model_train_pipeline(seq_runner, catalog):  # noqa: F811
    # create the pipeline
    pipe = pipeline(pipe=use_model_train_pipe)

    catalog.add("passenderId_list", MemoryDataSet())
    catalog.add("predicted", MemoryDataSet())

    # run the pipeline
    seq_runner.run(pipe, catalog)

    # check passengerId_list and predicted
    passengerId_list = catalog.load("passenderId_list")
    predicted = catalog.load("predicted")

    # assert passengerId_list
    # assert predicted
