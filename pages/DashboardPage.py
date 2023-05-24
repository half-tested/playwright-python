from playwright.sync_api import Page
from pages.BasePage import BasePage


class DashboardPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.refresh_stats_button = page.get_by_role("button", name="Refresh Stats")
