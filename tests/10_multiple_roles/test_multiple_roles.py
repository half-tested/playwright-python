import pytest
from playwright.sync_api import expect

from pages.LoginPage import LoginPage


@pytest.fixture()
def alice(page):
    return LoginPage(page) \
        .navigate() \
        .login("alice", "Qamania123")


@pytest.fixture()
def bob(browser_type, browser_type_launch_args, browser_context_args):
    bob_browser = browser_type.launch(**browser_type_launch_args)
    bob_context = bob_browser.new_context(**browser_context_args)
    bob_page = bob_context.new_page()

    yield LoginPage(bob_page) \
        .navigate() \
        .login("bob", "Qamania123")
    bob_page.close()
    bob_context.close()
    bob_browser.close()


def test_multiple_roles(alice, bob):
    test_case = "Multiple roles test case"
    alice\
        .navigate_to_create_new_test()\
        .create_test_case(test_case, "description for bob")
    test_case = bob\
        .navigate_to_test_cases()\
        .test_case_row_by_name(test_case)
    expect(test_case.locator, "Bob should see test case created by alice").to_be_visible()
    test_case.click_delete_button()
    expect(test_case.locator, "Bob should be able to delete test case created by alice").not_to_be_visible()