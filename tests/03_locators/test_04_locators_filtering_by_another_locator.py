from playwright.sync_api import Page


def test_locators_filtered_by_another_locator(page: Page) -> None:
    page.goto("http://127.0.0.1:8000/login")
    page.get_by_label("Username:").fill("default")
    page.get_by_label("Password:").fill("QADqwerty")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("link", name="Test Cases").click()
    page.get_by_role("row").filter(has=page.locator(".FAIL")).filter(has_text="secondary").get_by_role("button", name="Details").first.click()
    page.get_by_text("Test author: secondary").wait_for(timeout=2000, state="visible")
    