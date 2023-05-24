import re


def test_locators_filtering(page):
    page.goto("http://127.0.0.1:8000/login")
    page.get_by_label("Username:").fill("default")
    page.get_by_label("Password:").fill("QADqwerty")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("link", name="Test Cases").click()

    page.locator("tbody tr").filter(has_text="Login test").wait_for()
    # page.locator("tbody tr").filter(has_text=re.compile("login\stest", re.IGNORECASE)).wait_for()  # regex applicable

    page.locator("tbody tr").filter(has_not_text="default").wait_for()
    # page.locator("tbody tr").filter(has_not_text=re.compile("[de]+fault")).wait_for()  # regex applicable

    page.locator("tbody tr").filter(has=page.get_by_text("Login test")).wait_for()

    page.locator("tbody tr").filter(has_not=page.get_by_text("default")).wait_for()

