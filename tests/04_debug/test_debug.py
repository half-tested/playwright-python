# Note: by default Playwright is not available in browser
# To make it available use on of 1, 2, 3 options below


# Option #1 --> Playwright inspector available and developer tools
# To run in debug mode set environment variable:
# PWDEBUG=1


# Option #2 --> Playwright available in developer tools
# To run with developer tools set environment variable:
# PWDEBUG=console


# Option #3 --> Playwright inspector available and developer tools
# To run with breakpoint add uncommented line in the code:
# page.pause()


# Option #4 --> Verbose API logs
# Playwright supports verbose logging with the DEBUG environment variable.
# To enable verbose logging set environment variable:
# DEBUG=pw:api
from playwright.sync_api import Page


def test_debug_tools(page: Page):
    page.goto("http://127.0.0.1:8000/login")
    page.get_by_label("Username:").fill("default")
    page.get_by_label("Password:").fill("QADqwerty")
    page.get_by_label("Password:").press("Enter")
    # page.pause()
    page.get_by_role("link", name="Test Runs").click()