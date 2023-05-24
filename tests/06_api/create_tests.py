import random
import string

import pytest
from playwright.sync_api import Page


@pytest.fixture()
def login(page: Page):
    payload = {
        "username": "alice",
        "password": "Qamania123"
    }
    page.request.post("/api/auth/login", data=payload)


@pytest.fixture()
def token(login, page):
    return page.context.cookies()[0].get("value")


def test_create_tests(token, page):
    for _ in range(2):
        random_suffix = ''.join(random.sample((string.ascii_uppercase + string.digits), 6))
        test_name = f"api created test {random_suffix}"
        test_description = f"description of {test_name}"
        payload = {
            "name": f"{test_name}",
            "description": f"{test_description}"
        }
        headers = {"X-CSRFToken": f"{token}"}
        response = page.request.post("/api/tests/new", data=payload, headers=headers)
