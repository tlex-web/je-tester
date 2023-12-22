from abc import ABC, abstractmethod
from typing import Union, Optional

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp


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
    def plot_missing_values(self, dataframe: pd.DataFrame):
        """plot missing values method"""

    @abstractmethod
    def plot_bar(self, dataframe: pd.DataFrame, options: ReportContext):
        """plot bar method"""

    @abstractmethod
    def plot_line(self, dataframe: pd.DataFrame, options: ReportContext):
        """plot line method"""

    @abstractmethod
    def plot_scatter(self, dataframe: pd.DataFrame, options: ReportContext):
        """plot scatter method"""

    @abstractmethod
    def plot_histogram(self, dataframe: pd.DataFrame, options: ReportContext):
        """plot histogram method"""

    @abstractmethod
    def plot_pie(self, dataframe: pd.DataFrame, options: ReportContext):
        """plot pie method"""

    @abstractmethod
    def plot_box(self, dataframe: pd.DataFrame, options: ReportContext):
        """plot box method"""

    @abstractmethod
    def plot_heatmap(self, dataframe: pd.DataFrame, options: ReportContext):
        """plot heatmap method"""

    @abstractmethod
    def plot_3d(self, dataframe: pd.DataFrame, options: ReportContext):
        """plot 3d method"""

    @abstractmethod
    def plot_grouped_bar(self, dataframe: pd.DataFrame, options: ReportContext):
        """plot grouped bar method"""


# create a concrete class for each type of report
class ReporterPlotly(Report):
    """
    reporter class using plotly

    Returns
    -------
    None
    """

    def plot_missing_values(self, dataframe) -> None:
        """plot missing values

        Args:
            dataframe (pd.Dataframe): expect the full dataframe
            options (ReportContext):
        """
        y_count_mv = pd.DataFrame(dataframe.isnull().sum())
        y_count_mv.columns = ["count"]
        y_count_mv.index.names = ["Name"]
        y_count_mv["Name"] = y_count_mv.index
        y_count_mv = y_count_mv[y_count_mv["count"] != 0]
        y_count_mv.sort_values(by=["count"], inplace=True, ascending=True)

        missing_values = pd.DataFrame(y_count_mv["count"] / len(dataframe) * 100)
        missing_values.columns = ["count"]
        missing_values.index.names = ["Name"]
        missing_values.sort_values(by=["count"], inplace=True, ascending=True)

        x = y_count_mv["Name"]

        # Creating two subplots
        fig = sp.make_subplots(
            rows=1,
            cols=2,
            specs=[[{}, {}]],
            shared_xaxes=True,
            shared_yaxes=False,
            vertical_spacing=0.001,
        )

        fig.append_trace(
            go.Bar(
                x=missing_values["count"],
                y=x,
                marker=dict(
                    color="rgba(18, 63, 90, 0.95)",
                    line=dict(color="rgba(18, 63, 90, 1.0)", width=1),
                ),
                name="Relative amount of missing values (%)",
                orientation="h",
            ),
            1,
            1,
        )

        fig.append_trace(
            go.Scatter(
                x=y_count_mv["count"],
                y=x,
                mode="lines+markers",
                line_color="rgb(0, 68, 27)",
                name="Absolute values of missing values",
            ),
            1,
            2,
        )

        fig.update_layout(
            title="Absolute and relative amount of missing values per variable",
            yaxis=dict(
                showgrid=False,
                showline=False,
                showticklabels=True,
                domain=[0, 0.85],
            ),
            yaxis2=dict(
                showgrid=False,
                showline=False,
                showticklabels=False,
                linecolor="rgba(102, 102, 102, 0.8)",
                linewidth=2,
                domain=[0, 0.85],
            ),
            xaxis=dict(
                zeroline=False,
                showline=False,
                showticklabels=True,
                showgrid=True,
                domain=[0, 0.42],
            ),
            xaxis2=dict(
                zeroline=False,
                showline=False,
                showticklabels=True,
                showgrid=True,
                domain=[0.47, 1],
                dtick=2000,
            ),
            legend=dict(x=0.029, y=1.038, font_size=10),
            margin=dict(l=100, r=20, t=70, b=70),
            paper_bgcolor="rgb(248, 248, 255)",
            plot_bgcolor="rgb(248, 248, 255)",
        )

        annotations = []

        y_s = np.round(missing_values["count"], decimals=2)
        y_nw = np.rint(y_count_mv["count"])

        # add labels
        for ydn, yd, xd in zip(y_nw, y_s, x):
            annotations.append(
                dict(
                    xref="x2",
                    yref="y2",
                    y=xd,
                    x=ydn + 500
                    if ydn == max(y_nw)
                    else ydn
                    - 500,  # move the label to the left side if it is the maximum value
                    text="{:,}".format(ydn),
                    font=dict(family="Arial", size=12, color="rgb(0, 68, 27)"),
                    showarrow=False,
                )
            )
            annotations.append(
                dict(
                    xref="x1",
                    yref="y1",
                    y=xd,
                    x=yd + 0.75,
                    text=str(yd) + "%",
                    font=dict(family="Arial", size=12, color="rgb(18, 63, 90)"),
                    showarrow=False,
                )
            )

        fig.update_layout(annotations=annotations)

        fig.show()

    def plot_bar(self, dataframe, options):
        fig = px.bar(
            dataframe,
            x=options.x,
            y=options.y,
            color=options.color,
            barmode=options.barmode if options.barmode else "group",
            title=options.title,
        )
        fig.show()

    def plot_line(self, dataframe, options):
        fig = px.line(
            dataframe,
            x=options.x,
            y=options.y,
            color=options.color,
            title=options.title,
        )
        fig.show()

    def plot_scatter(self, dataframe, options):
        fig = px.scatter(
            dataframe,
            x=options.x,
            y=options.y,
            color=options.color,
            title=options.title,
        )
        fig.show()

    def plot_histogram(self, dataframe, options):
        fig = px.histogram(
            dataframe,
            x=options.x,
            y=options.y,
            color=options.color,
            title=options.title,
        )
        fig.show()

    def plot_pie(self, dataframe, options):
        fig = px.pie(
            dataframe,
            names=options.names,
            values=options.values,
            color=options.color,
            title=options.title,
        )
        fig.show()

    def plot_box(self, dataframe, options):
        fig = px.box(
            dataframe,
            x=options.x,
            y=options.y,
            color=options.color,
            title=options.title,
        )
        fig.show()

    def plot_heatmap(self, dataframe, options):
        fig = px.imshow(
            dataframe,
            x=options.x,
            y=options.y,
            color_continuous_scale=options.color_discrete_map,
            title=options.title,
        )
        fig.show()

    def plot_3d(self, dataframe, options):
        fig = px.scatter_3d(
            dataframe,
            x=options.x,
            y=options.y,
            color=options.color,
            title=options.title,
        )
        fig.show()

    def plot_grouped_bar(self, dataframe, options):
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

    def plot_missing_values(self, dataframe) -> None:
        """plot missing values

        Args:
            dataframe (pd.Dataframe): expect the full dataframe
            options (ReportContext):
        """

        y_count_mv = pd.DataFrame(dataframe.isnull().sum())
        y_count_mv.columns = ["count"]
        y_count_mv.index.names = ["Name"]
        y_count_mv["Name"] = y_count_mv.index
        y_count_mv = y_count_mv[y_count_mv["count"] != 0]
        y_count_mv.sort_values(by=["count"], inplace=True, ascending=True)

        missing_values = pd.DataFrame(y_count_mv["count"] / len(dataframe) * 100)
        missing_values.columns = ["count"]
        missing_values.index.names = ["Name"]
        missing_values.sort_values(by=["count"], inplace=True, ascending=True)

        x = y_count_mv["Name"]

        fig, ax = plt.subplots(1, 2, figsize=(15, 5))

        ax[0].barh(x, missing_values["count"])
        ax[0].set_title("Relative amount of missing values (%)")
        ax[0].set_xlabel("Percentage")
        ax[0].set_ylabel("Variable")

        ax[1].plot(y_count_mv["count"], x)
        ax[1].set_title("Absolute values of missing values")
        ax[1].set_xlabel("Number of missing values")
        ax[1].set_ylabel("Variable")

        fig.show()

    def plot_bar(self, dataframe, options):
        fig, ax = plt.subplots()
        ax.bar(dataframe[options.x], dataframe[options.y])
        ax.set_title(options.title)
        fig.show()

    def plot_line(self, dataframe, options):
        fig, ax = plt.subplots()
        ax.plot(dataframe[options.x], dataframe[options.y])
        ax.set_title(options.title)
        fig.show()

    def plot_scatter(self, dataframe, options):
        fig, ax = plt.subplots()
        ax.scatter(dataframe[options.x], dataframe[options.y])
        ax.set_title(options.title)
        fig.show()

    def plot_histogram(self, dataframe, options):
        fig, ax = plt.subplots()
        ax.hist(dataframe[options.x], dataframe[options.y])
        ax.set_title(options.title)
        fig.show()

    def plot_pie(self, dataframe, options):
        fig, ax = plt.subplots()
        ax.pie(dataframe[options.x], dataframe[options.y])
        ax.set_title(options.title)
        fig.show()

    def plot_box(self, dataframe, options):
        fig, ax = plt.subplots()
        ax.boxplot(dataframe[options.x], dataframe[options.y])
        ax.set_title(options.title)
        fig.show()

    def plot_heatmap(self, dataframe, options):
        fig, ax = plt.subplots()
        ax.imshow(dataframe[options.x], dataframe[options.y])
        ax.set_title(options.title)
        fig.show()

    def plot_3d(self, dataframe, options):
        fig, ax = plt.subplots()
        ax.scatter3d(dataframe[options.x], dataframe[options.y])
        ax.set_title(options.title)
        fig.show()

    def plot_grouped_bar(self, dataframe, options):
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
