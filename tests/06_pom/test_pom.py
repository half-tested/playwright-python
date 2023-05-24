import random
import string

from pages.App import App
from pages.DashboardPage import DashboardPage
from pages.LoginPage import LoginPage
from pages.TestCasesPage import TestCasesPage


def test_case_change_status_check(page):
    existing_test = "Login test"

    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("default", "QADqwerty")

    dash_board = DashboardPage(page)
    dash_board.navigate_to_test_cases()

    testcases_page = TestCasesPage(page)
    test_case = testcases_page.test_case_row_by_name(existing_test)

    test_case.click_fail_button()
    assert test_case.get_status() == "FAIL", f"status should be FAIL for test '{existing_test}"''

    test_case.click_pass_button()
    assert test_case.get_status() == "PASS", f"status should be PASS for test '{existing_test}"''


def test_create_new_testcase(page):
    random_string = ''.join(random.sample((string.ascii_uppercase + string.digits), 6))
    test_name = f"test {random_string}"
    test_description = f"description from {test_name}"
    print(f"test_name: {test_name}")
    print(f"test_description: {test_description}")

    test_case = LoginPage(page) \
        .navigate() \
        .login("default", "QADqwerty") \
        .navigate_to_create_new_test() \
        .create_test_case(test_name, test_description) \
        .navigate_to_test_cases() \
        .test_case_row_by_name(test_name)

    assert test_case.is_displayed(), f"'{test_name}' is not in the test cases list"
    assert test_case.get_status() == "Norun", f"default status 'Norun' is not set for '{test_name}'"

    test_case.click_delete_button()  # WARNING: Bad practice any interaction after assertion. Use yield fixtures.


def test_from_meta_class(page):
    existing_test = "Login test"

    app = App(page)
    app.login.navigate()
    app.login.login("default", "QADqwerty")
    app.navigate.navigate_to_test_cases()
    assert app.test_cases.test_case_row_by_name(existing_test).is_displayed(), \
        f"'{existing_test}' is not in the test cases list"


def test_with_defined_page_fixtures(login_screen, dashboard_screen, testcases_screen):
    existing_test = "Login test"

    login_screen.navigate()
    login_screen.login("default", "QADqwerty")
    dashboard_screen.navigate_to_test_cases()
    assert testcases_screen.test_case_row_by_name(existing_test).is_displayed(), \
        f"'{existing_test}' is not in the test cases list"