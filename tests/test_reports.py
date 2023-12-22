from tests.fixtures import dataframe, options
from reports.reports import ReporterFactory


def test_plot_bar_with_plotly(dataframe, options):
    reporter = ReporterFactory().get_reporter("plotly")
    reporter.plot_bar(dataframe, options)


def test_plot_line_with_plotly(dataframe, options):
    reporter = ReporterFactory().get_reporter("plotly")
    reporter.plot_line(dataframe, options)


def test_plot_scatter_with_plotly(dataframe, options):
    reporter = ReporterFactory().get_reporter("plotly")
    reporter.plot_scatter(dataframe, options)


def test_plot_histogram_with_plotly(dataframe, options):
    reporter = ReporterFactory().get_reporter("plotly")
    reporter.plot_histogram(dataframe, options)


def test_plot_pie_with_plotly(dataframe, options):
    reporter = ReporterFactory().get_reporter("plotly")
    reporter.plot_pie(dataframe, options)


def test_plot_box_with_plotly(dataframe, options):
    reporter = ReporterFactory().get_reporter("plotly")
    reporter.plot_box(dataframe, options)


def test_plot_heatmap_with_plotly(dataframe, options):
    reporter = ReporterFactory().get_reporter("plotly")
    reporter.plot_heatmap(dataframe, options)


def test_plot_3d_with_plotly(dataframe, options):
    reporter = ReporterFactory().get_reporter("plotly")
    reporter.plot_3d(dataframe, options)


def test_plot_grouped_bar_with_plotly(dataframe, options):
    reporter = ReporterFactory().get_reporter("plotly")
    reporter.plot_grouped_bar(dataframe, options)


def test_plot_bar_with_matplotlib(dataframe, options):
    reporter = ReporterFactory().get_reporter("matplotlib")
    reporter.plot_bar(dataframe, options)


def test_plot_line_with_matplotlib(dataframe, options):
    reporter = ReporterFactory().get_reporter("matplotlib")
    reporter.plot_line(dataframe, options)


def test_plot_scatter_with_matplotlib(dataframe, options):
    reporter = ReporterFactory().get_reporter("matplotlib")
    reporter.plot_scatter(dataframe, options)


def test_plot_histogram_with_matplotlib(dataframe, options):
    reporter = ReporterFactory().get_reporter("matplotlib")
    reporter.plot_histogram(dataframe, options)


def test_plot_pie_with_matplotlib(dataframe, options):
    reporter = ReporterFactory().get_reporter("matplotlib")
    reporter.plot_pie(dataframe, options)


def test_plot_box_with_matplotlib(dataframe, options):
    reporter = ReporterFactory().get_reporter("matplotlib")
    reporter.plot_box(dataframe, options)


def test_plot_heatmap_with_matplotlib(dataframe, options):
    reporter = ReporterFactory().get_reporter("matplotlib")
    reporter.plot_heatmap(dataframe, options)


def test_plot_3d_with_matplotlib(dataframe, options):
    reporter = ReporterFactory().get_reporter("matplotlib")
    reporter.plot_3d(dataframe, options)


def test_plot_grouped_bar_with_matplotlib(dataframe, options):
    reporter = ReporterFactory().get_reporter("matplotlib")
    reporter.plot_grouped_bar(dataframe, options)
