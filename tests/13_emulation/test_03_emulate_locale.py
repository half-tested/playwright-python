import pytest
from playwright.sync_api import expect


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {**browser_context_args, "locale": "fr_FR", "timezone_id": "Europe/Paris"}


def test_emulate_locale(login, page):
    page.goto("http://google.com")
    # check auth button translation based on locale
    expect(page.get_by_role("link", name="Connexion")).to_be_visible()
