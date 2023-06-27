# Note: by default Playwright is not available in browser
# To make it available use on of options below


# Option #1 --> Playwright inspector available and developer tools
# To run in debug mode set environment variable:
# PWDEBUG=1


# Option #2 --> Playwright available in developer tools
# To run with developer tools set environment variable:
# PWDEBUG=console


# Option #3 --> Playwright inspector available and developer tools
# To run with breakpoint add line in the code:
# page.pause()
from playwright.sync_api import Page


def test_example(page: Page) -> None:
    page.goto("http://127.0.0.1:8000/login")
    page.get_by_label("Username:").fill("default")
    page.get_by_label("Password:").fill("QADqwerty")
    page.get_by_label("Password:").press("Enter")
    page.pause()
    page.get_by_role("link", name="Test Runs").click()