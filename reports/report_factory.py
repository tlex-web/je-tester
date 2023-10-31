from reports.reports import ReporterMatplotlib, ReporterPlotly


class ReportFactory:
    """ReportFactory class"""

    def __init__(self, report_type):
        self.report_type = report_type

    def get_report(self):
        """get_report method"""
        if self.report_type == "matplotlib":
            return ReporterMatplotlib
        elif self.report_type == "plotly":
            return ReporterPlotly
        else:
            raise Exception("Unknown report type.")
