import sys

from helpers.helper_funcs import exception_handler


def test_exception_handler_logs_error(caplog):
    exception_type = ValueError
    exception = ValueError("test error")
    traceback = None

    exception_handler(exception_type, exception, traceback)

    assert "Exception type: ValueError" in caplog.text
    assert "Exception: test error" in caplog.text


def test_exception_handler_calls_sys_excepthook():
    exception_type = ValueError
    exception = ValueError("test error")
    traceback = None

    def mock_sys_excepthook(exc_type, exc, tb):
        assert exc_type == exception_type
        assert exc == exception
        assert tb == traceback

    original_sys_excepthook = sys.excepthook
    sys.excepthook = mock_sys_excepthook

    try:
        exception_handler(exception_type, exception, traceback)
    finally:
        sys.excepthook = original_sys_excepthook
