import pytest
from kedro.pipeline import pipeline
from sklearn.metrics import accuracy_score


from spaceship_titanic.pipelines.data_science.pipeline import model_pipe

from tests.conftest import seq_runner, catalog  # noqa: F401


@pytest.mark.parametrize("filepath", ["conf/base/test/catalog_data_science.yml"])
def test_data_proc_pipeline(seq_runner, catalog):  # noqa: F811
    # create the pipeline
    pipe = pipeline(pipe=model_pipe)

    # run the pipeline
    seq_runner.run(pipe, catalog)

    # check preprocessed matches reference
    model = catalog.load("regressor")
    # run over known test training data and get at least matching accuracy
    X_test = catalog.load("X_test")
    y_test = catalog.load("y_test")
    y_pred = model.predict(X_test)

    ref_model = catalog.load("regressor_ref")
    y_pred_ref = ref_model.predict(X_test)
    ref_accuracy = accuracy_score(y_test, y_pred_ref)

    # expected accuracy within 1% of reference model
    assert accuracy_score(y_test, y_pred) > (ref_accuracy - 0.01)
