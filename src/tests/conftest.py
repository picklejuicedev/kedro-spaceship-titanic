import pytest
from kedro.runner import SequentialRunner
from kedro.io import DataCatalog
import yaml


@pytest.fixture
def seq_runner():
    return SequentialRunner()


@pytest.fixture
def catalog(filepath: str) -> DataCatalog:
    config = yaml.safe_load(open(filepath))
    cat = DataCatalog.from_config(config)
    # print(f"catalog: {cat.list()}")
    return cat
