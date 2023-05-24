from playwright.sync_api import Page

from pages.BasePage import BasePage
from pages.DashboardPage import DashboardPage
from pages.LoginPage import LoginPage
from pages.NewTestCasePage import NewTestCasePage
from pages.TestCasesPage import TestCasesPage


class App:
    def __init__(self, page: Page):
        self.page = page
        self.login = LoginPage(self.page)
        self.dashboard = DashboardPage(self.page)
        self.test_cases = TestCasesPage(self.page)
        self.new_test_case = NewTestCasePage(self.page)
        self.navigate = BasePage(self.page)
