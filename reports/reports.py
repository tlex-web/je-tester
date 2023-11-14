from abc import ABC, abstractmethod
from typing import Type, TypeVar, Union

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go


class Report(ABC):
    """Report class interface"""

    @abstractmethod
    def plot_bar(self):
        """plot bar method"""

    @abstractmethod
    def plot_line(self):
        """plot line method"""

    @abstractmethod
    def plot_scatter(self):
        """plot scatter method"""

    @abstractmethod
    def plot_histogram(self):
        """plot histogram method"""


class ReporterPlotly(Report):
    """
    reporter class using plotly

    Parameters
    ----------
    df : pd.DataFrame
        the dataframe to use

    Returns
    -------
    None
    """

    def __init__(self, df: pd.DataFrame) -> None:
        self.df = df

    def plot_bar(self, x, y, title=""):
        fig = px.bar(self.df, x=x, y=y, title=title)
        fig.show()

    def plot_line(self, x, y, title=""):
        fig = px.line(self.df, x=x, y=y, title=title)
        fig.show()

    def plot_scatter(self, x, y, title=""):
        fig = px.scatter(self.df, x=x, y=y, title=title)
        fig.show()

    def plot_pie(self, names, values, title=""):
        fig = px.pie(self.df, names=names, values=values, title=title)
        fig.show()

    def plot_box(self, x, y, title=""):
        fig = px.box(self.df, x=x, y=y, title=title)
        fig.show()

    def plot_histogram(self, x, title=""):
        fig = px.histogram(self.df, x=x, title=title)
        fig.show()

    def plot_heatmap(self, x, y, z, title=""):
        fig = px.density_heatmap(self.df, x=x, y=y, z=z, title=title)
        fig.show()

    def plot_3d(self, x, y, z, title=""):
        fig = px.scatter_3d(self.df, x=x, y=y, z=z, title=title)
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

    def plot_grouped_bar(self, group1, group2, color, title=""):
        fig = px.bar(
            self.df, x=group1, y=group2, color=color, title=title, barmode="group"
        )
        fig.show()

    def plot_grouped_line(self, group1, group2, color, title=""):
        fig = px.line(
            self.df, x=group1, y=group2, color=color, title=title, line_group=color
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

    def __init__(self, df: pd.DataFrame) -> None:
        self.df = df

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


class Reports:
    """
    Reports class

    Parameters
    ----------
    df : pd.DataFrame
        the dataframe to use

    Returns
    -------
    None
    """

    def __init__(self, df, reporter) -> None:
        self.df = df
        self.reporter = reporter
