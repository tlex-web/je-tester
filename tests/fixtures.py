import pytest
import os

from modules.JET import JETester


@pytest.fixture
def project_root() -> str:
    return os.path.dirname(os.path.abspath(os.path.dirname(__file__)))


@pytest.fixture
def data_path(project_root) -> str:
    return str(project_root) + os.sep + "tests" + os.sep + "test_data" + os.sep


@pytest.fixture
def jet(project_root):
    return JETester(
        str(project_root) + os.sep + "tests" + os.sep + "test_data" + os.sep
    )
