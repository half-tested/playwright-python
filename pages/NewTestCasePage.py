import allure
from playwright.sync_api import Page
from pages.BasePage import BasePage


class NewTestCasePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.test_name_input = page.locator("#id_name")
        self.test_description_input = page.get_by_label("Test description")
        self.create_button = page.get_by_role("button", name="Create")

    @allure.step
    def create_test_case(self, test_name: str, test_description: str):
        self.test_name_input.fill(test_name)
        self.test_description_input.fill(test_description)
        self.create_button.click()
        return self