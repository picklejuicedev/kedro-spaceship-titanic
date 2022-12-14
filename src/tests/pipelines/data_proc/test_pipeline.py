import pytest
from kedro.pipeline import pipeline
from spaceship_titanic.pipelines.data_proc.pipeline import base_proc
from pandas.testing import assert_frame_equal

from tests.conftest import seq_runner, catalog  # noqa: F401 - disable linting error


@pytest.mark.parametrize("filepath", ["conf/base/test/catalog_data_proc.yml"])
def test_data_proc_pipeline(seq_runner, catalog):  # noqa: F811 - disable linting error
    # create the pipeline
    train_pipe = pipeline(pipe=base_proc)

    # run the pipeline
    seq_runner.run(train_pipe, catalog)

    # check preprocessed matches reference
    df_a = catalog.load("preprocessed")
    df_b = catalog.load("preprocessed_ref")
    assert_frame_equal(df_a, df_b)
