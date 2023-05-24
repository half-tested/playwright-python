import pytest
from playwright.sync_api import Page, expect


# @pytest.fixture()
# def page(browser_type, browser_type_launch_args, browser_context_args):
#     viewport = {"width": 1280, "height": 1024}
#     browser = browser_type.launch(**browser_type_launch_args)
#     context = browser.new_context(**browser_context_args, viewport=viewport)
#     yield context.new_page()
#     context.close()
#     browser.close()


# page.set_viewport_size({"width": 1280, "height": 1024})
# or use fixture browser_context_args with device setup
def test_emulate_viewport(login, page):
    page.set_viewport_size({"width": 1280, "height": 1024})
    page.goto("/tests", wait_until="domcontentloaded")
    expect(page.get_by_role("cell", name="Author")).to_be_visible()
