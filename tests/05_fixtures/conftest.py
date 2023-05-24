import pytest
from playwright.sync_api import Page

from pages.DashboardPage import DashboardPage
from pages.LoginPage import LoginPage


@pytest.fixture()
def home_page(page: Page) -> DashboardPage:
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("alice", "Qamania123")
    yield DashboardPage(page)
