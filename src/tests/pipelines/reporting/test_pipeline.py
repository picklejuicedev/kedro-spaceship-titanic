import pytest
from kedro.pipeline import pipeline
import pandas as pd
from pandas.testing import assert_frame_equal

from spaceship_titanic.pipelines.reporting.pipeline import kaggle_output, train_output
from kedro.io import MemoryDataSet

from tests.conftest import seq_runner, catalog  # noqa: F401


@pytest.mark.parametrize("filepath", ["conf/base/test/catalog_reporting.yml"])
def test_kaggle_output(seq_runner, catalog):  # noqa: F811
    data = {
        "PassengerId": ["0001_01", "0002_01", "0002_02", "0003_01"],
        "Transported": [True, False, False, True],
    }
    df_result = pd.DataFrame(data)

    passenger_id = pd.Series(["0001_01", "0002_01", "0002_02", "0003_01"])
    transported = pd.Series([True, False, False, True])

    catalog.add("test.passenderId_list", MemoryDataSet(data=passenger_id))
    catalog.add("test.predicted", MemoryDataSet(data=transported))

    # create the pipeline
    pipe = pipeline(pipe=kaggle_output)

    # run the pipeline
    seq_runner.run(pipe, catalog)

    # check preprocessed matches reference
    reported = catalog.load("test.reported")
    assert_frame_equal(reported, df_result)


@pytest.mark.parametrize("filepath", ["conf/base/test/catalog_reporting.yml"])
def test_report_accuracy(seq_runner, catalog):  # noqa: F811

    y_test = pd.Series([True, False, True, True])
    y_pred = pd.Series([True, False, False, True])

    catalog.add("train.y_test", MemoryDataSet(data=y_test))
    catalog.add("train.predicted", MemoryDataSet(data=y_pred))

    # create the pipeline
    pipe = pipeline(pipe=train_output)

    # run the pipeline
    seq_runner.run(pipe, catalog)

    # not much else to check, just ensure it runs
