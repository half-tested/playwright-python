import pytest
from playwright.sync_api import expect


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {**browser_context_args, "geolocation": {"longitude": 2.3, "latitude": 48.9}, "permissions": ["geolocation"]}


def test_emulate_geolocation(login, page):
    page.goto("/demoPages/testLocation")
    page.get_by_role("button", name="Get Location").click()
    expect(page.locator(".position")).to_have_text("48.9:2.3")
