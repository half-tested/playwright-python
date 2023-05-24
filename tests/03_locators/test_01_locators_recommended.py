from playwright.sync_api import Page


def test_recommended_locators(page: Page, playwright) -> None:
    page.goto("http://127.0.0.1:8000/login")
    page.get_by_label("Username:").fill("alice")
    page.get_by_label("Password:").fill("Qamania123")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("link", name="Demo pages").click()
    page.get_by_role("link", name="Demo controls").click()
    page.get_by_placeholder("entered value appears next").type("by Placeholder value entered")
    page.get_by_text("by Placeholder value entered").wait_for(timeout=3000)
    page.get_by_alt_text("logo one").click()
    page.get_by_text("by Placeholder value entered").wait_for(state="hidden", timeout=3000)