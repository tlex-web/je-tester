# create an abstract class to describe the interface of a JET

from abc import ABC, abstractmethod


class JournalEntryTests(ABC):
    @abstractmethod
    def prepare_data(self):
        pass

    @abstractmethod
    def run_test_scenario(self):
        pass

    @abstractmethod
    def create_report(self):
        pass

    @abstractmethod
    def export_data(self):
        pass

    def execute_test(self):
        self.prepare_data()
        self.run_test_scenario()
        self.create_report()
        self.export_data()


class JB0(JournalEntryTests):
    def prepare_data(self):
        print("JB0: prepare data")

    def run_test_scenario(self):
        print("JB0: run test scenario")

    def create_report(self):
        print("JB0: create report")

    def export_data(self):
        print("JB0: export data")
