import random
import string

import pytest
from playwright.sync_api import APIRequestContext


@pytest.fixture()
def create_test_by_api(api):
    token = api.storage_state()["cookies"][0].get("value")
    headers = {"X-CSRFToken": f"{token}"}
    test_ids = list()

    def perform(test_name: str, test_description: str):
        payload = {
            "name": f"{test_name}",
            "description": f"{test_description}"
        }
        response = api.post("/api/tests/new", data=payload, headers=headers)
        print(f"{response.status} {response.status_text}")
        test_id = response.json()["test_id"]
        print(f"test_id={test_id}")
        test_ids.append(test_id)

    yield perform

    for test in test_ids:
        response = api.delete(f"/api/tests/{test}", headers=headers)
        print(f"{response.status} {response.status_text}")


def get_test_count(api_context: APIRequestContext):
    token = api_context.storage_state()["cookies"][0].get("value")
    headers = {"X-CSRFToken": f"{token}"}
    response = api_context.get("/api/tests", headers=headers)
    total = response.json()["total"]
    return total


@pytest.fixture()
def api(playwright, base_url) -> APIRequestContext:
    payload = {
        "username": "default",
        "password": "QADqwerty"
    }
    api_context = playwright.request.new_context(base_url=base_url)
    api_context.post("/api/auth/login", data=payload)
    yield api_context
    api_context.dispose()


def test_no_ui(api, create_test_by_api):
    random_suffix = ''.join(random.sample((string.ascii_uppercase + string.digits), 6))
    test_name = f"api created test {random_suffix}"
    test_description = f"description of {test_name}"

    total_before = get_test_count(api)
    create_test_by_api(test_name, test_description)
    total_after = get_test_count(api)
    assert total_before + 1 == total_after
