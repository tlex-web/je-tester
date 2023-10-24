import pandas as pd
import os
import pytest

from fixtures import jet, data_path, project_root


def test_version(jet):
    assert jet.__version__() == "0.0.1"


def test_get_path(jet, data_path):
    assert jet._get_path() == data_path


def test_get_config(jet):
    assert isinstance(jet.config, dict)


def test_export_csv(jet, data_path):
    df = pd.DataFrame({"col1": [1, 2], "col2": [3, 4]})
    jet.export_df(df, type="csv")
    assert os.path.exists(f"{data_path}\\data.csv")


def test_export_excel(jet, data_path):
    df = pd.DataFrame({"col1": [1, 2], "col2": [3, 4]})
    jet.export_df(df, type="excel")
    assert os.path.exists(f"{data_path}\\data.xlsx")


def test_export_invalid_type(jet):
    df = pd.DataFrame({"col1": [1, 2], "col2": [3, 4]})
    with pytest.raises(Exception):
        jet.export_df(df, type="invalid")


def test_invalid_export(jet):
    # create invalid dataframe
    df = {"col1": [1, 2], "col2": [3, 4]}

    with pytest.raises(Exception):
        jet.export_df(df, type="csv")
