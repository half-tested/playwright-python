from playwright.sync_api import Page


def test_locators_filtered_by_another_locator(page: Page) -> None:
    page.goto("http://127.0.0.1:8000/login")
    page.get_by_label("Username:").fill("alice")
    page.get_by_label("Password:").fill("Qamania123")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("link", name="Test Cases").click()
    page.get_by_role("row").filter(has=page.locator(".FAIL")).filter(has_text="bob").get_by_role("button", name="Details").first.click()
    page.get_by_text("Test author: bob").wait_for(timeout=2000, state="visible")
    