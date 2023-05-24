import pytest
from playwright.sync_api import Page

from pages.DashboardPage import DashboardPage
from pages.LoginPage import LoginPage
from pages.TestCasesPage import TestCasesPage


@pytest.fixture()
def login_screen(page: Page):
    return LoginPage(page)


@pytest.fixture()
def dashboard_screen(page: Page):
    return DashboardPage(page)


@pytest.fixture()
def testcases_screen(page: Page):
    return TestCasesPage(page)