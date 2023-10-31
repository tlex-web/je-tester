from dependency_injector import containers, providers
from modules.JET import JETester

from reports.report_factory import ReportFactory
from reports.reports import ReporterMatplotlib, ReporterPlotly


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    report_factory = providers.Factory(ReportFactory)
    report_type_a = providers.Factory(ReporterMatplotlib)
    report_type_b = providers.Factory(ReporterPlotly)
    data_science_package = providers.Factory(
        JETester,
        report=report_factory.provided.get_report(config.report_type),
    )
