from abc import ABC, abstractmethod
from typing import Type, TypeVar, Union

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go


class ReportContext:
    """Report context class to encapsulate report parameters"""

    def __init__(self, title: str, color: str, x, y) -> None:
        self.title = title
        self.color = color
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


# create a concrete class for each type of report
class ReporterPlotly(Report):
    """
    reporter class using plotly

    Returns
    -------
    None
    """

    def plot_bar(self, df, options: ReportContext):
        fig = px.bar(
            df, x=options.x, y=options.y, color=options.color, title=options.title
        )
        fig.show()

    def plot_line(self, df, x, y, title=""):
        fig = px.line(df, x=x, y=y, title=title)
        fig.show()

    def plot_scatter(self, df, x, y, title=""):
        fig = px.scatter(df, x=x, y=y, title=title)
        fig.show()

    def plot_pie(self, df, names, values, title=""):
        fig = px.pie(df, names=names, values=values, title=title)
        fig.show()

    def plot_box(self, df, x, y, title=""):
        fig = px.box(df, x=x, y=y, title=title)
        fig.show()

    def plot_histogram(self, df, x, title=""):
        fig = px.histogram(df, x=x, title=title)
        fig.show()

    def plot_heatmap(self, df, x, y, z, title=""):
        fig = px.density_heatmap(df, x=x, y=y, z=z, title=title)
        fig.show()

    def plot_3d(self, df, x, y, z, title=""):
        fig = px.scatter_3d(df, x=x, y=y, z=z, title=title)
        fig.show()

    def plot_surface(self, x, y, z, title=""):
        fig = go.Figure(
            data=[
                go.Surface(
                    x=x,
                    y=y,
                    z=z,
                )
            ]
        )
        fig.show()

    def plot_grouped_bar(self, df, group1, group2, color, title=""):
        fig = px.bar(df, x=group1, y=group2, color=color, title=title, barmode="group")
        fig.show()

    def plot_grouped_line(self, df, group1, group2, color, title=""):
        fig = px.line(
            df, x=group1, y=group2, color=color, title=title, line_group=color
        )
        fig.show()


class ReporterMatplotlib(Report):
    """
    reporter class using matplotlib

    Parameters
    ----------
    df : pd.DataFrame
        the dataframe to use

    Returns
    -------
    None
    """

    def plot_bar(self, x, y, title=""):
        plt.bar(x, y)
        plt.title(title)
        plt.show()

    def plot_line(self, x, y, title=""):
        plt.plot(x, y)
        plt.title(title)
        plt.show()

    def plot_scatter(self, x, y, title=""):
        plt.scatter(x, y)
        plt.title(title)
        plt.show()

    def plot_pie(self, names, values, title=""):
        plt.pie(x=values, labels=names)
        plt.title(title)
        plt.show()

    def plot_box(self, x, y, title=""):
        plt.boxplot(x, y)
        plt.title(title)
        plt.show()

    def plot_histogram(self, x, title=""):
        plt.hist(x)
        plt.title(title)
        plt.show()

    def plot_heatmap(self, x, y, z, title=""):
        plt.imshow(z, cmap="hot", interpolation="nearest")
        plt.title(title)
        plt.show()

    def plot_3d(self, x, y, z, title=""):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection="3d")
        ax.scatter(x, y, z)
        plt.title(title)
        plt.show()

    def plot_grouped_bar(self, group1, group2, color, title=""):
        plt.bar(group1, group2, color=color)
        plt.title(title)
        plt.show()


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
