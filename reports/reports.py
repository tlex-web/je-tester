from abc import ABC, abstractmethod
from typing import Type, TypeVar, Union, Optional

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go


class ReportContext:
    """Report context class to encapsulate report parameters"""

    def __init__(
        self,
        title: str,
        color: Union[str, list[str]],
        x: Optional[Union[str, list[str], np.ndarray]] = None,
        y: Optional[Union[str, list[str], np.ndarray]] = None,
        barmode: Optional[str] = None,
        symbol: Optional[str] = None,
        values: Optional[Union[str, list[str], np.ndarray]] = None,
        names: Optional[str] = None,
        color_discrete_map: Optional[Union[dict[str, str], str]] = None,
    ) -> None:
        self.title = title
        self.color = color
        self.barmode = barmode
        self.symbol = symbol
        self.values = values
        self.names = names
        self.color_discrete_map = color_discrete_map
        self.x = x
        self.y = y


class Report(ABC):
    """Report class interface"""

    @abstractmethod
    def plot_bar(self, dataframe, options: ReportContext):
        """plot bar method"""

    @abstractmethod
    def plot_line(self, dataframe, options: ReportContext):
        """plot line method"""

    @abstractmethod
    def plot_scatter(self, dataframe, options: ReportContext):
        """plot scatter method"""

    @abstractmethod
    def plot_histogram(self, dataframe, options: ReportContext):
        """plot histogram method"""

    @abstractmethod
    def plot_pie(self, dataframe, options: ReportContext):
        """plot pie method"""

    @abstractmethod
    def plot_box(self, dataframe, options: ReportContext):
        """plot box method"""

    @abstractmethod
    def plot_heatmap(self, dataframe, options: ReportContext):
        """plot heatmap method"""

    @abstractmethod
    def plot_3d(self, dataframe, options: ReportContext):
        """plot 3d method"""

    @abstractmethod
    def plot_grouped_bar(self, dataframe, options: ReportContext):
        """plot grouped bar method"""


# create a concrete class for each type of report
class ReporterPlotly(Report):
    """
    reporter class using plotly

    Returns
    -------
    None
    """

    def plot_bar(self, dataframe, options: ReportContext):
        fig = px.bar(
            dataframe,
            x=options.x,
            y=options.y,
            color=options.color,
            barmode=options.barmode if options.barmode else "group",
            title=options.title,
        )
        fig.show()

    def plot_line(self, dataframe, options: ReportContext):
        fig = px.line(
            dataframe,
            x=options.x,
            y=options.y,
            color=options.color,
            title=options.title,
        )
        fig.show()

    def plot_scatter(self, dataframe, options: ReportContext):
        fig = px.scatter(
            dataframe,
            x=options.x,
            y=options.y,
            color=options.color,
            title=options.title,
        )
        fig.show()

    def plot_histogram(self, dataframe, options: ReportContext):
        fig = px.histogram(
            dataframe,
            x=options.x,
            y=options.y,
            color=options.color,
            title=options.title,
        )
        fig.show()

    def plot_pie(self, dataframe, options: ReportContext):
        fig = px.pie(
            dataframe,
            names=options.names,
            values=options.values,
            color=options.color,
            title=options.title,
        )
        fig.show()

    def plot_box(self, dataframe, options: ReportContext):
        fig = px.box(
            dataframe,
            x=options.x,
            y=options.y,
            color=options.color,
            title=options.title,
        )
        fig.show()

    def plot_heatmap(self, dataframe, options: ReportContext):
        fig = px.imshow(
            dataframe,
            x=options.x,
            y=options.y,
            color_continuous_scale=options.color_discrete_map,
            title=options.title,
        )
        fig.show()

    def plot_3d(self, dataframe, options: ReportContext):
        fig = px.scatter_3d(
            dataframe,
            x=options.x,
            y=options.y,
            color=options.color,
            title=options.title,
        )
        fig.show()

    def plot_grouped_bar(self, dataframe, options: ReportContext):
        fig = px.bar(
            dataframe,
            x=options.x,
            y=options.y,
            color=options.color,
            barmode=options.barmode if options.barmode else "group",
            title=options.title,
        )
        fig.show()


class ReporterMatplotlib(Report):
    """
    reporter class using matplotlib

    Returns
    -------
    None
    """

    def plot_bar(self, dataframe, options: ReportContext):
        fig, ax = plt.subplots()
        ax.bar(dataframe[options.x], dataframe[options.y])
        ax.set_title(options.title)
        fig.show()

    def plot_line(self, dataframe, options: ReportContext):
        fig, ax = plt.subplots()
        ax.plot(dataframe[options.x], dataframe[options.y])
        ax.set_title(options.title)
        fig.show()

    def plot_scatter(self, dataframe, options: ReportContext):
        fig, ax = plt.subplots()
        ax.scatter(dataframe[options.x], dataframe[options.y])
        ax.set_title(options.title)
        fig.show()

    def plot_histogram(self, dataframe, options: ReportContext):
        fig, ax = plt.subplots()
        ax.hist(dataframe[options.x], dataframe[options.y])
        ax.set_title(options.title)
        fig.show()

    def plot_pie(self, dataframe, options: ReportContext):
        fig, ax = plt.subplots()
        ax.pie(dataframe[options.x], dataframe[options.y])
        ax.set_title(options.title)
        fig.show()

    def plot_box(self, dataframe, options: ReportContext):
        fig, ax = plt.subplots()
        ax.boxplot(dataframe[options.x], dataframe[options.y])
        ax.set_title(options.title)
        fig.show()

    def plot_heatmap(self, dataframe, options: ReportContext):
        fig, ax = plt.subplots()
        ax.imshow(dataframe[options.x], dataframe[options.y])
        ax.set_title(options.title)
        fig.show()

    def plot_3d(self, dataframe, options: ReportContext):
        fig, ax = plt.subplots()
        ax.scatter3d(dataframe[options.x], dataframe[options.y])
        ax.set_title(options.title)
        fig.show()

    def plot_grouped_bar(self, dataframe, options: ReportContext):
        fig, ax = plt.subplots()
        ax.bar(dataframe[options.x], dataframe[options.y])
        ax.set_title(options.title)
        fig.show()


class ReporterFactory:
    """
    reporter factory class

    Parameters
    ----------
    df : pd.DataFrame
        the dataframe to use

    Returns
    -------
    None
    """

    def get_reporter(
        self, reporter_type: str
    ) -> Union[ReporterPlotly, ReporterMatplotlib]:
        if reporter_type == "plotly":
            return ReporterPlotly()
        elif reporter_type == "matplotlib":
            return ReporterMatplotlib()
        else:
            raise ValueError("Invalid reporter type")
