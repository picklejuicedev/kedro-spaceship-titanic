import pytest
from kedro.pipeline import pipeline

from spaceship_titanic.pipelines.data_encode.pipeline import encode_pipe
from pandas.testing import assert_frame_equal

from tests.conftest import seq_runner, catalog  # noqa: F401


@pytest.mark.parametrize("filepath", ["conf/test/catalog_data_encode.yml"])
def test_data_proc_pipeline(seq_runner, catalog):  # noqa: F811
    # create the pipeline
    pipe = pipeline(pipe=encode_pipe)

    # run the pipeline
    seq_runner.run(pipe, catalog)

    # check preprocessed matches reference
    df_a = catalog.load("encoded")
    df_b = catalog.load("encoded_ref")
    assert_frame_equal(df_a, df_b)
