import sys


def exception_handler(
    debug, exception_type, exception, traceback, debug_hook=sys.excepthook
):
    if debug:
        debug_hook(exception_type, exception, traceback)
    else:
        print("%s: %s" % (exception_type.__name__, exception))
