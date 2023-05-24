import pytest
from playwright.sync_api import Page, expect


@pytest.fixture()
def page(browser_type, browser_type_launch_args, browser_context_args):
    locale = "fr_FR"
    timezone_id = "Europe/Paris"
    browser = browser_type.launch(**browser_type_launch_args)
    context = browser.new_context(**browser_context_args, locale=locale, timezone_id=timezone_id)
    yield context.new_page()
    context.close()
    browser.close()


# page.set_viewport_size({"width": 1280, "height": 1024})
# or use fixture browser_context_args with device setup
def test_emulate_locale(login, page):
    page.goto("http://google.com")
    # check auth button translation based on locale
    expect(page.get_by_role("link", name="Connexion")).to_be_visible()
