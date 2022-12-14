"""
This module contains an end2end test of the entire pipeline.

Tests should be placed in ``src/tests``, in modules that mirror your
project's structure, and in files named test_*.py. They are simply functions
named ``test_*`` which test a unit of logic.

"""

from pathlib import Path

import pytest
from sklearn.metrics import accuracy_score


from kedro.framework.project import settings
from kedro.config import ConfigLoader
from kedro.framework.context import KedroContext
from kedro.framework.hooks import _create_hook_manager

from kedro.framework.startup import bootstrap_project
from kedro.framework.session.session import KedroSession
from kedro.io import DataCatalog
import yaml


@pytest.fixture
def config_loader():
    return ConfigLoader(conf_source=str(Path.cwd() / settings.CONF_SOURCE))


@pytest.fixture
def project_context(config_loader):
    return KedroContext(
        package_name="spaceship_titanic",
        project_path=Path.cwd(),
        config_loader=config_loader,
        hook_manager=_create_hook_manager(),
    )


def test_pipeline_end2end(project_context):
    """Test pipeline end-to-end."""
    # run the entire project
    bootstrap_project(Path.cwd())
    with KedroSession.create() as session:
        session.run()

    # check if we have the expected files
    assert (Path.cwd() / "data" / "02_intermediate" / "test_preprocessed.pq").exists()
    assert (Path.cwd() / "data" / "02_intermediate" / "train_preprocessed.pq").exists()
    assert (Path.cwd() / "data" / "03_primary" / "test_encoded.pq").exists()
    assert (Path.cwd() / "data" / "03_primary" / "train_encoded.pq").exists()
    assert (Path.cwd() / "data" / "06_models" / "regressor.pickle").exists()
    assert (Path.cwd() / "data" / "07_model_output" / "predicted.csv").exists()

    # run the resulting model with known data and assess the result
    config = yaml.safe_load(open("conf/test/catalog_end2end.yml"))
    cat = DataCatalog.from_config(config)
    model = cat.load("regressor")
    X_test = cat.load("X_test")
    y_test = cat.load("y_test")
    X_test = X_test.drop(
        columns=["PassengerId", "Firstname", "Lastname", "Transported"]
    )

    y_pred = model.predict(X_test)

    ref_model = cat.load("regressor_ref")

    y_pred_ref = ref_model.predict(X_test)
    ref_accuracy = accuracy_score(y_test, y_pred_ref)

    # expected accuracy within 1% of reference model
    assert accuracy_score(y_test, y_pred) > (ref_accuracy - 0.01)
