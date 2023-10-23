import pandas as pd
import os
import pytest

import importlib
import json
import sys


def exception_handler(
    debug, exception_type, exception, traceback, debug_hook=sys.excepthook
):
    if debug:
        debug_hook(exception_type, exception, traceback)
    else:
        print("%s: %s" % (exception_type.__name__, exception))


# data preparation and sanitization should be handled outside the class
# since the quality and the completeness of the dataset is unknown


class JETester:
    """
    A class to perform journal entry tests

    Attributes
    ----------
    path : str
        The path to the journal entry test
    config : dict
        The configuration of the journal entry test
    data : dict
        The data of the journal entry test

    Methods
    -------
    __version__()
        Returns the version of the journal entry test
    """

    def __init__(self, path: str):
        """
        Parameters
        ----------

        path : str
            The path to the journal entry test

        Returns
        -------
        None
        """
        self.path = path
        self.df = None
        self.config = {}
        self.is_dev = True
        self._load()

    def __version__(self):
        return "0.0.1"

    def __repr__(self):
        return f"JETester(path={self.path})"

    def __str__(self):
        return f"JETester(path={self.path})"

    def __print__(self):
        return f"{self}"

    def _check_dependencies(self):
        """
        Checks if the dependencies are installed

        Returns
        -------
        None
        """

        try:
            if isinstance(self.config["dependencies"], list):
                for dependency in self.config["dependencies"]:
                    try:
                        importlib.import_module(dependency)
                    except ImportError:
                        raise ImportError(f"Dependency {dependency} not installed")
            else:
                raise TypeError("Dependencies must be a list")
        except Exception as e:
            exception_handler(self.is_dev, e, e, e)

    def _load(self) -> None:
        self._load_config()
        self._load_data()
        self._check_dependencies()

    def _load_config(self) -> None:
        """
        Loads the configuration of the journal entry test

        Returns
        -------
        None

        Raises
        ------
        FileNotFoundError
            If the config.json file is not found

        JSONDecodeError
            If the config.json file is not a valid JSON file
        """
        self.config = {}
        with open(self.path + "/config.json") as f:
            self.config = json.load(f)

    def _load_data(self):
        self.data = {}
        with open(self.path + "/data.json") as f:
            self.data = json.load(f)

    def _save_config(self):
        with open(self.path + "/config.json", "w") as f:
            json.dump(self.config, f)

    def _save_data(self):
        with open(self.path + "/data.json", "w") as f:
            json.dump(self.data, f)

    def _save(self):
        self._save_config()
        self._save_data()

    def _get_data(self, key: str):
        return self.data[key]

    def _set_data(self, key: str, value: str):
        self.data[key] = value
        self._save_data()

    def _get_config(self, key: str):
        return self.config[key]

    def _set_config(self, key: str, value: str):
        self.config[key] = value
        self._save_config()

    def _get_data_path(self):
        return self.path + "/data.json"

    def _get_config_path(self):
        return self.path + "/config.json"

    def _get_path(self):
        return self.path

    def export_df(self, dataframe, type="csv") -> None:
        """
        Exports the dataframe to a csv or excel file

        Parameters
        ----------
        type : str
            The type of file to export to (either 'csv' or 'excel')

        Returns
        -------
        None
        """

        try:
            if type == "csv":
                return dataframe.to_csv(f"{self.path}/data.csv")
            elif type == "excel":
                return dataframe.to_excel(f"{self.path}/data.xlsx", engine="xlsxwriter")
            else:
                raise ValueError("type must be either 'csv' or 'excel'")

        except Exception as e:
            exception_handler(self.is_dev, e, e, e)


path = "tests/test_data"


@pytest.fixture
def jet():
    return JETester(os.path.join(os.getcwd(), path))


def test_version(jet):
    assert jet.__version__() == "0.0.1"


def test_get_path(jet):
    assert jet._get_path() == os.path.join(os.getcwd(), path)


def test_get_config(jet):
    assert isinstance(jet.config, dict)


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
    with pytest.raises(Exception):
        jet.export_df(df, type="invalid")


def test_invalid_export(jet):
    # create invalid dataframe
    df = {"col1": [1, 2], "col2": [3, 4]}

    with pytest.raises(Exception):
        jet.export_df(df, type="csv")
