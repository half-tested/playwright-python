import pytest
from playwright.sync_api import Page, expect


# todo - check with modifying 'browser_context_args' only
@pytest.fixture()
def page(browser_type, browser_type_launch_args, browser_context_args):
    geolocation = {"longitude": 2.3, "latitude": 48.9}
    browser = browser_type.launch(**browser_type_launch_args)
    context = browser.new_context(**browser_context_args, geolocation=geolocation, permissions=["geolocation"])
    # geolocation may be setup separately
    # context.set_geolocation(geolocation)
    yield context.new_page()
    context.close()
    browser.close()

def test_emulate_geolocation(login, page):
    page.goto("/demoPages/testLocation", wait_until="domcontentloaded")
    page.get_by_role("button", name="Get Location").click()
    expect(page.locator(".position")).to_have_text("48.9:2.3")
