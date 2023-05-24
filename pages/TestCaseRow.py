import allure
from playwright.sync_api import Locator


class TestCaseRow:
    __test__ = False

    def __init__(self, locator: Locator):
        self.locator = locator
        self.pass_button = self.locator.get_by_role("button", name="PASS")
        self.fail_button = self.locator.get_by_role("button", name="FAIL")
        self.edit_button = self.locator.get_by_role("button", name="Details")
        self.delete_button = self.locator.get_by_role("button", name="Delete")
        self.description = self.locator.locator(".ttDes")
        self.author = self.locator.locator(".ttAuthor")
        self.status = self.locator.locator(".ttStatus")

    @allure.step
    def click_pass_button(self):
        self.pass_button.click()

    @allure.step
    def click_fail_button(self):
        self.fail_button.click()

    @allure.step
    def click_delete_button(self):
        self.delete_button.click()
        return self

    @allure.step
    def get_status(self):
        return self.status.text_content()

    def is_displayed(self):
        return self.locator.is_visible()