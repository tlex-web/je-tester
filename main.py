import sys
from containers.report_container import Container

from helpers.helper_funcs import exception_handler


def main():
    container = Container()
    container.config.set("report_type", "matplotlib")
    container.wire(modules=[sys.modules[__name__]])

    jet = container.JETester()
    jet.run()


if __name__ == "__main__":
    sys.excepthook = exception_handler

    main()
