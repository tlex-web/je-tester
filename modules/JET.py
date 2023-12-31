import importlib
import json
import os
import pandas as pd

from reports.reports import Report, ReportContext


# data preparation and sanitization should be handled outside the class
# since the quality and the completeness of the dataset is unknown


class JETester:
    """
    A class to perform journal entry tests

    Attributes
    ----------
    path : str
        The path to the journal entry test

    Methods
    -------
    """

    def __init__(self, path: str, reporter: Report):
        """
        Parameters
        ----------

        path : str
            The path to the journal entry test

        Returns
        -------
        None
        """
        self.path = path if os.path.exists(path) else os.mkdir(path) or path
        self.df = None
        self.reporter = reporter
        self.config = {}
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
        if "dependencies" in self.config:
            if isinstance(self.config["dependencies"], list):
                for dependency in self.config["dependencies"]:
                    try:
                        importlib.import_module(dependency)
                    except ImportError:
                        raise ImportError(f"Dependency {dependency} not installed")
            else:
                raise TypeError("Dependencies must be a list")

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
        try:
            with open(self.path + "config.json") as f:
                self.config = json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(
                "config.json not found at: " + self.path + "config.json"
            )

    def _load_data(self):
        self.data = {}
        with open(self.path + "data.json") as f:
            self.data = json.load(f)

    def _save_config(self):
        with open(self.path + "config.json", "w") as f:
            json.dump(self.config, f)

    def _save_data(self):
        with open(self.path + "data.json", "w") as f:
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
        return self.path + "data.json"

    def _get_config_path(self):
        return self.path + "config.json"

    def _get_path(self):
        return self.path

    def _get_df(self):
        return self.df if self.df is not None else pd.DataFrame(self.data)

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
        if isinstance(dataframe, pd.DataFrame):
            if type == "csv":
                return dataframe.to_csv(f"{self.path}\\data.csv")
            elif type == "excel":
                return dataframe.to_excel(
                    f"{self.path}\\data.xlsx", engine="xlsxwriter"
                )
            else:
                raise ValueError("type must be either 'csv' or 'excel'")
        else:
            raise TypeError("dataframe must be a pandas dataframe")

    def create_scatter_plot(self, df, x, y, title, color) -> None:
        context = ReportContext(df, x, y, title, color)

        self.reporter.plot_scatter(df, context)

    def create_histogram(self, df, x, y, title, color) -> None:
        context = ReportContext(df, x, y, title, color)

        self.reporter.plot_histogram(df, context)

    def create_pie_chart(self, df, x, y, title, color) -> None:
        context = ReportContext(df, x, y, title, color)

        self.reporter.plot_pie(df, context)

    def create_box_plot(self, df, x, y, title, color) -> None:
        context = ReportContext(df, x, y, title, color)

        self.reporter.plot_box(df, context)

    def create_heatmap(self, df, x, y, title, color) -> None:
        context = ReportContext(df, x, y, title, color)

        self.reporter.plot_heatmap(df, context)

    def create_3d_plot(self, df, x, y, title, color) -> None:
        context = ReportContext(df, x, y, title, color)

        self.reporter.plot_3d(df, context)

    def create_grouped_bar_chart(self, df, x, y, title, color) -> None:
        context = ReportContext(df, x, y, title, color)

        self.reporter.plot_grouped_bar(df, context)
