import os
import random
import string

import allure
import pytest
from playwright.sync_api import expect, APIRequestContext

from pages.DashboardPage import DashboardPage
from pages.LoginPage import LoginPage
from pages.TestCasesPage import TestCasesPage


# 1. run all tests:
# pytest --alluredir=allure --clean-alluredir --allure-features=custom --screenshot=on --video=on --tracing=on

# 2. generate report:
# allure serve allure

class Test:
    __test__ = False

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description


@pytest.fixture()
def random_string():
    return ''.join(random.sample((string.ascii_uppercase + string.digits), 6))


@pytest.fixture()
def default_user_api(default_user_creds, playwright, pytestconfig) -> APIRequestContext:
    payload = {
        "username": f"{default_user_creds.username}",
        "password": f"{default_user_creds.password}"
    }
    api_context = playwright.request.new_context(base_url=pytestconfig.getini("base_url"))
    api_context.post("/api/auth/login", data=payload)
    yield api_context
    api_context.dispose()


@pytest.fixture()
def new_test_unique_data(random_string, default_user_api):
    name = f"test {random_string}"
    description = f"description from {name}"
    test = Test(name, description)

    yield test

    token = default_user_api.storage_state()["cookies"][0].get("value")
    headers = {"X-CSRFToken": f"{token}"}
    response = default_user_api.get("/api/tests?size=100500", headers=headers)
    tests = response.json()["tests"]
    for test_on_backend in tests:
        if test.name == test_on_backend["name"]:
            default_user_api.delete(f"/api/tests/{test_on_backend['id']}", headers=headers)


@allure.feature('custom')
def test_create_new_testcase(default_user_page, default_user_creds, new_test_unique_data):
    test_case = LoginPage(default_user_page) \
        .navigate() \
        .login(default_user_creds.username, default_user_creds.password) \
        .navigate_to_create_new_test() \
        .create_test_case(new_test_unique_data.name, new_test_unique_data.description) \
        .navigate_to_test_cases() \
        .test_case_row_by_name(new_test_unique_data.name)

    expect(test_case.locator, f"'{new_test_unique_data.name}' is not in the test cases list").to_be_visible()


@allure.feature('custom')
def test_case_change_status_check(default_user_page, default_user_creds):
    existing_test = "Login test"

    login_page = LoginPage(default_user_page)
    login_page.navigate()
    login_page.login(default_user_creds.username, default_user_creds.password)

    dash_board = DashboardPage(default_user_page)
    dash_board.navigate_to_test_cases()

    testcases_page = TestCasesPage(default_user_page)
    test_case = testcases_page.test_case_row_by_name(existing_test)

    test_case.click_fail_button()
    expect(test_case.status, f"status should be FAIL for test '{existing_test}"'').to_have_text("FAIL")

    test_case.click_pass_button()
    expect(test_case.status, f"status should be PASS for test '{existing_test}"'').to_have_text("PASS")


@allure.feature('custom')
def test_login_failing(default_user_page):
    welcome_text = LoginPage(default_user_page)\
        .navigate()\
        .login("1", "1")\
        .welcome_text

    expect(welcome_text).to_contain_text("Hello")