import pandas as pd
import os
import pytest

from fixtures import jet, data_path, project_root


def test_version(jet):
    assert jet.__version__() == "0.0.1"


def test_get_path(jet, data_path):
    assert jet._get_path() == data_path


def test_set_path(jet, data_path):
    pass


def test_get_config(jet):
    assert isinstance(jet.config, dict)


def test_config_not_found(jet):
    jet.path = "invalid_path"
    with pytest.raises(FileNotFoundError):
        jet._load_config()


def test_data_not_found(jet):
    jet.path = "invalid_path"
    with pytest.raises(FileNotFoundError):
        jet._load_data()


def test_config_not_list(jet):
    jet.config = {"dependencies": "not a list"}
    with pytest.raises(TypeError):
        jet._check_dependencies()


def test_config_list(jet):
    jet.config = {"dependencies": ["os"]}
    jet._check_dependencies()


def test_dependencies_not_installed(jet):
    jet.config = {"dependencies": ["not_installed"]}
    with pytest.raises(ImportError):
        jet._check_dependencies()


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
    # create dict instead of df
    df = {"col1": [1, 2], "col2": [3, 4]}

    with pytest.raises(Exception):
        jet.export_df(df, type="csv")
