import allure

from pages.App import App
from pages.DashboardPage import DashboardPage
from pages.LoginPage import LoginPage
from pages.TestCasesPage import TestCasesPage


# 1. run all tests:
# pytest --alluredir=allure --clean-alluredir --allure-features=native --screenshot=on --video=on --tracing=on

# 2. generate report:
# allure serve allure

@allure.feature('native')
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


@allure.feature('native')
def test_verify_existing_record(page):
    existing_test = "Login test"

    app = App(page)
    app.login.navigate()
    app.login.login("default", "QADqwerty")
    app.navigate.navigate_to_test_cases()
    assert app.test_cases.test_case_row_by_name(existing_test).is_displayed(), \
        f"'{existing_test}' is not in the test cases list"
