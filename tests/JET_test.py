import pandas as pd
import os
import pytest

from JET import JETester

path = "./tests/test_data"


@pytest.fixture
def jet():
    return JETester(path)


def test_version(jet):
    assert jet.__version__() == "0.0.1"


def test_get_path(jet):
    assert jet._get_path() == path


def test_get_config(jet):
    assert isinstance(jet._get_config(), dict)


def test_export_csv(jet):
    df = pd.DataFrame({"col1": [1, 2], "col2": [3, 4]})
    jet.export_df(df, type="csv")
    assert os.path.exists(f"{path}/data.csv")


def test_export_excel(jet):
    df = pd.DataFrame({"col1": [1, 2], "col2": [3, 4]})
    jet.export_df(df, type="excel")
    assert os.path.exists(f"{path}/data.xlsx")


def test_export_invalid_type(jet):
    df = pd.DataFrame({"col1": [1, 2], "col2": [3, 4]})
    with pytest.raises(ValueError):
        jet.export_df(df, type="invalid")
