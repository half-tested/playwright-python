from playwright.sync_api import Page


def test_locators_chaining_selectors(page: Page) -> None:
    page.goto("http://127.0.0.1:8000/login")
    page.get_by_label("Username:").fill("alice")
    page.get_by_label("Password:").fill("Qamania123")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("link", name="Demo controls").click()
    page.frame_locator("iframe[title='description']").get_by_role("textbox").type("123")
    page.pause()
    # frame = page.frame("iframe")
    # frame.fill("textbox", "4")
