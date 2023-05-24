from playwright.sync_api import Page


def test_locators_chaining_selectors(page: Page) -> None:
    page.goto("http://127.0.0.1:8000/login")
    page.get_by_label("Username:").fill("alice")
    page.get_by_label("Password:").fill("Qamania123")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("link", name="Test Cases").click()
    page.pause()
    # playwright.$("xpath=//table >> css=tr >> css=.PASS")
    # playwright.$("xpath=//table >> *css=tr >> css=.PASS")
    # playwright.$("xpath=//table >> *css=tr:has-text('bob') >> css=.PASS")
    # playwright.$("xpath=//table >> css=tr:has-text('bob'):has(.FAIL) >> css=.editBtn")
    # playwright.$("xpath=//table >> css=tr >> text='Details'")
