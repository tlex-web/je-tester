# create an abstract class to describe the interface of a JET

from abc import ABC, abstractmethod


class ScenarioContext:
    def __init__(self, name, description):
        self.name = name
        self.description = description


class JournalEntryTests(ABC):
    @abstractmethod
    def prepare_data(self):
        pass

    @abstractmethod
    def run_test_scenarios(self):
        pass

    @abstractmethod
    def create_report(self):
        pass

    @abstractmethod
    def export_data(self):
        pass


class JB0(JournalEntryTests):
    def prepare_data(self):
        print("JB0: prepare data")

    def run_test_scenario(self):
        print("JB0: run test scenario")

    def create_report(self):
        print("JB0: create report")

    def export_data(self):
        print("JB0: export data")


class JB1(JournalEntryTests):
    def prepare_data(self):
        print("JB1: prepare data")

    def run_test_scenario(self):
        print("JB1: run test scenario")

    def create_report(self):
        print("JB1: create report")

    def export_data(self):
        print("JB1: export data")


class JB2(JournalEntryTests):
    def prepare_data(self):
        print("JB2: prepare data")

    def run_test_scenario(self):
        print("JB2: run test scenario")

    def create_report(self):
        print("JB2: create report")

    def export_data(self):
        print("JB2: export data")


class JB3(JournalEntryTests):
    def prepare_data(self):
        print("JB3: prepare data")

    def run_test_scenario(self):
        print("JB3: run test scenario")

    def create_report(self):
        print("JB3: create report")

    def export_data(self):
        print("JB3: export data")


class JB4(JournalEntryTests):
    def prepare_data(self):
        print("JB4: prepare data")

    def run_test_scenario(self):
        print("JB4: run test scenario")

    def create_report(self):
        print("JB4: create report")

    def export_data(self):
        print("JB4: export data")


class JB5(JournalEntryTests):
    def prepare_data(self):
        print("JB5: prepare data")

    def run_test_scenario(self):
        print("JB5: run test scenario")

    def create_report(self):
        print("JB5: create report")

    def export_data(self):
        print("JB5: export data")


class JB6(JournalEntryTests):
    def prepare_data(self):
        print("JB6: prepare data")

    def run_test_scenario(self):
        print("JB6: run test scenario")

    def create_report(self):
        print("JB6: create report")

    def export_data(self):
        print("JB6: export data")


class JB7(JournalEntryTests):
    def prepare_data(self):
        print("JB7: prepare data")

    def run_test_scenario(self):
        print("JB7: run test scenario")

    def create_report(self):
        print("JB7: create report")

    def export_data(self):
        print("JB7: export data")


class JB8(JournalEntryTests):
    def prepare_data(self):
        print("JB8: prepare data")

    def run_test_scenario(self):
        print("JB8: run test scenario")

    def create_report(self):
        print("JB8: create report")

    def export_data(self):
        print("JB8: export data")


class JB9(JournalEntryTests):
    def prepare_data(self):
        print("JB9: prepare data")

    def run_test_scenario(self):
        print("JB9: run test scenario")

    def create_report(self):
        print("JB9: create report")

    def export_data(self):
        print("JB9: export data")


class JB10(JournalEntryTests):
    def prepare_data(self):
        print("JB10: prepare data")

    def run_test_scenario(self):
        print("JB10: run test scenario")

    def create_report(self):
        print("JB10: create report")

    def export_data(self):
        print("JB10: export data")
