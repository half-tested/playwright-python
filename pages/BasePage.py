import allure
from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.logo_icon = page.get_by_role("link", name="logo")
        self.welcome_text = page.get_by_role("heading", name="Hello")
        self.logout_icon = page.locator(".logOut")

    @allure.step
    def navigate_to(self, menu_item: str):
        self.page.get_by_role("link", name=f"{menu_item}").click()

    @allure.step
    def navigate_to_create_new_test(self):
        self.navigate_to("Create new test")
        from pages.NewTestCasePage import NewTestCasePage
        return NewTestCasePage(self.page)

    @allure.step
    def navigate_to_test_cases(self):
        self.navigate_to("Test Cases")
        from pages.TestCasesPage import TestCasesPage
        return TestCasesPage(self.page)
