import pytest
from playwright.sync_api import expect


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {**browser_context_args, "viewport": {"width": 1280, "height": 1024}}


# page.set_viewport_size({"width": 1280, "height": 1024})
# or use updated fixture browser_context_args
def test_emulate_viewport(login, page):
    # page.set_viewport_size({"width": 1280, "height": 1024})
    page.goto("/tests")
    expect(page.get_by_role("cell", name="Author")).to_be_visible()
