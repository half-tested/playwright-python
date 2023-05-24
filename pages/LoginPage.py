import allure
from playwright.sync_api import Page
from pages.DashboardPage import DashboardPage


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.get_by_label("Username")
        self.password_input = page.get_by_label("Password")
        self.login_button = page.get_by_role("button", name="Login")

    @allure.step
    def login(self, username: str, password: str) -> DashboardPage:
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
        return DashboardPage(self.page)

    @allure.step
    def navigate(self):
        self.page.goto("/login")
        return self
