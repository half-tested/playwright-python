import pytest
from playwright.sync_api import expect

from pages.LoginPage import LoginPage


@pytest.fixture()
def default(page):
    return LoginPage(page) \
        .navigate() \
        .login("default", "QADqwerty")


@pytest.fixture()
def secondary(browser_type, browser_type_launch_args, browser_context_args):
    secondary_browser = browser_type.launch(**browser_type_launch_args)
    secondary_context = secondary_browser.new_context(**browser_context_args)
    secondary_page = secondary_context.new_page()

    yield LoginPage(secondary_page) \
        .navigate() \
        .login("secondary", "QASqwerty")
    secondary_page.close()
    secondary_context.close()
    secondary_browser.close()


def test_multiple_roles(default, secondary):
    test_case = "Multiple roles test case"
    default\
        .navigate_to_create_new_test()\
        .create_test_case(test_case, "description for secondary user")
    test_case = secondary\
        .navigate_to_test_cases()\
        .test_case_row_by_name(test_case)
    expect(test_case.locator, "Secondary user should see test case created by default user").to_be_visible()
    test_case.click_delete_button()
    expect(test_case.locator, "Secondary user should be able to delete test case created by default user").not_to_be_visible()