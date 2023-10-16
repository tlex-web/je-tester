import importlib
import json

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
        if isinstance(self.config["dependencies"], list):
            for dependency in self.config["dependencies"]:
                try:
                    importlib.import_module(dependency)
                except ImportError:
                    raise ImportError(f"Dependency {dependency} not installed")
        else:
            raise TypeError("Dependencies must be a list")

    def _load(self):
        self._load_config()
        self._load_data()
        self._check_dependencies()

    def _load_config(self):
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
        if type == "csv":
            return dataframe.to_csv(f"{self.path}/data.csv")
        elif type == "excel":
            return dataframe.to_excel(f"{self.path}/data.xlsx", engine="xlsxwriter")
        else:
            raise ValueError("type must be either 'csv' or 'excel'")


if __name__ == "__main__":
    t = JETester("./tests/test_data")
    print(t)
    print(t.config)
    print(t.data)
    print(t._get_path())
    print(t.__print__())
