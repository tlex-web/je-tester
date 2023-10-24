import logging
from types import TracebackType
from typing import Type
import sys


def exception_handler(
    exception_type: Type[BaseException],
    exception: BaseException,
    traceback: TracebackType | None,
):
    """
    A function to handle exceptions

    Parameters
    ----------
    exception_type : Exception
        The type of exception
    exception : Exception
        The exception
    traceback : Exception
        The traceback of the exception

    Returns
    -------
    None
    """

    logging.error(
        f"\nException type: {exception_type.__name__} \nException: {exception} \nTraceback: {traceback}"
    )

    sys.__excepthook__(exception_type, exception, traceback)
