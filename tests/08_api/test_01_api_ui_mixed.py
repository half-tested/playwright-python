import random
import string

import pytest
from playwright.sync_api import Page

from pages.App import App


@pytest.fixture()
def login(page: Page):
    payload = {
        "username": "default",
        "password": "QADqwerty"
    }
    page.request.post("/api/auth/login", data=payload)


@pytest.fixture()
def token(login, page):
    return page.context.cookies()[0].get("value")


@pytest.fixture()
def created_test_by_api(page, token):
    random_suffix = ''.join(random.sample((string.ascii_uppercase + string.digits), 6))
    test_name = f"api created test {random_suffix}"
    test_description = f"description of {test_name}"
    payload = {
        "name": f"{test_name}",
        "description": f"{test_description}"
    }
    headers = {"X-CSRFToken": f"{token}"}
    response = page.request.post("/api/tests/new", data=payload, headers=headers)
    print(f"{response.status} {response.status_text}")
    test_id = response.json()["test_id"]

    yield test_name, test_description

    response = page.request.delete(f"/api/tests/{test_id}", headers=headers)
    print(f"{response.status} {response.status_text}")


def test_api_row_appears_for_created_test(page, created_test_by_api):
    test_name, test_description = created_test_by_api
    print(f"test_name={test_name}")
    print(f"test_description={test_description}")

    page.goto("/tests")
    assert page.get_by_role("row").filter(has_text=test_description).is_visible()
    page.pause()


def test_api_testcases_row_counter_check(page, login, created_test_by_api):
    page.goto("/tests")
    response = page.request.get("/api/tests")
    total = response.json()["total"]
    assert page.locator(".tableTitle span").text_content() == f"(Total {total})"
    page.pause()


def test_api_initial_testcases_row_counter_check(page):
    app = App(page)
    app.login.navigate()
    app.login.login("default", "QADqwerty")
    app.navigate.navigate_to_test_cases()

    response = page.request.get("/api/tests")
    total_count = response.json()["total"]

    assert app.test_cases.totals_text() == f"(Total {total_count})"
    page.pause()