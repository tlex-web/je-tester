import sys


def exception_handler(
    debug: bool,
    exception_type: Exception,
    exception: Exception,
    traceback: Exception,
    debug_hook=sys.__excepthook__,
):
    if debug:
        debug_hook(exception_type, exception, traceback.__traceback__)
    else:
        print("%s: %s" % (exception_type, exception))
