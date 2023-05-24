import pytest
from playwright.sync_api import expect


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, playwright):
    return {**browser_context_args, **playwright.devices["iPhone 13 Pro"]}


def test_emulate_device(login, page):
    page.goto("/tests")
    expect(page.get_by_role("columnheader", name="Author")).not_to_be_visible()
