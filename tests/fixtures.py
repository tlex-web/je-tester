# Setup for the test suite in pytest using fixtures
# The fixture decorator is used to create a fixture function.
# The fixture function is called to create reusable objects that can be used in tests to prevent code duplication.
# We need to specify the absolute paths the data and config files are located in and fixate the JETester class.


import pytest
import os

from modules.JET import JETester
from reports.reports import ReporterMatplotlib


@pytest.fixture
def project_root() -> str:
    return os.path.dirname(os.path.abspath(os.path.dirname(__file__)))


@pytest.fixture
def data_path(project_root) -> str:
    return str(project_root) + os.sep + "tests" + os.sep + "test_data" + os.sep


@pytest.fixture
def jet(project_root):
    return JETester(
        str(project_root) + os.sep + "tests" + os.sep + "test_data" + os.sep,
        ReporterMatplotlib(),
    )
