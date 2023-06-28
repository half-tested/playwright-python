import allure
from playwright.sync_api import Page
from pages.BasePage import BasePage
from pages.TestCaseRow import TestCaseRow


class TestCasesPage(BasePage):
    __test__ = False

    def __init__(self, page: Page):
        super().__init__(page)
        self.rows = page.get_by_role("row")

    @allure.step
    def rows_by_name(self, test_name: str):
        return self.rows.filter(has_text=f"{test_name}")

    @allure.step
    def test_case_rows_by_name(self, test_name: str) -> list[TestCaseRow]:
        test_case_rows = []
        for locator in self.rows_by_name(test_name).all():
            test_case_rows.append(TestCaseRow(locator))
        return test_case_rows

    @allure.step
    def test_case_row_by_name(self, test_name: str) -> TestCaseRow:
        locator = self.rows_by_name(test_name)
        return TestCaseRow(locator)

    def totals_text(self):
        return self.page.locator(".tableTitle span").text_content()
